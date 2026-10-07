# Episode 062: You accept webhooks from Stripe without verifying the

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Async Queues & Webhooks (`صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcbzcfyioD9/) |

---

## 🚨 1. The Incident & Attack Vector
You accept webhooks from Stripe without verifying the signature.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Accepts incoming webhooks without verifying digital signatures, letting attackers inject counterfeit payment confirmations. | Validates cryptographic webhook signatures against the raw unparsed payload buffer before dispatching business logic. |

---

## 💡 3. Root Cause & Architectural Principle
That's a payment post request that hits your web hook endpoint. The body says payment succeeded. So your server reads that event, marks the order as paid, triggers fulfillment, ships out a product.

---

## ⚡ 4. Hardening Action Checklist
- [ ] signature verification on every incoming web hook.
- [ ] event item potency to prevent replay attack.
- [ ] endpoint URL protection and IP allow listing.

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
> **Production Heuristic:** Stripe already secured their side. Secure yours.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

You accept web hooks from Stripe without verifying the signature. Now anyone can send your server a fake payment confirmation. That's a payment post request that hits your web hook endpoint. The body says payment succeeded. So your server reads that event, marks the order as paid, triggers fulfillment, ships out a product. However, you never checked whether Stripe actually sent you that request. You see, an attacker who knows your endpoint URL can send the same payload and your server will process it the exact same way. What does that mean? Free products, free subscriptions, fake revenue in your dashboard. You see, Stripe signs every web hook. It's your server that's ignoring the signature. Here's how we're going to fix it. Step one, signature verification on every incoming web hook. Stripe includes a signature header on every event. Your server must validate that signature against your web hook, signing secret before or processing any event. If the signature doesn't match, reject the request immediately. So, direct your AI to implement stripe web web hook signature verification using the official SDK method that will compare the signature headers against your endpoint signing secret and that's a win. Step two, event item potency to prevent replay attack. An attacker can capture a legitimate web hook and replay it. Your server processes that same payment event twice. Do duplicate fulfillment, duplicate credits, duplicate access. So, Directory AI to implement item potency tracking. That way, it logs every processed event ID and rejects any event that has already been handled. And step three, endpoint URL protection and IP allow listing. Your web hook URL should not be guessable. A predictable path like web hooks back/stripe is an open invitation. Use a randomized path or token in the URL. RL where possible restrict incoming requests to stripes published IP ranges. So directory AI to configure web hook endpoint security with a non-guessable URL and IP allow listing based on Stripe's current IP list. Stripe already secured their side. It's time to secure yours.

</div>
