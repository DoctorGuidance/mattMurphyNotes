# Episode 095: Your AI agent forgot what it was doing halfway through the

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbwB5V_EvJS/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI agent forgot what it was doing halfway through the job.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends unvalidated user inputs straight to LLMs without budget caps or injection defenses in 'Your AI agent forgot what it was doing halfway through the'. | Applies prompt sanitization, structured output validation (Zod), spend ceilings, and SGI metadata compliance. |

---

## 💡 3. Root Cause & Architectural Principle
Step one was great. Step five was pretty solid. By step 15, it was contradicting step three.

---

## ⚡ 4. Hardening Action Checklist
- [ ] was great.
- [ ] it was contradicting step three.
- [ ] it had forgotten the project altogether.

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
> **Production Heuristic:** Directed in pieces verify in between that is orchestration and that is the win

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Did your AI agent forget what it was doing halfway through the job? It started strong. Step one was great. Step five was pretty solid. By step 15, it was contradicting step three. And by step 30, it had forgotten the project altogether. Well, that's not a bug, folks. That is a context window limit. And every single builder using AI agents for complex work hits it every day. So, here are three things you direct your AI to build so your agent stays coherent. across long operations. Step one, a structured context document that travels with every task. Your AI agent does not remember what it did 10 steps ago unless you tell it. So direct your AI to create a running project state file that updates after every step, what has been completed, what is in progress, what the constraints might be, and what decisions have been made. So when the agent starts a new step, it reads that state file first. And that file is the memory your agent does not not have natively. So that's a win. Step two, task decomposition before execution. A 30-step job should never run as one continuous conversation. So direct your AI to break complex work into discrete chunks of five to seven steps each. Each chunk gets its own session with the state file that passed in the start. So smaller scopes mean the agent never drifts far enough to contradict itself. The architecture of how you feed your work work to your agent matters more than which model you're using. So figure it out. Step three, a validation checkpoint between every chunk. Before the agent moves from chunk one to chunk two, something has to verify that output. And that something, that's you. So direct your AI to pause after each chunk and present a summary for you to review before proceeding. The builders who let agents run unsupervised for 30 steps, they know they're getting hallucinated garbage. The builders who check every live step before it goes to production get quality output. So your AI agent is powerful but it's not persistent. Directed in pieces verify in between that is orchestration and that is the win.

</div>
