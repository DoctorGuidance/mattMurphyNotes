# Episode 020: An attacker just downloaded your entire API schema

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdbnwpOiEZJ/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI just let an attacker download your entire API schema. Every query, every mutation, every type and relationship in your database. So your AI deployed a GraphQL endpoint and left introspection enabled.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
So your AI deployed a GraphQL endpoint and left introspection enabled. When your AI set up Apollo server or GraphQL API, introspection is enabled by default. In development, it powers autocomplete and documentation.

---

## ⚡ 4. Hardening Action Checklist
- [ ] introspection returns your full schema on a single request. Every type name, every field, every argument, every relationship.
- [ ] an attacker who knows your schema crafts queries that request deeply nested relationships. A query that joins users to orders to payments to addresses five levels deep, right?
- [ ] even with introspection disabled, an attacker can reconstruct your schema by sending queries and observing which ones succeed and which ones fail. So field suggestions and error messages reveal valid field names one at a time.

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #020
// Domain: 02-security-defense
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #020 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #020');
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

Your AI just let an attacker download your entire API schema. Every query, every mutation, every type and relationship in your database. So your AI deployed a GraphQL endpoint and left introspection enabled. When your AI set up Apollo server or GraphQL API, introspection is enabled by default. In development, it powers autocomplete and documentation. But in production, it hands an attacker a complete map of your back end. And a map of every door is the first thing a burglar wants. So let's get all those doors locked down. Number one, introspection returns your full schema on a single request. Every type name, every field, every argument, every relationship. So an attacker does not guess your API service. They read it. Your mutations reveal what actions exist. Your types reveal what data exists. Your field names reveal your database structure. So direct your AI to disable introspection in production with one configuration flag. That's a win. Number two, an attacker who knows your schema crafts queries that request deeply nested relationships. A query that joins users to orders to payments to addresses five levels deep, right? Well, that can return gigabytes of data in single request and crash your server completely. So your AI never set a depth limit. So direct your AI to enforce a maximum query depth and complexity score on every single request. And number three, even with introspection disabled, an attacker can reconstruct your schema by sending queries and observing which ones succeed and which ones fail. So field suggestions and error messages reveal valid field names one at a time. So your AI left field suggestion enabled in your production error responses. So direct your AI to disable field suggestions and return generic error messages that reveal nothing about your schema. This way your API documentation is for your developers only and your schema is for your application. An attacker should have access to neither of them. That's the win.

</div>
