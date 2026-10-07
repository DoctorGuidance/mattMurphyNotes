# Episode 227: Bots are scanning every public repo for API keys right now

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZnYDewRV_h/) |

---

## 🚨 1. The Incident & Attack Vector
Bots are scanning every public repo for API keys right now.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |

---

## 💡 3. Root Cause & Architectural Principle
Step one, check your git history. Not your current code, your history. You might have removed the key from your file, but git remembers everything.

---

## ⚡ 4. Hardening Action Checklist
- [ ] check your git history.
- [ ] use Git Secret scanning.
- [ ] scope your keys.

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
> **Production Heuristic:** Plan accordingly.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Right now, like right now, there are bots scanning every single public GitHub repository for API keys, every commit, every pull request, every accidentally pushv file. Here are the three things you're going to do right now to prevent it. Step one, check your git history. Not your current code, your history. You might have removed the key from your file, but git remembers everything. That API key you accidentally committed 6 months ago and then deleted in the next commit. Guess what? It's still in the repository. Anyone who clones your repo can find it. If that repo was ever public, even for 5 minutes, assume that key was harvested by bots. Rotate it today. That's the win. Step two, use Git Secret scanning. GitHub has push protection. It scans every commit before it is pushed and blocks every known secret pattern. GitG Guardian does the same thing. Get leaks runs locally. Truffle hog digs through your entire history. These are the tools that catch the mistakes before it becomes a breach. And don't forget, turn on push protection. It takes 2 minutes. It prevents the kind of incident that takes two weeks to recover from. And that's a win. Step three, scope your keys. Most API providers let you restrict what a key can do. So, only specific endpoints, specific IP addresses, specific domains. If your Stripe key can do everything and it leaks, everything's at risk. If your Stripe key can only create checkout sessions from one domain, that blast radius nice and small. So scoping a key is free. Recovering from an unscoped key is not free. So the lesson is assume every key will leak and plan accordingly every day.

</div>
