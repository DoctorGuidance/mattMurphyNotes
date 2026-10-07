# Episode 130: Your AI built a product. It did not register a business

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbBCtEGiaMM/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI built a product. It did not register a business.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Charges paying customers for AI software before establishing registered business entities, exposing founders to personal liability. | Registers formal business entities, establishes dedicated commercial banking pipelines, and enforces terms of service. |

---

## 💡 3. Root Cause & Architectural Principle
And you're sitting there with no refund policy, no dispute response template, no chargeback threshold alerts because your AI never built any of it for you. So, here are the three things you direct your AI to set up before your first dispute hits. Number one, a published refund policy that matches your actual terms, not the Stripe default, not some template that you downloaded.

---

## ⚡ 4. Hardening Action Checklist
- [ ] a published refund policy that matches your actual terms, not the Stripe default, not some template that you downloaded.
- [ ] charge back threshold alerts.

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
> **Production Heuristic:** Murphy's law

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your first customer dispute will freeze your Stripe account. Not some of your funds, all of your funds, your rent money, your server cost, your next payroll frozen. And you're sitting there with no refund policy, no dispute response template, no chargeback threshold alerts because your AI never built any of it for you. So, here are the three things you direct your AI to set up before your first dispute hits. Number one, a published refund policy that matches your actual terms, not the Stripe default, not some template that you downloaded. You got to get your terms written out specific for you, linked from your checkout page, visible before the customer pays because when a customer disputes a charge and you have no published refund policy, Stripe sides with that customer every single time. It's not a bug. That's how the system works. Step two, charge back threshold alerts. Stripe will let your dispute rate climb silently until it crosses their threshold. Cha-ching. And then they act. By then, it's too late. So, your AI can configure alerts that warn you when disputes start trending. So, you can fix the problem before Stripe fixes it for you. The difference between monitoring and reacting is the difference between keeping your account and potentially losing it. Step three. a dispute response workflow. When a chargeback hits, you have days to respond with evidence, not weeks, not whenever you get around to it. You have days, and it has to be organized. So, your AI can build a response template for you with transaction logs, delivery confirmations, a refund policy with screenshots preloaded. Having that template built before the first claim, well, that means you respond with documentation instead of panicking like you've never dealt with it before. You built the revenue engine. Now you have to direct your AI to protect it for you. Because your first dispute is not a question of if, it's when. Murphy's law. It's coming.

</div>
