# Episode 079: Your database just lost 14 hours of customer data

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Database & Storage Engineering |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcEoX9xCZ8Q/) |

---

## 🚨 1. The Incident & Attack Vector
Your database just lost 14 hours of customer data.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Relies on unverified nightly snapshot backups, discovering corruption only after catastrophic disk failure destroys 14 hours of data. | Configures continuous Write-Ahead Log (WAL) archiving with Point-in-Time Recovery (PITR) and verifies automated test restores. |

---

## 💡 3. Root Cause & Architectural Principle
Everything users did today. Every transaction, every upload, every message, every account change gone. Because your AI set up nightly backups, but your database failed at 2 p.m.

---

## ⚡ 4. Hardening Action Checklist
- [ ] a tested restoration runbook.
- [ ] a defined RTO and RPO.

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
> **Production Heuristic:** Your backup is not your recovery plan. Your tested plan is.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your database just lost 14 hours of customer data. Your last backup from midnight. Everything users did today. Every transaction, every upload, every message, every account change gone. Because your AI set up nightly backups, but your database failed at 2 p.m. in the afternoon. So, nightly backups are not disaster recovery. They are a 24-hour gamble on nothing going wrong between those two snapshots. So, here's what the real Database disaster recovery looks like one point in time recovery, not nightly snapshots, continuous right ahead log archiving that lets you restore your database to any second, not just midnight. So if your database crashes at 2:47 p.m., your restore comes back at 2:46. You lose 1 minute of data instead of 14 hours. Your AI knows how to configure W archiving. Superbase supports PIT are on paid plans and every major provider offers it. Your AI never turned it on because nightly felt like enough. Step two, a tested restoration runbook. Not a backup that exists, a backup that has been restored. When was the last time you actually restored from a backup into a working database? If the answer is never, your backup is a hope, not a plan. Direct your AI to schedule a quarterly restoration test at a minimum. Spin up clean environment. store into it. Verify the data is intact and the application runs. Document the steps. Time it. Your recovery time is not theoretical. It's always measured every time. That's a win. And step three, a defined RTO and RPO. Recovery time objective is how long your business can survive with the database down. Recovery point objective is how much data can you afford to lose. If you do not know these numbers, your AI cannot build a recovery plan. that meets them. So, direct your AI to define both based on your business requirements, not your infrastructure defaults. Your backup is not your recovery plan. Your tested, timed, documented recovery plan is your recovery plan. Get out there and make one.

</div>
