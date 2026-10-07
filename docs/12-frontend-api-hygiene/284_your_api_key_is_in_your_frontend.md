# Episode 284: Your API key is in your frontend

> **Category:** Frontend Architecture & API Hygiene (معماری فرانت‌اند، طراحی واسط و بهداشت API)  
> **Production Layer:** Layer 1  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DYpNvXGg_WM/](https://www.instagram.com/reel/DYpNvXGg_WM/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Last week, I told you to hit F12 and search for the word key. If you found your API key sitting in your front-end JavaScript, that message was for you. Every visitor to your app, they can see it, too.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
Every visitor to your app, they can see it, too. Here's how you lock it down in 15 minutes. Step one, move all secrets to server side environment variables.

---

## ⚡ 3. Hardening Action Checklist
- [ ] move all secrets to server side environment variables. Not in your code, not in your config file that ships to the browser, not in thev file that's committed to git, server side only.
- [ ] create a proxy API route. Your front end should never call an external API directly.
- [ ] rotate every key that was ever in your front end. Even if you just moved it, even if you think no one saw it, your git history remembers everything.

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

Last week, I told you to hit F12 and search for the word key. If you found your API key sitting in your front-end JavaScript, that message was for you. Every visitor to your app, they can see it, too. Here's how you lock it down in 15 minutes. Step one, move all secrets to server side environment variables. Not in your code, not in your config file that ships to the browser, not in thev file that's committed to git, server side only. Vers has an EMV vase. Netlfi has an EMV vase. Railway, Render, Fly, they all have them. Put your keys there. Delete them from your code. Step two, create a proxy API route. Your front end should never call an external API directly. Instead, front end calls your server. Your server calls the API. The key lives on the server. The browser never sees it. One route, one file, 15 lines of code. Your secrets are invisible. Step three, rotate every key that was ever in your front end. Even if you just moved it, even if you think no one saw it, your git history remembers everything. If a key was ever committed, it's already been scraped. Go to open AI, go to Stripe, generate new keys, update your EMV vars. Old keys, dead keys out. Get them out. How many of your keys are still in your frontend code right now? Be honest. Drop it in the comments.

</div>
