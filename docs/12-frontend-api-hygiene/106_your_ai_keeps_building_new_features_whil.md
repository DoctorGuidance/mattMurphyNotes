# Episode 106: Your AI keeps building new features while your existing

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Frontend Architecture & API Hygiene |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbeZo5Zx5i2/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI keeps building new features while your existing features are broken.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Rushes to build shiny new frontend features while existing customer workflows suffer from reported, unaddressed regressions. | Prioritizes stabilizing existing user journeys and fixing reported bugs before commencing new UI feature development. |

---

## 💡 3. Root Cause & Architectural Principle
Instead of fixing it, you ask your AI to build the next feature. Guess what? Been there, done that.

---

## ⚡ 4. Hardening Action Checklist
- [ ] every new feature stacked on a broken foundation makes the foundation more fragile.
- [ ] Your customers are not asking for new features.
- [ ] direct your AI to run a feature health audit before it builds anything new.

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
> **Production Heuristic:** But your job as an AIdirected engineer is to tell it when to stop building and start fixing

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI keeps building new features while your existing features are totally broken and you keep letting it because building feels like progress. Something breaks, a payment flow fails, your onboarding drops people at step three. Instead of fixing it, you ask your AI to build the next feature. Guess what? Been there, done that. Because new features feel like momentum, and there's a lot of dopamine in the AI system. Fixing feels like you're going backwards. Here are three reasons that your instinct is destroying your product. Step one, every new feature stacked on a broken foundation makes the foundation more fragile. Your AI will happily add a notification system on top of an offflow that drops sessions. It will build a reporting dashboard that queries a database that has no indexes. So, your AI builds what you ask for, but it never asks whether the thing underneath it can hold the weight of what you're building. Step two, Your customers are not asking for new features. They are asking for the current ones to work perfectly. Go read your support inbox. The signal is not, I wish this had more features. It never is. The signal is this does not work the way I expected. New features attract customers. Sure, broken features lose them fast. And losing is more expensive than delaying. Step three, direct your AI to run a feature health audit before it builds anything new. What is live? What is broken? What has active users versus zero adoption? Broken and used gets fixed first. Broken and unused gets killed. Only after the foundation is solid do you build the next thing. Your AI will build forever if you let it. But your job as an AIdirected engineer is to tell it when to stop building and start fixing.

</div>
