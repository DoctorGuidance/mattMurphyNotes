# Episode 259: Not software engineering

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZGpm6StEZS/) |

---

## 🚨 1. The Incident & Attack Vector
Not software engineering.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Abandons software engineering rigor for vibe coding, deploying un-tested AI code that crashes under real concurrency. | Enforces software engineering foundations: unit test suites, integration tests, strict typing, and concurrency stress testing. |

---

## 💡 3. Root Cause & Architectural Principle
It's called AIDirected Engineering. It's not software engineering that we all know. You're not writing code line by line.

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
> **Production Heuristic:** And this is the future we are building towards

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

You know, there's a career that does not have a LinkedIn title yet. No job boards are currently listing it, and no university actually teaches it, but the people doing it are making $300 to $500,000 a year. It's called AIDirected Engineering. It's not software engineering that we all know. You're not writing code line by line. It's not prompt engineering. You're not optimizing one prompt for one task. It's architecture by design and the system you design is written by AI code. AI reviews the code. AI deploys the code. AI maintains the code and you direct the entire pipeline. A traditional engineer ships one feature per sprint. An AI directed engineer ships the whole product because they're not typing anymore. They're orchestrating. Chapter 12 of my book, Not Murphy's Law, is called the orchestrator. And it maps out how this role will work in the future completely. What you own, what you delegate, how you validate. This is not a future prediction at all. I run my entire company this way today and our team is substantial, but the AI operates like we're 10 times bigger than we are. And the AI directed engineering certification program we built at Faction for you. It's not how you code, it's how you direct code. And this is the future we are building towards. So I hope you join in.

</div>
