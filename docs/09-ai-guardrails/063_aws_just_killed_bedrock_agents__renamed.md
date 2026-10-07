# Episode 063: AWS just killed Bedrock Agents. Renamed it to Classic.

> **Category:** AI Guardrails, LLM Security & Compliance (مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی)  
> **Production Layer:** Layer 2  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DcbP4U7G6QK/](https://www.instagram.com/reel/DcbP4U7G6QK/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
AWS just killed Bedrock Agents. Now everyone who built on it for the healthcare baa has a migration path they did not plan for. And if you built your healthcare app on bedrock agents, your compliance path just got rerouted.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
And if you built your healthcare app on bedrock agents, your compliance path just got rerouted. So agent core is the replacement, but it's a different architecture, a different runtime and different integration surface altogether. So your existing deployment does not migrate itself.

---

## ⚡ 3. Hardening Action Checklist
- [ ] an abstraction layer between your application and any cloud provider's agent framework. Your business logic should never be hardwired to a vendor's SDK.
- [ ] a BAA audit on every service in your stack after any provider migration. So your BAA covers specific services by name.
- [ ] a migration runway, not a migration emergency. Classic is not shutting down tomorrow.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #063
// Domain: 09-ai-guardrails
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #063 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #063');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

AWS just killed Bedrock Agents. Now everyone who built on it for the healthcare baa has a migration path they did not plan for. And if you built your healthcare app on bedrock agents, your compliance path just got rerouted. So agent core is the replacement, but it's a different architecture, a different runtime and different integration surface altogether. So your existing deployment does not migrate itself. Here's how you're going to handle it. Step one, an abstraction layer between your application and any cloud provider's agent framework. Your business logic should never be hardwired to a vendor's SDK. If your agent orchestration is built directly on Bedrock's API surface, every line of that code is now migration liability. So, direct your AI to refactor your agent orchestration behind an internal interface. That way, the underlying framework can be swapped without rewriting your application. That's That's a win. Step two, a BAA audit on every service in your stack after any provider migration. So your BAA covers specific services by name. When the service changes, the BAA coverage may not follow it automatically. So moving from bedrock agents classic to agent core means you need to reverify that every service in your healthcare data path is covered under the current agreement. Direct your AI to map every service that touches PHI. and verify the BAA coverage against the current AWS service list. That's a win. And step three, a migration runway, not a migration emergency. Classic is not shutting down tomorrow. So, it's also no longer receiving any of the new features, which means every month you stay on it, you fall a little further behind the platform providers actually investing in. So, direct your AI to build a migration timeline that moves your agent orchestration to the supported framework. That way, Before classic becomes a liability, instead of a convenience, you're already ahead of it. This way, your cloud provider will always build the next thing. We hear it. But architect your system so the next thing doesn't break what you built.

</div>
