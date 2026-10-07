# Episode 105: Seven out of my last ten audits had API keys committed to

> **Category:** Application Security & Defense (امنیت نرم‌افزار، حملات و دفاع لایه‌ای)  
> **Production Layer:** Layer 8  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DbgDhezjelJ/](https://www.instagram.com/reel/DbgDhezjelJ/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Seven of my last 10 audits had API keys committed to GitHub, database credentials, secret stripe keys, thirdparty service tokens, all of them sitting in a public repository where anyone with a browser can find them. This is not a hypothetical. I saw this in 70% of the apps that we reviewed just last week.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
I saw this in 70% of the apps that we reviewed just last week. Your AI does not know the difference between a config file and an environmental variable. Period.

---

## ⚡ 3. Hardening Action Checklist
- [ ] move every secret into environmental variables. And verify nothing's hard-coded.
- [ ] rotate every key that has ever been committed. If your keys have been in a public repo for even more than an hour, assume they're compromised.
- [ ] install a pre-commit hook that blocks secrets from ever being pushed out again. Your AI can configure tools that scan every commit pattern and what it looks like and stop API keys, tokens, and credentials and reject pushing out before it reaches the repo.

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

Seven of my last 10 audits had API keys committed to GitHub, database credentials, secret stripe keys, thirdparty service tokens, all of them sitting in a public repository where anyone with a browser can find them. This is not a hypothetical. I saw this in 70% of the apps that we reviewed just last week. Your AI does not know the difference between a config file and an environmental variable. Period. So, puts everything in the code and it pushes everything to that repo. Public, private, it's in there. And here are the three things you direct your AI to fix before someone finds your keys before you do. Number one, move every secret into environmental variables. And verify nothing's hard-coded. Simple as that. Your AI knows how to use files. It will never move your key on its own because it does not think about what happens when code goes public. So direct your AI to scan your entire codebase for hard-coded strings that match API key patterns and then move every one of them into environmental variables. Then verify your MV file is in your.getit ignore file because if it's not, you just moved your keys from one committed file to another committed file. That's not a win. Step two, rotate every key that has ever been committed. If your keys have been in a public repo for even more than an hour, assume they're compromised. cuz they are. It does not matter that you deleted the file. Get history is permanent and being crawled by bots non-stop. Anyone can pull a previous commit and see exactly what you removed. So, direct your AI to generate new keys for every single service. Revoke the old ones and update your environmental variables. The old keys, they're burned. Treat them exactly that way. And step three, install a pre-commit hook that blocks secrets from ever being pushed out again. Your AI can configure tools that scan every commit pattern and what it looks like and stop API keys, tokens, and credentials and reject pushing out before it reaches the repo. This is a 5minut setup that prevents the problem permanently. Without it, you're one careless commit away from doing this all over again. We find this in 70% of the apps we audit. So, do not let yours be the next one. Direct your AI to fix it today.

</div>
