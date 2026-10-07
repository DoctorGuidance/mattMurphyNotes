# Episode 165: Your user reported a bug

> **Category:** Authentication & Identity (احراز هویت و مدیریت نشست‌ها)  
> **Production Layer:** Layer 4  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DafuL1lggp3/](https://www.instagram.com/reel/DafuL1lggp3/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your user reported a bug. You asked them to describe it. They just said everything stopped working.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
They just said everything stopped working. So, that's not necessarily a great bug report. It's definitely a cry for help.

---

## ⚡ 3. Hardening Action Checklist
- [ ] session replays. Direct your AI to integrate session replays into your application.
- [ ] connect replay to error tracking. Direct your AI to link session replays directly to error events.
- [ ] Flag rage clicks. A user who clicks the same button seven times in 3

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #165
// Domain: 01-auth-identity
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #165 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #165');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your user reported a bug. You asked them to describe it. They just said everything stopped working. So, that's not necessarily a great bug report. It's definitely a cry for help. Here are the three things you direct your AI to do right now to fix it. Step one, session replays. Direct your AI to integrate session replays into your application. That way, every user session is fully recorded. So, every click, every scroll, every error, when a user reports a bug, You don't have to ask what happened. You watch what happened from their screen in real time. That's a win. Step two, connect replay to error tracking. Direct your AI to link session replays directly to error events. So when Sentry catches an exception, the replay is attached automatically. You see the error and the user experience that caused it side by side. No guessing, no reproducing. It's all right there. And step three, Flag rage clicks. A user who clicks the same button seven times in 3 seconds is not patient. They're stuck. Direct your AI to detect rage clicks and flag them as UX failures before a support ticket is filed. So stop asking users to describe bugs. Start watching what they experienced. That is orchestration and that is the win.

</div>
