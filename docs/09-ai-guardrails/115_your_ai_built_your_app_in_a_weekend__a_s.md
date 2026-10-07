# Episode 115: Your AI built your app in a weekend. A security auditor

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbTF4zkEegn/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI built your app in a weekend. A security auditor would shut it down by Monday.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends unvalidated user inputs straight to LLMs without budget caps or injection defenses in 'Your AI built your app in a weekend. A security auditor'. | Applies prompt sanitization, structured output validation (Zod), spend ceilings, and SGI metadata compliance. |

---

## 💡 3. Root Cause & Architectural Principle
Rate limits that don't even exist and logging that's capturing nothing. So yeah, your AI optimized for speed and built something fast, but a security auditor that walks in is going to optimize for survival. Right now, your app won't pass a basic review.

---

## ⚡ 4. Hardening Action Checklist
- [ ] error handling that protects your internals.
- [ ] security headers on every response.
- [ ] input validation on every endpoint, not just your login form, every form, every API parameter, every query string.

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
> **Production Heuristic:** So direct your AI to lock it down before someone else tests what your AI left wide open

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Yeah, your AI built an app in a weekend, but a security auditor walks in on Monday morning, shuts it right down. Every default wide open stack trace totally public endpoints accepting requests from anywhere. Rate limits that don't even exist and logging that's capturing nothing. So yeah, your AI optimized for speed and built something fast, but a security auditor that walks in is going to optimize for survival. Right now, your app won't pass a basic review. So, here are three things you direct your AI to lock down right now. Before someone tests your app the way an auditor would step one, error handling that protects your internals. Right now, when something breaks, your app returns a stack trace that tells an attacker exactly what framework you're running, what databases you're using, where your code has failed. So, your AI built error handling for debugging, right? But it didn't build error handling for production protection. So, generic messages to the users, detailed logs on the back end, and your AI can split all these in an hour. Without it, every error your app throws is a map for someone who wants to break in. And those those actually for sale on the dark web. Step two, security headers on every response. Content security policies, X-frame options, strict transport security. These are HTTP P level headers that tell browsers how to protect your users. Your AI never set them because most frameworks do not even include them by default. The security auditor checks these first because they take 5 minutes to configure and their absence tells the auditor that nobody is paying attention in this build. And step three, input validation on every endpoint, not just your login form, every form, every API parameter, every query string. Your AI validates what it thinks a user will submit. An attacker submits what your AI never imagined. SQL injections, cross-sight scripting, malformed payloads designed to break your parser in half. Your AI can add validation libraries to every input in an afternoon. Without them, your app is trusting every request it receives. And trust is how breaches always start. So your AI builds fast, doesn't build quality, and it does not build safe. So direct your AI to lock it down before someone else tests what your AI left wide open.

</div>
