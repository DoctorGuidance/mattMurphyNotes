# Episode 087: Your AI is running on six-month-old instructions. That is

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Db6VI3WFqKD/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI is running on six-month-old instructions. That is why it is getting worse, not better.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends unvalidated user inputs straight to LLMs without budget caps or injection defenses in 'Your AI is running on six-month-old instructions. That is'. | Applies prompt sanitization, structured output validation (Zod), spend ceilings, and SGI metadata compliance. |

---

## 💡 3. Root Cause & Architectural Principle
Every MCP file you loaded, every MD file you wrote, every skill you installed, every automation you've configured, all of it still running right now, right? But your AI checks all of it every single time, even when it does not need any of it. So your context window is full of dated instructions for an LLM system that has been updated 15 times.

---

## ⚡ 4. Hardening Action Checklist
- [ ] stale files compete with current instructions.
- [ ] the LLM systems are getting better every single day.
- [ ] you got to clear your stack.

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
> **Production Heuristic:** We rebuild every 100 days. Version 9.0. Clear the stack. Rebuild clean.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI is running on sixmon old instructions. And that's why it's getting worse, not better. Every MCP file you loaded, every MD file you wrote, every skill you installed, every automation you've configured, all of it still running right now, right? But your AI checks all of it every single time, even when it does not need any of it. So your context window is full of dated instructions for an LLM system that has been updated 15 times. since you wrote any of those. And here are the three reasons why this is killing your output today. So, step one, stale files compete with current instructions. Your AI is trying to follow what you told it 6 months ago and what you're telling it right now at the exact same time. And when those two things conflict, and they will, the output just gets worse. Not because the model got dumber, because you were feeding it contradictions from the past. Every old skill, every old automation, every old connector that is still loaded is noise. And the more noise in your context window, the less room your AI has to think clearly about the task that's right in front of it. Step two, the LLM systems are getting better every single day. The model you are running today is materially more capable than the one you configured your stack for 6 months ago, but you're still forcing it to work through the same rappers, the same connectors, the same instructions you wrote when it was less capable. I get it. We've all been there. It's time to move forward. You're putting training wheels on a machine that no longer needs them. Those training wheels are slowing it down completely. That's not a win. And step three, you got to clear your stack. The head engineer at Anthropic will tell you straight up, all of his MD files, skills, and system configurations are cleared every 90 days at a minimum. I know we rebuild our entire agent infrastructure at Faction every 100 days. Not because they're broken. But because the tools get better and the old configurations hold them back. This is engineering discipline. Every 90 days, strip it down, rebuild it clean. Let the current model work at its current capability without dragging 6 months of baggage behind it. You get that? Your AI didn't get worse. Your instructions got a little stale. Clear the stack, rebuild it clean, and let it run. That's a win.

</div>
