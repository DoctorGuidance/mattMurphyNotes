# Episode 293: Most people think full-stack means frontend and backend

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Frontend Architecture & API Hygiene (`معماری فرانت‌اند، طراحی واسط و بهداشت API`) |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYchN42gIoy/) |

---

## 🚨 1. The Incident & Attack Vector
Most people think full-stack means frontend and backend.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Leaves endpoints open without rate limiting, allowing scrapers or brute-force bots to drain resources. | Implements token bucket rate limiting at gateway level, throttling abusive IPs with exponential backoff. |

---

## 💡 3. Root Cause & Architectural Principle
The real production stack includes off hosting, cloud infrastructure, CI/CD, security, rate limiting, caching, load balancing, error tracking, and disaster recovery. And most vibecoded apps ship with none of it. This isn't a knock-on vibe coding.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Inspect the existing code paths and identify unvalidated boundary inputs.
- [ ] Implement defense-in-depth guardrails preventing unauthorized state modification.
- [ ] Add automated regression tests verifying failure scenarios before shipping.

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
> **Production Heuristic:** Swipe through to see what’s missing.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Most people think full stack means front end and back end. That's two layers out of 13. The real production stack includes off hosting, cloud infrastructure, CI/CD, security, rate limiting, caching, load balancing, error tracking, and disaster recovery. And most vibecoded apps ship with none of it. This isn't a knock-on vibe coding. It's the reality of what it takes to go from it works on my laptop to it works for 10,000 users at 2:00 a.m. when something breaks. Over the next few weeks, I'm breaking down all 13 of these layers, what they are, why they matter, and how to add each one to your app. Whether you're an operator running your business on AI, training your staff to deploy it, or a builder shipping code to production, there's a path through the stack. Swipe through to see what's missing. Mm.

</div>
