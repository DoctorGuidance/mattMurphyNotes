# Episode 063: AWS just killed Bedrock Agents. Renamed it to Classic.

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcbP4U7G6QK/) |

---

## 🚨 1. The Incident & Attack Vector
AWS just killed Bedrock Agents. Renamed it to Classic. Closed to new customers.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Binds application architectures to proprietary cloud AI orchestration services that deprecate and rename features abruptly. | Builds AI agent workflows using modular, open abstractions (LangGraph/Custom State Machines) decoupled from proprietary cloud silos. |

---

## 💡 3. Root Cause & Architectural Principle
And if you built your healthcare app on bedrock agents, your compliance path just got rerouted. So agent core is the replacement, but it's a different architecture, a different runtime and different integration surface altogether. So your existing deployment does not migrate itself.

---

## ⚡ 4. Hardening Action Checklist
- [ ] an abstraction layer between your application and any cloud provider's agent framework.
- [ ] a BAA audit on every service in your stack after any provider migration.
- [ ] a migration runway, not a migration emergency.

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
> **Production Heuristic:** Your cloud provider will always build the next thing. Architect so it does not break yours.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

AWS just killed Bedrock Agents. Now everyone who built on it for the healthcare baa has a migration path they did not plan for. And if you built your healthcare app on bedrock agents, your compliance path just got rerouted. So agent core is the replacement, but it's a different architecture, a different runtime and different integration surface altogether. So your existing deployment does not migrate itself. Here's how you're going to handle it. Step one, an abstraction layer between your application and any cloud provider's agent framework. Your business logic should never be hardwired to a vendor's SDK. If your agent orchestration is built directly on Bedrock's API surface, every line of that code is now migration liability. So, direct your AI to refactor your agent orchestration behind an internal interface. That way, the underlying framework can be swapped without rewriting your application. That's That's a win. Step two, a BAA audit on every service in your stack after any provider migration. So your BAA covers specific services by name. When the service changes, the BAA coverage may not follow it automatically. So moving from bedrock agents classic to agent core means you need to reverify that every service in your healthcare data path is covered under the current agreement. Direct your AI to map every service that touches PHI. and verify the BAA coverage against the current AWS service list. That's a win. And step three, a migration runway, not a migration emergency. Classic is not shutting down tomorrow. So, it's also no longer receiving any of the new features, which means every month you stay on it, you fall a little further behind the platform providers actually investing in. So, direct your AI to build a migration timeline that moves your agent orchestration to the supported framework. That way, Before classic becomes a liability, instead of a convenience, you're already ahead of it. This way, your cloud provider will always build the next thing. We hear it. But architect your system so the next thing doesn't break what you built.

</div>
