# Episode 223: Your payment gateway handles the charge

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Async Queues & Webhooks (`صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZqZW3svYY_/) |

---

## 🚨 1. The Incident & Attack Vector
Your payment gateway handles the charge.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Fails to handle transient payment gateway 500 errors gracefully, abandoning transactions instead of retrying securely. | Applies automated exponential backoff with jitter on transient gateway failures while preserving idempotency tokens. |

---

## 💡 3. Root Cause & Architectural Principle
Your job is everything that happens after that. So, here are the three things you do right now to protect yourself. Step one, trust the event, not the button.

---

## ⚡ 4. Hardening Action Checklist
- [ ] trust the event, not the button.
- [ ] prevent the double charge.
- [ ] update the business, not just the database.

---

## 💻 5. Hardened Production Implementation
```typescript
// routes/webhook.ts
import express from 'express';
import Stripe from 'stripe';
import { redis } from '../lib/redis';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

export async function handleWebhook(req: express.Request, res: express.Response) {
  const sig = req.headers['stripe-signature'] as string;
  try {
    const event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET!);
    const isNew = await redis.set(`evt:${event.id}`, 'processed', 'NX', 'EX', 86400 * 3);
    if (!isNew) return res.status(200).json({ received: true, note: 'Duplicate event discarded' });
    
    // Process business logic idempotently...
    res.status(200).json({ received: true });
  } catch (err: any) {
    res.status(400).send(`Webhook Signature Verification Failed: ${err.message}`);
  }
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Your job is everything that happens after.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your payment gateway is not your payment system. Stripe already solved the hard part for you. Your job is everything that happens after that. So, here are the three things you do right now to protect yourself. Step one, trust the event, not the button. Stripe handles PCI, tokenization, and encryption. The entire checkout surface is on them. But the confirmation your app receives is a web hook. And if you trust a web hook without verifying it, you're trusting a stranger at your front door. Always verify the source, validate the signature, then act. That's a win. Step two, prevent the double charge. Every web hook can fire more than once. Network hiccup, timeout, retries. If your system processes the same event twice, you just charge someone twice. Item potency is not a feature. It is a policy to live by. One event, one action every single time. That's the win. Step three, update the business, not just the database. A successful charge should trigger a chain. Mark the invoice paid, activate the subscription, grant tenant access, send the receipt, update CRM. A charge that clears but does not trigger the workflow is a support ticket just waiting to happen. So, never trust the click. Verify the event, then run the business. That is the game and that's a win.

</div>
