# Episode 036: NIST says most agents run on borrowed credentials

> **Category:** AI Guardrails, LLM Security & Compliance (مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی)  
> **Production Layer:** Layer 2  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DdCbUuPFMA9/](https://www.instagram.com/reel/DdCbUuPFMA9/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Most AI agents in production environments are running on borrowed human credentials with no clear audit trail. And that that's really dangerous. And it's not an argument against AI agents.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
And it's not an argument against AI agents. I think they're awesome. It's an argument for directing them to operate safely.

---

## ⚡ 3. Hardening Action Checklist
- [ ] every AI agent you deploy needs its own identity, not your API key and not your login credentials. A unique credential scoped for that agent and to that task.
- [ ] short-lived keys and approval gates before production. An agent's credentials should expire.
- [ ] separate logs for every agent session. Your agents are making decisions you're not watching in real time.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #036
// Domain: 09-ai-guardrails
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #036 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #036');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Most AI agents in production environments are running on borrowed human credentials with no clear audit trail. And that that's really dangerous. And it's not an argument against AI agents. I think they're awesome. It's an argument for directing them to operate safely. So here are some safety tips. Number one, every AI agent you deploy needs its own identity, not your API key and not your login credentials. A unique credential scoped for that agent and to that task. When one of your agent takes an action you did not expect, and it will. Trust me, Murphy's law. You need to know which agent did what and when. If all your agents share your credentials, a compromised agent is a compromised you with a really bad audit trail, your code, your data, your access. It was your fault. So, direct your AI to create scoped identities for every agent before you deploy any of them. That is a win. Step two, short-lived keys and approval gates before production. An agent's credentials should expire. An agent that needs to touch live data, customer records, or production systems should always require your approval before it does. Anthropic literally just froze reinforcement learning for a month this quarter after those agents escaped their sandboxes. So, these are not theoretical controls. They are the difference between an a agent that serves your business and an agent that operates without a leash on your infrastructure. And that's dangerous, right? Step three, separate logs for every agent session. Your agents are making decisions you're not watching in real time. Jetream, Orchestra, and Crowd Strike all launched agent control planes this last quarter for this exact reason. So, a director using their system decides what agents are allowed to do before they start it all. And Per agent log lets you reconstruct what just happened. Without it, you are trusting and never verifying. So direct your AI agents or they will direct themselves and get you in trouble.

</div>
