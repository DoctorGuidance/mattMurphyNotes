# Episode 202: Self-hosted or managed

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Cloud Infrastructure & FinOps |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZ-pcdzFqfu/) |

---

## 🚨 1. The Incident & Attack Vector
Self-hosted or managed.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Migrates to self-hosted infrastructure under the illusion of 'free compute', underestimating engineering maintenance hours. | Calculates Total Cost of Ownership (TCO) including maintenance, security patch management, and on-call engineer overhead. |

---

## 💡 3. Root Cause & Architectural Principle
One costs money, the other costs you time. Here are the three things that you're going to weigh right now before you decide. Step one, manage services buy you time.

---

## ⚡ 4. Hardening Action Checklist
- [ ] manage services buy you time.
- [ ] self-hosted gives you full control.
- [ ] most builders start managed and migrate later.

---

## 💻 5. Hardened Production Implementation
```typescript
// middleware/rateLimiter.ts
import { RateLimiterRedis } from 'rate-limiter-flexible';
import { redisClient } from '../lib/redis';
import { Request, Response, NextFunction } from 'express';

const limiter = new RateLimiterRedis({
  storeClient: redisClient,
  keyPrefix: 'rl_global',
  points: 10,       // Max 10 requests
  duration: 60,     // Per 60 seconds
  blockDuration: 60 // Block for 60s if exceeded
});

export async function rateLimitMiddleware(req: Request, res: Response, next: NextFunction) {
  try {
    await limiter.consume(req.ip);
    next();
  } catch (err) {
    res.status(429).json({ error: 'Rate limit exceeded. Try again in 60s.' });
  }
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Know which currency you have.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

self-hosted or managed. Every builder hits this decision at some point. One costs money, the other costs you time. Here are the three things that you're going to weigh right now before you decide. Step one, manage services buy you time. Someone else handles the updates, the security patches, the backups, the 3:00 a.m. incidentals. That's on them. For early stage products and small teams, that time is more valuable than cost savings or doing it yourself. You're not paying for a data days, you're paying for sleep, right? Step two, self-hosted gives you full control. Your data lives where you decide it lives. Your costs scale the way you design them to. No vendor pricing changes at renewal. No rate limits you didn't agree to. But that control comes with a job title. You're now the infrastructure team 24/7, 365. Patches are your responsibility. Uptime is your reputation. Step three, most builders start managed and migrate later. when the economics justify it. The mistake is overinvesting in infrastructure before you have the traffic to justify it or underinvesting in reliability when your users depend on you. So self-hosted or manage is not a technical decision. It's a time and money decision. Know which one you have less of.

</div>
