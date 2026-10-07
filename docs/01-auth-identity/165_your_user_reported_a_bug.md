# Episode 165: Your user reported a bug

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Authentication & Identity (`احراز هویت و مدیریت نشست‌ها`) |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DafuL1lggp3/) |

---

## 🚨 1. The Incident & Attack Vector
Your user reported a bug.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Implements naive authentication in 'Your user reported a bug', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Your user reported a bug'. |

---

## 💡 3. Root Cause & Architectural Principle
They just said everything stopped working. So, that's not necessarily a great bug report. It's definitely a cry for help.

---

## ⚡ 4. Hardening Action Checklist
- [ ] session replays.
- [ ] connect replay to error tracking.
- [ ] Flag rage clicks.

---

## 💻 5. Hardened Production Implementation
```typescript
// guardrails/aiAuditTrail.ts
import crypto from 'crypto';
import { db } from '../lib/db';

export async function recordAIGeneration(userId: string, model: string, prompt: string, output: string) {
  const promptHash = crypto.createHash('sha256').update(prompt).digest('hex');
  await db.aiAuditLogs.create({
    data: {
      userId,
      modelName: model,
      promptSha256: promptHash,
      isSyntheticallyGenerated: true,
      timestamp: new Date()
    }
  });
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Stop asking. Start watching. That is orchestration.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your user reported a bug. You asked them to describe it. They just said everything stopped working. So, that's not necessarily a great bug report. It's definitely a cry for help. Here are the three things you direct your AI to do right now to fix it. Step one, session replays. Direct your AI to integrate session replays into your application. That way, every user session is fully recorded. So, every click, every scroll, every error, when a user reports a bug, You don't have to ask what happened. You watch what happened from their screen in real time. That's a win. Step two, connect replay to error tracking. Direct your AI to link session replays directly to error events. So when Sentry catches an exception, the replay is attached automatically. You see the error and the user experience that caused it side by side. No guessing, no reproducing. It's all right there. And step three, Flag rage clicks. A user who clicks the same button seven times in 3 seconds is not patient. They're stuck. Direct your AI to detect rage clicks and flag them as UX failures before a support ticket is filed. So stop asking users to describe bugs. Start watching what they experienced. That is orchestration and that is the win.

</div>
