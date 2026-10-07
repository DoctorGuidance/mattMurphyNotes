# Episode 128: Your user clicked delete my account

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Observability & Error Tracking (`مشاهده‌پذیری، لاگ ساختاریافته و رهگیری خطا`) |
| **Target Production Layer** | Layer 12 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbDv862jzKb/) |

---

## 🚨 1. The Incident & Attack Vector
Your user clicked delete my account. So you deleted all their data. Well, you just broke a federal law.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
Well, you just broke a federal law. Certain industries require you to retain customer records for up to 7 years after your relationship ends. Financial services, health care, tax related transactions, and even some legal agreements.

---

## ⚡ 4. Hardening Action Checklist
- [ ] a data retention policy engine. This isn't a toggle that says active or deleted.
- [ ] a retention schedule mapped to your actual obligations. 7 years is not universal to all companies and all projects, right?
- [ ] an audit trail that proves you followed the policy. When a regulator asks, and in certain industries they absolutely will, you need to show exactly what was retained, what was anonymized, and when the clock started, and also when it expires.

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #128
// Domain: 06-observability-logs
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #128 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #128');
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

Your user clicked delete my account. So you deleted all their data. Well, you just broke a federal law. Certain industries require you to retain customer records for up to 7 years after your relationship ends. Financial services, health care, tax related transactions, and even some legal agreements. So your user might want their data gone, but the federal government says you have to keep it. Here are the three things you're going to direct your AI to build right now to handle this for you going forward. Step one, a data retention policy engine. This isn't a toggle that says active or deleted. It's a system that knows the difference between the data a user controls and the data the law requires you to keep. Those are two completely different categories and your AI will lump them together unless you tell it not to. So your customer-f facing data gets anonymized and your compliance data stays locked in a separate retention layer with an expiration date attached to it. That's a win. All right. Step two, a retention schedule mapped to your actual obligations. 7 years is not universal to all companies and all projects, right? It depends on your industry, your state, and the type of record you're collecting. Payment records, for example, have a different timeline than user communications. So, your AI can research the requirements for your specific business, but it'll never do it unprompted. because it does not know what industry you're in or what laws apply to you wherever you're at. And step three, an audit trail that proves you followed the policy. When a regulator asks, and in certain industries they absolutely will, you need to show exactly what was retained, what was anonymized, and when the clock started, and also when it expires. Your AI can build that logging system in an afternoon. Without it, your policy retention is a promise with no proof. So last week I told you to soft delete. This week I'm telling you that sometimes you cannot delete at all. The rules depend on what you are building. You have to do the research. So direct your AI to find out before your your first user asks you to leave.

</div>
