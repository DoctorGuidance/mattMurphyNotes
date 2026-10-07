# Episode 139: Your AI generated a feature in 20 minutes

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Authentication & Identity |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Da2uC94Da2K/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI generated a feature in 20 minutes.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Allows user profile update endpoints to modify email and phone identifiers without sending verification challenges. | Requires re-authentication and automated one-time confirmation challenges before altering primary identity attributes. |

---

## 💡 3. Root Cause & Architectural Principle
It's gorgeous. But nobody tested any of it. Here are the three things you're going to direct your AI to do right now to fix it.

---

## ⚡ 4. Hardening Action Checklist
- [ ] write tests alongside the feature, not after the fact.
- [ ] set a coverage threshold.
- [ ] separate unit from integration.

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
> **Production Heuristic:** The quality gate is yours.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI generated a complete feature in 22 minutes. Login flow, dashboard, payment processing, all functional. It's gorgeous. But nobody tested any of it. Here are the three things you're going to direct your AI to do right now to fix it. Step one, write tests alongside the feature, not after the fact. You direct your AI to generate tests for every feature it builds as you're building those features. Same conversation. Build the login flow. Write the tests that verify it. Login, log out, wrong password, and account lockout. If you do not ask AI for tests, you do not get tests. Your AI does not know that they are missing. Step two, set a coverage threshold. Direct your AI to run the test suite on every commit. If coverage drops below 60%, the commit is failed. 60% is the floor where you catch the failures that matter before. your customers catch them. And for step three, separate unit from integration. Unit tests verify individual functions. They run in seconds on every push. Integration tests verify the full user path. So they run on merges. Direct your AI to split them up. Running everything on every push is slow and inefficient. Running nothing though, totally reckless. So your AI ships untested code all day long. It does not know the code. is untested because you never asked for it. The quality gate is solely yours, not your AIS.

</div>
