# Episode 313: Something broke. Users noticed before you did

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Observability & Error Tracking (`مشاهده‌پذیری، لاگ ساختاریافته و رهگیری خطا`) |
| **Target Production Layer** | Layer 12 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYAwPCav_eC/) |

---

## 🚨 1. The Incident & Attack Vector
Something broke in production last night

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Discovers application crashes from angry user tweets hours after going down. | Automates Sentry stack-trace capture and Better Stack 30-second uptime pings with instant SMS alerts. |

---

## 💡 3. Root Cause & Architectural Principle
Something broke in production last night

---

## ⚡ 4. Hardening Action Checklist
- [ ] Isolate unverified components behind automated integration tests.
- [ ] Enforce fail-safe boundaries preventing cascade outages.
- [ ] Establish real-time observability alerts on critical paths.

---

## 💻 5. Hardened Production Implementation
```typescript
// monitoring/sentry.ts
import * as Sentry from '@sentry/node';

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 1.0,
  beforeSend(event) {
    // Strip sensitive PII before transmission
    delete event.user?.ip_address;
    return event;
  }
});
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Let us know if you're sure

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Something broke in production last night. You only know because a user told you in an email. You don't know what broke, when it broke, how many users it impacted because your vibecoded app doesn't have any logging. AI generates features. It doesn't generate observability. Your app can do 12 things really great, but you can't see any of them happening. No request logs, no error tracking, no performance metrics, no audit trail. nightmare. So when something goes wrong, your debugging process is read the code, guess what happened, deploy a fix, and hope. That's not engineering, folks. That's archaeology. That's the old way for dinosaurs. We inherited a vibecoded app that had been in production for 3 months. The founder told us it was mostly working, whatever that means. We added basic logging in the first week. In 7 days of logs, we discovered the app was throwing silent errors on 14% of all requests. A third party API was timing out three times a day and failing without any notifications. And one endpoint was taking 18 seconds to respond. Users were just sitting there waiting, right? So 3 months in production, nobody knew any of this because nobody could see any of it. So if you can't see what your app is doing, you can't fix what your app is doing. Logging isn't overhead. It's the difference between operating a system and hoping a system is going to work. So when we finish a vibe coded project at Faction, structured logging goes in before anything else, right? Because you can't improve what you can't observe. Does your app have logging? Real logging, not just console.log. Drop it in the comments. Let us know if you're sure.

</div>
