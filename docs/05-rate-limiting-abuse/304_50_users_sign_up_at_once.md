# Episode 304: 50 users sign up at once

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Rate Limiting & Abuse Prevention (`محدودسازی نرخ، مقابله با DoS و بات‌ها`) |
| **Target Production Layer** | Layer 9 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYQMWv2Pohr/) |

---

## 🚨 1. The Incident & Attack Vector
You shipped your vibecoded app

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Ships demo code directly into production without verifying boundary limits or failure fallback paths. | Hardens systems with circuit breakers, exponential backoff retries, and isolated fault boundaries. |

---

## 💡 3. Root Cause & Architectural Principle
You shipped your vibecoded app

---

## ⚡ 4. Hardening Action Checklist
- [ ] Isolate unverified components behind automated integration tests.
- [ ] Enforce fail-safe boundaries preventing cascade outages.
- [ ] Establish real-time observability alerts on critical paths.

---

## 💻 5. Hardened Production Implementation
```typescript
// infrastructure/resilienceGuard.ts
export const config = {
  timeoutMs: 5000,
  retryPolicy: { retries: 3, backoffFactor: 2 },
  circuitBreaker: { failureThreshold: 5, resetTimeoutMs: 30000 }
};
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Follow along so you don't miss That's it

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

You shipped your vibecoded app. Users absolutely love it. Five people are using it perfectly. 15 people still great. It's growing. 50 people sign up at the same time and your database just locked up. Your API cues backed up, too. And your app returns a blank screen to all users. So, you didn't build a scaling problem. You inherited one. Unfortunately, because the AI that built your app to work for one user at a time, which many of these tools do. Every database query runs in sequence. Every API call waits for the last one to finish. And there's no connection pooling. There's no caching layer also. And someone in my comments said 30,000 users in 5 days and their app completely buckled. So, you're out there and you know all about it. Success shouldn't break your app, but right now it will. So, you need to prepare for it. The fix is coming next week. Follow along so you don't miss That's it.

</div>
