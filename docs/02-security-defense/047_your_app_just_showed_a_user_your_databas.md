# Episode 047: Your app just showed a user your database name, your server

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcybEeAEhP8/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI built app just showed a user your database name, your server file path, and their query that failed. And they were not trying to hack you. They accidentally clicked on a broken link.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
They accidentally clicked on a broken link. Your AI built error handling. Great.

---

## ⚡ 4. Hardening Action Checklist
- [ ] separate your error responses by environment. Development shows the full stack trace.
- [ ] route every error to centralized logging, not to the user screen. Every error your app throws should be captured, timestamped, and searchable in your monitoring system.
- [ ] build custom error pages that reveal nothing. So your 404 or your 500 or your timeout page, every one of them should be branded, helpful, and architecturally silent.

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #047
// Domain: 02-security-defense
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #047 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #047');
  }
  return true;
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Never deploy unverified AI-generated code directly to production without testing failure modes.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI built app just showed a user your database name, your server file path, and their query that failed. And they were not trying to hack you. They accidentally clicked on a broken link. Your AI built error handling. Great. Detailed stack traces, full database queries, and internal file paths. However, you shipped it to production, and now your users are seeing the same data. So, an attacker does not need to probe your system. Your error pages are doing the reconnaissance for them. So, let's get it cleaned up. Step one, separate your error responses by environment. Development shows the full stack trace. Production shows a generic message. Your users should never see an error that contains a file path, a query string, or a database name, or even a package version. So, direct your AI to implement environmentaware error handling so that it returns detailed errors only in development and returns generic userfriendly responses in production. That's definitely a win. Step two, route every error to centralized logging, not to the user screen. Every error your app throws should be captured, timestamped, and searchable in your monitoring system. No doubt about it. The user sees a clean error page. You see the full detail in your logs. So, direct your AI to implement structured error logging that captures the full stack trace request context and the user session data in your monitoring tool without exposing any of it to the client. That's also a win. And step three, build custom error pages that reveal nothing. So your 404 or your 500 or your timeout page, every one of them should be branded, helpful, and architecturally silent. So direct your AI to build custom error pages for every common error code. so that it gives the user a clear next step without revealing any server side details. Those users who found a bug, do not let the bug write itself or the report. That's not a win.

</div>
