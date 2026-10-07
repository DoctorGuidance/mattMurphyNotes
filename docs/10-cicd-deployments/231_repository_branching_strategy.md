# Episode 231: Repository Branching Strategy

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Testing, Staging & CI/CD (`تست، محیط‌های کاری، CI/CD و خط لوله استقرار`) |
| **Target Production Layer** | Layer 7 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZkd5y_xpqP/) |

---

## 🚨 1. The Incident & Attack Vector
Repository Branching Strategy.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Repository Branching Strategy'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Repository Branching Strategy'. |

---

## 💡 3. Root Cause & Architectural Principle
Let's talk about it. Here are the three things you need to know right now about branching repositories. Step one, your main branch is always production.

---

## ⚡ 4. Hardening Action Checklist
- [ ] your main branch is always production.
- [ ] feature branches exist so you can break things without breaking users.
- [ ] the more complex your release, the more branches you need.

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
> **Production Heuristic:** Your main branch is always production — treat it that way.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Somebody in my comments yesterday was talking about repository branching strategies. So, guess what? Let's talk about it. Here are the three things you need to know right now about branching repositories. Step one, your main branch is always production. It's not a playground. It's not a testing ground. It's the version your users are running right now. Every change that touches Maine should be tested, reviewed, and deliberate. If your team pushes directly to Maine, You do not have a branching strategy. Step two, feature branches exist so you can break things without breaking users. One branch per feature, one branch per fix. Build it, test it, merge it. If the feature is not ready, Maine does not know it exists. GitHub flow keeps this really simple. One main branch, shortlive feature branches, pull requests before merge that covers 90% of all teams. teams. That's a win. Step three, the more complex your release, the more branches you need. Staging branches, release branches, hot fix branches, all of them. Gitflow was literally designed just for this. Unfortunately, most builders adopt Git Flow before they really need it and they end up spending way more time managing branches than writing code. So, start simple. Add complexity when the pain demands it. Not before branch like You deploy with rigger.

</div>
