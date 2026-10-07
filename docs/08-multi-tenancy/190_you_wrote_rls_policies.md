# Episode 190: You wrote RLS policies

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Multi-Tenancy & Data Isolation (`معماری چندمستأجره و جداسازی قطعی داده‌ها`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaLDSqRgaBG/) |

---

## 🚨 1. The Incident & Attack Vector
You wrote RLS policies.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Filters tenant data in frontend or application code, leaking records across accounts on missed WHERE clauses. | Enforces Row-Level Security (RLS) directly in PostgreSQL, guaranteeing zero cross-tenant data leakage. |

---

## 💡 3. Root Cause & Architectural Principle
The service ro key bypasses every RS policy you just wrote. Every single one of them. Your front end calls an API endpoint.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Inspect the existing code paths and identify unvalidated boundary inputs.
- [ ] Implement defense-in-depth guardrails preventing unauthorized state modification.
- [ ] Add automated regression tests verifying failure scenarios before shipping.

---

## 💻 5. Hardened Production Implementation
```sql
-- migrations/001_row_level_security.sql
ALTER TABLE user_documents ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy ON user_documents
  FOR ALL
  USING (tenant_id = current_setting('app.current_tenant_id', true)::uuid)
  WITH CHECK (tenant_id = current_setting('app.current_tenant_id', true)::uuid);
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Not just the front door.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

You just spent two long hours writing rowle security policies, beautiful rules, tenant isolation, role-based access on every single table. And then you built an API route that queries the database with the service ro key. The service ro key bypasses every RS policy you just wrote. Every single one of them. Your front end calls an API endpoint. That endpoint connects to the database as a service role. The service role sees everything. every tenant, every row, every table, every time. So your RLS policies are performing for an audience of nobody. The attacker does not go through the front door where your policies are watching. They find the API route where your service key already opened every lock in the building for them. 45% of vibecoded applications that we review have a security vulnerability. And this one, they seem to all share. A database policy that protects nothing because the application code walks right around around it every time. Your security, it's not your policies. Your security is every path to the data. And right now, one of those critical paths has the door fully unlocked. I just dropped the fix to this in the free faction community. The link is in my bio. Come check it out.

</div>
