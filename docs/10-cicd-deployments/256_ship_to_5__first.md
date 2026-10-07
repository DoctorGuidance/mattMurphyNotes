# Episode 256: Ship to 5% first

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Testing, Staging & CI/CD (`تست، محیط‌های کاری، CI/CD و خط لوله استقرار`) |
| **Target Production Layer** | Layer 7 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZKp4rPAasV/) |

---

## 🚨 1. The Incident & Attack Vector
You push to main, the deploy runs. Every user gets a new code simultaneously. If it is broken, every user is broken simultaneously.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Rolls out major application updates to all users at once, risking widespread customer churn during regressions. | Automates phased rollouts (5% -> 25% -> 100%) with automated rollbacks triggered if error rates exceed 0.1%. |

---

## 💡 3. Root Cause & Architectural Principle
If it is broken, every user is broken simultaneously. That's not a deployment. That's a dice roll.

---

## ⚡ 4. Hardening Action Checklist
- [ ] deploy to 5% of the traffic first.
- [ ] gate rollouts with feature flags.
- [ ] automate the promotion.

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
> **Production Heuristic:** Never break prod for everyone.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

You push to main, the deploy runs. Every user gets a new code simultaneously. If it is broken, every user is broken simultaneously. That's not a deployment. That's a dice roll. Here are the three things you do right now to fix it. Step one, deploy to 5% of the traffic first. Verscell supports gradual rollouts natively. So does Cloudflare. Push your new version, route 5% of requests to it, make sure everything's working. working. The other 95% stay on the current stable version until you're ready to move them. Monitor error rates for 15 minutes. If errors spike, roll back instantly. Nobody even noticed. Step two, gate rollouts with feature flags. Launch Darkly, Flag Smmith, or even a simple JSON config in your database. New feature ships to production behind a flag. You enable it for internal users first, then beta users, then 10% Then everybody, if something breaks, kill the flag. The code stays deployed but the feature disappears. No roll back needed. Step three, automate the promotion. Your CI pipeline should watch error rates after Canary deployments. If error rate stays below your threshold for, let's say, 30 minutes, automatically promote to 100%. If it exceeds the threshold, automatically roll it back. No human watching a dashboard at midnight. That's old stuff. Just GitHub action plus your error monitoring API. 20 lines of code between you and a fully automated safe deployment. 5% canary feature flags and automated promotion. You never ship broken code to all your users again. So tell me, what's your scariest deploy story? Share it in the comments.

</div>
