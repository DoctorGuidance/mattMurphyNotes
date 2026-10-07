# Episode 220: If your frontend hides the button but your API still

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Frontend Architecture & API Hygiene (`معماری فرانت‌اند، طراحی واسط و بهداشت API`) |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZs5JDxPOrW/) |

---

## 🚨 1. The Incident & Attack Vector
Your app has users. Some of them are admins, some of them are not. And right now, you're checking it with an if statement.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
And right now, you're checking it with an if statement. Here are the three things you do right now to fix that. Step one, understand what RBAC actually is.

---

## ⚡ 4. Hardening Action Checklist
- [ ] understand what RBAC actually is. Ro based access control.
- [ ] start with three roles always. Admin, member, viewer.
- [ ] enforce it everywhere. Every API route checks the role.

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #220
// Domain: 12-frontend-api-hygiene
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #220 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #220');
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

Your app has users. Some of them are admins, some of them are not. And right now, you're checking it with an if statement. Here are the three things you do right now to fix that. Step one, understand what RBAC actually is. Ro based access control. Every user gets a role. Every role gets permissions. Admin can delete. Editor can update. Viewer can read. Those are the basics. Roles are enforced. at the API layer, not the UI layer. The UI hides things for convenience. The API blocks things for security. That's the win. Step two, start with three roles always. Admin, member, viewer. That covers 90% of SAS application use cases at launch. Do not build custom permission matrix. Well, not before you have your first paying customer. Ship three roles. Add complexity when the business demands it. That's the win. And step three, enforce it everywhere. Every API route checks the role. Every server action validates the user. If your front end hides the delete button, but your API still accepts the delete request, you do not have access control. You have a suggestion and suggestions do not survive a curious user with browser console. Right? You must enforce permission or it does not exist. That's The win.

</div>
