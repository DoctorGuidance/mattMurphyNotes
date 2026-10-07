# Episode 200: Self-hosted or managed

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Testing, Staging & CI/CD (`تست، محیط‌های کاری، CI/CD و خط لوله استقرار`) |
| **Target Production Layer** | Layer 7 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaBItqrFHiF/) |

---

## 🚨 1. The Incident & Attack Vector
Self-hosted or managed.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |

---

## 💡 3. Root Cause & Architectural Principle
Here are the three things that are different between CI and local that you never checked. Step one, environmental variables. Your local machine has variables set from 6 months ago, hard set, right?

---

## ⚡ 4. Hardening Action Checklist
- [ ] environmental variables.
- [ ] database state.

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
> **Production Heuristic:** Know which currency you have.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your tests are passing locally, but they're failing in CI. You run them again locally and they pass again. Here are the three things that are different between CI and local that you never checked. Step one, environmental variables. Your local machine has variables set from 6 months ago, hard set, right? But your CI environment starts fresh every single run. That missing variable does not throw an error. It returns as undefined. And undefined, we all know, behaves differently than the value you had expected. Your test is passing because your local machine is remembering something, but CI does not. Step two, database state. Your local database has seed data from the last time you ran a test suite, right? Well, CI starts with an empty database every single time. The test that passes locally depends on data that exists because a different test created it last Tuesday. Tests that depend on other tests are not tests, they're assumptions. Step three. timing. Your local machine runs the test in 200 milliseconds. CI runs it on a shared runner with limited resources. The timeout you never thought about triggers. The race condition that never reproduces locally reproduces every single time under load. Right? So CI does not lie. Your local machine does. You have to trust the pipeline. So go check these things.

</div>
