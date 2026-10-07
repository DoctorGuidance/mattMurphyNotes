# Episode 148: Your user clicked delete my account. Now what

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DavJP42gfEJ/) |

---

## 🚨 1. The Incident & Attack Vector
You have a user that just clicked delete my account. Now what? Your AI built a login system, but it did not build a deletion system.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
Your AI built a login system, but it did not build a deletion system. Here are the three things you're going to direct your AI to do right now to fix it. Step one, the cascade map.

---

## ⚡ 4. Hardening Action Checklist
- [ ] the cascade map. Direct your AI to map every table relationship that touches the user.
- [ ] soft delete with a retention window. Direct your AI to deactivate the user immediately, but retain the data for 30 more days.
- [ ] the GDPR response. A user in Europe requests a deletion.

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #148
// Domain: 09-ai-guardrails
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #148 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #148');
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

You have a user that just clicked delete my account. Now what? Your AI built a login system, but it did not build a deletion system. Here are the three things you're going to direct your AI to do right now to fix it. Step one, the cascade map. Direct your AI to map every table relationship that touches the user. Orders, messages, uploads, payment history, session data, and support tickets. When the user is deleted, what happens to each of those records. If you do not know, your AI does not know either. Map it before the first deletion request arrives in your system. That's a win. Step two, soft delete with a retention window. Direct your AI to deactivate the user immediately, but retain the data for 30 more days. The user is gone from the application. The data lives just long enough for a compliance review. After 30 days, hard delete automatically. No manual cleanup. And step three, the GDPR response. A user in Europe requests a deletion. You have 72 hours. So direct your AI to generate a data report of everything you hold on that user and then confirm complete removal within the compliance window of 72 hours. If your AI cannot produce that report on demand, you have a legal exposure you do not know about. Delete is not a button. It's a business process. Build it. Like you have it from day one.

</div>
