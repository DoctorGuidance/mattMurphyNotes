# Episode 248: 45-second request

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Async Queues & Webhooks (`صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZSYNBNxE1k/) |

---

## 🚨 1. The Incident & Attack Vector
A user clicks export report. Your API generates a PDF. It takes 45 seconds, so the request times out.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Processes asynchronous jobs or webhooks without raw signature checks or idempotency locks in '45-second request'. | Verifies webhook HMAC signatures on raw buffers and uses Redis idempotency keys with Dead-Letter Queues (DLQ). |

---

## 💡 3. Root Cause & Architectural Principle
It takes 45 seconds, so the request times out. The user clicks it again. So now you're generating two PDFs.

---

## ⚡ 4. Hardening Action Checklist
- [ ] never do heavy processing in the request cycle.
- [ ] process jobs with a worker.
- [ ] implement item potency keys.

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
> **Production Heuristic:** Fix it with background architecture.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

A user clicks export report. Your API generates a PDF. It takes 45 seconds, so the request times out. The user clicks it again. So now you're generating two PDFs. Here are three things you can do right now to fix it. Step one, never do heavy processing in the request cycle. When the user clicks export, your API does one thing. Create a job record. Return a job ID immediately. status processing. The user sees a progress indicator. The actual work happens in the background. Your API responds in 200 milliseconds every time. That's a win. Step two, process jobs with a worker. Injest, trigger.dev, or bull mq. Injest is the easiest for server list. I use it the most. Define a function that runs when a job event fires. It processes at its own pace. If it fails, it retries with exponential backoff. The user isn't watching a spinner. They get a notification when it's done. That's a win. Step three, implement item potency keys. The user who clicked twice both clicks should produce one job, not two. Attach a unique key to every request. Before creating a new job, check if that key exists. If it does, return the existing job. No duplicates, immediate response times. background processing. So, no timeouts, no duplicates, and no angry users. That's a win. So, are you running operations synchronously that you should be running async? Let me know.

</div>
