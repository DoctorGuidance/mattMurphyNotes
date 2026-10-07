# Episode 073: GitHub just showed you exactly where your AI money goes

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcMWtOgEgaE/) |

---

## 🚨 1. The Incident & Attack Vector
GitHub has just showed you exactly where your AI money goes, and most of you might not ever look, but GitHub's new usage report now breaks down your AI credits by model. Input tokens, output tokens, cash reads, and cash rights. For the first time, you can see exactly which model consumed the credits and what kind of tokens created the costs.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
For the first time, you can see exactly which model consumed the credits and what kind of tokens created the costs. So, your AI bill used to be a black box. Not anymore.

---

## ⚡ 4. Hardening Action Checklist
- [ ] model routing by task complexity. When an agent picks a model, it picks the best model available for every single call.
- [ ] input caching on repeating workflows. If your agent sends the same project context, the same system prompt, the same instructions on every single call, you're paying full token price for identical outputs on every cycle.
- [ ] a weekly cost breakdown by model, by workflow, and by token type. A monthly invoice tells you what you spent, sure, but a weekly breakdown tells you where to cut.

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #073
// Domain: 09-ai-guardrails
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #073 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #073');
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

GitHub has just showed you exactly where your AI money goes, and most of you might not ever look, but GitHub's new usage report now breaks down your AI credits by model. Input tokens, output tokens, cash reads, and cash rights. For the first time, you can see exactly which model consumed the credits and what kind of tokens created the costs. So, your AI bill used to be a black box. Not anymore. And here's what you're going to do with that vis. ibility. Step one, model routing by task complexity. When an agent picks a model, it picks the best model available for every single call. Formatting, parsing, boilerplate, routine lookups, all of it running through the most capable model because nobody told the agent to go match a model to the job. That one routing decision can cut a bill in half without changing a single output. So, direct your AI to build a routing layer that sends complex tasks to the best model and routes routine work to the cheapest model that produces the equivalent output. That's a win. Step two, input caching on repeating workflows. If your agent sends the same project context, the same system prompt, the same instructions on every single call, you're paying full token price for identical outputs on every cycle. So, low cache reads on the report, meaning nothing is being reused. The same input sent 10 times cost 10 times what it should. That's not a win. That is not a cost problem and it's actually an architecture problem that you're going to solve. So, direct your AI to restructure repeated inputs into cacheed context that carries across all calls. That's a win. And step three, a weekly cost breakdown by model, by workflow, and by token type. A monthly invoice tells you what you spent, sure, but a weekly breakdown tells you where to cut. Set a budget per workflow and flag anything that spikes. above that baseline. The difference between paying a bill and engineering cost structure is the difference between reacting and operating a business. So, direct your ad to build a weekly cost report you can actually review. Your AI bill just became fully readable. So, it's time to start reading it and that is definitely a win.

</div>
