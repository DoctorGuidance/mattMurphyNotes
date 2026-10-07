# Episode 182: Vercel's Hobby plan allows 10 concurrent serverless

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Cloud Infrastructure & FinOps (`معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaSxssyiLWe/) |

---

## 🚨 1. The Incident & Attack Vector
Vercel's Hobby plan allows 10 concurrent serverless executions.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |

---

## 💡 3. Root Cause & Architectural Principle
Versel's hobby plan that allows what 10 concurrent executions. So your 11th gets a cold start, your 20th gets a timeout, and your 50th error page out of here. You're not hitting your codes limits, you're hitting your platform's limits.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Inspect the existing code paths and identify unvalidated boundary inputs.
- [ ] Implement defense-in-depth guardrails preventing unauthorized state modification.
- [ ] Add automated regression tests verifying failure scenarios before shipping.

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
> **Production Heuristic:** You never read the limits page.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

You deploy to Versell serverless functions that scale automatically except when they don't. And that's usually on launch day when traffic spikes and your functions all start queuing up. Versel's hobby plan that allows what 10 concurrent executions. So your 11th gets a cold start, your 20th gets a timeout, and your 50th error page out of here. You're not hitting your codes limits, you're hitting your platform's limits. The marketing page page said serverless scales automatically and it does. It scales automatically within the boundaries of the plan and the plan has boundaries that you never read. Execution time limits 10 seconds on hobby, 60 seconds on pro. So your AI feature needs 15 to 20 seconds says a lot. What about bandwidth caps? 100 gigabytes sounds like a lot until your imageheavy app burns through it in a week. Or function size limits. Your bundled serverless function exceeds the 50 megabyte ceiling and the deploy fails silently. Netlefi has different walls. AWS Lambda has different walls. Cloudflare workers has different walls. Every platform markets infinite scale, but every platform also has a ceiling. And you, you're about to find yours on the worst possible day ever.

</div>
