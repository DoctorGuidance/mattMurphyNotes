# Episode 205: Silent 2 AM Server Crashes: Unhandled Promise Rejections

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Observability & Error Tracking (`مشاهده‌پذیری، لاگ ساختاریافته و رهگیری خطا`) |
| **Target Production Layer** | Layer 12 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZ8HOqlgZy5/) |

---

## 🚨 1. The Incident & Attack Vector
An asynchronous background task throws an unhandled rejection at 2 AM. The Node.js event loop terminates immediately. The server crashes silently with no log entries, leaving customers facing 502 Bad Gateway until morning.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Leaves uncaught exceptions and unhandled promise rejections unhandled in Node.js, crashing the server process silently. | Registers global process handlers for uncaughtException and unhandledRejection, logging context to Sentry with graceful restart. |

---

## 💡 3. Root Cause & Architectural Principle
Asynchronous runtimes require proactive error budgeting. Capture unhandled exceptions globally, report structured context to monitoring systems, and restart gracefully.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Register global handlers for `unhandledRejection` and `uncaughtException` in your entry file.
- [ ] Send complete error contexts with correlation IDs to an error tracking service (Sentry/Datadog).
- [ ] Configure Docker restart policies (`restart: unless-stopped`) or PM2 process supervisors.

---

## 💻 5. Hardened Production Implementation
```typescript
// server.ts - Global Unhandled Error Boundary
import * as Sentry from '@sentry/node';

process.on('unhandledRejection', (reason: Error) => {
  console.error('CRITICAL: Unhandled Rejection:', reason);
  Sentry.captureException(reason);
});

process.on('uncaughtException', (error: Error) => {
  console.error('FATAL: Uncaught Exception:', error);
  Sentry.captureException(error);
  process.exit(1); // Exit to let Docker/PM2 cleanly restart container
});
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** An unhandled promise rejection in production is a ticking time bomb. Capture it globally or let your users tell you when you're down.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your app just crashed at 2:00 in the morning and you found out at 9 in the morning when a customer emailed support. 7 hours of downtime, zero alerts. Here are the three things you set up right now to make sure that never happens again. Step one, health checks. A process that pings your application every 60 seconds and asks it one question. Are you alive? Not are you fast, not are you correct, not are you connected, but are you alive? When the answer is no, your phone instantly rings, not your customer's patience. This takes 10 minutes to configure and saves you every single time it happens. That's a win. Step two, error tracking. Your application throws errors every single day. Most of them you never ever see. An error tracker captures every single exception, groups them by frequency, and shows you which ones affect real users. The error that crashes one user's workflow 300 times a week has been happening for months, and you didn't even know it. you just never looked and that's the reason that you set these systems up. Step three, uptime monitoring from your outside infrastructure. Your server says it is healthy all the time, but your users in Singapore can't reach it. External monitoring checks from multiple regions of the world. Your internal dashboard is not your customer's experience. So, stop finding out about downtime from people who are paying to use your system.

</div>
