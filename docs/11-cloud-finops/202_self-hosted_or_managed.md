# Episode 202: Self-hosted or managed

> **Category:** Cloud Infrastructure & FinOps (معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه)  
> **Production Layer:** Layer 6  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DZ-pcdzFqfu/](https://www.instagram.com/reel/DZ-pcdzFqfu/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
self-hosted or managed. Every builder hits this decision at some point. One costs money, the other costs you time.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
One costs money, the other costs you time. Here are the three things that you're going to weigh right now before you decide. Step one, manage services buy you time.

---

## ⚡ 3. Hardening Action Checklist
- [ ] manage services buy you time. Someone else handles the updates, the security patches, the backups, the 3:00 a.m.
- [ ] self-hosted gives you full control. Your data lives where you decide it lives.
- [ ] most builders start managed and migrate later. when the economics justify it.

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

self-hosted or managed. Every builder hits this decision at some point. One costs money, the other costs you time. Here are the three things that you're going to weigh right now before you decide. Step one, manage services buy you time. Someone else handles the updates, the security patches, the backups, the 3:00 a.m. incidentals. That's on them. For early stage products and small teams, that time is more valuable than cost savings or doing it yourself. You're not paying for a data days, you're paying for sleep, right? Step two, self-hosted gives you full control. Your data lives where you decide it lives. Your costs scale the way you design them to. No vendor pricing changes at renewal. No rate limits you didn't agree to. But that control comes with a job title. You're now the infrastructure team 24/7, 365. Patches are your responsibility. Uptime is your reputation. Step three, most builders start managed and migrate later. when the economics justify it. The mistake is overinvesting in infrastructure before you have the traffic to justify it or underinvesting in reliability when your users depend on you. So self-hosted or manage is not a technical decision. It's a time and money decision. Know which one you have less of.

</div>
