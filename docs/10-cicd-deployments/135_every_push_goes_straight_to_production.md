# Episode 135: Every push goes straight to production

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Testing, Staging & CI/CD (`تست، محیط‌های کاری، CI/CD و خط لوله استقرار`) |
| **Target Production Layer** | Layer 7 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Da51JT3DSQi/) |

---

## 🚨 1. The Incident & Attack Vector
So every push goes directly to production. One bad merge and your customers see the bug before you do. Your AI builds on main and ships it live.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
Your AI builds on main and ships it live. Here are the three things you direct your AI to set up right now to fix it. Step one, build a staging environment.

---

## ⚡ 4. Hardening Action Checklist
- [ ] build a staging environment. So direct your AI to create an environment that mirrors your production environment.
- [ ] nothing ships without passing staging. Direct your AI to build a CI pipeline that runs tests against staging.
- [ ] one-click roll back. Something got through.

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #135
// Domain: 10-cicd-deployments
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #135 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #135');
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

So every push goes directly to production. One bad merge and your customers see the bug before you do. Your AI builds on main and ships it live. Here are the three things you direct your AI to set up right now to fix it. Step one, build a staging environment. So direct your AI to create an environment that mirrors your production environment. Same database schema, same services, same environmental variables. Versel preview deployments give you this almost for free. But if it doesn't, you got to build it. Every pull request gets its own preview. Test there, not in production. That's the win. Step two, nothing ships without passing staging. Direct your AI to build a CI pipeline that runs tests against staging. Tests pass, the pipeline promotes to production automatically. Tests fail, production never sees it. Your customers never see a broken feature, your team catches it for first. That's also a win. And step three, one-click roll back. Something got through. A bug made it past staging. These things happen to the best of us. Direct your AI to implement roll back to the last known good deploy. Not SSH into the server. Just one button previous version immediately. Every deployment is either a confident push or a quick roll back. It's time to stop shipping to production on a prayer. Start shipping to staging with a full plan. That's the win.

</div>
