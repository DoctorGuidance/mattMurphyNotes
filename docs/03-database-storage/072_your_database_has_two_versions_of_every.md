# Episode 072: Your database has two versions of every record right now

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Database & Storage Engineering |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcOX9AdERD2/) |

---

## 🚨 1. The Incident & Attack Vector
Your database has two versions of every record right now.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Reads from asynchronously replicated database read replicas immediately after writes, serving stale or conflicting state to users. | Implements read-after-write consistency routing, directing queries immediately following mutations to the primary database node. |

---

## 💡 3. Root Cause & Architectural Principle
So your right went to primary, but your read came back from a replica that's 3 seconds behind it. Two databases, two versions of the truth, and your user is staring at the wrong one. They submitted a support ticket saying your app is broken.

---

## ⚡ 4. Hardening Action Checklist
- [ ] read after write consistency routing.
- [ ] replica lag monitoring with automatic failover thresholds.
- [ ] conflict resolution on concurrent rights across regions.

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
> **Production Heuristic:** Your database scaled. Your consistency did not.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your database has two versions of every record right now. And your app is showing users the wrong one. So your right went to primary, but your read came back from a replica that's 3 seconds behind it. Two databases, two versions of the truth, and your user is staring at the wrong one. They submitted a support ticket saying your app is broken. It is not broken. It is lying to them. Here's what happens when your app scales past one database and Your AI never accounted for replication lag. Step one, read after write consistency routing. When a user writes data, the next read from that same user must come from a primary, not a replica. A short consistency window routes that user's reads to the primary for a defined period after any write. Everyone else continues reading from replicas. So, direct your AI to implement sessionaware read routing that pins the user to the primary for a configurable window after any write. That's a win. Step two, replica lag monitoring with automatic failover thresholds. So, replication lag spikes under load, during large transactions, and during schema changes. If your replica falls 10 seconds behind, every read from it returns data your users changed 10 seconds ago. So, direct your AI to instrument replica lag monitoring and define a threshold. that reads automatically reroute to all primary until the replica catches up. And step three, conflict resolution on concurrent rights across regions. Two users editing the same record in two regions. Both rights succeed on their local primary. Replication carries both changes. One overwrites the other with no warning at all. So direct your AI to implement last right wins with timestamp resolution or operational transforms that merge concurrent changes instead of silently dropping one. Your database scaled. Your consistency, well, it didn't. So, direct your AI to fix the gap before your users find it for you. And that's the win.

</div>
