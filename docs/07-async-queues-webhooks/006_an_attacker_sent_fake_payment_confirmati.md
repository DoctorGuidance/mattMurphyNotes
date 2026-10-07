# Episode 006: An attacker sent fake payment confirmations to your Stripe

> **Category:** Async Queues & Webhooks (صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی)  
> **Production Layer:** Layer 6  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DduM5W5k4HF/](https://www.instagram.com/reel/DduM5W5k4HF/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your AI integrated those Stripe web hooks, but an attacker just sent fake payment confirmation to your Stripe web hook endpoint and your application processed every single one of them. Stripe signs every event it sends. Your AI never checked the signature.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
Your AI never checked the signature. So when a payment succeeds, Stripe sends a post to your endpoint. Your application reads the event body and provisions the service.

---

## ⚡ 3. Hardening Action Checklist
- [ ] Stripe includes a signature header with every web hook event. The signature is a hash of the payload using a secret only you and Stripe share.
- [ ] this is not limited to Stripe at all. Clerk signs user events.
- [ ] an attacker who captures a legitimate web hook payload can absolutely replay it. Same event, same signature, different timing, right?

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Raw Buffer Webhook Signature Verification
const sig = req.headers['stripe-signature'] as string;
const event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET!);
// Idempotency check:
const isNew = await redis.set(`evt:${event.id}`, '1', 'NX', 'EX', 86400 * 3);
if (!isNew) return res.status(200).json({ received: true });
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your AI integrated those Stripe web hooks, but an attacker just sent fake payment confirmation to your Stripe web hook endpoint and your application processed every single one of them. Stripe signs every event it sends. Your AI never checked the signature. So when a payment succeeds, Stripe sends a post to your endpoint. Your application reads the event body and provisions the service. So the endpoint accepts any post request with the right JSON structure. A web hook without signature verification is a command line anyone can type. It's time to tighten it up. Step one, Stripe includes a signature header with every web hook event. The signature is a hash of the payload using a secret only you and Stripe share. So your AI skipped verification because the integration worked without it. An attacker sends a post with a crafted event body, whether it's payment succeeded, subscription upgraded, or access granted. And so your application processes it because it never checked who sent it. So direct your AI to verify the Stripe web hook signature using your endpoint secret before processing any event at all. That's a win. Step two, this is not limited to Stripe at all. Clerk signs user events. GitHub signs repository web hooks. So every major service signs their payload. your AI integrated three services and verified none of them. So each unverified endpoint is a separate door without a lock. So direct your AI to audit every web hook endpoint in your application and implement signature verification for each one of those providers. That's a win. And step three, an attacker who captures a legitimate web hook payload can absolutely replay it. Same event, same signature, different timing, right? So a payment event replayed three times provisions three separate accounts. So direct your AI to store processed event ids and reject all duplicates. Stripe event ids are unique. Use them everywhere. Your web hook endpoint is not a notification. It's a command. Always verify who sent it before you execute it. That's the way it rolls.

</div>
