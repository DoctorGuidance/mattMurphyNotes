# Episode 164: Three questions every builder should answer before launch

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Frontend Architecture & API Hygiene (`معماری فرانت‌اند، طراحی واسط و بهداشت API`) |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DagUP6WjhPx/) |

---

## 🚨 1. The Incident & Attack Vector
Three questions every builder should answer before launch.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes successful network responses and relies solely on frontend validation for business state in 'Three questions every builder should answer before launch'. | Implements all 4 UI states, treats client state as untrusted, and verifies payload schemas on both client and server. |

---

## 💡 3. Root Cause & Architectural Principle
Question one, do you have cyber liability insurance? Their eyes light up. When you handle someone else's data and something goes wrong, you're personally liable.

---

## ⚡ 4. Hardening Action Checklist
- [ ] have you read your platform's terms of service?
- [ ] that stumps most people.

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
> **Production Heuristic:** Protecting the business underneath it is where most never start.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

This is a conversation I never expected to be having with vibe coders, but I'm having it almost every week now. Someone builds a product with AI, it works, they're ready to launch, and I ask them three questions that stop the conversation in its tracks. Question one, do you have cyber liability insurance? Their eyes light up. When you handle someone else's data and something goes wrong, you're personally liable. Not your LLC. You are. A data breach on an uninsured platform means you're paying for notification, remediation, legal fees, and any damages out of your own pocket. Cyber liability insurance costs $200 to $600 a year for most small SAS platforms. $200 to protect yourself from a breach that could cause 50,000. That's a win. And here's the part that nobody's talking to you about. Most insurance underwriters want to see basic security practices before they're even going to cover you. So, vulnerability scans, access controls, encryption at rest. The security audit is not just a good practice. It is a requirement for the coverage that protects your whole business. Question number two, have you read your platform's terms of service? Does anybody read a terms of service? Superbase for sale, Stripe. Every platform has terms that define what happens when things go wrong. Most include limitation of liability clauses that cap their exposure at what you paid them last month. month. So you paid Superbase 25 bucks. If their service causes a data loss that cost you 10 grand, their liability 25 bucks. Yours 10 grand plus. So understanding your platform agreement is not legal paranoia. It is basic business literacy. And question number three that stumps most people. Does your privacy policy match what your app actually does? Your app collects emails, payment information, and usage data. Your privacy policy is a template you copied from the internet that references cookies and nothing else. If a user in Europe asks you to delete their data under GDPR and your database was never built for deletion, you have a compliance violation that carries some real serious fines. Your AI can build the product. Your AI can even draft the privacy policy, but you have to direct it with the right requirements. And most builders do not know what the requirements are until the first in didn't teaches them all about it. So building the product is usually the easiest part. Protecting the business underneathneath it is where most builders never start. Right? So start before you launch, not after. It's a business. It's a product. It's not just a build.

</div>
