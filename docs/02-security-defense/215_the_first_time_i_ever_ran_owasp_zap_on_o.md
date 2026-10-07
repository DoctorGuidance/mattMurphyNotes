# Episode 215: The first time I ever ran OWASP ZAP on one of my own apps

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZyEXA6vDXs/) |

---

## 🚨 1. The Incident & Attack Vector
The first time I ever ran OWASP ZAP on one of my own apps.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Deploys web applications to production without running automated dynamic application security testing (DAST) tools. | Integrates OWASP ZAP dynamic vulnerability scanning into CI/CD pipelines to detect injection and header flaws before release. |

---

## 💡 3. Root Cause & Architectural Principle
Step one, you got to know what OASP's app even is. It's a free open-source security scanner. You point it at your app.

---

## ⚡ 4. Hardening Action Checklist
- [ ] you got to know what OASP's app even is.
- [ ] run it before launch, never after.
- [ ] do not try to fix everything at once.

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
> **Production Heuristic:** Scan yourself before someone else does.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

The first time I ran OWAP Zap against one of my own applications, I found 11 vulnerabilities, 11 in an app that I thought was totally ready to ship. So, here are the three things you can do right now to fix it. Step one, you got to know what OASP's app even is. It's a free open-source security scanner. You point it at your app. It crawls every page, tests every form, probes every API endpoint, and it tells you exactly where you're exposed. cross-sight scripting, SQL injections, missing security headers, open redirects, things you did not know to look for, and your vibe coded app didn't tell you about them either. And these are things that your users will never report. Things an attacker will find in minutes. Step two, run it before launch, never after. Not when a customer asks if you've done a security audit, not when an investor asks about sock 2, but before the first user signs up because the vulnerability zap finds are the same ones every automated bot scanner on the internet finds. The only question is whether you're going to find them first. Step three, do not try to fix everything at once. Zap will give you a report. The report will be long. Start with the highs and the criticals. Injection flaws, authentication bypasses, sensitive data exposures. Those are the ones that end companies. The mediums and lows, they're real, but they're not emergencies. You triage the list the same you would triage your set of bugs, right? Severity first, velocity second. The lesson today is scan yourself but before someone else does. Security first.

</div>
