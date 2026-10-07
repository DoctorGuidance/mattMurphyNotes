# Episode 248: 45-second request

> **Category:** Async Queues & Webhooks (صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی)  
> **Production Layer:** Layer 6  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DZSYNBNxE1k/](https://www.instagram.com/reel/DZSYNBNxE1k/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
A user clicks export report. Your API generates a PDF. It takes 45 seconds, so the request times out.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
It takes 45 seconds, so the request times out. The user clicks it again. So now you're generating two PDFs.

---

## ⚡ 3. Hardening Action Checklist
- [ ] never do heavy processing in the request cycle. When the user clicks export, your API does one thing.
- [ ] process jobs with a worker. Injest, trigger.dev, or bull mq.
- [ ] implement item potency keys. The user who clicked twice both clicks should produce one job, not two.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #248
// Domain: 07-async-queues-webhooks
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #248 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #248');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

A user clicks export report. Your API generates a PDF. It takes 45 seconds, so the request times out. The user clicks it again. So now you're generating two PDFs. Here are three things you can do right now to fix it. Step one, never do heavy processing in the request cycle. When the user clicks export, your API does one thing. Create a job record. Return a job ID immediately. status processing. The user sees a progress indicator. The actual work happens in the background. Your API responds in 200 milliseconds every time. That's a win. Step two, process jobs with a worker. Injest, trigger.dev, or bull mq. Injest is the easiest for server list. I use it the most. Define a function that runs when a job event fires. It processes at its own pace. If it fails, it retries with exponential backoff. The user isn't watching a spinner. They get a notification when it's done. That's a win. Step three, implement item potency keys. The user who clicked twice both clicks should produce one job, not two. Attach a unique key to every request. Before creating a new job, check if that key exists. If it does, return the existing job. No duplicates, immediate response times. background processing. So, no timeouts, no duplicates, and no angry users. That's a win. So, are you running operations synchronously that you should be running async? Let me know.

</div>
