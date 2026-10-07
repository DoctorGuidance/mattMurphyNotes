# Episode 241: Two multi-agent patterns

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZaJ_faRdcV/) |

---

## 🚨 1. The Incident & Attack Vector
Two multi-agent patterns.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Deploys chaotic multi-agent networks where agents talk in unconstrained loops, generating massive token bills without completing tasks. | Structures multi-agent workflows as deterministic supervisor-worker state machines with strict turn limits and goal gates. |

---

## 💡 3. Root Cause & Architectural Principle
There's two patterns. It's one decision to make. And here are the three things you do to determine which one.

---

## ⚡ 4. Hardening Action Checklist
- [ ] start with orchestrator pattern by default.
- [ ] know when to switch to the conductor pattern.
- [ ] never start with the conductor ever.

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
> **Production Heuristic:** Earn conductor with data.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

You're about to build a multi- aent system. The first architecture decision you make is going to determine whether it scales or it fails. There's two patterns. It's one decision to make. And here are the three things you do to determine which one. Step one, start with orchestrator pattern by default. I say this to everyone. Don't change it. One central agent receives every request. It decides which sub aents to call. It collects all of their outputs. It then synthesizes is the final response. Typical hub and spoke situation. Simple to reason about, simple to debug. That is your default. That is a win. Step two, know when to switch to the conductor pattern. Conductor means agents are passing work to each other in a chain or a graph. There's no single controller. So each agent decides who gets the baton next. You use this for emergent workflows like research tasks or complex reasoning chains or deep creative generation anywhere. The next step depends on what the previous agent discovered. So step three, never start with the conductor ever. The mistakes most builders make that we see is choosing conductor because it sounds cool or it looks cool, right? They then spend weeks debugging circular agent calls. So you start with orchestrator, get your outputs validated, get your error handling solid, and only migrate specific sub workflows to conductor when your data proves that the orchestrator is your bottleneck. So orchestrator first, conductor when earned always, that's the best practice. So what are you building right now with multi- aents? Tell me about it in the comments.

</div>
