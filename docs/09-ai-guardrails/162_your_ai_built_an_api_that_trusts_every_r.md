# Episode 162: Your AI built an API that trusts every request it receives

> **Category:** AI Guardrails, LLM Security & Compliance (مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی)  
> **Production Layer:** Layer 2  
> **Official Instagram Reel:** [https://www.instagram.com/reel/Dai-n_LjPMS/](https://www.instagram.com/reel/Dai-n_LjPMS/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your AI built an API that processes every single request it receives. No validation, no sanitization, no rejection. A request with a missing field gets processed.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
A request with a missing field gets processed. A request with a malicious payload gets processed. Everything your API receives, your AI trusts.

---

## ⚡ 3. Hardening Action Checklist
- [ ] input validation on every route. Direct your AI to validate the shape of every request before it touches your business logic.
- [ ] sanitization. Direct your AI to clean every string input before processing.
- [ ] rate awareness at the middleware level. Direct your AI to track request patterns per user per endpoint.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #162
// Domain: 09-ai-guardrails
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #162 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #162');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your AI built an API that processes every single request it receives. No validation, no sanitization, no rejection. A request with a missing field gets processed. A request with a malicious payload gets processed. Everything your API receives, your AI trusts. Here are the three things you need to direct your AI to do right now to fix it. Step one, input validation on every route. Direct your AI to validate the shape of every request before it touches your business logic. Wrong type rejected. Missing field rejected. Unexpected field stripped. If the request does not match the schema, it never reaches your database. And that's a win. Step two, sanitization. Direct your AI to clean every string input before processing. A user who types a script tag into a form field is either confused or possibly attacking you. Either way, your API should not execute it. And step three, rate awareness at the middleware level. Direct your AI to track request patterns per user per endpoint. A user hitting the same endpoint 50 times per second, they aren't using your app. They're probing it. Your middleware catches the pattern before your business logic ever sees it. So you always follow this rule. Trust nothing and validate everything. That is how you orchestrate an API.

</div>
