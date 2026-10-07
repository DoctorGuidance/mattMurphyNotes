# Episode 141: Your AI handles 70% of support

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Authentication & Identity |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Da02icHj2ss/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI handles 70% of support.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Permits automated AI support workflows to execute account actions based on unauthenticated user-supplied email claims. | Verifies cryptographic session signatures and tenant scopes before allowing AI agents to trigger administrative or billing operations. |

---

## 💡 3. Root Cause & Architectural Principle
Your AI handles 70% of the support automatically from the playbooks you built, the known issues, the documented fixes, password resets, permission syncs, configuration errors. So again, when those playbooks exist, the agent follows them perfectly. The customer never files a ticket in most cases.

---

## ⚡ 4. Hardening Action Checklist
- [ ] the billing dispute where the customer is right but the system said otherwise.
- [ ] the feature request disguised as a bug report.
- [ ] the angry email that is not about the bug.

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
> **Production Heuristic:** Build the 70% so you have time for the 30%.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Just last week, I told you your AI assistant is your first support engineer. And this week, I want to tell you where the agent stops and you start as the human in the loop. Your AI handles 70% of the support automatically from the playbooks you built, the known issues, the documented fixes, password resets, permission syncs, configuration errors. So again, when those playbooks exist, the agent follows them perfectly. The customer never files a ticket in most cases. That is the way the 70% is supposed to work. But the 30% that determines whether customers stay or leave is because the human in the loop. So step one, the billing dispute where the customer is right but the system said otherwise. So a customer is charged twice. Your AI system shows one charge. They have a screenshot of two charges. When your AI assistant reviews it, it sees one charge. It closes the ticket as resolved. The customer is furious because your bot just told them everything's fine. This is one of those spots that requires a human in the loop that can check the payment dashboard, find the duplicate authorization, issue the customer a refund, and write or tell the customer that they acknowledge the mistake. It's normal human stuff, right? Step two, the feature request disguised as a bug report. A customer says a filter is broken, right? It works exactly the way it was designed, but they expected it to do something else completely. Your AI doesn't see an error in that, so it closes the ticket. The customer feels totally dismissed, cancels. This requires a human who reads the intent behind the request and decides whether the product should change to serve other customers with the same request. Step three, the angry email that is not about the bug. A customer sends a furious message about a minor formatting issue, but we all know it's not about formatting. It's about the three other issues they had last month that were never resolved. The formatting issue is just the last straw. So, your AI responds to the formatting issue. Uh-oh, the customer cancels. This requires a human who reads the history and picks up the phone and calls that customer. The 30% is not about technical complexity. It's judgment, empathy mixed with nuanced context that your AI does not have. So, you need to build the 70% so the time you save for the 30% is there because 30% is where the trust is earned or lost with every customer. So get it cleared up.

</div>
