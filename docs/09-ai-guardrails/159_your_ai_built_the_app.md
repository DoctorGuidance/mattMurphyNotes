# Episode 159: Your AI built the app

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DamFvyUj3U0/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI built the app.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Relies on AI coding tools to design business logic architectures, resulting in tangled domain models and circular dependencies. | Designs core domain models and transactional boundaries using domain-driven design before delegating implementation to AI. |

---

## 💡 3. Root Cause & Architectural Principle
And at 2 in the morning, a customer can't log in. So tell me, who handles that? Your AI assistant?

---

## ⚡ 4. Hardening Action Checklist
- [ ] your agent builds a support playbook during development, not after launch.
- [ ] connect your agent to your production APIs.
- [ ] build the support tier.

---

## 💻 5. Hardened Production Implementation
```typescript
// auth/session.ts
import { Response } from 'express';

export function setSecureSessionCookie(res: Response, token: string) {
  res.cookie('session_token', token, {
    httpOnly: true,                               // Inaccessible to client JS
    secure: process.env.NODE_ENV === 'production', // HTTPS only
    sameSite: 'lax',                              // CSRF protection
    path: '/',
    maxAge: 15 * 60 * 1000                        // 15-minute rotation window
  });
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Your agent is not just your builder. It is your first support engineer.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI assistant built your app and shipped it to production. Customers, they're now paying for it. And at 2 in the morning, a customer can't log in. So tell me, who handles that? Your AI assistant? Probably not because it's not connected to your production system. So your AI assistant built the product, but nobody told it to build the support system, too. And that gap, well, it kills more launch products than bad code ever will. Here's how I think about Post-launch support as an AIdirected engineer. And this is how I help my clients. Step one, your agent builds a support playbook during development, not after launch. Every feature your AI builds should generate a support playbook right alongside it. So for your login system, the playbook covers password reset failures, expired tokens, locked accounts. Like a payment flow, for example, the playbook would cover failed charges, missed web hooks, and subscription issues. These aren't afterthoughts. These are the minimum production deliverables for any app. So if your AI is building the feature, your AI documents how to support that feature. Same sprint, same conversation. That's a win. Step two, connect your agent to your production APIs. When a notification fires, your agent receives it in real time. Not tomorrow and not when you check your email, but in real time. I run this model with all my own builds. My agent Bertha is connected to every API. in real time. She keeps me fully aware. So, a known issue with the documented fix, the agent can resolve it automatically. Something the agent hasn't seen before, she can package the context, escalate it to me with a recommendation. Then I make the call, the agent executes it, and the playbook keeps growing. The compounding effect of a system that gets smarter every week around support, that is a big win for you and your customers. Step three, build the support tier. before you ever need them. Tier one, automated resolutions, known issues, documented fixes. 60 to 70% of volume never reaches your desk. That is a win. Tier two, assisted triage. Unknown issues, the agent packages context, and escalates it to you. You decide, the playbook grows. That's a win. And tier three, incident response. Multiple users are affected. Security or data integrity is involved. The agent triggers the playbook. Who gets notified? What gets locked down? How customers are communicated with. This playbook should exist before your first customer ever signs up. Your agent is not just your builder. It's your first support engineer, likely the most important one. So, you need to start treating it like it.

</div>
