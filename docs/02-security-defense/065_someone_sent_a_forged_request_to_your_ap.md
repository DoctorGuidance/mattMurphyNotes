# Episode 065: Someone sent a forged request to your API last Tuesday

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcYrFHSAOhJ/) |

---

## 🚨 1. The Incident & Attack Vector
Someone sent a forged request to your API last Tuesday.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Accepts state-modifying POST requests without Cross-Site Request Forgery (CSRF) tokens on cookie-authenticated sessions. | Implements Double Submit Cookie patterns or SameSite=Strict cookie policies to neutralize cross-site request forgery. |

---

## 💡 3. Root Cause & Architectural Principle
No questions asked. No request signing, no verification that the request came from a legitimate client. No check on whether the payload was tampered with in transit.

---

## ⚡ 4. Hardening Action Checklist
- [ ] request signing on every mutating endpoint.
- [ ] API versioning.
- [ ] Deprecation policy with sunset headers.

---

## 💻 5. Hardened Production Implementation
```typescript
// schemas/userUpdate.ts
import { z } from 'zod';

// Explicitly whitelist allowed user fields - NEVER allow role, isAdmin, or accountStatus
export const updateUserProfileSchema = z.object({
  name: z.string().min(2).max(50),
  avatarUrl: z.string().url().optional(),
  bio: z.string().max(250).optional()
}).strict(); // Rejects any unknown or injected administrative properties
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Your API is your contract. Harden it.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Someone sent a forged request to your API last Tuesday. Your server processed it. No questions asked. No request signing, no verification that the request came from a legitimate client. No check on whether the payload was tampered with in transit. So your server accepted the request, ran the mutation, and returned a 200. The attacker now knows your API better than your documentation does cuz your API is a front door with no lock, no doorbell. and no one watching. So, here is how we're going to fix it. Step one, request signing on every mutating endpoint. Every post, put, patch, and delete should carry a signature. An HMAC hash of the request body signed with a shared secret. So, your server verifies the signature before processing. So, unassigned requests, they get rejected. So, direct your AI to implement request signing middleware that validates HMAC signatures on all mutating API calls. That's a win. Step two, API versioning. From day one, your API path includes a version. V1 stays stable. V2 introduces breaking changes. Consumers migrate on their schedule. Without versioning, though, every schema change is a production incident for every consumer. So, direct your AI to implement path-based API versioning and a version negotiation strategy. That is definitely a win. And step three, Deprecation policy with sunset headers. When an endpoint is scheduled for removal, the response includes a sunset header with retirement date. Consumers get warnings. Monitoring tracks usage of deprecating endpoints. And when usage hits zero, the endpoint, it's removed. So, direct your AI to implement sunset headers and deprecating monitoring on every endpoint scheduled for retirement. Your API is your contract with every consumer. It's time to harden it.

</div>
