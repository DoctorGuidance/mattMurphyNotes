# Episode 133: Serverless was predictable at 10 users. At 1,000 the bill

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Cloud Infrastructure & FinOps |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Da8FYMdlAL9/) |

---

## 🚨 1. The Incident & Attack Vector
Serverless was predictable at 10 users. At 1,000 the bill is climbing.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Leaves serverless functions configured with default 15-minute execution timeouts, accumulating massive bills during hanging loops. | Enforces hard function timeouts (15-30 seconds) and memory limits across all serverless function definitions. |

---

## 💡 3. Root Cause & Architectural Principle
And your team, they want to move to containers. That means managing infrastructure for the first time for your team. And this is not a technology decision.

---

## ⚡ 4. Hardening Action Checklist
- [ ] the cost of convenience.
- [ ] the cost of control.
- [ ] is the hybrid answer.

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
> **Production Heuristic:** The decision is based on your business reality.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

That serverless bill sure was predictable at 10 users. At a thousand users, it's unpredictable climbing fast. And your team, they want to move to containers. That means managing infrastructure for the first time for your team. And this is not a technology decision. It's a business maturity decision. And everybody goes through it when you're scaling. Step one, the cost of convenience. Serverless charges per invocation. Every request cost you money. You pay pay more per unit than a dedicated server, but you manage nothing at all. No updates, no capacity planning, no on call rotations. For early stage companies and products, that's the right deal. Your time is worth more than the premium. The question is, when does that premium exceed the cost of managing it yourself? Figure that out. Step two, the cost of control. Containers cost less per unit, but they also cost you operationally. Someone monitor server health, someone's handling your scaling, someone manages deployments. If that someone is you and you are also the founder, the salesperson, the support team, and the product designer, which many soloreneurs are, so that means the operations burden may cost more in lost focus than serverless premium costs and dollars. I'd suggest you direct your AI to run that gap analysis. Monthly servers list cost at current usage, equivalent container costs, and hours per week for container operations. That math or the result of it will tell you which model fits your stage. And step three is the hybrid answer. Most production systems should be running both. Serverless for request response and containers for background processing. Your API stays serverless. Q workers move to containers. Scheduled jobs run on dedicated compute. And you direct your AI to architect the split by the workload type. not by what a YouTube tutorial recommended, but the decision is not serverless versus containers. It is which workloads belong where based on your business reality, not a technical preference, the business reality. And that's where you're going to find the win.

</div>
