# Episode 222: Serverless Postgres or serverless MySQL

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Cloud Infrastructure & FinOps |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZsJytJxv2d/) |

---

## 🚨 1. The Incident & Attack Vector
Serverless Postgres or serverless MySQL.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Picks serverless database engines without testing compatibility with application transaction patterns and relational constraints. | Evaluates serverless database compatibility against relational constraints, transaction isolation levels, and migration tools. |

---

## 💡 3. Root Cause & Architectural Principle
Both are excellent. Both will confuse you if you do not understand what they actually solve. Here are three things you do right now to deploy them correctly.

---

## ⚡ 4. Hardening Action Checklist
- [ ] know the engine difference.
- [ ] think about branching strategies.
- [ ] pricing changes.

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
> **Production Heuristic:** Choose the engine you know.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

You need a serverless database. Neon or planet scale are on the table. Both are excellent. Both will confuse you if you do not understand what they actually solve. Here are three things you do right now to deploy them correctly. Step one, know the engine difference. Right? Neon is serverless Postgress, full Postgress. Planet scale is serverless with my SQL built on vitess. The same technology that runs YouTube super powerful. If your team knows Postgress, run Neon. If your team knows MySQL, run Planet Scale. Do not switch database engines for marketing reasons. That's a win. Step two, think about branching strategies. Both platforms let you branch your database like you branch your code. Create a copy, test your migration, merge it back. This is how you stop breaking production with schema changes. If you've ever run a migration on a Friday and regretted it by Saturday, Branching is the fix and that's a win. Step three, pricing changes. Planet Scale has removed their free tier and Neon still has one. And that matters if you're testing prototype ideas, right? But do not pick a production database based on the free tier. Pick it based on what happens at 10,000 users. The free tier is the lobby for everyone. Production is the whole building. So, choose the engine. You know, that's the win.

</div>
