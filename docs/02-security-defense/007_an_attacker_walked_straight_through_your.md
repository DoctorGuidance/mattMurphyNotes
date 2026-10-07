# Episode 007: An Attacker Walked Straight Through Your Application Firewall (WAF)

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdtpUHxiirn/) |

---

## 🚨 1. The Incident & Attack Vector
You turned on a Web Application Firewall (WAF) and assumed your security was solved. An attacker encoded their payload, bypassed generic rule thresholds, and executed SQL injection directly on your database.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Treats WAF as a substitute for secure coding; leaves default rule sets uncalibrated for application endpoints. | Defense-in-depth: parameterized queries and strict schema validation in code, combined with tuned WAF blocking rules. |

---

## 💡 3. Root Cause & Architectural Principle
A WAF is an outer gatekeeper, not a replacement for backend input sanitization and parameterized queries. Implement defense-in-depth across code, gateway, and database.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Use parameterized SQL queries (Prisma/Drizzle/Prepared Statements) to make SQL injection mathematically impossible.
- [ ] Tune WAF rules to block abnormal payload encodings and enforce strict rate limits on search endpoints.
- [ ] Implement schema validation (Zod/Valibot) on every API endpoint before processing inputs.

---

## 💻 5. Hardened Production Implementation
```typescript
// schemas/inputValidation.ts
import { z } from 'zod';

export const userSearchSchema = z.object({
  query: z.string().min(1).max(100).regex(/^[a-zA-Z0-9 _-]+$/),
  page: z.number().int().min(1).default(1),
});
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** A firewall buys you time; clean code and parameterized queries buy you security.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

An attacker just walked through your application firewall because you don't even have one. You do have a reverse proxy pretending to be a security layer that your AI set up engine X and stopped at load balancing. So your AI configured engine X is a reverse proxy. So traffic routes to your application, headers pass through, SSL terminates, but no rule inspects what is inside those requests. Could be a SQL injection cross-sight scripting and path traversal all pass through completely untouched. So a reverse proxy routes traffic, but a firewall reads it and yours only routes. So let's get it configured. Step one, mod security is an open-source web application firewall that plugs directly into Engine X. It inspects every request against a rule set before it reaches your application. The OAS core rule set blocks the most common attacks right out of the box. SQL injections, cross-ite scripting, remote code execution. So your AI installed engine X and it never added mod security because the proxy worked without it. So direct your AI to install mod security with the OASP core rule set and enable it to blocking mode on every route that accepts user input. That's a win. Step two, an attacker who is blocked by the firewall comes back from a different IP without rate limiting. At infrastructure level, they rotate through addresses and probe your application continuously. Fail to ban monitors your engine X logs and automatically bans IPs that trigger too many blocked requests. So direct your AI to configure fail to ban to monitor mod security logs and ban repeat offenders for escalating durations. Step three, your AI logs request but does not alert on the patterns. So a spike in blocked request just means someone is actively probing your application right now. Without alerting, the attack ends before you know it even started. So, direct your AI to configure log based alerts for unusual volumes of mod security blocks and fail to ban bans. An open- source WFT stacks cost nothing to run. The alternative costs everything when somebody breaks in, so let's keep them out.

</div>
