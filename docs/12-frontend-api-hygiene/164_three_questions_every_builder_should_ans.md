# Episode 164: Three questions every builder should answer before launch

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Frontend Architecture & API Hygiene (`معماری فرانت‌اند، طراحی واسط و بهداشت API`) |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DagUP6WjhPx/) |

---

## 🚨 1. The Incident & Attack Vector
This is a conversation I never expected to be having with vibe coders, but I'm having it almost every week now. Someone builds a product with AI, it works, they're ready to launch, and I ask them three questions that stop the conversation in its tracks. Question one, do you have cyber liability insurance?

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
Question one, do you have cyber liability insurance? Their eyes light up. When you handle someone else's data and something goes wrong, you're personally liable.

---

## ⚡ 4. Hardening Action Checklist
- [ ] have you read your platform's terms of service? Does anybody read a terms of service?
- [ ] that stumps most people. Does your privacy policy match what your app actually does?

---

## 💻 5. Hardened Production Implementation
```typescript
// Secure HttpOnly Cookie Issuance
res.cookie('session_token', token, {
  httpOnly: true,                               // Inaccessible to client JS
  secure: process.env.NODE_ENV === 'production', // HTTPS only
  sameSite: 'lax',                              // CSRF protection
  path: '/',
  maxAge: 15 * 60 * 1000                        // 15-minute short-lived
});
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Never deploy unverified AI-generated code directly to production without testing failure modes.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

This is a conversation I never expected to be having with vibe coders, but I'm having it almost every week now. Someone builds a product with AI, it works, they're ready to launch, and I ask them three questions that stop the conversation in its tracks. Question one, do you have cyber liability insurance? Their eyes light up. When you handle someone else's data and something goes wrong, you're personally liable. Not your LLC. You are. A data breach on an uninsured platform means you're paying for notification, remediation, legal fees, and any damages out of your own pocket. Cyber liability insurance costs $200 to $600 a year for most small SAS platforms. $200 to protect yourself from a breach that could cause 50,000. That's a win. And here's the part that nobody's talking to you about. Most insurance underwriters want to see basic security practices before they're even going to cover you. So, vulnerability scans, access controls, encryption at rest. The security audit is not just a good practice. It is a requirement for the coverage that protects your whole business. Question number two, have you read your platform's terms of service? Does anybody read a terms of service? Superbase for sale, Stripe. Every platform has terms that define what happens when things go wrong. Most include limitation of liability clauses that cap their exposure at what you paid them last month. month. So you paid Superbase 25 bucks. If their service causes a data loss that cost you 10 grand, their liability 25 bucks. Yours 10 grand plus. So understanding your platform agreement is not legal paranoia. It is basic business literacy. And question number three that stumps most people. Does your privacy policy match what your app actually does? Your app collects emails, payment information, and usage data. Your privacy policy is a template you copied from the internet that references cookies and nothing else. If a user in Europe asks you to delete their data under GDPR and your database was never built for deletion, you have a compliance violation that carries some real serious fines. Your AI can build the product. Your AI can even draft the privacy policy, but you have to direct it with the right requirements. And most builders do not know what the requirements are until the first in didn't teaches them all about it. So building the product is usually the easiest part. Protecting the business underneathneath it is where most builders never start. Right? So start before you launch, not after. It's a business. It's a product. It's not just a build.

</div>
