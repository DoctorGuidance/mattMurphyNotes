# Episode 058: You installed an npm package last week. It has been sending

> **Category:** Application Security & Defense (امنیت نرم‌افزار، حملات و دفاع لایه‌ای)  
> **Production Layer:** Layer 8  
> **Official Instagram Reel:** [https://www.instagram.com/reel/Dcg9G7PjY6E/](https://www.instagram.com/reel/Dcg9G7PjY6E/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
You installed an NPM package just last week. Since then, it has been sending your environment variables to a server you've never heard of. Your database credentials, your API keys, your Stripe secret, your Jot signing key.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
Your database credentials, your API keys, your Stripe secret, your Jot signing key. All of it read from process. MV and posted to an external endpoint every time your application starts up.

---

## ⚡ 3. Hardening Action Checklist
- [ ] a dependency audit on every package in your lock file. Not just your direct dependencies, your transitive dependencies, the package your packages installed.
- [ ] environment variable isolation. Your application should not expose every environment variable to every process.
- [ ] lock file integrity verification on CI. Your lock file pins exact versions.

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

You installed an NPM package just last week. Since then, it has been sending your environment variables to a server you've never heard of. Your database credentials, your API keys, your Stripe secret, your Jot signing key. All of it read from process. MV and posted to an external endpoint every time your application starts up. The package had 50,000 weekly downloads. The name was one character off from the real one. So you installed it because your AI recommended it and you never checked. So your dependency list is an attack surface. Every package on it is code you did not write running with full access to your environment. So let's get this cleaned up. Step one, a dependency audit on every package in your lock file. Not just your direct dependencies, your transitive dependencies, the package your packages installed. A single application can pull in 800 packages from a dozen containers you have never ever heard of. Direct your AI to run a full dependency tree audit. Flag any package with fewer than 100 weekly downloads, any package where the maintainer changed in the last 90 days, and any package with postinstall scripts that execute on install. Injections are not cool. That's the win if you run that program. Step two, environment variable isolation. Your application should not expose every environment variable to every process. Secrets needed by one module should not be readable by every package in the dependency tree. So direct your AI to implement scoped secret access where each module receives only the environment variables that it needs, not the full process object. That's a win. And step three, lock file integrity verification on CI. Your lock file pins exact versions. If a dependency is modified upstream after you installed, the check sum will not match. Your CI pipeline should verify lock file integrity integrity on every build and reject any build where the check sums do not match the expected values. So, direct your AI to configure lock file integrity up checks in your CI pipeline that block deployment on any checksum mismatch. Your code is only as trustworthy as your least trusted dependency. So, audit the list before the list is auditing you.

</div>
