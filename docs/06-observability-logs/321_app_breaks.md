# Episode 321: App breaks

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Observability & Error Tracking (`مشاهده‌پذیری، لاگ ساختاریافته و رهگیری خطا`) |
| **Target Production Layer** | Layer 12 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DXuq33Sjzgh/) |

---

## 🚨 1. The Incident & Attack Vector
The app breaks, so you check the logs

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Runs applications without automated healthcheck probes, causing container orchestrators to route traffic to dead instances. | Implements separate `/health/liveness` and `/health/readiness` probes for automated Kubernetes/Docker restart and routing. |

---

## 💡 3. Root Cause & Architectural Principle
The app breaks, so you check the logs

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
> **Production Heuristic:** If your app broke right now, would you know why or would you be guessing

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

The app breaks, so you check the logs. Holy moly, there are no logs. Welcome to the logging black hole in Vibe Coding. Here's what happens when vibe coded apps. AI generates code that works, the happy path. But it doesn't generate code that tells you what it's doing. No logging, no tracing, no breadcrumbs. User reports a bug, it just stopped working, like they all say, right? Well, great. When did it stop working? What were they doing when it stopped working? What error occurred? Well, no logging means nobody knows. Nothing was recorded. So, you're now debugging blind, adding console.log statements after the fact, trying to reproduce something you can't see. And in production, forget about it. That bug that happens sometimes for some users, you're never going to find it. Actually, there's not even any evidence that it actually happened, right? So, here's what productionready logging really looks like. Structured logs with time stamps, user ids, and request ids, not console.log, actual structured data you can query or log levels that make sense, right? Debug for development, info for normal operations, and error for things that break. Not everything needs to be dumped into the same stream or centralized logging, right? Not scattered across every server file that nobody checks, but aggregated somewhere you can actually search and get to it. When we finish vibe coded projects at Faction for customers, Logging infrastructure is foundational because you can't fix what you can't see. Be honest. If your app broke right now, would you know why or would you be guessing? Drop it in the comments.

</div>
