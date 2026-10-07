# Episode 028: Your server just charged the same card twice, provisioned

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Async Queues & Webhooks (`صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdMufvsE6Z3/) |

---

## 🚨 1. The Incident & Attack Vector
Your server just charged the same card twice, provisioned the same user twice, sent the same email twice.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Processes asynchronous jobs or webhooks without raw signature checks or idempotency locks in 'Your server just charged the same card twice, provisioned'. | Verifies webhook HMAC signatures on raw buffers and uses Redis idempotency keys with Dead-Letter Queues (DLQ). |

---

## 💡 3. Root Cause & Architectural Principle
And that quite frankly is the problem. So your AI verified the web hook signature, clerk, resend, and GitHub all retry failed web hooks, right? But your server processes the same valid event two times.

---

## ⚡ 4. Hardening Action Checklist
- [ ] but your AI stopped at step one.
- [ ] direct your AI to store every event ID before it processes the handler logic.
- [ ] set a replay window.

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
> **Production Heuristic:** The signature proves the sender. Idempotency proves you only acted once.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Uh-oh. Your server just charged the same credit card twice, provisioned the same user twice, and sent the exact same email to them twice, but every web hook signature was totally valid. And that quite frankly is the problem. So your AI verified the web hook signature, clerk, resend, and GitHub all retry failed web hooks, right? But your server processes the same valid event two times. So signature ver ification is step one. Item potency is step two, but your AI stopped at step one. So, let's get it fixed. Number one, direct your AI to store every event ID before it processes the handler logic. Check the ID against your database. If it already exists, return a success response and do nothing at all. If it does not, store it, then process it. The order definitely matters. Store first, process second. If the handler crashes mid process, process. The retry sees the stored ID and skips the duplicate process. Without this, every network timeout, every slow response, every infrastructure hiccup triggers a retry with a valid signature that your server treats as a brand new event. So, a user provisioned twice, a payment recorded twice, and an email sent twice. That web hook wasn't forged, folks. It was just delivered more than once. And that is not a win. Number two, set a replay window. Reject event IDs older than 24 hours. Without a window, your storage grows indefinitely, and an attacker can replay a captured web hook from 3 months ago with a valid signature. So, a timestamp checks close that gap permanently. Direct your AI to compare the events creation time against a 24-hour threshold and reject anything. side of it. That's a win. And number three, return a success response for all duplicates. Right? If your server returns an error on a duplicate event, the provider will retry it again. So more duplicates equals more duplicate processing, which equals more duplicate emails. That's not a win. So a success response tells the provider the event was received even if your server already handled it. Especially if your server already handled it, right? So the sign proves the sender. Item potency proves you only acted once. And that that's the double check system that works.

</div>
