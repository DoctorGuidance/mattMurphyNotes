# Episode 036: NIST says most agents run on borrowed credentials

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdCbUuPFMA9/) |

---

## 🚨 1. The Incident & Attack Vector
NIST says most agents run on borrowed credentials.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends unvalidated user inputs straight to LLMs without budget caps or injection defenses in 'NIST says most agents run on borrowed credentials'. | Applies prompt sanitization, structured output validation (Zod), spend ceilings, and SGI metadata compliance. |

---

## 💡 3. Root Cause & Architectural Principle
And it's not an argument against AI agents. I think they're awesome. It's an argument for directing them to operate safely.

---

## ⚡ 4. Hardening Action Checklist
- [ ] every AI agent you deploy needs its own identity, not your API key and not your login credentials.
- [ ] short-lived keys and approval gates before production.
- [ ] separate logs for every agent session.

---

## 💻 5. Hardened Production Implementation
```typescript
// pages/api/secureProxy.ts
import type { NextApiRequest, NextApiResponse } from 'next';

// Server-side gateway: Secret keys NEVER touch the client bundle
export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const secretKey = process.env.INTERNAL_SERVICE_KEY; // Kept strictly on server
  const response = await fetch('https://api.upstream.com/v1/data', {
    headers: { 'Authorization': `Bearer ${secretKey}` }
  });
  const data = await response.json();
  res.status(200).json(data);
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Direct your agents or they direct themselves.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Most AI agents in production environments are running on borrowed human credentials with no clear audit trail. And that that's really dangerous. And it's not an argument against AI agents. I think they're awesome. It's an argument for directing them to operate safely. So here are some safety tips. Number one, every AI agent you deploy needs its own identity, not your API key and not your login credentials. A unique credential scoped for that agent and to that task. When one of your agent takes an action you did not expect, and it will. Trust me, Murphy's law. You need to know which agent did what and when. If all your agents share your credentials, a compromised agent is a compromised you with a really bad audit trail, your code, your data, your access. It was your fault. So, direct your AI to create scoped identities for every agent before you deploy any of them. That is a win. Step two, short-lived keys and approval gates before production. An agent's credentials should expire. An agent that needs to touch live data, customer records, or production systems should always require your approval before it does. Anthropic literally just froze reinforcement learning for a month this quarter after those agents escaped their sandboxes. So, these are not theoretical controls. They are the difference between an a agent that serves your business and an agent that operates without a leash on your infrastructure. And that's dangerous, right? Step three, separate logs for every agent session. Your agents are making decisions you're not watching in real time. Jetream, Orchestra, and Crowd Strike all launched agent control planes this last quarter for this exact reason. So, a director using their system decides what agents are allowed to do before they start it all. And Per agent log lets you reconstruct what just happened. Without it, you are trusting and never verifying. So direct your AI agents or they will direct themselves and get you in trouble.

</div>
