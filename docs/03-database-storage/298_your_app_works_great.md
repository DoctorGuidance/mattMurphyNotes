# Episode 298: Your app works great

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Database & Storage Engineering (`پایگاه‌داده، روابط، ایندکس و پایداری داده`) |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYXGdH4AtnZ/) |

---

## 🚨 1. The Incident & Attack Vector
You think your vibe coded app works great, right? Until the API changes or the rate limit kicks in or that free tier you're using disappears and your entire app stops working right then. Well, here's how you're going to fix it.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
Well, here's how you're going to fix it. Number one, abstract your API calls. Never call an API directly from your main code.

---

## ⚡ 4. Hardening Action Checklist
- [ ] abstract your API calls. Never call an API directly from your main code.
- [ ] build a fallback plan. What happens when the API is down?
- [ ] own your data layer. Your database should be yours, not theirs.

---

## 💻 5. Hardened Production Implementation
```typescript
// Redis Token Bucket Rate Limiter
import { RateLimiterRedis } from 'rate-limiter-flexible';
const rateLimiter = new RateLimiterRedis({
  storeClient: redisClient,
  points: 10,   // 10 requests
  duration: 60, // per 60 seconds
});
await rateLimiter.consume(req.ip);
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Never deploy unverified AI-generated code directly to production without testing failure modes.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

You think your vibe coded app works great, right? Until the API changes or the rate limit kicks in or that free tier you're using disappears and your entire app stops working right then. Well, here's how you're going to fix it. Number one, abstract your API calls. Never call an API directly from your main code. Wrap it in a function, one place, one file. When the API changes, like Murphy's law, inevitably it will, You update it once, not 40 times. If you have open AI calls scattered across your whole app, that's a problem. You're only one breaking change away from rewriting the whole thing. So, one wrapper, one source of truth. That's the power move. Number two, build a fallback plan. What happens when the API is down? If the answer is my whole app breaks, you don't have an app. You have a wrapper around someone else's app that you cannot control. So, you need to build a grace fallback, a cached response of some sort, a cue that retries, even a message that says back in 60 seconds. Anything is better than a blank screen and silence, and you know it. Number three, own your data layer. Your database should be yours, not theirs. If you're storing everything inside a third party API and they shut down tomorrow, you lost everything for you and your customers. Keep a copy of everything that matters in a database you can control. APIs are only rentals. Your database, that's your ownership. You got to know the difference. More tips and tricks coming tomorrow.

</div>
