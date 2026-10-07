# Episode 241: Two multi-agent patterns

> **Category:** AI Guardrails, LLM Security & Compliance (مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی)  
> **Production Layer:** Layer 2  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DZaJ_faRdcV/](https://www.instagram.com/reel/DZaJ_faRdcV/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
You're about to build a multi- aent system. The first architecture decision you make is going to determine whether it scales or it fails. There's two patterns.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
There's two patterns. It's one decision to make. And here are the three things you do to determine which one.

---

## ⚡ 3. Hardening Action Checklist
- [ ] start with orchestrator pattern by default. I say this to everyone.
- [ ] know when to switch to the conductor pattern. Conductor means agents are passing work to each other in a chain or a graph.
- [ ] never start with the conductor ever. The mistakes most builders make that we see is choosing conductor because it sounds cool or it looks cool, right?

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #241
// Domain: 09-ai-guardrails
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #241 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #241');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

You're about to build a multi- aent system. The first architecture decision you make is going to determine whether it scales or it fails. There's two patterns. It's one decision to make. And here are the three things you do to determine which one. Step one, start with orchestrator pattern by default. I say this to everyone. Don't change it. One central agent receives every request. It decides which sub aents to call. It collects all of their outputs. It then synthesizes is the final response. Typical hub and spoke situation. Simple to reason about, simple to debug. That is your default. That is a win. Step two, know when to switch to the conductor pattern. Conductor means agents are passing work to each other in a chain or a graph. There's no single controller. So each agent decides who gets the baton next. You use this for emergent workflows like research tasks or complex reasoning chains or deep creative generation anywhere. The next step depends on what the previous agent discovered. So step three, never start with the conductor ever. The mistakes most builders make that we see is choosing conductor because it sounds cool or it looks cool, right? They then spend weeks debugging circular agent calls. So you start with orchestrator, get your outputs validated, get your error handling solid, and only migrate specific sub workflows to conductor when your data proves that the orchestrator is your bottleneck. So orchestrator first, conductor when earned always, that's the best practice. So what are you building right now with multi- aents? Tell me about it in the comments.

</div>
