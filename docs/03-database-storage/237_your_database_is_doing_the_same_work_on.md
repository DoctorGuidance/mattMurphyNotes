# Episode 237: Your database is doing the same work on every request

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Database & Storage Engineering (`پایگاه‌داده، روابط، ایندکس و پایداری داده`) |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZfT4d5AiWg/) |

---

## 🚨 1. The Incident & Attack Vector
Your database is doing the same work on every request.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Repeats un-cached database queries for static configuration tables on every single incoming web request. | Implements in-memory or Redis caching with mutation-driven invalidation for static and slow-changing reference tables. |

---

## 💡 3. Root Cause & Architectural Principle
Your users feel it, your server feels it, and your bill feels it. Here are the three things you can do right now to fix it. Step one, add a response cache at the API layer.

---

## ⚡ 4. Hardening Action Checklist
- [ ] add a response cache at the API layer.
- [ ] put a CDN in front of your static and semi-static content.
- [ ] cache your most expensive database queries.

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
> **Production Heuristic:** Three caching layers fix that without changing business logic.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

your app, it hits the database on every single request. Same query, same result, full round trip every single time. Your users feel it, your server feels it, and your bill feels it. Here are the three things you can do right now to fix it. Step one, add a response cache at the API layer. Redis or mem cache, both work great. If the data has not changed in the last 60 seconds, serve it from memory. One line of middleware, instant speed improvement. Most read heavy endpoints can cache it aggressively. That's a win. Step two, put a CDN in front of your static and semi-static content. Cloudflare, Versel Edge, AWS, CloudFront. Images, scripts, and even API responses that do not change per user. That's what you put there. Edge caching means your server never sees the request. That's a win. Step three, cache your most expensive database queries. You know that analytics dashboard loading eight joins across four tables. That's the one. Cache the result. Invalidate on write. Don't let your database do the same heavy math on every page load. So, three layers, memory, edge, and database. Stack them and your app gets faster without changing a single line of business logic. And that's a win.

</div>
