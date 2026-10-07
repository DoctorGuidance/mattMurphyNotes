# Episode 080: An attacker logged into your app at 3 AM from another

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcEEyocD8II/) |

---

## 🚨 1. The Incident & Attack Vector
An attacker logged into your app at 3 AM from another country.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |

---

## 💡 3. Root Cause & Architectural Principle
Your app said, "Welcome back." Stolen credentials, foreign IP, middle of the night. So, your app cannot tell the difference between your real user and the person who has stolen their password. It's the same role, same permissions, same access to everything because your AI built static roles that never evaluate context in the moment.

---

## ⚡ 4. Hardening Action Checklist
- [ ] attribute-based access control.
- [ ] zero trust enforcement on every internal request, not just the login gate, every API call, every database query.
- [ ] continue.

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
> **Production Heuristic:** Static roles tell you who someone is. Context tells you whether to trust them right now.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

A hacker logged into your app at 3:00 a.m. from another country. Your app said, "Welcome back." Stolen credentials, foreign IP, middle of the night. So, your app cannot tell the difference between your real user and the person who has stolen their password. It's the same role, same permissions, same access to everything because your AI built static roles that never evaluate context in the moment. So, here's what tier 3 RBAC actually looks like for your app. Step one, attribute-based access control. Permissions that evaluate context, not just the role. What time of day it is, what location, where the device fingerprint is, what's the IP reputation, what's the data sensitivity level. So, direct your AI to build a policy engine that evaluates these attributes on every single request. A user accessing financial records at 3:00 a.m. from an unrecognized device gets stepped up authentication or denied entirely. Same role, different context. effects different decision. That's definitely a win. Step two, zero trust enforcement on every internal request, not just the login gate, every API call, every database query. So every service to service request that reverifies identity and authorization. Your AI trusts everything inside the network perimeter. Zero trust assumes there is no perimeter. Every request who proves it is or gets rejected. And step three, continue. continuous session risk scoring, not a one-time check at login, a running evaluation that monitors behavior throughout their session. If a user's behavior pattern shifts midsession, the system challenges or terminates automatically. So, direct your AI to build session anomaly detection that watches for impossible travel, unusual data access volume, or privilege escalation attempts in real time. Static roles tell you who someone else is. Context tells you whether to trust them right now or not. So, direct your eye to build for both.

</div>
