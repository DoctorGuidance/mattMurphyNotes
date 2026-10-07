# Episode 145: Your security kicks users out every 15 minutes

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Authentication & Identity (`احراز هویت و مدیریت نشست‌ها`) |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Daxv0QLgG8B/) |

---

## 🚨 1. The Incident & Attack Vector
Your security settings are kicking users out every 15 minutes, even when they're actively working. So, your definition of idle might be broken. Here are the three things you're going to direct your AI to fix right now.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
Here are the three things you're going to direct your AI to fix right now. Step one, define meaningful activity. Mouse movement, not an activity.

---

## ⚡ 4. Hardening Action Checklist
- [ ] define meaningful activity. Mouse movement, not an activity.
- [ ] warn them before you kill them. Direct your AI to show a modal 60
- [ ] preserve state on reauthentication. The session expired.

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #145
// Domain: 01-auth-identity
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #145 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #145');
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

Your security settings are kicking users out every 15 minutes, even when they're actively working. So, your definition of idle might be broken. Here are the three things you're going to direct your AI to fix right now. Step one, define meaningful activity. Mouse movement, not an activity. A tab open in the background, also not an activity. Direct your AI to track actions that prove the user is still working. Form submissions, but button clicks, API calls, page navigation. If the user is reading a long document without clicking, that also is not idle. So, build an exception for sustained focus. That's a win. Step two, warn them before you kill them. Direct your AI to show a modal 60 seconds before the session expires. Your session expires in 60 seconds. Click to stay logged in. The user who stepped away for coffee sees it when they return. The user who left the office for the day doesn't That's the win. One warning will save you hundreds of frustrated support tickets. Trust me. Step three, preserve state on reauthentication. The session expired. The user logs back in. You need to direct your AI to return them exactly where they were at. Not the homepage, not a blank dashboard, their unsaved form, their half-completed workflow, wherever they were. If reauthentication erases that work, your security just cost you a customer. Secure sessions, smart timeouts, and preserve state. Those are best practices. So, build security that protects you without punishing your users.

</div>
