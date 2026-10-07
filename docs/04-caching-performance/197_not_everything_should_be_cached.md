# Episode 197: Not Everything Should Be Cached

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Caching & Edge Performance (`کشینگ، توزیع لبه و پرفورمنس سیستمی`) |
| **Target Production Layer** | Layer 10 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaDuf2DFSP-/) |

---

## 🚨 1. The Incident & Attack Vector
Not Everything Should Be Cached.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Caches rapidly mutating transactional states like inventory balances, causing overselling and financial reconciliation bugs. | Restricts caching to static, reference, or read-heavy data while reading volatile transactional state directly from ACID databases. |

---

## 💡 3. Root Cause & Architectural Principle
The naming part, that's a joke. The cash part, not a joke. Here are three things you can do about it right now.

---

## ⚡ 4. Hardening Action Checklist
- [ ] stale data.
- [ ] invalidation strategy.
- [ ] cash stampede.

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
> **Production Heuristic:** Caching is a tradeoff.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

There are two hard problems in computer science. Cash invalidation and naming things. The naming part, that's a joke. The cash part, not a joke. Here are three things you can do about it right now. Step one, stale data. Your user updates their profile. The cache still holds the old version. For 30 seconds or 30 minutes, every request returns yesterday's data. The user sees the old name, the old photo, the old permissions. C. ing is not a performance feature. It's a consistency decision. Know what you are willing to show stale and for how long. That's the win. Step two, invalidation strategy. Timebased expiration is simple. Set a lifetime. When it expires, fetch fresh every time. Event-based invalidation is precise. Data changes. Cache clears immediately. Most applications need both. Static content gets timebased. User data gets event-based. The mistake is treating all cache data the exact same way. Step three, cash stampede. Your cash expires. 1,000 requests hit the database at the same instant. That one request should refresh the cache, but the other 999, they're going to wait. Without protection, your database sees a spike every time a popular key expires. Caching solves one problem, but it creates three. Solve all four.

</div>
