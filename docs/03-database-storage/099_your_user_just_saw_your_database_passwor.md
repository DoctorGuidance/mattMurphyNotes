# Episode 099: Your user just saw your database password on their screen

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Database & Storage Engineering |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbqUuqlk7L6/) |

---

## 🚨 1. The Incident & Attack Vector
Your user just saw your database password on their screen.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Exposes raw database connection strings containing administrative passwords in client-facing exception stack traces. | Scrubs sensitive database connection strings and passwords from all application error boundaries and logging middleware. |

---

## 💡 3. Root Cause & Architectural Principle
Instead of a friendly error message, it dumped a raw stack trace with your database connection string, your framework versions, and the exact line of code that failed. That's not a bug, people. That is your AI showing the world exactly how to break into your application.

---

## ⚡ 4. Hardening Action Checklist
- [ ] split your error handling into two layers.
- [ ] catch errors at every boundary.
- [ ] build an error logging pipeline.

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
> **Production Heuristic:** Split your error handling. Catch errors at every boundary. Build a logging pipeline. Fix it today.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your user just saw your database password on their screen. Your app crashed. Instead of a friendly error message, it dumped a raw stack trace with your database connection string, your framework versions, and the exact line of code that failed. That's not a bug, people. That is your AI showing the world exactly how to break into your application. So, here are the three things you're going to direct your AI to do right now to fix it. Number one, split your error handling into two layers. A public layer that shows your user a clean, helpful message and a private layer that logs the full technical detail on your server where only you can see it. Your AI built a handler that does both jobs. That is not efficiency. That is a security hole disguised as a feature. The moment you separate what your user sees from what your server records is the moment your app starts behaving like a product instead of a prototype. That's a win. Step two, catch errors at every boundary. Not just your login form, your API routes, your background jobs, your web hook receivers, your payment call backs. Every uncaught error is a stack trace waiting to leak. Directory AI to set up automated testing that catches these before your users do. Unit test with something like vi test or endtoend test with something like playright. Your AI knows how to configure both. turn them on, but it'll never do it unless you ask it to. Step three, build an error logging pipeline. Timestamps, user sessions, routes, inputs, stack traces, all of it. All private, all searchable. When something breaks at 2 a.m., you trace it in minutes, not 3 hours of guessing what happened. Your users should never see your internals, your logs. They should see everything. That is the difference between a product and a total liability. So, get Get out there and make it a win.

</div>
