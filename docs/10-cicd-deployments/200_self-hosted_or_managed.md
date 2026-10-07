# Episode 200: Self-hosted or managed

> **Category:** Testing, Staging & CI/CD (تست، محیط‌های کاری، CI/CD و خط لوله استقرار)  
> **Production Layer:** Layer 7  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DaBItqrFHiF/](https://www.instagram.com/reel/DaBItqrFHiF/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your tests are passing locally, but they're failing in CI. You run them again locally and they pass again. Here are the three things that are different between CI and local that you never checked.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
Here are the three things that are different between CI and local that you never checked. Step one, environmental variables. Your local machine has variables set from 6 months ago, hard set, right?

---

## ⚡ 3. Hardening Action Checklist
- [ ] environmental variables. Your local machine has variables set from 6 months ago, hard set, right?
- [ ] database state. Your local database has seed data from the last time you ran a test suite, right?

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #200
// Domain: 10-cicd-deployments
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #200 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #200');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your tests are passing locally, but they're failing in CI. You run them again locally and they pass again. Here are the three things that are different between CI and local that you never checked. Step one, environmental variables. Your local machine has variables set from 6 months ago, hard set, right? But your CI environment starts fresh every single run. That missing variable does not throw an error. It returns as undefined. And undefined, we all know, behaves differently than the value you had expected. Your test is passing because your local machine is remembering something, but CI does not. Step two, database state. Your local database has seed data from the last time you ran a test suite, right? Well, CI starts with an empty database every single time. The test that passes locally depends on data that exists because a different test created it last Tuesday. Tests that depend on other tests are not tests, they're assumptions. Step three. timing. Your local machine runs the test in 200 milliseconds. CI runs it on a shared runner with limited resources. The timeout you never thought about triggers. The race condition that never reproduces locally reproduces every single time under load. Right? So CI does not lie. Your local machine does. You have to trust the pipeline. So go check these things.

</div>
