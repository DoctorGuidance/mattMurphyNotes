# Episode 106: Your AI keeps building new features while your existing

> **Category:** Frontend Architecture & API Hygiene (معماری فرانت‌اند، طراحی واسط و بهداشت API)  
> **Production Layer:** Layer 1  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DbeZo5Zx5i2/](https://www.instagram.com/reel/DbeZo5Zx5i2/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your AI keeps building new features while your existing features are totally broken and you keep letting it because building feels like progress. Something breaks, a payment flow fails, your onboarding drops people at step three. Instead of fixing it, you ask your AI to build the next feature.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
Instead of fixing it, you ask your AI to build the next feature. Guess what? Been there, done that.

---

## ⚡ 3. Hardening Action Checklist
- [ ] every new feature stacked on a broken foundation makes the foundation more fragile. Your AI will happily add a notification system on top of an offflow that drops sessions.
- [ ] Your customers are not asking for new features. They are asking for the current ones to work perfectly.
- [ ] direct your AI to run a feature health audit before it builds anything new. What is live?

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #106
// Domain: 12-frontend-api-hygiene
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #106 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #106');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your AI keeps building new features while your existing features are totally broken and you keep letting it because building feels like progress. Something breaks, a payment flow fails, your onboarding drops people at step three. Instead of fixing it, you ask your AI to build the next feature. Guess what? Been there, done that. Because new features feel like momentum, and there's a lot of dopamine in the AI system. Fixing feels like you're going backwards. Here are three reasons that your instinct is destroying your product. Step one, every new feature stacked on a broken foundation makes the foundation more fragile. Your AI will happily add a notification system on top of an offflow that drops sessions. It will build a reporting dashboard that queries a database that has no indexes. So, your AI builds what you ask for, but it never asks whether the thing underneath it can hold the weight of what you're building. Step two, Your customers are not asking for new features. They are asking for the current ones to work perfectly. Go read your support inbox. The signal is not, I wish this had more features. It never is. The signal is this does not work the way I expected. New features attract customers. Sure, broken features lose them fast. And losing is more expensive than delaying. Step three, direct your AI to run a feature health audit before it builds anything new. What is live? What is broken? What has active users versus zero adoption? Broken and used gets fixed first. Broken and unused gets killed. Only after the foundation is solid do you build the next thing. Your AI will build forever if you let it. But your job as an AIdirected engineer is to tell it when to stop building and start fixing.

</div>
