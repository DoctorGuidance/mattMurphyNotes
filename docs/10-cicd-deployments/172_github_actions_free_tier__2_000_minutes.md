# Episode 172: GitHub Actions free tier. 2,000 minutes

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Testing, Staging & CI/CD (`تست، محیط‌های کاری، CI/CD و خط لوله استقرار`) |
| **Target Production Layer** | Layer 7 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaaYDrMkbpW/) |

---

## 🚨 1. The Incident & Attack Vector
You use the free tier of GitHub actions on CI/CD. 2,000 minutes a month, automatic builds on every push. Your solo project uses 80 minutes.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
Your solo project uses 80 minutes. No problem. It's got you covered.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Your solo project uses 80 minutes.
- [ ] A bug ships to production because the safety net ran out of minutes.
- [ ] And that day always arrives during a sprint and not in between them.

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #172
// Domain: 10-cicd-deployments
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #172 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #172');
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

You use the free tier of GitHub actions on CI/CD. 2,000 minutes a month, automatic builds on every push. Your solo project uses 80 minutes. No problem. It's got you covered. You add a team member, the minutes double. You add integration testing, the minutes triple. You add a staging and deployment step, quadruple. On day 19 of the month, guess what? 2,000 minutes totally gone. And now your pipeline has stopped running. Your team is pushing code without tests, without linting, and without checks. A bug ships to production because the safety net ran out of minutes. And so you upgrade to pay as you go, which is like $4 per additional minute on Mac OS. So your 300minut overrun cost you $1,200 for a CI tool that was free 19 days ago. The free tier was designed to get you started. The pricing was designed to capture you when it mattered the most, and it captured you on the day your team needed a pipeline the most. So, every CI platform has a free tier. Also, every CI platform has a trapdoor underneath it. You do not plan for the day that your team outgrows that ceiling. And that day always arrives during a sprint and not in between them.

</div>
