# Episode 288: Your frontend talks to the database directly

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Database & Storage Engineering (`پایگاه‌داده، روابط، ایندکس و پایداری داده`) |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYiSfwGP2D9/) |

---

## 🚨 1. The Incident & Attack Vector
Your app calls the database from the front end. That's not an architecture strategy. That's a security hole with UI.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
That's a security hole with UI. Layer two of 13 is where your app's brain lives. Business logic, data validation, rate limiting, request authentication.

---

## ⚡ 4. Hardening Action Checklist
- [ ] A user can send a thousand requests in a second, your app is going to process all of them.
- [ ] A user sends malformed data, your app's just going to store it.
- [ ] And a user manipulates the client side code, your app trusts it.

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

Your app calls the database from the front end. That's not an architecture strategy. That's a security hole with UI. Layer two of 13 is where your app's brain lives. Business logic, data validation, rate limiting, request authentication. Without a proper backend, your front end talks to the database directly and your secrets live directly in your browser. Your logic can be inspected by anyone at that point. The AI builds you a front that calls Superbase directly works great for a demo, but that's terrible for production. There's no input validation. There's no rate limiting. There's no business rules enforcement. A user can send a thousand requests in a second, your app is going to process all of them. A user sends malformed data, your app's just going to store it. And a user manipulates the client side code, your app trusts it. Layer 2 is not glamorous. It's the bouncer at the door. And right now, your door is wide open. It's time to lock it up so you can ship.

</div>
