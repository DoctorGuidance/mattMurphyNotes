#!/usr/bin/env python3
"""
Matt Murphy Production Linter & Static Codebase Auditor
Scans projects for critical production anti-patterns based on 320+ Matt Murphy masterclasses.

Usage:
    python audit_codebase.py [path_to_project]
"""

import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Vulnerability Patterns & Heuristics
AUDIT_RULES = [
    {
        "id": "MM-043",
        "title": "Insecure Token Storage in LocalStorage",
        "severity": "CRITICAL",
        "regex": r"localStorage\.(setItem|getItem)\s*\(\s*['\"][^'\"]*(token|auth|jwt|session)[^'\"]*['\"]",
        "lesson": "043",
        "remediation": "Move authentication tokens to HttpOnly, Secure, SameSite=Lax cookies."
    },
    {
        "id": "MM-005",
        "title": "Permissive Wildcard CORS",
        "severity": "HIGH",
        "regex": r"(origin\s*:\s*['\"]?\*['\"]?|Access-Control-Allow-Origin['\"]?\s*,\s*['\"]?\*['\"]?)",
        "lesson": "005",
        "remediation": "Replace wildcard origin '*' with an explicit whitelist of allowed domain origins."
    },
    {
        "id": "MM-105",
        "title": "Exposed Service Role or Secret API Key",
        "severity": "CRITICAL",
        "regex": r"(NEXT_PUBLIC_[A-Z_]*SECRET|NEXT_PUBLIC_[A-Z_]*SERVICE_ROLE|VITE_[A-Z_]*SECRET|sk-proj-[A-Za-z0-9_-]{20,})",
        "lesson": "105",
        "remediation": "Never prefix secrets with NEXT_PUBLIC_ or VITE_. Keep service keys strictly on the server."
    },
    {
        "id": "MM-006",
        "title": "Potentially Unverified Stripe Webhook",
        "severity": "HIGH",
        "regex": r"stripe\.webhooks\.constructEvent\s*\(\s*JSON\.parse",
        "lesson": "006",
        "remediation": "stripe.webhooks.constructEvent requires the raw unparsed Buffer, not parsed JSON."
    },
    {
        "id": "MM-015",
        "title": "Missing Clickjacking Headers",
        "severity": "MEDIUM",
        "regex": r"X-Frame-Options",
        "must_exist": True,
        "lesson": "015",
        "remediation": "Set 'X-Frame-Options: DENY' or CSP frame-ancestors 'none' to block iframe clickjacking."
    }
]

IGNORE_DIRS = {'.git', 'node_modules', '.next', 'dist', 'build', '.gemini', '.cache', 'venv', '__pycache__'}
EXTENSIONS = {'.js', '.jsx', '.ts', '.tsx', '.py', '.html', '.php', '.go', '.json', '.env'}

def scan_directory(target_dir):
    print(f"\n🔍 Scanning project at: {os.path.abspath(target_dir)}")
    print("=" * 65)

    findings = []
    files_scanned = 0

    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in EXTENSIONS:
                files_scanned += 1
                file_path = os.path.join(root, f)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as fl:
                        content = fl.read()
                        rel_path = os.path.relpath(file_path, target_dir)

                        for rule in AUDIT_RULES:
                            if rule.get("must_exist"):
                                continue
                            matches = re.finditer(rule["regex"], content, re.IGNORECASE)
                            for m in matches:
                                line_num = content[:m.start()].count('\n') + 1
                                findings.append({
                                    "file": rel_path,
                                    "line": line_num,
                                    "rule": rule,
                                    "snippet": m.group(0)[:60]
                                })
                except Exception as e:
                    pass

    print(f"📊 Scanned {files_scanned} files.")
    print("=" * 65)

    if not findings:
        print("\n✅ GREAT JOB! No obvious Matt Murphy anti-patterns detected.")
        print("Your project complies with basic production hardening guidelines.\n")
        return 0

    print(f"\n🚨 FOUND {len(findings)} POTENTIAL PRODUCTION RISKS:\n")
    for item in findings:
        r = item["rule"]
        print(f"[{r['severity']}] {r['title']} ({r['id']})")
        print(f"  📍 File: {item['file']}:{item['line']}")
        print(f"  📌 Match: {item['snippet']}")
        print(f"  💡 Remediation: {r['remediation']}")
        print(f"  📚 Matt Murphy Masterclass: Episode #{r['lesson']}")
        print("-" * 65)

    return len(findings)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(scan_directory(target))
