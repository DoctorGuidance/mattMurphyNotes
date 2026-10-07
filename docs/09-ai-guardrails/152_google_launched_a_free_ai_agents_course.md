# Episode 152: Google launched a free AI agents course

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Daq9JyhiZT9/) |

---

## 🚨 1. The Incident & Attack Vector
Google launched a free AI agents course.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends unvalidated user inputs straight to LLMs without budget caps or injection defenses in 'Google launched a free AI agents course'. | Applies prompt sanitization, structured output validation (Zod), spend ceilings, and SGI metadata compliance. |

---

## 💡 3. Root Cause & Architectural Principle
My reaction is, thank you, Google, because here's what that course teaches. How to build an agent. Here's what it does not teach.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Inspect the existing code paths and identify unvalidated boundary inputs.
- [ ] Implement defense-in-depth guardrails preventing unauthorized state modification.
- [ ] Add automated regression tests verifying failure scenarios before shipping.

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
> **Production Heuristic:** Google builds the rocket. We teach you how to land it.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Both Google and Kaggle just launched free 5-day agent courses. The whole world can now learn how to build AI agents for free. My reaction is, thank you, Google, because here's what that course teaches. How to build an agent. Here's what it does not teach. What happens after you build an agent? How to direct your AI to secure it. How to monitor it. How to scale it. How to handle it when it fails at 2 in the morning when real users and real data are all up in it. 76% of every AI agent build fails in the first 90 days. Not because builders can't build them, because nobody teaches builders what comes after the build launches. Google just built the largest awareness funnel on Earth for AI agents. We own the space where those builders land when that agent is going to break. I wrote a deeper breakdown of what the Google course covers and where the gaps are on the Matt Murphy AI blog. Links in the bio. Check it out. But Google, they teach you how to build a rocket. The faction community teaches you how to land it.

</div>
