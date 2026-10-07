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

# Comprehensive Production Rules
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
        "regex": r"(NEXT_PUBLIC_[A-Z_]*(SECRET|SERVICE_ROLE|PRIVATE_KEY)|VITE_[A-Z_]*(SECRET|SERVICE_ROLE|PRIVATE_KEY)|sk-proj-[A-Za-z0-9_-]{20,})",
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
        "id": "MM-015",
        "title": "Missing Clickjacking Headers (X-Frame-Options or frame-ancestors)",
        "layer": "Layer 08 (Security & Defense)",
        "severity": "MEDIUM",
        "regex": r"(X-Frame-Options|frame-ancestors)",
        "must_exist": True,
        "lesson": "015",
        "remediation": "Configure X-Frame-Options: DENY or CSP frame-ancestors 'none' to block framing attacks."
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
        "id": "MM-205",
        "title": "Uncaught Exception or Silent Crash in Node.js Process",
        "layer": "Layer 06 & 12 (Observability)",
        "severity": "HIGH",
        "regex": r"process\.on\s*\(\s*['\"](uncaughtException|unhandledRejection)['\"]",
        "must_exist": True,
        "lesson": "205",
        "remediation": "Register global process handlers for uncaughtException and unhandledRejection to log to Sentry."
    },
    {
        "id": "MM-103",
        "title": "Missing Rate Limiter on Public or Auth Route",
        "layer": "Layer 05 & 09 (Rate Limiting)",
        "severity": "HIGH",
        "regex": r"router\.(post|put)\s*\(\s*['\"][^'\"]*(login|signup|reset-password|chat|generate)['\"]\s*,\s*(?!.*(rateLimit|limiter))",
        "lesson": "103",
        "remediation": "Protect authentication and AI generation endpoints with Redis-backed Token Bucket rate limiting."
    }
]

IGNORE_DIRS = {'.git', 'node_modules', '.next', 'dist', 'build', '.gemini', '.cache', 'venv', '__pycache__', '.turbo', 'site'}
IGNORE_FILES = {'data.json', 'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml'}
EXTENSIONS = {'.js', '.jsx', '.ts', '.tsx', '.py', '.html', '.go', '.env'}

def run_audit(target_dir, output_json=False):
    target_dir = os.path.abspath(target_dir)
    findings = []
    files_scanned = 0
    file_contents = {}

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
                        file_contents[rel_path] = content
                        
                        for rule in AUDIT_RULES:
                            if rule.get("must_exist"):
                                continue
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

    # Check "must_exist" rules across entire codebase
    combined_content = "\n".join(file_contents.values())
    if file_contents:
        for rule in AUDIT_RULES:
            if rule.get("must_exist"):
                if not re.search(rule["regex"], combined_content, re.IGNORECASE):
                    findings.append({
                        "rule_id": rule["id"],
                        "title": rule["title"],
                        "severity": rule["severity"],
                        "layer": rule["layer"],
                        "file": "GLOBAL CODEBASE",
                        "line": 0,
                        "match": "MISSING REQUIRED ARCHITECTURAL PATTERN",
                        "remediation": rule["remediation"],
                        "lesson": rule["lesson"]
                    })

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
        print("Architectural integrity verified.\n")
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
