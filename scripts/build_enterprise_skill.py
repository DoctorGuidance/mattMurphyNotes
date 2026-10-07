#!/usr/bin/env python3
"""
Enterprise Skill Builder for Matt Murphy Production Engineering
Synthesizes all 321 masterclasses from data.json into an authoritative,
multi-layered AI Agent Skill with modular rules, reference catalogs,
and static analysis tools.
"""

import os
import sys
import json
import shutil

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_DIR = os.path.join(ROOT_DIR, 'skills', 'matt-murphy-production-engineer')
RULES_DIR = os.path.join(SKILL_DIR, 'rules')
REFS_DIR = os.path.join(SKILL_DIR, 'references')
SCRIPTS_DIR = os.path.join(SKILL_DIR, 'scripts')
GLOBAL_SKILL_DIR = r"C:\Users\ersha\.gemini\config\skills\matt-murphy-production-engineer"

def load_dataset():
    data_path = os.path.join(ROOT_DIR, 'data.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_skill():
    print("🚀 Starting Enterprise Skill generation from 321 Masterclasses...")
    data = load_dataset()
    episodes = data['episodes']
    modules = data['modules']

    os.makedirs(RULES_DIR, exist_ok=True)
    os.makedirs(REFS_DIR, exist_ok=True)
    os.makedirs(SCRIPTS_DIR, exist_ok=True)

    # Clean old rules if any
    for f in os.listdir(RULES_DIR):
        if f.endswith('.md'):
            os.remove(os.path.join(RULES_DIR, f))

    # 1. Generate 12 Module Rules
    print("📦 Generating 12 Architectural Module Rulebooks...")
    module_rule_files = {}

    invariants_map = {
        "01-auth-identity": "Authentication tokens must NEVER touch `localStorage` or `sessionStorage`. All sessions must rely on `HttpOnly; Secure; SameSite=Lax` cookies with short-lived access tokens (10-15m) and rotating refresh token families. Every entity lookup MUST be composite-scoped (`tenant_id` + `user_id`) to mathematically eliminate IDOR.",
        "02-security-defense": "Zero secrets in client code or frontend bundles. No wildcard CORS (`*`) on authenticated APIs. Clickjacking frames must be blocked via CSP `frame-ancestors 'none'`. All user inputs crossing system boundaries must be strictly sanitized and parameterized to prevent injection.",
        "03-database-storage": "Direct database connections in serverless or high-concurrency environments are strictly prohibited; PgBouncer / Supavisor connection pooling is mandatory. Every query column in `WHERE`, `JOIN`, or `ORDER BY` must be covered by a B-Tree or composite index. Relational integrity via Foreign Keys is required.",
        "04-caching-performance": "Never cache without a deterministic invalidation strategy. Prevent Dogpile/Thundering Herd stampedes using distributed mutex locks or probabilistic early expiration. All cached keys must be tenant-namespaced (`tenant:{id}:key`) to prevent cross-tenant data leaks.",
        "05-rate-limiting-abuse": "Every public endpoint must be guarded by Redis-backed Token Bucket rate limiting across 3 tiers: unauthenticated IP caps, authenticated user quotas, and tenant/API-key rate limits. Return HTTP 429 with standard `Retry-After` headers.",
        "06-observability-logs": "Zero opaque console.logs in production. All logs must be structured JSON containing timestamps, correlation IDs (`x-request-id`), severity levels, and sanitized contexts. PII and secrets must be scrubbed at the logging boundary.",
        "07-async-queues-webhooks": "All incoming financial and external webhooks (Stripe, Paddle, GitHub) MUST verify HMAC signatures against the raw unparsed request buffer (`req.body` as raw Buffer, NOT parsed JSON). All state-mutating jobs must be idempotent via Redis or unique DB constraints.",
        "08-multi-tenancy": "Cross-tenant leakage is an existential failure. PostgreSQL Row Level Security (RLS) must be enabled on every table containing multi-tenant data. Every query, cache entry, search index, and background job must explicitly propagate and verify `tenant_id`.",
        "09-ai-guardrails": "Comply strictly with EU AI Act Article 50: clearly watermarked and labeled Synthetic Generated Information (SGI). Separate untrusted user instructions from system prompts. Enforce strict output schema validation (e.g. Zod) and hard spending caps/circuit breakers on token usage.",
        "10-cicd-deployments": "Production parity across Dev, Staging, and Prod is absolute. Database migrations must be backward-compatible and tested for zero-downtime rollbacks before deployment. Release via automated canary/blue-green pipelines with automatic regression rollbacks.",
        "11-cloud-finops": "Eliminate cloud cost traps. Impose strict execution timeouts on serverless functions. Eliminate idle provisioned resources. Beware of NAT Gateway egress bandwidth multipliers and configure hard budget alarms with automated kill-switches.",
        "12-frontend-api-hygiene": "Every dynamic UI component MUST handle all 4 mandatory states: Loading, Error with interactive Retry, Empty with clear next action, and Success. Client-side HTTP 200 is NOT proof of validity—always verify payload data schemas and server error streams."
    }

    for mod_id, mod_info in modules.items():
        mod_eps = [e for e in episodes if e.get('category') == mod_id]
        mod_name_en = mod_info.get('name_en', mod_id)
        mod_name_fa = mod_info.get('name_fa', '')
        primary_layer = mod_eps[0].get('layer', 1) if mod_eps else 1

        rule_filename = f"{mod_id}.md"
        rule_path = os.path.join(RULES_DIR, rule_filename)
        module_rule_files[mod_id] = rule_filename

        crit_eps = [e for e in mod_eps if e.get('severity') == 'CRITICAL']
        high_eps = [e for e in mod_eps if e.get('severity') == 'HIGH']
        med_eps = [e for e in mod_eps if e.get('severity') == 'MEDIUM']

        md_content = []
        md_content.append(f"# 🛡️ Rulebook: {mod_name_en}")
        md_content.append(f"**زیرسیستم:** {mod_name_fa} | **Domain ID:** `{mod_id}` | **Target Layer:** Layer {primary_layer}")
        md_content.append(f"> **Corpus Evidence:** Synthesized from {len(mod_eps)} Matt Murphy Production Engineering Masterclasses ({len(crit_eps)} Critical, {len(high_eps)} High, {len(med_eps)} Medium).")
        md_content.append("")
        md_content.append("---")
        md_content.append("")
        md_content.append("## 👑 1. Executive Summary & Core Invariant")
        md_content.append(f"In modern high-scale software engineering, **{mod_name_en}** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.")
        md_content.append(f"Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.")
        md_content.append("")
        md_content.append("### ⚡ The Non-Negotiable Invariant:")
        md_content.append(f"> {invariants_map.get(mod_id, 'Enforce strict production boundaries, explicit validation, and zero silent failures.')}")
        md_content.append("")
        md_content.append("---")
        md_content.append("")
        md_content.append("## 🚨 2. Critical Attack Vectors & Failure Scenarios")
        md_content.append(f"Analysis of {len(mod_eps)} incidents and breakdowns from this domain:")
        md_content.append("")

        # Detail top critical & high episodes
        top_eps = (crit_eps + high_eps)[:10]
        if not top_eps:
            top_eps = mod_eps[:8]

        for ep in top_eps:
            md_content.append(f"### 📍 Episode #{ep['number']}: {ep['title']} (Severity: `{ep.get('severity', 'MEDIUM')}`)")
            md_content.append(f"- **The Attack Vector / Incident:** {ep.get('problem_en', 'Production breakdown.')}")
            md_content.append(f"- **The Root Cause:** {ep.get('root_cause_en', 'Inadequate architectural boundaries.')}")
            if ep.get('golden_takeaway_en'):
                md_content.append(f"- **Matt Murphy Takeaway:** *\"{ep['golden_takeaway_en']}\"*")
            md_content.append("")

        md_content.append("---")
        md_content.append("")
        md_content.append("## ❌ 3. Vibe-Coding Traps vs. Production Reality Matrix")
        md_content.append("| # | ❌ The Vibe-Coding Trap (What Naive AI Builds) | ✅ Hardened Production Standard |")
        md_content.append("|---|:---|:---|")
        
        # Include all episodes with mistake and production rows
        for ep in mod_eps:
            mistake = ep.get('table_mistake_en', '').replace('\n', ' ').strip()
            prod = ep.get('table_production_en', '').replace('\n', ' ').strip()
            if mistake and prod:
                md_content.append(f"| **#{ep['number']}** | {mistake} | {prod} |")
        md_content.append("")
        md_content.append("---")
        md_content.append("")
        md_content.append("## 💻 4. Production-Hardened Code Patterns")
        md_content.append("The following hardened patterns demonstrate the exact production implementation required:")
        md_content.append("")

        # Select up to 4 best code snippets
        snippets_eps = [e for e in mod_eps if e.get('code_snippet') and len(e['code_snippet'].strip()) > 30][:4]
        for idx, ep in enumerate(snippets_eps, 1):
            md_content.append(f"### Pattern {idx}: Hardened Implementation for #{ep['number']} ({ep['title']})")
            snippet = ep['code_snippet'].strip()
            if not snippet.startswith('```'):
                md_content.append("```typescript")
                md_content.append(snippet)
                md_content.append("```")
            else:
                md_content.append(snippet)
            md_content.append("")

        md_content.append("---")
        md_content.append("")
        md_content.append("## 📋 5. Architectural Checklist & Verification Heuristics")
        md_content.append("Before shipping any code in this domain, verify each item:")
        md_content.append("")

        # Extract action items
        action_items = set()
        for ep in mod_eps:
            for item in ep.get('action_plan_en', []):
                cleaned = item.strip().rstrip('.')
                if len(cleaned) > 15 and len(cleaned) < 160:
                    action_items.add(cleaned)
                    if len(action_items) >= 12:
                        break
            if len(action_items) >= 12:
                break

        for item in sorted(action_items):
            md_content.append(f"- [ ] {item}.")

        md_content.append("")
        md_content.append("---")
        md_content.append("")
        md_content.append("## 📚 6. Full Domain Catalog of Masterclasses")
        md_content.append("| Episode | Severity | Masterclass Title | Production Layer | Source Reel |")
        md_content.append("|:---:|:---:|:---|:---:|:---:|")
        for ep in mod_eps:
            md_content.append(f"| **#{ep['number']}** | `{ep.get('severity', 'MEDIUM')}` | {ep['title']} | Layer {ep.get('layer', primary_layer)} | [Watch Reel]({ep.get('url', '#')}) |")

        with open(rule_path, 'w', encoding='utf-8') as rf:
            rf.write("\n".join(md_content) + "\n")
        print(f"  ✓ Written rulebook: {rule_filename} ({len(md_content)} lines)")

    # 2. Generate Master References
    print("\n📚 Generating References (Catalog, Anti-Vibe Traps, Heuristics)...")
    
    # 2.1 Masterclass Catalog
    catalog_path = os.path.join(REFS_DIR, "masterclass-catalog.md")
    cat_md = []
    cat_md.append("# 📖 Complete Matt Murphy Production Engineering Masterclass Catalog")
    cat_md.append(f"> Comprehensive catalog of all {len(episodes)} masterclasses, organized across 12 architectural modules and 13 production layers.")
    cat_md.append("")
    cat_md.append("---")
    cat_md.append("")
    cat_md.append("## 📊 Summary by Architectural Domain")
    cat_md.append("")
    cat_md.append("| Domain ID | Module Name | Episode Count | Critical | High | Medium |")
    cat_md.append("|:---|:---|:---:|:---:|:---:|:---:|")

    for mod_id, mod_info in modules.items():
        mod_eps = [e for e in episodes if e.get('category') == mod_id]
        crit = sum(1 for e in mod_eps if e.get('severity') == 'CRITICAL')
        high = sum(1 for e in mod_eps if e.get('severity') == 'HIGH')
        med = sum(1 for e in mod_eps if e.get('severity') == 'MEDIUM')
        cat_md.append(f"| `{mod_id}` | [{mod_info.get('name_en')}](../rules/{mod_id}.md) | {len(mod_eps)} | {crit} | {high} | {med} |")

    cat_md.append("")
    cat_md.append("---")
    cat_md.append("")
    cat_md.append("## 📑 Full Chronological Catalog")
    cat_md.append("")
    cat_md.append("| Ep # | Sev | Layer | Module | Title | Core Golden Takeaway |")
    cat_md.append("|:---:|:---:|:---:|:---|:---|:---|")

    for ep in episodes:
        num = ep.get('number', '---')
        sev = ep.get('severity', 'MED')
        layer = ep.get('layer', '-')
        cat = ep.get('category', '-')
        title = ep.get('title', '').replace('|', '\\|')
        takeaway = ep.get('golden_takeaway_en', '').replace('\n', ' ').replace('|', '\\|')[:100]
        cat_md.append(f"| **#{num}** | `{sev}` | L{layer} | `{cat}` | {title} | {takeaway}... |")

    with open(catalog_path, 'w', encoding='utf-8') as cf:
        cf.write("\n".join(cat_md) + "\n")
    print(f"  ✓ Written catalog: masterclass-catalog.md ({len(episodes)} episodes indexed)")

    # 2.2 Anti-Vibe Traps
    traps_path = os.path.join(REFS_DIR, "anti-vibe-traps.md")
    traps_md = []
    traps_md.append("# 🚨 Master Anti-Vibe-Coding Matrix")
    traps_md.append("> Catalog of catastrophic traps commonly introduced by naive AI vibe-coding, contrasted against senior production engineering standards.")
    traps_md.append("")
    traps_md.append("---")
    traps_md.append("")

    for mod_id, mod_info in modules.items():
        mod_eps = [e for e in episodes if e.get('category') == mod_id and e.get('table_mistake_en')]
        if not mod_eps:
            continue
        traps_md.append(f"## 📁 {mod_info.get('name_en')} (`{mod_id}`)")
        traps_md.append("| Ep # | ❌ The Naive Vibe-Coding Antipattern | ✅ Senior Production Standard |")
        traps_md.append("|:---:|:---|:---|")
        for ep in mod_eps:
            m = ep.get('table_mistake_en', '').replace('\n', ' ').replace('|', '\\|')
            p = ep.get('table_production_en', '').replace('\n', ' ').replace('|', '\\|')
            traps_md.append(f"| **#{ep['number']}** | {m} | {p} |")
        traps_md.append("")

    with open(traps_path, 'w', encoding='utf-8') as tf:
        tf.write("\n".join(traps_md) + "\n")
    print(f"  ✓ Written traps matrix: anti-vibe-traps.md")

    # 2.3 Verification Heuristics
    heuristics_path = os.path.join(REFS_DIR, "production-verification-heuristics.md")
    heur_md = []
    heur_md.append("# 🔬 Production Verification Heuristics & Diagnostic Questions")
    heur_md.append("> Deep diagnostic questions and verification gates for every layer of the modern production stack.")
    heur_md.append("")
    heur_md.append("---")
    heur_md.append("")
    
    heuristics_by_layer = [
        (1, "UI & Accessibility Hygiene", [
            "Are all 4 UI states (Loading skeleton, Error with Retry, Empty state, Success) fully implemented and tested?",
            "Is user input debounced on search/filter to prevent event loop saturation?",
            "Are touch targets at least 44x44px with WCAG 4.5:1 color contrast ratio?",
            "Does the UI prevent multi-click duplicate submissions by disabling buttons on pending state?"
        ]),
        (2, "APIs & Business Logic", [
            "Is the frontend treated strictly as a display layer, with 100% of validation re-enforced on the server?",
            "Are API endpoints protected by request timeouts (e.g. 5-10s) using AbortController or server timeouts?",
            "Do state-mutating requests accept and verify an Idempotency-Key header to prevent duplicate side effects?",
            "Are HTTP 200 responses verified to contain actual valid data rather than wrapped error strings?"
        ]),
        (3, "Database & Storage Engineering", [
            "Is connection pooling (PgBouncer, Supavisor) active for all database access, especially serverless functions?",
            "Does every WHERE, JOIN, and ORDER BY column have an explicit B-tree or composite index?",
            "Are foreign keys explicitly defined with CASCADE or SET NULL policies to prevent orphaned records?",
            "Has an automated Point-In-Time Recovery (PITR) restore drill been executed within the last 30 days?"
        ]),
        (4, "Auth & Identity Security", [
            "Are authentication tokens stored exclusively in HttpOnly, Secure, SameSite=Lax cookies, NEVER in localStorage?",
            "Do direct object queries include composite scoping: `WHERE id = :id AND tenant_id = :tenant_id` (Anti-IDOR)?",
            "Are access tokens short-lived (10-15 minutes) with rotating refresh token families?",
            "Are OAuth flows protected by state parameter validation and PKCE code challenge verification?"
        ]),
        (5, "Staging & Environment Parity", [
            "Is the staging database running the identical major.minor database version and extensions as production?",
            "Are environment variables strictly segregated between preview, staging, and production environments?",
            "Are external APIs (Stripe, Twilio, OpenAI) using isolated sandbox credentials in staging?"
        ]),
        (6, "Cloud & Compute Reliability", [
            "Are serverless functions bounded by hard execution timeouts (e.g. 15-30s) to prevent runaway billing?",
            "Are egress data paths monitored to prevent unexpected NAT Gateway bandwidth charges?",
            "Are auto-scaling groups configured with hard maximum instance limits and billing alert thresholds?"
        ]),
        (7, "CI/CD & Release Safety", [
            "Does every release pipeline run automated unit and regression tests prior to artifact creation?",
            "Are database migrations applied in a backward-compatible manner (expand-and-contract pattern)?",
            "Is an automated rollback runbook configured for canary/blue-green deployment failures?"
        ]),
        (8, "Security & Row-Level Defense", [
            "Is Row Level Security (RLS) enabled on all tables containing multi-user or multi-tenant records?",
            "Are all API keys, database credentials, and service roles excluded from client bundles and git commits?",
            "Is CORS strictly configured with an explicit domain whitelist rather than wildcard `*`?",
            "Are clickjacking framing attacks blocked via `X-Frame-Options: DENY` or CSP `frame-ancestors 'none'`?"
        ]),
        (9, "Rate Limiting & Abuse Prevention", [
            "Is Redis-backed Token Bucket rate limiting applied to all public, auth, and LLM endpoints?",
            "Are rate limits tiered across IP caps (unauthenticated), user sessions, and tenant API keys?",
            "Does the rate limiter return HTTP 429 with explicit `Retry-After` response headers?"
        ]),
        (10, "Caching & CDN Edge Strategy", [
            "Are cached keys explicitly namespaced by tenant ID (`tenant:{id}:key`) to prevent data leakage?",
            "Is Dogpile / Thundering Herd stampede prevented using distributed mutex locks?",
            "Is cache invalidation hooked into database mutations rather than relying purely on time-to-live (TTL)?"
        ]),
        (11, "Connection Pooling & Resource Limits", [
            "Is the application pool size configured strictly below the database server's max connection capacity?",
            "Are connection timeouts configured to fail fast rather than hanging threads indefinitely?",
            "Are database connections properly closed/released back to the pool in finally blocks?"
        ]),
        (12, "Observability & Error Tracing", [
            "Are all server logs formatted as structured JSON with ISO timestamps, log levels, and context?",
            "Is an `x-request-id` correlation token propagated across all microservices and database queries?",
            "Are stack traces captured and grouped in Sentry or equivalent error monitoring with PII stripped?",
            "Are health check probes (`/health/live` and `/health/ready`) separated and monitored?"
        ]),
        (13, "Disaster Recovery & Redundancy", [
            "Are automated database backups verified with automated spin-up test restores?",
            "Is the RTO (Recovery Time Objective) and RPO (Recovery Point Objective) explicitly defined and tested?",
            "Is critical object storage (S3) configured with cross-region replication or versioning against ransomware?"
        ])
    ]

    for layer_num, layer_title, questions in heuristics_by_layer:
        heur_md.append(f"### Layer {layer_num:02d}: {layer_title}")
        for q in questions:
            heur_md.append(f"- [ ] **Diagnostic Check:** {q}")
        heur_md.append("")

    with open(heuristics_path, 'w', encoding='utf-8') as hf:
        hf.write("\n".join(heur_md) + "\n")
    print(f"  ✓ Written heuristics: production-verification-heuristics.md")

    # 3. Generate Static Analysis Audit Script
    print("\n🔍 Generating Audit Script (audit_guardrails.py)...")
    audit_script_path = os.path.join(SCRIPTS_DIR, "audit_guardrails.py")
    
    script_code = r'''#!/usr/bin/env python3
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
'''
    with open(audit_script_path, 'w', encoding='utf-8') as sf:
        sf.write(script_code)
    print(f"  ✓ Written audit script: audit_guardrails.py")

    # 4. Generate Master SKILL.md
    print("\n👑 Generating Master SKILL.md...")
    skill_md_path = os.path.join(SKILL_DIR, "SKILL.md")
    
    skill_content = [
        "---",
        "name: matt-murphy-production-engineer",
        "description: Production-grade architectural hardening and security guardrails based on 320+ Matt Murphy production engineering masterclasses. Enforces resilient authentication, database connection pooling, zero-leak multi-tenancy, raw-buffer webhook validation, rate limiting, and 4-state UI hygiene. Prevents naive 'vibe coding' anti-patterns.",
        "version: 3.0.0",
        "---",
        "",
        "# 🧠 Matt Murphy Production Engineering Guardrails (321 Masterclasses)",
        "",
        "## 👑 Executive Persona & Directives",
        "You are operating in the capacity of a **Principal Systems Architect, Production Reliability Engineer, and Security Hardener**.",
        "Your mission is to eradicate fragile, prototype-level code ('vibe coding') and enforce battle-tested engineering standards derived from **321 Matt Murphy Production Masterclasses**.",
        "",
        "### 🏛️ The Anti-Vibe-Coding Doctrine",
        "- **Vibe Coding:** Code that runs once in development on a single happy path, stores JWTs in `localStorage`, accepts unverified webhooks, queries databases by bare IDs without tenant scoping, and ignores error states.",
        "- **Production Engineering:** Code built for concurrency, malicious attacks, network partitions, sudden traffic spikes, and strict regulatory compliance (EU AI Act, SOC 2, HIPAA).",
        "",
        "---",
        "",
        "## 🏗️ The 13 Production Layers Platform Matrix",
        "",
        "Every production system must be verified against the **13 Production Layers**:",
        "",
        "```",
        " ┌─────────────────────────────────────────────────────────────┐",
        " │                13 PRODUCTION LAYERS PLATFORM                │",
        " ├─────────────────────────────────────────────────────────────┤",
        " │ Layer 01: UI & Accessibility (WCAG 4.5:1, Zero Jank, 4-UI)  │",
        " │ Layer 02: APIs & Business Logic (Display != Trust Layer)    │",
        " │ Layer 03: Database & Storage (Indexes, Normalization, ACID) │",
        " │ Layer 04: Auth & Identity (HttpOnly Cookies, PKCE, Rotation)│",
        " │ Layer 05: Staging & Parity (Dev/Staging/Prod Strict Parity) │",
        " │ Layer 06: Cloud & Compute (Timeout Hard Caps, Egress Gates) │",
        " │ Layer 07: CI/CD & Pipelines (Automated Regression, Rollback)│",
        " │ Layer 08: Security & RLS (Zero Secret Leaks, Row-Level Sec) │",
        " │ Layer 09: Rate Limiting & DoS (Token Bucket, Tier Quotas)   │",
        " │ Layer 10: Caching & CDN (Tenant Keys, Explicit Invalidation)│",
        " │ Layer 11: Connection Pooling (PgBouncer, Zero Thread Starve)│",
        " │ Layer 12: Observability & Logs (JSON Traces, Correlation ID)│",
        " │ Layer 13: Disaster Recovery (Tested PITR Backups Runbooks)  │",
        " └─────────────────────────────────────────────────────────────┘",
        "```",
        "",
        "---",
        "",
        "## 📚 Architectural Modules Directory (`rules/`)",
        "",
        "The complete knowledge base is modularized into 12 authoritative rulebooks:",
        "",
        "| Module ID | Domain Title | Lessons | Primary Invariant |",
        "|:---|:---|:---:|:---|",
        "| [`01-auth-identity`](./rules/01-auth-identity.md) | Authentication & Identity | 30 | HttpOnly cookies, PKCE OAuth, IDOR composite scoping |",
        "| [`02-security-defense`](./rules/02-security-defense.md) | Application Security & Defense | 47 | Zero secrets in client bundles, CSP framing denial, no wildcard CORS |",
        "| [`03-database-storage`](./rules/03-database-storage.md) | Database & Storage Engineering | 33 | Connection pooling, index coverage, tested PITR backups |",
        "| [`04-caching-performance`](./rules/04-caching-performance.md) | Caching & Edge Performance | 12 | Thundering herd mutex locks, tenant-namespaced keys |",
        "| [`05-rate-limiting-abuse`](./rules/05-rate-limiting-abuse.md) | Rate Limiting & Abuse Prevention | 4 | Redis token bucket, IP/User/Tenant tiers, standard 429 headers |",
        "| [`06-observability-logs`](./rules/06-observability-logs.md) | Observability & Error Tracking | 16 | Structured JSON logging, Request-ID tracing, Sentry capture |",
        "| [`07-async-queues-webhooks`](./rules/07-async-queues-webhooks.md) | Async Queues & Webhooks | 19 | Raw request buffer signatures, idempotency gates, DLQ backoff |",
        "| [`08-multi-tenancy`](./rules/08-multi-tenancy.md) | Multi-Tenancy & Data Isolation | 6 | Row-Level Security (RLS), composite tenant keys, worker context |",
        "| [`09-ai-guardrails`](./rules/09-ai-guardrails.md) | AI Guardrails, LLM Security & Compliance | 46 | EU AI Act Art. 50 SGI labels, prompt injection defense, spend limits |",
        "| [`10-cicd-deployments`](./rules/10-cicd-deployments.md) | Testing, Staging & CI/CD | 39 | Strict environment parity, zero-downtime migration rollbacks |",
        "| [`11-cloud-finops`](./rules/11-cloud-finops.md) | Cloud Infrastructure & FinOps | 32 | Serverless timeout hard caps, NAT gateway egress control, cost alarms |",
        "| [`12-frontend-api-hygiene`](./rules/12-frontend-api-hygiene.md) | Frontend Architecture & API Hygiene | 37 | 4 mandatory UI states, client != trust, zero false HTTP 200s |",
        "",
        "---",
        "",
        "## 🛡️ Core Production Invariants (Non-Negotiable)",
        "",
        "### 1. Authentication & Session Hygiene (Lessons 043, 044, 048, 118, 124, 206)",
        "- **Zero Token in LocalStorage:** NEVER store JWTs, access tokens, or session IDs in `localStorage` or `sessionStorage`. All tokens MUST be issued as `HttpOnly`, `Secure`, `SameSite=Lax` cookies.",
        "- **Strict Tenant & User Scoping (Anti-IDOR):** Direct object lookups must never query records purely by the ID provided in route parameters (`WHERE id = :id`). All queries must be composite scoped: `WHERE id = :id AND tenant_id = :tenantId AND user_id = :userId`.",
        "- **OAuth Integrity:** Implement state parameters and PKCE (Proof Key for Code Exchange) on all third-party OAuth flows (Google, GitHub) to eliminate authorization code interception.",
        "- **Token Lifespans:** Access tokens must expire within 10–15 minutes. Long-lived sessions must use rotating refresh tokens with database family tracking to detect token reuse attacks.",
        "",
        "### 2. Application Security & Defense (Lessons 004, 005, 007, 015, 105, 191)",
        "- **Zero Secrets in Client Bundles:** Never expose database connection strings, Service-Role keys (Supabase), Stripe secret keys, or LLM API keys in frontend code or repository commits.",
        "- **Strict CORS Scoping:** Never configure CORS with wildcard `Access-Control-Allow-Origin: *` on authenticated APIs. Specify explicit allowed origin domains.",
        "- **Clickjacking Protection:** Set `X-Frame-Options: DENY` or CSP `frame-ancestors 'none'` to block malicious iframe framing.",
        "- **Database Row-Level Security (RLS):** When using Supabase, PostgreSQL, or Convex, always enable RLS policies on tables containing multi-user data. Never rely on frontend client filters to hide private rows.",
        "",
        "### 3. Database Engineering & Storage (Lessons 003, 174, 192, 211, 287, 288)",
        "- **Connection Pooling Mandatory:** High-concurrency or serverless architectures (Vercel, AWS Lambda) must connect to PostgreSQL through a transaction pooler (PgBouncer, Supavisor). Direct connection exhaustion crashes production.",
        "- **Zero Unindexed Queries:** Every column participating in `WHERE`, `JOIN`, or `ORDER BY` clauses must have an explicit B-tree or composite index. Eliminate full table scans.",
        "- **Relational Integrity:** Define explicit Foreign Keys with logical cascade constraints (`ON DELETE CASCADE` / `SET NULL`). Never store raw files or large blobs in relational tables; offload to S3/Object Storage.",
        "- **Tested Backups:** A backup is merely a hypothesis until a restore drill has succeeded. Verify automated daily Point-In-Time Recovery (PITR).",
        "",
        "### 4. Financial Webhooks & Asynchronous Queues (Lessons 006, 022, 103)",
        "- **Raw Buffer Signature Verification:** Stripe, Paddle, and payment webhooks MUST verify signatures using the raw HTTP request buffer (`req.body` as raw Buffer, NOT parsed JSON).",
        "- **Idempotency Keys:** Every state-mutating webhook and financial charge endpoint MUST check an idempotency key (stored in Redis or a DB unique index) to prevent double charging on retry attempts.",
        "- **Async Isolation:** Long-running jobs (video encoding, report generation, LLM batch calls) must be pushed to a dedicated background queue (BullMQ, Celery) with Dead-Letter Queues (DLQ) and exponential backoff retry policies.",
        "",
        "### 5. Rate Limiting & Denial of Service Protection (Lessons 103, 104, 215)",
        "- **Multi-Tier Rate Limiting:** Protect all public endpoints with Redis-backed Token Bucket rate limiting across 3 tiers:",
        "  1. *IP-based hard cap* for unauthenticated routes (e.g., 10 req/min for login or search).",
        "  2. *User-based quota* for authenticated API usage.",
        "  3. *Tenant/API-key quota* for enterprise B2B consumers.",
        "- Return explicit HTTP `429 Too Many Requests` with a standard `Retry-After` header.",
        "",
        "### 6. Error Handling & The 4 Mandatory UI States (Lessons 205, 289, 291)",
        "- **No Silent Server Crashes:** Register global Node.js process handlers for `uncaughtException` and `unhandledRejection`. Capture stack traces to Sentry and perform graceful process restart via PM2/Docker.",
        "- **Four UI States Requirement:** Every data-fetching frontend component MUST implement:",
        "  1. `Loading State`: Non-blocking skeleton/spinner.",
        "  2. `Error State`: User-friendly Persian/English error notice with an interactive \"تلاش مجدد (Retry)\" action.",
        "  3. `Empty State`: Meaningful guidance when zero records exist (no broken tables).",
        "  4. `Success State`: Hardened, typed rendering.",
        "",
        "### 7. AI Agent Security & EU AI Act Compliance (Lessons 001, 008, 110, 114)",
        "- **Synthetic Generated Information (SGI):** Comply with EU AI Act Article 50: clearly label synthetic text, images, or media produced by models.",
        "- **User Consent Gates:** Never send private user inputs or photos to LLM endpoints without an explicit affirmative consent action.",
        "- **Prompt Injection Defense:** Separate untrusted user instructions from system prompts. Treat all external tool outputs as untrusted input.",
        "- **Immutable Generation Logs:** Maintain a write-only audit trail recording timestamp, model identifier, prompt hash, and user ID for all model generations.",
        "",
        "---",
        "",
        "## 🛠️ Pre-Deploy Audit Checklist (Run Before Every Release)",
        "",
        "- [ ] Auth tokens stored exclusively in `HttpOnly; Secure; SameSite=Lax` cookies.",
        "- [ ] All database queries include `tenant_id` and `user_id` where appropriate (Anti-IDOR).",
        "- [ ] Row Level Security (RLS) enabled on all multi-tenant tables.",
        "- [ ] Stripe/Payment webhooks verify raw body buffer signatures (`req.body` as Buffer).",
        "- [ ] Database connection pooling configured with PgBouncer / Supavisor.",
        "- [ ] Rate limiter active on auth, search, and LLM generation endpoints.",
        "- [ ] Frontend console (F12) free of sensitive credentials and unhandled rejections.",
        "- [ ] 4 UI states (Loading, Error with Retry, Empty, Success) implemented for all async components.",
        "- [ ] Staging environment verified with strict production parity before merging to main.",
        "- [ ] Hard timeouts configured on all serverless functions and outbound API calls.",
        "",
        "---",
        "",
        "## 📁 Supporting References & Tools",
        "",
        "- **[Complete Masterclass Catalog](./references/masterclass-catalog.md):** Full index of all 321 episodes.",
        "- **[Anti-Vibe-Coding Matrix](./references/anti-vibe-traps.md):** 50+ catastrophic traps vs senior standards.",
        "- **[Verification Heuristics](./references/production-verification-heuristics.md):** Diagnostic checks for all 13 layers.",
        "- **[Static Guardrail Auditor (`scripts/audit_guardrails.py`)](./scripts/audit_guardrails.py):** Automated linter for scanning repositories."
    ]

    with open(skill_md_path, 'w', encoding='utf-8') as smf:
        smf.write("\n".join(skill_content) + "\n")
    print(f"  ✓ Written Master SKILL.md ({len(skill_content)} lines)")

    # 5. Deploy to Global Skills Directory
    print(f"\n🚀 Deploying to Global Skills Directory: {GLOBAL_SKILL_DIR}")
    if os.path.exists(GLOBAL_SKILL_DIR):
        shutil.rmtree(GLOBAL_SKILL_DIR)
    shutil.copytree(SKILL_DIR, GLOBAL_SKILL_DIR)
    print("  ✓ Successfully synchronized global skill directory!")

    # 6. Verify Deployment
    deployed_files = []
    for root, dirs, files in os.walk(GLOBAL_SKILL_DIR):
        for f in files:
            deployed_files.append(os.path.relpath(os.path.join(root, f), GLOBAL_SKILL_DIR))
    print(f"  ✓ Global skills directory now contains {len(deployed_files)} files across rules, references, and scripts.")

    print("\n🎉 Enterprise Skill successfully built and deployed!")

if __name__ == '__main__':
    build_skill()
