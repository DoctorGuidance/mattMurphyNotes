# Episode 250: Flat rate

> **Category:** Observability & Error Tracking (مشاهده‌پذیری، لاگ ساختاریافته و رهگیری خطا)  
> **Production Layer:** Layer 12  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DZP2LwegIXN/](https://www.instagram.com/reel/DZP2LwegIXN/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your app is free. People are using it. You need to charge money for it, but have no idea how to structure it.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
You need to charge money for it, but have no idea how to structure it. Well, flat rates feel a little bit wrong. Per seat feels a little random.

---

## ⚡ 3. Hardening Action Checklist
- [ ] pick your pricing metric based on what correlates to the most value. If your app saves time, charge per user.
- [ ] implement a credit system. Credits abstract away from the complexity.
- [ ] build usage tracking into your architecture from day one. Every billable action gets an event.

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

Your app is free. People are using it. You need to charge money for it, but have no idea how to structure it. Well, flat rates feel a little bit wrong. Per seat feels a little random. And usage base sounds cool until you try to implement it. Here are three things you can do right now to decide on pricing. Step one, pick your pricing metric based on what correlates to the most value. If your app saves time, charge per user. More users means more time saved. If your app processes data, charge per unit processed. More data means more value. And if your app generates output, charge per generation. More output means more ROI. The metric that you're using should scale with the customer's success. When they win more, you earn more. That alignment keeps churn really low, and that's a win. Step two, implement a credit system. Credits abstract away from the complexity. A user buys a th000 credits per month. An API call costs one credit. An AI generation costs 10 credits. A document export costs five credits. You can adjust cost per action without changing your price range at all. Stripe billing supports metered usage reporting natively. Report credit consumption via an API. Stripe handles invoicing. So that's a win. Step three, build usage tracking into your architecture from day one. Every billable action gets an event. User X performed action Y at time stamp Z. Store these events in a dedicated table of some sort. Your billing system reads from this table. Your analytic system reads from the same table. One source of truth for revenue and usage. That's a win. Do not try to reconstruct billing data from application logs later. That's not a win. Build the event stream now. So tell me, how are you charging? Does it feel broken? Dr. You sin.

</div>
