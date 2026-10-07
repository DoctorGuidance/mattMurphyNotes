# Episode 046: Your AI built your Stripe checkout

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Async Queues & Webhooks (`صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Dcy-rVRD5jM/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI built your Stripe checkout.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |

---

## 💡 3. Root Cause & Architectural Principle
So if you change it to $1, Stripe will still process it. So your AI integrated Stripe, your user clicks the buy button, your front end sends a checkout request with the price in the body, and Stripe charges whatever amount your code sends. So your server never checks whether that number matches your actual product pricing.

---

## ⚡ 4. Hardening Action Checklist
- [ ] create checkout sessions on your server with prices from your database.
- [ ] use Stripe price IDs instead of raw dollar amounts.
- [ ] verify payment through web hooks before or granting any access.

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
> **Production Heuristic:** Your checkout page is not your pricing. Your server is.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI built your Stripe checkout. The price lives in your front end. So if you change it to $1, Stripe will still process it. So your AI integrated Stripe, your user clicks the buy button, your front end sends a checkout request with the price in the body, and Stripe charges whatever amount your code sends. So your server never checks whether that number matches your actual product pricing. And that's the hack. So now your checkout is just a suggestion. Here's how we're going to make it a contract. Step one, create checkout sessions on your server with prices from your database. The client sends a product ID, never a dollar amount. So, your server looks up the price, creates the Stripe session with the verified amount, and returns the session to the client. So, direct your AI to move all Stripe session creation to a server endpoint that ignores any price the frontend sends. That's definitely a win. Step two, use Stripe price IDs instead of raw dollar amounts. So Stripe will let you create price objects tied to your products in your dashboard. So when your server references a price ID, the charge amount is locked inside of Stripe system. So no code on your side can ever override it. So direct your AI to replace every raw amount in your checkout flow with a Stripe price ID. That's a win. And number three, verify payment through web hooks before or granting any access. Your checkout success page is not proof of payment. A user can still navigate to your success URL without paying. So direct your AI to implement a Stripe web web hook listener so that it confirms the payment event, validates the amount against your product price, and only then provisions access to the purchase resource. Your checkout folks is not your pricing. Your server is and right now your server believes whatever the browser is telling it at checkout. So, let's get it cleaned up. That's a win.

</div>
