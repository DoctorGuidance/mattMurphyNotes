# 🛡️ Rulebook: Multi-Tenancy & Data Isolation
**زیرسیستم:** معماری چندمستأجره و جداسازی قطعی داده‌ها | **Domain ID:** `08-multi-tenancy` | **Target Layer:** Layer 8
> **Corpus Evidence:** Synthesized from 6 Matt Murphy Production Engineering Masterclasses (3 Critical, 0 High, 3 Medium).

---

## 👑 1. Executive Summary & Core Invariant
In modern high-scale software engineering, **Multi-Tenancy & Data Isolation** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.
Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.

### ⚡ The Non-Negotiable Invariant:
> Cross-tenant leakage is an existential failure. PostgreSQL Row Level Security (RLS) must be enabled on every table containing multi-tenant data. Every query, cache entry, search index, and background job must explicitly propagate and verify `tenant_id`.

---

## 🚨 2. Critical Attack Vectors & Failure Scenarios
Analysis of 6 incidents and breakdowns from this domain:

### 📍 Episode #190: You wrote RLS policies (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You wrote RLS policies.
- **The Root Cause:** The service ro key bypasses every RS policy you just wrote. Every single one of them. Your front end calls an API endpoint.
- **Matt Murphy Takeaway:** *"Not just the front door."*

### 📍 Episode #221: Application-level filtering is a prayer (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Application-level filtering is a prayer.
- **The Root Cause:** In most applications, nothing can stop this. But rowle security certainly will. Here are the three things you need to know right now about RLS.
- **Matt Murphy Takeaway:** *"Row Level Security is a policy."*

### 📍 Episode #270: Vibe Coded Multi-Tenant Platform (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Vibe Coded Multi-Tenant Platform.
- **The Root Cause:** 20,000 users across 50 schools, three portals per school, admin, staff, and students. That's a real production system, and it needs real data architecture. So, here are the three things you do right now to build it.
- **Matt Murphy Takeaway:** *"Here’s the architecture."*

---

## ❌ 3. Vibe-Coding Traps vs. Production Reality Matrix
| # | ❌ The Vibe-Coding Trap (What Naive AI Builds) | ✅ Hardened Production Standard |
|---|:---|:---|
| **#061** | Attempts to build multi-tenant SaaS platforms by creating separate databases per tenant, creating operational maintenance nightmares. | Employs shared database architectures with strict PostgreSQL Row-Level Security (RLS) enforcing tenant isolation at scale. |
| **#156** | Shares global database tables across tenants without automated tenant-scoping assertions, risking cross-tenant data leaks. | Enforces tenant context scoping on all queries and validates tenant isolation using automated multi-tenant regression suites. |
| **#190** | Deploys PostgreSQL Row-Level Security policies without verifying that application database users bypass superuser privileges. | Runs application database connections under dedicated non-superuser roles with `FORCE ROW LEVEL SECURITY` enabled on tables. |
| **#221** | Relies on fragile application-level ORM filters (`where: { tenantId }`), risking catastrophic data leaks if a single query forgets it. | Enforces tenant isolation natively at the database engine level via PostgreSQL Row-Level Security (RLS) policies. |
| **#225** | Treats multi-tenant architecture as a purely technical decision, ignoring enterprise customer compliance and silo requirements. | Supports flexible tenant isolation tiers: cost-effective shared pooling for standard users and dedicated silo databases for enterprise tiers. |
| **#270** | Builds multi-tenant platforms without scoping file storage or cache keys, allowing users to view peer organization assets. | Enforces composite tenant namespaces across all 13 layers: database tables, Redis cache keys, S3 storage prefixes, and logs. |

---

## 💻 4. Production-Hardened Code Patterns
The following hardened patterns demonstrate the exact production implementation required:

### Pattern 1: Hardened Implementation for #061 (There are 10,000 business owners within 50 miles of you)
```typescript
-- migrations/001_row_level_security.sql
ALTER TABLE user_documents ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy ON user_documents
  FOR ALL
  USING (tenant_id = current_setting('app.current_tenant_id', true)::uuid)
  WITH CHECK (tenant_id = current_setting('app.current_tenant_id', true)::uuid);
```

### Pattern 2: Hardened Implementation for #156 (Starting in August…..35 new courses every week for ten weeks)
```typescript
-- migrations/001_row_level_security.sql
ALTER TABLE user_documents ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy ON user_documents
  FOR ALL
  USING (tenant_id = current_setting('app.current_tenant_id', true)::uuid)
  WITH CHECK (tenant_id = current_setting('app.current_tenant_id', true)::uuid);
```

### Pattern 3: Hardened Implementation for #190 (You wrote RLS policies)
```typescript
-- migrations/001_row_level_security.sql
ALTER TABLE user_documents ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy ON user_documents
  FOR ALL
  USING (tenant_id = current_setting('app.current_tenant_id', true)::uuid)
  WITH CHECK (tenant_id = current_setting('app.current_tenant_id', true)::uuid);
```

### Pattern 4: Hardened Implementation for #221 (Application-level filtering is a prayer)
```typescript
-- migrations/001_row_level_security.sql
ALTER TABLE user_documents ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy ON user_documents
  FOR ALL
  USING (tenant_id = current_setting('app.current_tenant_id', true)::uuid)
  WITH CHECK (tenant_id = current_setting('app.current_tenant_id', true)::uuid);
```

---

## 📋 5. Architectural Checklist & Verification Heuristics
Before shipping any code in this domain, verify each item:

- [ ] Add automated regression tests verifying failure scenarios before shipping.
- [ ] Implement defense-in-depth guardrails preventing unauthorized state modification.
- [ ] Inspect the existing code paths and identify unvalidated boundary inputs.
- [ ] RLS is a database level firewall.
- [ ] Superbase makes RLS accessible.
- [ ] build one and sell it to every bakery in town.
- [ ] database per tenant.
- [ ] schema per tenant.
- [ ] shared schema with rowle security.
- [ ] the math is in the sales pitch.
- [ ] the operator owns the asset.
- [ ] this is not the same as filtering in your application code.

---

## 📚 6. Full Domain Catalog of Masterclasses
| Episode | Severity | Masterclass Title | Production Layer | Source Reel |
|:---:|:---:|:---|:---:|:---:|
| **#061** | `MEDIUM` | There are 10,000 business owners within 50 miles of you | Layer 8 | [Watch Reel](https://www.instagram.com/reel/Dcd0uMTCHsl/) |
| **#156** | `MEDIUM` | Starting in August…..35 new courses every week for ten weeks | Layer 8 | [Watch Reel](https://www.instagram.com/reel/Dap6ZkSChfG/) |
| **#190** | `CRITICAL` | You wrote RLS policies | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DaLDSqRgaBG/) |
| **#221** | `CRITICAL` | Application-level filtering is a prayer | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DZslOCNRDNh/) |
| **#225** | `MEDIUM` | Your multi-tenant isolation model is not a technical | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DZphyuUgS1A/) |
| **#270** | `CRITICAL` | Vibe Coded Multi-Tenant Platform | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DY4jQHeR4Gb/) |
