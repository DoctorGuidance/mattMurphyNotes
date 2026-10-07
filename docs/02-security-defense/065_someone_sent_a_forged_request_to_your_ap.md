# Episode 065: Someone sent a forged request to your API last Tuesday

> **Category:** Application Security & Defense (امنیت نرم‌افزار، حملات و دفاع لایه‌ای)  
> **Production Layer:** Layer 8  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DcYrFHSAOhJ/](https://www.instagram.com/reel/DcYrFHSAOhJ/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Someone sent a forged request to your API last Tuesday. Your server processed it. No questions asked.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
No questions asked. No request signing, no verification that the request came from a legitimate client. No check on whether the payload was tampered with in transit.

---

## ⚡ 3. Hardening Action Checklist
- [ ] request signing on every mutating endpoint. Every post, put, patch, and delete should carry a signature.
- [ ] API versioning. From day one, your API path includes a version.
- [ ] Deprecation policy with sunset headers. When an endpoint is scheduled for removal, the response includes a sunset header with retirement date.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #065
// Domain: 02-security-defense
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #065 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #065');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Someone sent a forged request to your API last Tuesday. Your server processed it. No questions asked. No request signing, no verification that the request came from a legitimate client. No check on whether the payload was tampered with in transit. So your server accepted the request, ran the mutation, and returned a 200. The attacker now knows your API better than your documentation does cuz your API is a front door with no lock, no doorbell. and no one watching. So, here is how we're going to fix it. Step one, request signing on every mutating endpoint. Every post, put, patch, and delete should carry a signature. An HMAC hash of the request body signed with a shared secret. So, your server verifies the signature before processing. So, unassigned requests, they get rejected. So, direct your AI to implement request signing middleware that validates HMAC signatures on all mutating API calls. That's a win. Step two, API versioning. From day one, your API path includes a version. V1 stays stable. V2 introduces breaking changes. Consumers migrate on their schedule. Without versioning, though, every schema change is a production incident for every consumer. So, direct your AI to implement path-based API versioning and a version negotiation strategy. That is definitely a win. And step three, Deprecation policy with sunset headers. When an endpoint is scheduled for removal, the response includes a sunset header with retirement date. Consumers get warnings. Monitoring tracks usage of deprecating endpoints. And when usage hits zero, the endpoint, it's removed. So, direct your AI to implement sunset headers and deprecating monitoring on every endpoint scheduled for retirement. Your API is your contract with every consumer. It's time to harden it.

</div>
