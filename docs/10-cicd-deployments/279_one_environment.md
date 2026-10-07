# Episode 279: One environment

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Testing, Staging & CI/CD (`تست، محیط‌های کاری، CI/CD و خط لوله استقرار`) |
| **Target Production Layer** | Layer 7 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYuVqaeRi8q/) |

---

## 🚨 1. The Incident & Attack Vector
Last week, I showed you the one environment trap. One environment, your laptop, full production. Every change goes straight to live users.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Develops directly against production databases, risking accidental table drops and catastrophic customer data corruption. | Enforces strict three-tier environment isolation (Dev, Staging, Production) with isolated database clusters and credentials. |

---

## 💡 3. Root Cause & Architectural Principle
Every change goes straight to live users. Here's how you set up three environments in 30 minutes. Step one, branch strategy.

---

## ⚡ 4. Hardening Action Checklist
- [ ] branch strategy.
- [ ] staging environments.
- [ ] deploy checklist test and staging, review and diff, merge and main autodeploy fires.

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
> **Production Heuristic:** Let's hear about it in the comments

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Last week, I showed you the one environment trap. One environment, your laptop, full production. Every change goes straight to live users. Here's how you set up three environments in 30 minutes. Step one, branch strategy. Main branch equals production. Dev branch equals your playground. Never push to main directly. Ever. Work in dev, test in dev, break things in dev. When it works, merge it to Maine. Step two, staging environments. You got to have them. Versel and Netlefi both give you this for free. Every branch gets its own URL. Dev branch equals a staging URL. Main branch equals your production URL. Same code, same infrastructure, totally different audience. Test with staging, demo with staging. Let your team break staging. Then deploy production with total confidence. Step three, deploy checklist test and staging, review and diff, merge and main autodeploy fires. That's it. No manual deploys, no FTP uploads, no editing code on the live server. The whole thing takes 30 minutes to set up and it'll save you from every 2 a.m. panic for the rest of your app's life. So, are you still deploying straight to production? Let's hear about it in the comments.

</div>
