# Episode 129: Your first customer dispute will freeze your Stripe account

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Async Queues & Webhooks (`صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbBsA6ljkur/) |

---

## 🚨 1. The Incident & Attack Vector
Your first customer dispute will freeze your Stripe account. Not some of your funds, all of your funds, your rent money, your server cost, your next payroll frozen. And you're sitting there with no refund policy, no dispute response template, no chargeback threshold alerts because your AI never built any of it for you.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
And you're sitting there with no refund policy, no dispute response template, no chargeback threshold alerts because your AI never built any of it for you. So, here are the three things you direct your AI to set up before your first dispute hits. Number one, a published refund policy that matches your actual terms, not the Stripe default, not some template that you downloaded.

---

## ⚡ 4. Hardening Action Checklist
- [ ] a published refund policy that matches your actual terms, not the Stripe default, not some template that you downloaded. You got to get your terms written out specific for you, linked from your checkout page, visible before the customer pays because when a customer disputes a charge and you have no published refund policy, Stripe sides with that customer every single time.
- [ ] charge back threshold alerts. Stripe will let your dispute rate climb silently until it crosses their threshold.

---

## 💻 5. Hardened Production Implementation
```typescript
// Raw Buffer Webhook Signature Verification
const sig = req.headers['stripe-signature'] as string;
const event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET!);
// Idempotency check:
const isNew = await redis.set(`evt:${event.id}`, '1', 'NX', 'EX', 86400 * 3);
if (!isNew) return res.status(200).json({ received: true });
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Never deploy unverified AI-generated code directly to production without testing failure modes.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your first customer dispute will freeze your Stripe account. Not some of your funds, all of your funds, your rent money, your server cost, your next payroll frozen. And you're sitting there with no refund policy, no dispute response template, no chargeback threshold alerts because your AI never built any of it for you. So, here are the three things you direct your AI to set up before your first dispute hits. Number one, a published refund policy that matches your actual terms, not the Stripe default, not some template that you downloaded. You got to get your terms written out specific for you, linked from your checkout page, visible before the customer pays because when a customer disputes a charge and you have no published refund policy, Stripe sides with that customer every single time. It's not a bug. That's how the system works. Step two, charge back threshold alerts. Stripe will let your dispute rate climb silently until it crosses their threshold. Ch-ching and then they act. By then, it's too late. So, your AI can configure alerts that warn you when disputes start trending. So, you can fix the problem before Stripe fixes it for you. The difference between monitoring and reacting is the difference between keeping your account and potentially losing it. Step three. a dispute response workflow. When a chargeback hits, you have days to respond with evidence, not weeks, not whenever you get around to it. You have days, and it has to be organized. So, your AI can build a response template for you with transaction logs, delivery confirmations, a refund policy with screenshots preloaded. Having that template built before the first claim, well, that means you respond with documentation instead of panicking like you've never dealt with it before. You built the revenue engine. Now you have to direct your AI to protect it for you. Because your first dispute is not a question of if, it's when. Murphy's law. It's coming.

</div>
