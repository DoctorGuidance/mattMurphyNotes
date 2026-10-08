#!/usr/bin/env python3
"""
Matt Murphy Enterprise Production Guardrail Auditor
Static Analysis Tool for verifying codebase compliance against
Matt Murphy's 321 Production Engineering Masterclasses.

Usage:
    python audit_guardrails.py [path_to_codebase] [--json]
"""

import os
import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

# Comprehensive Production Rules Across All 13 Layers
AUDIT_RULES = [
    {
        "id": "MM-043",
        "title": "Insecure Token Storage in LocalStorage/SessionStorage",
        "layer": "Layer 04 (Auth & Identity)",
        "severity": "CRITICAL",
        "regex": r"(localStorage|sessionStorage)\.(setItem|getItem)\s*\(\s*['\"][^'\"]*(token|auth|jwt|session|access_token)['\"]",
        "lesson": "043",
        "remediation": "Move authentication tokens out of localStorage into HttpOnly; Secure; SameSite=Lax cookies."
    },
    {
        "id": "MM-044",
        "title": "Unscoped Direct Object Query (IDOR Vulnerability)",
        "layer": "Layer 04 & 08 (IDOR & Multi-Tenancy)",
        "severity": "CRITICAL",
        "regex": r"(prisma|db)\.[a-zA-Z]+\.(findUnique|findFirst)\s*\(\s*\{\s*where:\s*\{\s*id:\s*(req\.params|params)",
        "lesson": "044",
        "remediation": "Mandatory composite scoping: add tenantId and userId to query where clause."
    },
    {
        "id": "MM-005",
        "title": "Permissive Wildcard CORS Configuration",
        "layer": "Layer 08 (Security & RLS)",
        "severity": "HIGH",
        "regex": r"(origin\s*:\s*['\"]?\*['\"]?|Access-Control-Allow-Origin['\"]?\s*,\s*['\"]?\*['\"]?)",
        "lesson": "005",
        "remediation": "Replace wildcard origin '*' with an explicit whitelist of allowed domains."
    },
    {
        "id": "MM-105",
        "title": "Exposed Secret API Key in Public Frontend Variable",
        "layer": "Layer 08 (Security & Defense)",
        "severity": "CRITICAL",
        "regex": r"(NEXT_PUBLIC_[A-Z_]*(SECRET|SERVICE_ROLE|PRIVATE_KEY)|VITE_[A-Z_]*(SECRET|SERVICE_ROLE|PRIVATE_KEY)|sk-proj-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16})",
        "lesson": "105",
        "remediation": "Never prefix secrets with NEXT_PUBLIC_ or VITE_. Keep private keys strictly on the server."
    },
    {
        "id": "MM-006",
        "title": "Potentially Unverified Stripe Webhook (Parsed JSON instead of Raw Buffer)",
        "layer": "Layer 07 (Async Queues & Webhooks)",
        "severity": "CRITICAL",
        "regex": r"stripe\.webhooks\.constructEvent\s*\(\s*(JSON\.parse|req\.body)",
        "lesson": "006",
        "remediation": "stripe.webhooks.constructEvent requires raw Buffer (express.raw({type: 'application/json'})), NOT parsed JSON."
    },
    {
        "id": "MM-007",
        "title": "Raw SQL String Interpolation / SQL Injection",
        "layer": "Layer 03 (Database & Storage)",
        "severity": "CRITICAL",
        "regex": r"(\$queryRawUnsafe|\.query\s*\(\s*`[^`]*\$\{[^}]+\}[^`]*`|\.execute\s*\(\s*['\"][^'\"]*%\s*[a-zA-Z])",
        "lesson": "007",
        "remediation": "Use parameterized queries or Prisma $queryRaw with prepared statement templates."
    },
    {
        "id": "MM-014",
        "title": "Unsanitized HTML in User Content / Stored XSS",
        "layer": "Layer 02 (APIs & Business Logic)",
        "severity": "HIGH",
        "regex": r"dangerouslySetInnerHTML\s*=\s*\{\s*\{\s*__html:\s*(?!\s*DOMPurify)",
        "lesson": "014",
        "remediation": "Sanitize HTML payloads with DOMPurify.sanitize() before rendering in dangerouslySetInnerHTML."
    },
    {
        "id": "MM-017",
        "title": "Unvalidated Open Redirect",
        "layer": "Layer 02 & 04 (Auth & APIs)",
        "severity": "HIGH",
        "regex": r"res\.redirect\s*\(\s*(req\.query|query|params)\.(redirect|returnTo|next|url)\s*\)",
        "lesson": "017",
        "remediation": "Validate redirect destinations against an explicit domain allowlist before calling res.redirect."
    },
    {
        "id": "MM-018",
        "title": "Insecure SSL Certificate Verification Disabled",
        "layer": "Layer 08 (Security & Defense)",
        "severity": "CRITICAL",
        "regex": r"rejectUnauthorized\s*:\s*false",
        "lesson": "018",
        "remediation": "Never set rejectUnauthorized: false in production. Install proper CA certificate bundles."
    },
    {
        "id": "MM-040",
        "title": "Mass Assignment Vulnerability in ORM Mutation",
        "layer": "Layer 02 (APIs & Business Logic)",
        "severity": "HIGH",
        "regex": r"(prisma|db)\.[a-zA-Z]+\.(update|create)\s*\(\s*\{\s*data:\s*req\.body\s*\}",
        "lesson": "040",
        "remediation": "Validate and whitelist fields using Zod schemas with .strict() before passing to ORM."
    },
    {
        "id": "MM-041",
        "title": "Insecure Legacy Password Hashing Algorithm",
        "layer": "Layer 04 (Auth & Identity)",
        "severity": "CRITICAL",
        "regex": r"crypto\.createHash\s*\(\s*['\"](md5|sha1)['\"]\)",
        "lesson": "041",
        "remediation": "Replace MD5/SHA1 password hashes with Argon2id or bcrypt (cost factor >= 12)."
    },
    {
        "id": "MM-085",
        "title": "Outbound HTTP Call Without Timeout or AbortSignal",
        "layer": "Layer 02 (APIs & Business Logic)",
        "severity": "MEDIUM",
        "regex": r"fetch\s*\(\s*['\"][^'\"]+['\"]\s*\)(?!.*(signal|timeout))",
        "lesson": "085",
        "remediation": "Wrap external fetch requests with AbortSignal.timeout(5000) or AbortController."
    },
    {
        "id": "MM-103",
        "title": "Missing Rate Limiter on Public or Auth Route",
        "layer": "Layer 05 & 09 (Rate Limiting)",
        "severity": "HIGH",
        "regex": r"router\.(post|put)\s*\(\s*['\"][^'\"]*(login|signup|reset-password|chat|generate)['\"]\s*,\s*(?!.*(rateLimit|limiter))",
        "lesson": "103",
        "remediation": "Protect authentication and AI generation endpoints with Redis-backed Token Bucket rate limiting."
    },
    {
        "id": "MM-174",
        "title": "Missing Database Connection Pooler in Serverless Setup",
        "layer": "Layer 11 (Connection Pooling)",
        "severity": "HIGH",
        "regex": r"postgresql://[^:]+:[^@]+@[^:]+:5432/[^\?]+\?sslmode=require(?!.*(pgbouncer|pooler))",
        "lesson": "174",
        "remediation": "High-concurrency serverless connections must route through PgBouncer or Supavisor (port 6543)."
    },
    {
        "id": "MM-206",
        "title": "Unverified JWT Token Decode Without Signature Validation",
        "layer": "Layer 04 (Auth & Identity)",
        "severity": "CRITICAL",
        "regex": r"jwt\.decode\s*\(",
        "lesson": "206",
        "remediation": "Never rely on jwt.decode() for authentication assertions; always use jwt.verify() with secret/public key."
    },
    {
        "id": "MM-216",
        "title": "Base64 Binary Media Stored in Database Payload",
        "layer": "Layer 03 (Database & Storage)",
        "severity": "MEDIUM",
        "regex": r"['\"]data:image\/(png|jpeg|webp);base64,[A-Za-z0-9+/=]{100,}['\"]",
        "lesson": "216",
        "remediation": "Offload image and file binaries to S3/Object Storage; store only normalized URLs/keys in the database."
    },
    {
        "id": "MM-288",
        "title": "Direct Database Access in Client Component",
        "layer": "Layer 02 & 03 (Frontend & Database)",
        "severity": "CRITICAL",
        "regex": r"['\"]use client['\"][^;]*;[\s\S]*?(import\s+.*from\s+['\"]@prisma\/client['\"]|import\s+.*from\s+['\"]\.\.\/.*db['\"])",
        "lesson": "288",
        "remediation": "Never import Prisma or database clients in 'use client' components. Move database queries to Server Actions or API routes."
    },
    {
        "id": "MM-326",
        "title": "Unsegmented Service Network or Unauthenticated Internal RPC",
        "layer": "Layer 08 (Security & Defense)",
        "severity": "CRITICAL",
        "regex": r"(networks\s*:\s*\[\s*['\"]default['\"]\s*\]|http:\/\/localhost:\d+\/(admin|db|internal))",
        "lesson": "326",
        "remediation": "Enforce network microsegmentation and mandate mTLS or signed service tokens for internal RPC calls."
    },
    {
        "id": "MM-327",
        "title": "Permissive Origin Reflection / Dynamic Echo Without Allowlist",
        "layer": "Layer 08 (Security & RLS)",
        "severity": "CRITICAL",
        "regex": r"res\.setHeader\s*\(\s*['\"]Access-Control-Allow-Origin['\"]\s*,\s*(req\.headers\.origin|req\.get\(['\"]origin['\"]\))",
        "lesson": "327",
        "remediation": "Never reflect incoming Origin headers dynamically without validating against an immutable allowlist."
    },
    {
        "id": "MM-329",
        "title": "Public Storage Bucket Configuration / Missing Signed URL TTL",
        "layer": "Layer 03 (Database & Storage)",
        "severity": "CRITICAL",
        "regex": r"(ACL\s*:\s*['\"]public-read['\"]|publicAccess\s*:\s*true|getSignedUrl\([^)]*expiresIn:\s*(?:[1-9]\d{4,}|86400))",
        "lesson": "329",
        "remediation": "Never set storage buckets to public-read for application data; enforce short-lived expiring pre-signed URLs (TTL < 900s)."
    }
]

IGNORE_DIRS = {'.git', 'node_modules', '.next', 'dist', 'build', '.gemini', '.cache', 'venv', '__pycache__', '.turbo', 'site', 'skills', 'docs'}
IGNORE_FILES = {'data.json', 'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'build_enterprise_skill.py', 'enrich_all_masterclasses.py', 'synthesize_bespoke_matrices.py', 'update_docs_tables.py', 'audit_guardrails.py', 'audit_codebase.py', 'app.js'}
EXTENSIONS = {'.js', '.jsx', '.ts', '.tsx', '.go', '.env'}

def run_audit(target_dir, output_json=False):
    target_dir = os.path.abspath(target_dir)
    findings = []
    files_scanned = 0

    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for f in files:
            if f in IGNORE_FILES:
                continue
            ext = os.path.splitext(f)[1].lower()
            if ext in EXTENSIONS:
                files_scanned += 1
                fp = os.path.join(root, f)
                try:
                    with open(fp, 'r', encoding='utf-8', errors='ignore') as fl:
                        content = fl.read()
                        rel_path = os.path.relpath(fp, target_dir)
                        
                        for rule in AUDIT_RULES:
                            matches = re.finditer(rule["regex"], content, re.IGNORECASE)
                            for m in matches:
                                line_num = content[:m.start()].count('\n') + 1
                                findings.append({
                                    "rule_id": rule["id"],
                                    "title": rule["title"],
                                    "severity": rule["severity"],
                                    "layer": rule["layer"],
                                    "file": rel_path,
                                    "line": line_num,
                                    "match": m.group(0)[:80].strip(),
                                    "remediation": rule["remediation"],
                                    "lesson": rule["lesson"]
                                })
                except Exception:
                    pass

    if output_json:
        result = {
            "target": target_dir,
            "files_scanned": files_scanned,
            "total_findings": len(findings),
            "critical": sum(1 for f in findings if f['severity'] == 'CRITICAL'),
            "high": sum(1 for f in findings if f['severity'] == 'HIGH'),
            "medium": sum(1 for f in findings if f['severity'] == 'MEDIUM'),
            "findings": findings
        }
        print(json.dumps(result, indent=2))
        return len(findings)

    print(f"\n🔍 Matt Murphy Production Guardrail Audit: {target_dir}")
    print("=" * 70)
    print(f"📊 Total files scanned: {files_scanned}")
    print(f"🚨 Total findings: {len(findings)}")
    print("=" * 70)

    if not findings:
        print("\n✅ COMPLIANT: No critical Matt Murphy production anti-patterns detected!")
        print("Architectural integrity verified across all scanned files.\n")
        return 0

    for item in findings:
        sev = item['severity']
        print(f"\n[{sev}] {item['title']} ({item['rule_id']})")
        print(f"  🏛️ Layer: {item['layer']}")
        print(f"  📍 Location: {item['file']}:{item['line']}")
        print(f"  📌 Code Match: {item['match']}")
        print(f"  💡 Remediation: {item['remediation']}")
        print(f"  📚 Masterclass: Episode #{item['lesson']}")
        print("-" * 70)

    return len(findings)

if __name__ == '__main__':
    target = "."
    json_mode = False
    for arg in sys.argv[1:]:
        if arg == '--json':
            json_mode = True
        else:
            target = arg
    sys.exit(run_audit(target, output_json=json_mode))
