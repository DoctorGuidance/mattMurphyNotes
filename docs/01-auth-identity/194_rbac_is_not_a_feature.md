# Episode 194: RBAC is not a feature

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Authentication & Identity (`احراز هویت و مدیریت نشست‌ها`) |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaGcgHaiq3i/) |

---

## 🚨 1. The Incident & Attack Vector
RBAC, RO based access control. Everyone says they have it. Most people have a boolean called underscore admin.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
Most people have a boolean called underscore admin. Here are the three things you decide before you build it. Step one, roles versus permissions.

---

## ⚡ 4. Hardening Action Checklist
- [ ] roles versus permissions. A role is a label.
- [ ] where enforcement happens. Your front end hides the button.
- [ ] scope. Can this user edit any document or only documents they created?

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #194
// Domain: 01-auth-identity
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #194 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #194');
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

RBAC, RO based access control. Everyone says they have it. Most people have a boolean called underscore admin. Here are the three things you decide before you build it. Step one, roles versus permissions. A role is a label. Admin, editor, viewer. A permission is an action. Can create, can delete, can export. Most applications assign roles and hardcode what those roles can do. When the customer asks for a custom role, the whole system breaks. Build permissions first. Let roles be collections of those permissions. And that's the win. Step two, where enforcement happens. Your front end hides the button. Your API still accepts the request. That is not access control, folks. That's a suggestion and a security problem. Enforcement must happen at the API layer. Every route, every endpoint, the front end controls that experience. The backend controls all the access. Step three, scope. Can this user edit any document or only documents they created? Can this admin manage all teams or only their team? RBAC without scope is completely binary. You either have access or you do not. So RBAC with scope is granular. You have access to what belongs to you. The difference between a feature and architecture is whether it scales. So build the architecture right the first time.

</div>
