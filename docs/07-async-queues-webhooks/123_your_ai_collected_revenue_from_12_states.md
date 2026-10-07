# Episode 123: Your AI collected revenue from 12 states. You owe sales tax

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Async Queues & Webhooks (`صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbIyuH1D2Mx/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI collected revenue from 12 states. You owe sales tax in 9 of them.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Collects multi-state e-commerce revenue without calculating dynamic jurisdictional sales tax, incurring massive tax penalties. | Integrates automated sales tax webhooks (Stripe Tax/TaxJar) calculating precise jurisdictional liability per transaction. |

---

## 💡 3. Root Cause & Architectural Principle
The letter from the state revenue department is already on its way. And you did not even know you had an obligation. Selling a digital subscription to a customer in another state can trigger a tax obligation in that state.

---

## ⚡ 4. Hardening Action Checklist
- [ ] a nexus exposure map.
- [ ] tax collection at checkout.
- [ ] a filing calendar.

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
> **Production Heuristic:** And they have your Stripe data

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI collected revenue from 12 different states. Now you owe sales tax in nine of them. The letter from the state revenue department is already on its way. And you did not even know you had an obligation. Selling a digital subscription to a customer in another state can trigger a tax obligation in that state. It's called Nexus. Most builders have never heard the word until they get the letter. Here are three things you direct your AI to build before a state revenue department finds you first. Step one, a nexus exposure map. Direct your AI to pull your customer list by state and cross reference it against each state's economic nexus thresholds. Some states trigger at 100k in revenue. Some states trigger at 200 transactions. Some trigger at the first dollar of digital goods. So, the thresholds are different everywhere. And your AI can map them out in an hour. SAS sales tax is a whole different animal and it's coming for every builder collect. ing recurring revenue across state lines. Step two, tax collection at checkout. Your AI integrated Stripe. Stripe has tax automation built in, but your AI never turned it on because you never told it sales tax applies to digital subscriptions. Happens all the time. The integration takes an afternoon. The back taxes from 3 years of uncollected obligations takes a little bit longer to fix. And step three, a filing calendar. Once you are collect you have to remit. Every state has different remittance filing frequencies, different deadlines, and different penalties for late payments. Your AI can build a compliance calendar that tracks every filing date for every state where you have a nexus. Without it, you're collecting tax from your customers and not sending it to the state. That is not an oversight. It's a complete liability. And your AI never brings up sales tax. It does not even know what Nexus means. But the state of California They do. And they have your Stripe data.

</div>
