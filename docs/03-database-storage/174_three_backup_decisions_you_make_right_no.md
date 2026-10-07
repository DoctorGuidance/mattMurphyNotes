# Episode 174: Three backup decisions you make right now

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Database & Storage Engineering |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaYW16Ojg1C/) |

---

## 🚨 1. The Incident & Attack Vector
Three backup decisions you make right now.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Postpones backup configuration decisions until after production deployment, risking irreversible data corruption. | Establishes automated daily backup snapshots, geo-replicated offsite storage, and defines explicit RPO/RTO metrics. |

---

## 💡 3. Root Cause & Architectural Principle
Step one, frequency. Your database changes every time a user does anything. A daily backup means you accept losing up to 24 hours of their data.

---

## ⚡ 4. Hardening Action Checklist
- [ ] frequency.
- [ ] location.
- [ ] test the restore.

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
> **Production Heuristic:** Decide before your users decide for you.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your app has no backup strategy and that means that your users have no protection. So here are the three things you need to decide right now to fix it. Step one, frequency. Your database changes every time a user does anything. A daily backup means you accept losing up to 24 hours of their data. If your app processes payments, that's 24 hours of revenue you can't recover. So point in time recovery captur ers every transaction continuously and almost every managed database supports it. It's a setting. Turn it on. That's a win. Step two, location. Your backup lives on the same server as your database. When the server dies, the backup dies with it. That's not a win. That is not even a backup. That is a second copy of the exact same risk. So cross region or offsite backup is the backup that must survive things that kill your primary server. Step three, test the restore. And for the people in the back, test the restore. Your backup has been running for months. You've never restored it. A backup you've never tested is not a safety net. It's not even a backup. It's a guess. So, restore to a test environment once a month minimum. Verify that data. Verify the app runs because the worst time to find out your backup is broken is during the outage you need a backup. So, Oh, decide before your users decide for you.

</div>
