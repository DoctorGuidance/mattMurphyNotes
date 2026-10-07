# Episode 254: One mobile link

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Frontend Architecture & API Hygiene (`معماری فرانت‌اند، طراحی واسط و بهداشت API`) |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZLHBM9xY33/) |

---

## 🚨 1. The Incident & Attack Vector
Your mobile app exists, but when someone shares a link to your content, it opens in the browser, not the app like it was supposed to. The user hits a login wall, gets confused, and leaves. You lost them because of a missing configuration file.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Shares raw desktop web URLs on mobile marketing channels, landing mobile users on un-responsive, broken desktop layouts. | Implements universal mobile deep-linking and responsive viewport routing to ensure seamless mobile onboarding experiences. |

---

## 💡 3. Root Cause & Architectural Principle
You lost them because of a missing configuration file. Here are the three things you can do right now to fix it. Number one, configure Apple universal links.

---

## ⚡ 4. Hardening Action Checklist
- [ ] configure Apple universal links.
- [ ] configure Android app links.
- [ ] handle the fallback.

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
> **Production Heuristic:** Universal links in 30 minutes.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your mobile app exists, but when someone shares a link to your content, it opens in the browser, not the app like it was supposed to. The user hits a login wall, gets confused, and leaves. You lost them because of a missing configuration file. Here are the three things you can do right now to fix it. Number one, configure Apple universal links. Go create an apple.app site association file in your domain. Host it at your domain. com. This is a JSON file that tells iOS which URL path should open your app. No redirects. The link opens directly in your app every time. Apple verifies this file when the user installs your app. Step two, configure Android app links. Similarly, create a digital assets link file hosted at your doommain.com. Again, this JSON file tells Android which URLs open your app. Add intent filters to your Android manifest. X handles this with Expo linking package. Same URLs work on both platforms. Step three, handle the fallback. Not every user has your app installed on their phone. If the app is not installed, the link should go straight to your website. Your website shows the content plus a smart banner promoting the app install. Expo Router handles this with a single configuration. One URL, app installed, opens an app, not installed, opens in website with Install prompt. Universal links convert mobile web visitors into app users. Without them, every shared link is a dead end. Do you have any deep linking setups? What tripped you up? Tell me about it.

</div>
