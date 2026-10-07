# Episode 264: Supabase. Firebase. Neon. Convex

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Database & Storage Engineering (`پایگاه‌داده، روابط، ایندکس و پایداری داده`) |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZALI2bRljh/) |

---

## 🚨 1. The Incident & Attack Vector
Supabase. Firebase. Neon. Convex.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Executes unindexed or unconstrained database queries in 'Supabase. Firebase. Neon. Convex', degrading query throughput under load. | Applies composite B-tree indexing and query pagination constraints tailored to access patterns in 'Supabase. Firebase. Neon. Convex'. |

---

## 💡 3. Root Cause & Architectural Principle
Should I use Convex instead? What about Neon? Well, there's no universal answer about databases, but there is a universal framework.

---

## ⚡ 4. Hardening Action Checklist
- [ ] match your database to your data shape.
- [ ] evaluate the ecosystem, not just the database.
- [ ] plan your exit before your build.

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
> **Production Heuristic:** The right answer depends on these three things.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

I've gotten the same question three different ways this week from 20 different people. Should I use Superbase or Firebase? Should I use Convex instead? What about Neon? Well, there's no universal answer about databases, but there is a universal framework. So, here are the three things you can do right now to figure it out. Step one, match your database to your data shape. If your data is relational, meaning uh users have orders, orders have items, and items belong in C categories, you need Postgress. Well, Superbase and Neon both run Postgress under the hood from the factory. That's a win. But if your data is document shaped, meaning each record is a self-contained blob of JSON, Firebase and Convex might make more sense. In Convex on mobile apps, definitely a win. So, don't fight your data shape. Step two, evaluate the ecosystem, not just the database. Superbase gives you off storage and real time out of the box, right? Neon gives you serverless, Postgress with database branching. Firebase gives you Google's infrastructure and tight mobile integration and the database engine matters less than the tooling around it. Right? Pick the one where you write the least amount of custom code. Step three, plan your exit before your build. Superbase and neon run standard Postgress. You can leave anytime. Firebase and convex though use proprietary models. So if you want to leave, you're rewriting your entire data layer. No matter what you pick, the best database is the one you understand fully, you can afford, and you can leave when you need to.

</div>
