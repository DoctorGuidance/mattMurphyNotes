# Episode 239: Supabase gets you to production

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Testing, Staging & CI/CD (`تست، محیط‌های کاری، CI/CD و خط لوله استقرار`) |
| **Target Production Layer** | Layer 7 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZcoN1gRCgL/) |

---

## 🚨 1. The Incident & Attack Vector
Supabase gets you to production.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Applies database schema changes via the Supabase web dashboard in production, causing environmental drift from local code. | Manages Supabase schema migrations as versioned SQL migration files committed to Git and applied via CI pipelines. |

---

## 💡 3. Root Cause & Architectural Principle
Here are the three signs it's time to unbundle it. Step one, your O needs outgrew the built-in. You need SSO, custom claims, multi-tenant permission logic.

---

## ⚡ 4. Hardening Action Checklist
- [ ] your O needs outgrew the built-in.
- [ ] your database needs a different engine superbases Postgress Postgress is fantastic but if your workload is time series graph or edge first you're always fighting the architecture try this combo neon for serverless postgress that scales to zero terso for SQL light at the edge and and planet scale for MySQL with zero downtime migrations.
- [ ] your storage functions and database need to be scaling.

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
> **Production Heuristic:** Knowing when to unbundle auth, database, and storage gets you through it.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Superbase got you to production, but that does not mean it'll scale through production. There's a moment in every project when the all-in-one platform starts fighting you back. Here are the three signs it's time to unbundle it. Step one, your O needs outgrew the built-in. You need SSO, custom claims, multi-tenant permission logic. Superbase O handles the basics really well. But when your access control model gets complex, you need a dedicated Identity layer auth clerk work Oos all work great let off be its own service that's the win step two your database needs a different engine superbases Postgress Postgress is fantastic but if your workload is time series graph or edge first you're always fighting the architecture try this combo neon for serverless postgress that scales to zero terso for SQL light at the edge and and planet scale for MySQL with zero downtime migrations. Match the engine to the workload. That's a win. Step three, your storage functions and database need to be scaling. When one layer is bottlenecking the other, bundled infrastructure becomes the ceiling. Separate them. Scale them independently. Connect them through APIs. Superbase is a great starting point and a lot of you use it, but knowing when to leave it is what makes you a real Operator.

</div>
