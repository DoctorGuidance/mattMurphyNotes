# Episode 006: Counterfeit Payment Confirmations Sent to Your Stripe Webhook

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Async Queues & Webhooks (`صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DduM5W5k4HF/) |

---

## 🚨 1. The Incident & Attack Vector
An attacker sends a forged HTTP POST request mimicking a Stripe `checkout.session.completed` event. The server parses the JSON body, marks the order as paid, and grants the attacker enterprise tier access for free.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Relies on JSON body parameters directly without cryptographic signature checks; vulnerable to replay attacks. | Verifies signature against the raw request buffer (`constructEvent`); enforces idempotency locks via Redis. |

---

## 💡 3. Root Cause & Architectural Principle
Payment webhooks are unauthenticated public endpoints. You must verify digital signatures using the exact raw bytes received, and lock event IDs to guarantee idempotency.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Mount raw body parser (`express.raw({ type: 'application/json' })`) on payment webhook routes.
- [ ] Verify signatures with `stripe.webhooks.constructEvent` using your secret webhook signing key.
- [ ] Store event IDs in Redis with an expiration window to discard duplicate webhook deliveries.

---

## 💻 5. Hardened Production Implementation
```typescript
// routes/stripeWebhook.ts
import express from 'express';
import Stripe from 'stripe';
import { redis } from '../lib/redis';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

export async function handleStripeWebhook(req: express.Request, res: express.Response) {
  const sig = req.headers['stripe-signature'] as string;
  try {
    const event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET!);
    
    // Idempotency Gate:
    const isNew = await redis.set(`evt:${event.id}`, 'processed', 'NX', 'EX', 86400 * 3);
    if (!isNew) return res.status(200).json({ received: true, note: 'Duplicate event ignored' });

    // Process event...
    res.status(200).json({ received: true });
  } catch (err: any) {
    res.status(400).send(`Webhook Signature Error: ${err.message}`);
  }
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Never trust an unverified webhook payload. Validate the raw cryptographic signature, or you are handing out your product for free.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI integrated those Stripe web hooks, but an attacker just sent fake payment confirmation to your Stripe web hook endpoint and your application processed every single one of them. Stripe signs every event it sends. Your AI never checked the signature. So when a payment succeeds, Stripe sends a post to your endpoint. Your application reads the event body and provisions the service. So the endpoint accepts any post request with the right JSON structure. A web hook without signature verification is a command line anyone can type. It's time to tighten it up. Step one, Stripe includes a signature header with every web hook event. The signature is a hash of the payload using a secret only you and Stripe share. So your AI skipped verification because the integration worked without it. An attacker sends a post with a crafted event body, whether it's payment succeeded, subscription upgraded, or access granted. And so your application processes it because it never checked who sent it. So direct your AI to verify the Stripe web hook signature using your endpoint secret before processing any event at all. That's a win. Step two, this is not limited to Stripe at all. Clerk signs user events. GitHub signs repository web hooks. So every major service signs their payload. your AI integrated three services and verified none of them. So each unverified endpoint is a separate door without a lock. So direct your AI to audit every web hook endpoint in your application and implement signature verification for each one of those providers. That's a win. And step three, an attacker who captures a legitimate web hook payload can absolutely replay it. Same event, same signature, different timing, right? So a payment event replayed three times provisions three separate accounts. So direct your AI to store processed event ids and reject all duplicates. Stripe event ids are unique. Use them everywhere. Your web hook endpoint is not a notification. It's a command. Always verify who sent it before you execute it. That's the way it rolls.

</div>
