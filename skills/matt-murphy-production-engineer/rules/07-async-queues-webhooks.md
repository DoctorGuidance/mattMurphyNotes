# 🛡️ Rulebook: Async Queues & Webhooks
**زیرسیستم:** صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی | **Domain ID:** `07-async-queues-webhooks` | **Target Layer:** Layer 6
> **Corpus Evidence:** Synthesized from 19 Matt Murphy Production Engineering Masterclasses (2 Critical, 7 High, 10 Medium).

---

## 👑 1. Executive Summary & Core Invariant
In modern high-scale software engineering, **Async Queues & Webhooks** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.
Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.

### ⚡ The Non-Negotiable Invariant:
> All incoming financial and external webhooks (Stripe, Paddle, GitHub) MUST verify HMAC signatures against the raw unparsed request buffer (`req.body` as raw Buffer, NOT parsed JSON). All state-mutating jobs must be idempotent via Redis or unique DB constraints.

---

## 🚨 2. Critical Attack Vectors & Failure Scenarios
Analysis of 19 incidents and breakdowns from this domain:

### 📍 Episode #006: Counterfeit Payment Confirmations Sent to Your Stripe Webhook (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** An attacker sends a forged HTTP POST request mimicking a Stripe `checkout.session.completed` event. The server parses the JSON body, marks the order as paid, and grants the attacker enterprise tier access for free.
- **The Root Cause:** Payment webhooks are unauthenticated public endpoints. You must verify digital signatures using the exact raw bytes received, and lock event IDs to guarantee idempotency.
- **Matt Murphy Takeaway:** *"Never trust an unverified webhook payload. Validate the raw cryptographic signature, or you are handing out your product for free."*

### 📍 Episode #062: You accept webhooks from Stripe without verifying the (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You accept webhooks from Stripe without verifying the signature.
- **The Root Cause:** That's a payment post request that hits your web hook endpoint. The body says payment succeeded. So your server reads that event, marks the order as paid, triggers fulfillment, ships out a product.
- **Matt Murphy Takeaway:** *"Stripe already secured their side. Secure yours."*

### 📍 Episode #028: Your server just charged the same card twice, provisioned (Severity: `HIGH`)
- **The Attack Vector / Incident:** Your server just charged the same card twice, provisioned the same user twice, sent the same email twice.
- **The Root Cause:** And that quite frankly is the problem. So your AI verified the web hook signature, clerk, resend, and GitHub all retry failed web hooks, right? But your server processes the same valid event two times.
- **Matt Murphy Takeaway:** *"The signature proves the sender. Idempotency proves you only acted once."*

### 📍 Episode #075: You have paid your payment processor $30,000 (Severity: `HIGH`)
- **The Attack Vector / Incident:** You have paid your payment processor $30,000.
- **The Root Cause:** So, 6 months of monthly minimums with your payment processor with zero customers, zero transactions, and zero revenue. Your infrastructure is running, but your business is not. And the meter is still ticking.
- **Matt Murphy Takeaway:** *"Stop activating expensive infrastructure before demand forces you to. Sandbox it. Demo it. Sell it. Then turn it on. Validate. Sell. Activate. Scale. In that order."*

### 📍 Episode #076: One webhook failed. It took your authentication, your (Severity: `HIGH`)
- **The Attack Vector / Incident:** One webhook failed. It took your authentication, your dashboard, and your checkout down with it.
- **The Root Cause:** One third party service hung up and your server thread stacked up waiting for a response that was never coming. And every new request queued behind them until nothing moved and it crashed. So, a single slow to dependency froze your entire product.
- **Matt Murphy Takeaway:** *"Your app is only as strong as its weakest dependency."*

### 📍 Episode #166: Your Stripe webhook failed silently for six hours (Severity: `HIGH`)
- **The Attack Vector / Incident:** Your Stripe webhook failed silently for six hours.
- **The Root Cause:** Not your monitoring, not your alerts, not your dashboard, but a paying customer. Here's what that moment actually costs your business. First, the direct costs.
- **Matt Murphy Takeaway:** *"Close the discovery gap or your customers close their accounts."*

### 📍 Episode #223: Your payment gateway handles the charge (Severity: `HIGH`)
- **The Attack Vector / Incident:** Your payment gateway handles the charge.
- **The Root Cause:** Your job is everything that happens after that. So, here are the three things you do right now to protect yourself. Step one, trust the event, not the button.
- **Matt Murphy Takeaway:** *"Your job is everything that happens after."*

### 📍 Episode #248: 45-second request (Severity: `HIGH`)
- **The Attack Vector / Incident:** A user clicks export report. Your API generates a PDF. It takes 45 seconds, so the request times out.
- **The Root Cause:** It takes 45 seconds, so the request times out. The user clicks it again. So now you're generating two PDFs.
- **Matt Murphy Takeaway:** *"Fix it with background architecture."*

### 📍 Episode #275: Your app hit Vercel’s limits (Severity: `HIGH`)
- **The Attack Vector / Incident:** Your app hit Vercel’s limits.
- **The Root Cause:** That's not a bug. That's your app telling you it's time for a bigger house. So here are the three things you can do right now to fix it.
- **Matt Murphy Takeaway:** *"That’s a graduation. Railway, Render, and Fly exist for exactly this moment."*

---

## ❌ 3. Vibe-Coding Traps vs. Production Reality Matrix
| # | ❌ The Vibe-Coding Trap (What Naive AI Builds) | ✅ Hardened Production Standard |
|---|:---|:---|
| **#006** | Relies on JSON body parameters directly without cryptographic signature checks; vulnerable to replay attacks. | Verifies signature against the raw request buffer (`constructEvent`); enforces idempotency locks via Redis. |
| **#028** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#046** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#062** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#075** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#076** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#084** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#098** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#107** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#122** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#123** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#127** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#129** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#166** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#185** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#223** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#248** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#266** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#275** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |

---

## 💻 4. Production-Hardened Code Patterns
The following hardened patterns demonstrate the exact production implementation required:

### Pattern 1: Hardened Implementation for #006 (Counterfeit Payment Confirmations Sent to Your Stripe Webhook)
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

### Pattern 2: Hardened Implementation for #028 (Your server just charged the same card twice, provisioned)
```typescript
-- migrations/002_composite_indexes.sql
-- Eliminate table scans and guarantee unique constraints
CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS idx_users_org_email 
  ON users (organization_id, LOWER(email));

-- Covering index for frequent filtered lookups
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_customer_status_created 
  ON orders (customer_id, status) INCLUDE (total_amount, created_at);
```

### Pattern 3: Hardened Implementation for #046 (Your AI built your Stripe checkout)
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

### Pattern 4: Hardened Implementation for #062 (You accept webhooks from Stripe without verifying the)
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

## 📋 5. Architectural Checklist & Verification Heuristics
Before shipping any code in this domain, verify each item:

- [ ] Mount raw body parser (`express.raw({ type: 'application/json' })`) on payment webhook routes.
- [ ] Store event IDs in Redis with an expiration window to discard duplicate webhook deliveries.
- [ ] Verify signatures with `stripe.webhooks.constructEvent` using your secret webhook signing key.
- [ ] but your AI stopped at step one.
- [ ] create checkout sessions on your server with prices from your database.
- [ ] direct your AI to store every event ID before it processes the handler logic.
- [ ] endpoint URL protection and IP allow listing.
- [ ] event item potency to prevent replay attack.
- [ ] set a replay window.
- [ ] signature verification on every incoming web hook.
- [ ] use Stripe price IDs instead of raw dollar amounts.
- [ ] verify payment through web hooks before or granting any access.

---

## 📚 6. Full Domain Catalog of Masterclasses
| Episode | Severity | Masterclass Title | Production Layer | Source Reel |
|:---:|:---:|:---|:---:|:---:|
| **#006** | `CRITICAL` | Counterfeit Payment Confirmations Sent to Your Stripe Webhook | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DduM5W5k4HF/) |
| **#028** | `HIGH` | Your server just charged the same card twice, provisioned | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DdMufvsE6Z3/) |
| **#046** | `MEDIUM` | Your AI built your Stripe checkout | Layer 6 | [Watch Reel](https://www.instagram.com/reel/Dcy-rVRD5jM/) |
| **#062** | `CRITICAL` | You accept webhooks from Stripe without verifying the | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DcbzcfyioD9/) |
| **#075** | `HIGH` | You have paid your payment processor $30,000 | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DcJx3MyDnHE/) |
| **#076** | `HIGH` | One webhook failed. It took your authentication, your | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DcJOWioldeu/) |
| **#084** | `MEDIUM` | 10,000 people are working on your idea right now | Layer 6 | [Watch Reel](https://www.instagram.com/reel/Db-7JyYDdas/) |
| **#098** | `MEDIUM` | Four AI security roles that did not exist two years ago. | Layer 6 | [Watch Reel](https://www.instagram.com/reel/Dbs8D1xAMnX/) |
| **#107** | `MEDIUM` | Your AI can find your perfect customer before you post a | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DbbaGawGG3_/) |
| **#122** | `MEDIUM` | Your customer just paid you. And they think you are a scam | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DbJSeKTFKW0/) |
| **#123** | `MEDIUM` | Your AI collected revenue from 12 states. You owe sales tax | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DbIyuH1D2Mx/) |
| **#127** | `MEDIUM` | Your revenue is disappearing every month and you cannot see | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DbETSNnjeGn/) |
| **#129** | `MEDIUM` | Your first customer dispute will freeze your Stripe account | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DbBsA6ljkur/) |
| **#166** | `HIGH` | Your Stripe webhook failed silently for six hours | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DadwoMajh8E/) |
| **#185** | `MEDIUM` | Revenue dropped 40% | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DaQKiPRk6KN/) |
| **#223** | `HIGH` | Your payment gateway handles the charge | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DZqZW3svYY_/) |
| **#248** | `HIGH` | 45-second request | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DZSYNBNxE1k/) |
| **#266** | `MEDIUM` | Your AI app works | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DY90q5PAPHa/) |
| **#275** | `HIGH` | Your app hit Vercel’s limits | Layer 6 | [Watch Reel](https://www.instagram.com/reel/DYzc-WUAOlA/) |
