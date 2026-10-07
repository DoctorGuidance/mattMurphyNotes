# Episode 217: Three hundred dependencies in your App

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Testing, Staging & CI/CD |
| **Target Production Layer** | Layer 7 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZvd_LOvbRH/) |

---

## 🚨 1. The Incident & Attack Vector
Three hundred dependencies in your App.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Pulls in 300 unvetted third-party npm dependencies, creating a massive attack surface for supply chain compromises. | Audits the dependency tree, removes redundant packages, and pins exact versions with lockfile integrity verification. |

---

## 💡 3. Root Cause & Architectural Principle
Step one, understand your supply chain. Every package you install is code written by a stranger with full access to your environment variables, your file system, and your network. You trusted it because it had a lot of downloads.

---

## ⚡ 4. Hardening Action Checklist
- [ ] understand your supply chain.
- [ ] audit and pin your dependencies.
- [ ] reduce your surface area.

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
> **Production Heuristic:** Own what runs in your app.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

You have 300 dependencies in your project and you wrote zero of them and any one of them can compromise your entire application for your users. So here are the three things you're going to do right now to fix it. Step one, understand your supply chain. Every package you install is code written by a stranger with full access to your environment variables, your file system, and your network. You trusted it because it had a lot of downloads. Got it? We've all done it. But downloads, they are Definitely not a security audit. Run one. Step two, audit and pin your dependencies. Tools like MPM Audit, Sneak, and Dependabot all scan your dependency tree for well-known vulnerabilities. Pin your version so a compromised update does not automatically deploy to production. If you're not committing your lock file, the internet is going to decide what code runs your app. You don't want that. Step three, reduce your surface area. Every dependency is an open door to your app. Fewer doors, fewer entry points. Before you install a package, ask yourself this one question. Can I write this in 20 lines? If yes, write it yourself. A utility you control is safer than a package with 40 transitive dependencies that you've never read. So, not every problem needs a new package. Make sure you own what runs in your app.

</div>
