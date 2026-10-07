# Episode 247: $900month hosting

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Cloud Infrastructure & FinOps (`معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZSzeK0RgCd/) |

---

## 🚨 1. The Incident & Attack Vector
Your app has 200 users. Your infrastructure bill, it's $900 a month. If you charge $10 a month per user, half your revenue, it's going to AWS.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |

---

## 💡 3. Root Cause & Architectural Principle
If you charge $10 a month per user, half your revenue, it's going to AWS. Here are three fixes you can do right now. Step one, audit your always on resources.

---

## ⚡ 4. Hardening Action Checklist
- [ ] audit your always on resources.
- [ ] set spend alerts at every layer.
- [ ] right size your database.

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
> **Production Heuristic:** That math kills businesses.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your app has 200 users. Your infrastructure bill, it's $900 a month. If you charge $10 a month per user, half your revenue, it's going to AWS. Here are three fixes you can do right now. Step one, audit your always on resources. That database that's running 247 on a pro plan might be able to make changes there. So, check your traffic. If you have zero requests between midnight and 6:00 a.m., that means you're paying for idle compute. Most platforms will allow you to scale to zero. Neon pauses after 5 minutes. Railway will scale to zero on their obby plan. So, pay for compute when users are active, not when they're sleeping. That's a win. Step two, set spend alerts at every layer. Versel, Superbase, OpenAI, AWS, all of them have billing alerts. Set them at 50, then 75, then 90% of your budget. Set a hard cap anywhere possible. One misconfigured function Calling Opus 47 in a loop can burn $300 an hour. Ask me how. I know. Step three, right size your database. Superbase Pro is $25 a month for 8 gigs of RAM, but if you're only using one gig, you're overpaying. Downgrade it, monitor it, scale it when metrics demand it, not because you wanted it. Audit, alert, and right size. Your margins determine everything. Whether your platform is going to survive or whether you're going to bleed out slowly. Hope this helps.

</div>
