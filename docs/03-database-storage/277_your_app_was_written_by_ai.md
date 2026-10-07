# Episode 277: Your app was written by AI

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Database & Storage Engineering (`پایگاه‌داده، روابط، ایندکس و پایداری داده`) |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYwyDG3xBlg/) |

---

## 🚨 1. The Incident & Attack Vector
Your app was written by AI.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |

---

## 💡 3. Root Cause & Architectural Principle
So here are three things you can do right now to fix it. Step one, read every file in your codebase out loud. Not skim it, read it out loud.

---

## ⚡ 4. Hardening Action Checklist
- [ ] read every file in your codebase out loud.
- [ ] rename everything.
- [ ] delete anything that you don't use.

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
> **Production Heuristic:** That's what responsible app ownership means

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Last week I said your whole app is copy pasted from chat GPT. Same pattern, same vulnerabilities, same bugs that 10,000 other apps that were built the exact same way have. So here are three things you can do right now to fix it. Step one, read every file in your codebase out loud. Not skim it, read it out loud. If you can't explain what a function does in one sentence, you don't own it. Open your main API. I routes, open your off middleware, open your database queries. If any of it looks like a mystery to you, highlight it and don't move on until you completely understand it. Step two, rename everything. AI gives you generic aims. Process data, handle, submit, fetch results. Those names mean nothing to you. Rename them with what they actually do in your app. Create user account, validate payment amount, get active subscriptions. When you rename claim it, you claim it. You also make it easy and readable for the next person that needs it, which might be you 3 months from now. Step three, delete anything that you don't use. AI generates a ton of backup functions and helper utilities and abstractions that you never asked it for. Go through your codebase and delete every function that isn't called, every import that isn't used, and every component that isn't rendered. A smaller codebase is safer for you and your user. in your code. It doesn't have to be written from scratch. I get it. But it does have to be understood from the top to the bottom. That's what responsible app ownership means. And now you got it.

</div>
