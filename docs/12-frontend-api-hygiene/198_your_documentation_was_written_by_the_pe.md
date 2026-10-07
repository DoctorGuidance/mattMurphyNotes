# Episode 198: Your documentation was written by the person who built the

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Frontend Architecture & API Hygiene |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaDUZ3Lkc5S/) |

---

## 🚨 1. The Incident & Attack Vector
Your documentation was written by the person who built the feature.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Writes technical documentation loaded with internal jargon that confuses prospective customers and support staff. | Produces clean, user-centric documentation with searchable troubleshooting guides, interactive examples, and clear workflows. |

---

## 💡 3. Root Cause & Architectural Principle
So, here are the three things you want to document right now to get ahead of it. Step one, all architecture decisions. Why you chose a database, why you split a service, why this endpoint exists, what LLM you selected.

---

## ⚡ 4. Hardening Action Checklist
- [ ] all architecture decisions.
- [ ] environment setups.
- [ ] failure modes.

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
> **Production Heuristic:** And again, my best practice is have my AI assistant build me a playbook for every decision regarding the architecture that That's the win

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your application works, but your documentation does not exist. The next person to build on this system is probably you in 6 months, and you're not going to remember what you did. So, here are the three things you want to document right now to get ahead of it. Step one, all architecture decisions. Why you chose a database, why you split a service, why this endpoint exists, what LLM you selected. The code tells you what, but documentation tells you why. 6 months from now, someone's going to ask about your architecture. If your answer only lives in your head, it dies when you move on. Have your AI assistant create a playbook or at least just write it down. One paragraph per decision. That's the win. Step two, environment setups. How does the new person run this locally if it's not you? Cuz every project says it takes 5 minutes, but it really takes 2 days because the instructions skip the key steps. So, you need to document the commands, the variables, and the workarounds that you stop noticing. ing. Step three, failure modes. What happens when the database goes down or what happens when the rate limit hits? You do not need documentation where when things are working. You need it for when things are breaking. Documentation isn't overhead. It's not extra work. It's the difference between a project one person runs and a product a whole team can own and put into production. And again, my best practice is have my AI assistant build me a playbook for every decision regarding the architecture that That's the win.

</div>
