# Episode 119: Your AI built a healthcare app. It has never heard of HIPAA

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbOGY9aEY0-/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI built a healthcare app, but it's never heard of HIPPA. One complaint to the Office for Civil Rights triggers an investigation that starts at $100 per violation and scales all the way up to $2 million. Your AI doesn't know that.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
Your AI doesn't know that. It will literally store patient data wherever it wants and it'll transmit it however it feels like it and it'll log it again wherever it wants. So, if your application touches any patient data, student health records or protected health health information, you're already subject to a federal regulation and your AI never asked a single question about it.

---

## ⚡ 4. Hardening Action Checklist
- [ ] encryption at rest and in transit on every field that contains protected health information, not just your database, your backups, your logs, your exports. Your AI may have encrypted that database, but left PHI sitting in plain text in your application log.
- [ ] access controls with audit logging on every record that contains PHI. Who accessed it?
- [ ] a business associate agreement with every

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #119
// Domain: 09-ai-guardrails
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #119 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #119');
  }
  return true;
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Never deploy unverified AI-generated code directly to production without testing failure modes.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI built a healthcare app, but it's never heard of HIPPA. One complaint to the Office for Civil Rights triggers an investigation that starts at $100 per violation and scales all the way up to $2 million. Your AI doesn't know that. It will literally store patient data wherever it wants and it'll transmit it however it feels like it and it'll log it again wherever it wants. So, if your application touches any patient data, student health records or protected health health information, you're already subject to a federal regulation and your AI never asked a single question about it. So, here are the three things you direct your AI to build right now if your app is touching health data. Step one, encryption at rest and in transit on every field that contains protected health information, not just your database, your backups, your logs, your exports. Your AI may have encrypted that database, but left PHI sitting in plain text in your application log. One log file is all it takes for a pretty significant fine. Step two, access controls with audit logging on every record that contains PHI. Who accessed it? When, from where, and what did they do with it? HIPPO requires you to produce this on demand. Your AI built role based access, but it did not build the paper trail that proves what touched what. And step three, a business associate agreement with every third-party service that touches that data. your hosting provider, your email service, your analytics platform. If they can see protected health information, they need a BAA on file. Your AI integrated six services and signed zero agreements. One of those services has a breach and you're liable because you have no contract that defines the obligations. So, yeah, your AI builds fast, but it does not build compliant. Direct your AI to fix that before your first patient walks through the door.

</div>
