# Episode 223: Your payment gateway handles the charge

> **Category:** Async Queues & Webhooks (صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی)  
> **Production Layer:** Layer 6  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DZqZW3svYY_/](https://www.instagram.com/reel/DZqZW3svYY_/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your payment gateway is not your payment system. Stripe already solved the hard part for you. Your job is everything that happens after that.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
Your job is everything that happens after that. So, here are the three things you do right now to protect yourself. Step one, trust the event, not the button.

---

## ⚡ 3. Hardening Action Checklist
- [ ] trust the event, not the button. Stripe handles PCI, tokenization, and encryption.
- [ ] prevent the double charge. Every web hook can fire more than once.
- [ ] update the business, not just the database. A successful charge should trigger a chain.

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

Your payment gateway is not your payment system. Stripe already solved the hard part for you. Your job is everything that happens after that. So, here are the three things you do right now to protect yourself. Step one, trust the event, not the button. Stripe handles PCI, tokenization, and encryption. The entire checkout surface is on them. But the confirmation your app receives is a web hook. And if you trust a web hook without verifying it, you're trusting a stranger at your front door. Always verify the source, validate the signature, then act. That's a win. Step two, prevent the double charge. Every web hook can fire more than once. Network hiccup, timeout, retries. If your system processes the same event twice, you just charge someone twice. Item potency is not a feature. It is a policy to live by. One event, one action every single time. That's the win. Step three, update the business, not just the database. A successful charge should trigger a chain. Mark the invoice paid, activate the subscription, grant tenant access, send the receipt, update CRM. A charge that clears but does not trigger the workflow is a support ticket just waiting to happen. So, never trust the click. Verify the event, then run the business. That is the game and that's a win.

</div>
