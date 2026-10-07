# Episode 177: Your AI built the app

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaWCNkViYbI/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI built the app.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Leaves prototype mock data and temporary development shortcuts in production releases, causing intermittent customer data glitches. | Audits codebases for prototype artifacts before launch, replacing mock data with resilient transactional database queries. |

---

## 💡 3. Root Cause & Architectural Principle
Your AI built the database, the schema, the API routes, and the deployment pipeline. Heck, your AI shipped the working product to the customers. And at no point did anyone stop and ask what happens to this data when something goes wrong.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Inspect the existing code paths and identify unvalidated boundary inputs.
- [ ] Implement defense-in-depth guardrails preventing unauthorized state modification.
- [ ] Add automated regression tests verifying failure scenarios before shipping.

---

## 💻 5. Hardened Production Implementation
```sql
-- migrations/002_composite_indexes.sql
-- Eliminate table scans and guarantee unique constraints
CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS idx_users_org_email 
  ON users (organization_id, LOWER(email));

-- Covering index for frequent filtered lookups
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_customer_status_created 
  ON orders (customer_id, status) INCLUDE (total_amount, created_at);
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** The app is easy to rebuild. Your users' data is not.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI, it built the front end. Your AI built off. Your AI built the database, the schema, the API routes, and the deployment pipeline. Heck, your AI shipped the working product to the customers. And at no point did anyone stop and ask what happens to this data when something goes wrong. Your app, it's live right now. Real users, real data every day. And it's taking orders, messages, uploads, account settings, and payment. history. All of it lives in one place. One database, one provider, sitting in one region. No backup schedule, no retention policy, no tested restore. Actually, no plan for what happens next. So, if your database fails tonight, your users wake up to empty accounts. Not because you lost the app, but because you lost everything your users put inside of it. So, using AI to build the app, that's the easy part. The data, not so much. And your AI was never going to bring up backup strategy on its own because you really never asked for it. And nobody asked until the data is already gone. And that is not a win.

</div>
