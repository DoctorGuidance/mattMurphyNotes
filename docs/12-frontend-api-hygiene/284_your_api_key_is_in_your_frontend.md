# Episode 284: Your API key is in your frontend

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Frontend Architecture & API Hygiene (`معماری فرانت‌اند، طراحی واسط و بهداشت API`) |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYpNvXGg_WM/) |

---

## 🚨 1. The Incident & Attack Vector
Your API key is in your frontend.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Exposes private API secret keys in client-side bundles by prefixing sensitive tokens with public build prefixes (`NEXT_PUBLIC_`). | Keeps private API secrets on server backends, exposing lightweight proxy endpoints to frontend clients. |

---

## 💡 3. Root Cause & Architectural Principle
Every visitor to your app, they can see it, too. Here's how you lock it down in 15 minutes. Step one, move all secrets to server side environment variables.

---

## ⚡ 4. Hardening Action Checklist
- [ ] move all secrets to server side environment variables.
- [ ] create a proxy API route.
- [ ] rotate every key that was ever in your front end.

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
> **Production Heuristic:** Be honest

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Last week, I told you to hit F12 and search for the word key. If you found your API key sitting in your front-end JavaScript, that message was for you. Every visitor to your app, they can see it, too. Here's how you lock it down in 15 minutes. Step one, move all secrets to server side environment variables. Not in your code, not in your config file that ships to the browser, not in thev file that's committed to git, server side only. Vers has an EMV vase. Netlfi has an EMV vase. Railway, Render, Fly, they all have them. Put your keys there. Delete them from your code. Step two, create a proxy API route. Your front end should never call an external API directly. Instead, front end calls your server. Your server calls the API. The key lives on the server. The browser never sees it. One route, one file, 15 lines of code. Your secrets are invisible. Step three, rotate every key that was ever in your front end. Even if you just moved it, even if you think no one saw it, your git history remembers everything. If a key was ever committed, it's already been scraped. Go to open AI, go to Stripe, generate new keys, update your EMV vars. Old keys, dead keys out. Get them out. How many of your keys are still in your frontend code right now? Be honest. Drop it in the comments.

</div>
