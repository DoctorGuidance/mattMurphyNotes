# Episode 182: Vercel's Hobby plan allows 10 concurrent serverless

> **Category:** Cloud Infrastructure & FinOps (معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه)  
> **Production Layer:** Layer 6  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DaSxssyiLWe/](https://www.instagram.com/reel/DaSxssyiLWe/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
You deploy to Versell serverless functions that scale automatically except when they don't. And that's usually on launch day when traffic spikes and your functions all start queuing up. Versel's hobby plan that allows what 10 concurrent executions.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
Versel's hobby plan that allows what 10 concurrent executions. So your 11th gets a cold start, your 20th gets a timeout, and your 50th error page out of here. You're not hitting your codes limits, you're hitting your platform's limits.

---

## ⚡ 3. Hardening Action Checklist
- [ ] So your 11th gets a cold start, your 20th gets a timeout, and your 50th error page out of here.
- [ ] You're not hitting your codes limits, you're hitting your platform's limits.
- [ ] The marketing page page said serverless scales automatically and it does.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #182
// Domain: 11-cloud-finops
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #182 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #182');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

You deploy to Versell serverless functions that scale automatically except when they don't. And that's usually on launch day when traffic spikes and your functions all start queuing up. Versel's hobby plan that allows what 10 concurrent executions. So your 11th gets a cold start, your 20th gets a timeout, and your 50th error page out of here. You're not hitting your codes limits, you're hitting your platform's limits. The marketing page page said serverless scales automatically and it does. It scales automatically within the boundaries of the plan and the plan has boundaries that you never read. Execution time limits 10 seconds on hobby, 60 seconds on pro. So your AI feature needs 15 to 20 seconds says a lot. What about bandwidth caps? 100 gigabytes sounds like a lot until your imageheavy app burns through it in a week. Or function size limits. Your bundled serverless function exceeds the 50 megabyte ceiling and the deploy fails silently. Netlefi has different walls. AWS Lambda has different walls. Cloudflare workers has different walls. Every platform markets infinite scale, but every platform also has a ceiling. And you, you're about to find yours on the worst possible day ever.

</div>
