# Episode 046: Your AI built your Stripe checkout

> **Category:** Async Queues & Webhooks (صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی)  
> **Production Layer:** Layer 6  
> **Official Instagram Reel:** [https://www.instagram.com/reel/Dcy-rVRD5jM/](https://www.instagram.com/reel/Dcy-rVRD5jM/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your AI built your Stripe checkout. The price lives in your front end. So if you change it to $1, Stripe will still process it.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
So if you change it to $1, Stripe will still process it. So your AI integrated Stripe, your user clicks the buy button, your front end sends a checkout request with the price in the body, and Stripe charges whatever amount your code sends. So your server never checks whether that number matches your actual product pricing.

---

## ⚡ 3. Hardening Action Checklist
- [ ] create checkout sessions on your server with prices from your database. The client sends a product ID, never a dollar amount.
- [ ] use Stripe price IDs instead of raw dollar amounts. So Stripe will let you create price objects tied to your products in your dashboard.
- [ ] verify payment through web hooks before or granting any access. Your checkout success page is not proof of payment.

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

Your AI built your Stripe checkout. The price lives in your front end. So if you change it to $1, Stripe will still process it. So your AI integrated Stripe, your user clicks the buy button, your front end sends a checkout request with the price in the body, and Stripe charges whatever amount your code sends. So your server never checks whether that number matches your actual product pricing. And that's the hack. So now your checkout is just a suggestion. Here's how we're going to make it a contract. Step one, create checkout sessions on your server with prices from your database. The client sends a product ID, never a dollar amount. So, your server looks up the price, creates the Stripe session with the verified amount, and returns the session to the client. So, direct your AI to move all Stripe session creation to a server endpoint that ignores any price the frontend sends. That's definitely a win. Step two, use Stripe price IDs instead of raw dollar amounts. So Stripe will let you create price objects tied to your products in your dashboard. So when your server references a price ID, the charge amount is locked inside of Stripe system. So no code on your side can ever override it. So direct your AI to replace every raw amount in your checkout flow with a Stripe price ID. That's a win. And number three, verify payment through web hooks before or granting any access. Your checkout success page is not proof of payment. A user can still navigate to your success URL without paying. So direct your AI to implement a Stripe web web hook listener so that it confirms the payment event, validates the amount against your product price, and only then provisions access to the purchase resource. Your checkout folks is not your pricing. Your server is and right now your server believes whatever the browser is telling it at checkout. So, let's get it cleaned up. That's a win.

</div>
