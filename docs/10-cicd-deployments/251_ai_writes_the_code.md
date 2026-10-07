# Episode 251: AI writes the code

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Testing, Staging & CI/CD (`تست، محیط‌های کاری، CI/CD و خط لوله استقرار`) |
| **Target Production Layer** | Layer 7 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZN3Z3IPD9a/) |

---

## 🚨 1. The Incident & Attack Vector
The AI wrote your code. You shipped it without reading it. It's three months later and now you have tech debt that you do not understand.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
It's three months later and now you have tech debt that you do not understand. Here are the three things you can do right now to fix it. Step one, add an AI reviewer to your pull request pipeline.

---

## ⚡ 4. Hardening Action Checklist
- [ ] add an AI reviewer to your pull request pipeline. Code rabbit, sorcery, or even a custom GitHub action that calls Claude.
- [ ] prompt your reviewer for architecture, not syntax. The default AI review catches typos and formatting.
- [ ] gate merges on review completion. Add a required status check in GitHub.

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #251
// Domain: 10-cicd-deployments
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #251 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #251');
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

The AI wrote your code. You shipped it without reading it. It's three months later and now you have tech debt that you do not understand. Here are the three things you can do right now to fix it. Step one, add an AI reviewer to your pull request pipeline. Code rabbit, sorcery, or even a custom GitHub action that calls Claude. Every PR triggers an automated review. The AI checks for security vulnerabilities, performance issues, and lock Loic errors. It posts inline comments on your PR so you can review it. You read the AI's feedback before you merge anything. That's a win. Step two, prompt your reviewer for architecture, not syntax. The default AI review catches typos and formatting. That's totally useless. Customize your prompt. Focus on business logic correctness, SQL injection vectors, unhandled edge cases, and N plus1 queries. Tell it to ignore style preference. Tell it to flag anything that touches off payments or data deletions. The review should catch what breaks in production, not what breaks a llinter. That's a win. Step three, gate merges on review completion. Add a required status check in GitHub. The PR cannot merge until AI review passes. Set severity thresholds. Critical issues block the merge. Warnings are onlyformational. Combined with your Canary deployment, from yesterday's video I dropped. You now have two safety nets for your system. AI catches it before the merge. Canary catches it after the deploy. So your AI wrote the code. Your AI should also be reviewing the code. And you are the orchestrator in the middle making the final call just like an AI directed engineer. Talk to you soon.

</div>
