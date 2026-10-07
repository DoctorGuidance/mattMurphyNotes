# Episode 009: An attacker intercepted your magic link and landed inside

> **Category:** Application Security & Defense (امنیت نرم‌افزار، حملات و دفاع لایه‌ای)  
> **Production Layer:** Layer 8  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DdrEewmD01_/](https://www.instagram.com/reel/DdrEewmD01_/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your AI implemented magic link authentication, but an attacker just intercepted your magic link and landed inside your users's dashboard. So, your passwordless login just became a passwordless breakin and your AI built the flow without validating where the link resolves. So, the user enters their email, your server, generates a signed token, embeds it in a URL, and emails it out.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
So, the user enters their email, your server, generates a signed token, embeds it in a URL, and emails it out. The user clicks and authenticates the URL includes a redirect parameter your AI never locked down. So let's get it locked down.

---

## ⚡ 3. Hardening Action Checklist
- [ ] your magic link URL includes a redirect parameter that tells the application where to send the user after authentication. An attacker crafts a link with the redirect set to their server.
- [ ] magic link tokens that do not expire remain valid indefinitely in users email. So an attacker who gains access to a mailbox 6 months later finds every magic link still fully active.
- [ ] an attacker who discovers the Magic Link endpoint can request thousands of links per minute for any email address. So, each request sends a real email from your domain.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Redis Token Bucket Rate Limiter
import { RateLimiterRedis } from 'rate-limiter-flexible';
const rateLimiter = new RateLimiterRedis({
  storeClient: redisClient,
  points: 10,   // 10 requests
  duration: 60, // per 60 seconds
});
await rateLimiter.consume(req.ip);
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your AI implemented magic link authentication, but an attacker just intercepted your magic link and landed inside your users's dashboard. So, your passwordless login just became a passwordless breakin and your AI built the flow without validating where the link resolves. So, the user enters their email, your server, generates a signed token, embeds it in a URL, and emails it out. The user clicks and authenticates the URL includes a redirect parameter your AI never locked down. So let's get it locked down. Step one, your magic link URL includes a redirect parameter that tells the application where to send the user after authentication. An attacker crafts a link with the redirect set to their server. The user clicks that magic link from their real email, authenticates against your real application, and your server sends their authentic ated session to the attacker's domain. So now the attacker has the session token. So you need to direct your AI to validate the redirect parameter against all allow list of your own domains before issuing a redirect at all. That is a win. Step two, magic link tokens that do not expire remain valid indefinitely in users email. So an attacker who gains access to a mailbox 6 months later finds every magic link still fully active. Each one is a valid authentication bypass. So, direct your AI to set Magic Link tokens to expire within 10 minutes and invalidate them immediately after first use. And step three, an attacker who discovers the Magic Link endpoint can request thousands of links per minute for any email address. So, each request sends a real email from your domain. This floods the targets inbox and damages your sender reputation. That's important. So direct your AI to rate limit magic link request to three per email address per hour and throttle total request per IP. Your magic link removes that password, but it should not remove all of your security. Get it fixed.

</div>
