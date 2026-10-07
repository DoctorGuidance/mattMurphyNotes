# Episode 295: Hit F12 on your live app

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Observability & Error Tracking |
| **Target Production Layer** | Layer 12 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYaNabIR0KG/) |

---

## 🚨 1. The Incident & Attack Vector
Hit F12 on your live app.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Leaves debugging statements (`console.log`) and internal error details active in production frontend code. | Strips `console.log` statements in production build pipelines and routes client errors to Sentry with PII scrubbing. |

---

## 💡 3. Root Cause & Architectural Principle
Hit F12. Click on sources. Now search for the word key.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Inspect the existing code paths and identify unvalidated boundary inputs.
- [ ] Implement defense-in-depth guardrails preventing unauthorized state modification.
- [ ] Add automated regression tests verifying failure scenarios before shipping.

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
> **Production Heuristic:** You left the vault open.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Open your browser. Go to your live app. Hit F12. Click on sources. Now search for the word key. If you see your open API key, if you see your Stripe secret key, if you see your database connection screen sitting right there in JavaScript, congratulations. Every single person who visits your app can see it, too. The AI puts the key where the code needs it. It doesn't think about or the code runs. Front-end code ships to the browser, right? The browser is the user's machine. Your secrets are now their secrets. This is important to know cuz someone takes your Stripe key, they're making charges on your account. And my buddy last week, $2500. Someone takes your Open AI key, they're running your bill up to 10,000 bucks while you're sleeping. You didn't get hacked, you left the vault wide open. The fix is coming next week. Follow along so you don't Don't miss it. It's an important one.

</div>
