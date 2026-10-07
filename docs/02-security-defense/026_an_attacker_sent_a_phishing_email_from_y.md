# Episode 026: An attacker sent a phishing email from your domain

> **Category:** Application Security & Defense (امنیت نرم‌افزار، حملات و دفاع لایه‌ای)  
> **Production Layer:** Layer 8  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DdPTYpBAiuY/](https://www.instagram.com/reel/DdPTYpBAiuY/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
An attacker just sent a fishing email from your domain. SPF passed, DKIM passed, Demar passed. It was your own email system, but your AI let them in through a name field.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
It was your own email system, but your AI let them in through a name field. So, your AI integrated resend for transactional emails and drops user input into the template. No sanitization.

---

## ⚡ 3. Hardening Action Checklist
- [ ] a name field should contain a name, not a login button that links to an attacker's fishing page. The fishing email that results is indistinguishable from your legitimate ones because your infrastructure sent it to them.
- [ ] your template engine allows raw HTML insertion. User content should never use that path.
- [ ] send an email with angle brackets, link tags, and script tags in every input field. If any of them render as a clickable link instead of a plain text, your template is fully injectable.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #026
// Domain: 02-security-defense
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #026 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #026');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

An attacker just sent a fishing email from your domain. SPF passed, DKIM passed, Demar passed. It was your own email system, but your AI let them in through a name field. So, your AI integrated resend for transactional emails and drops user input into the template. No sanitization. So, an attacker types HTML into a form field and resend delivers it from your verified domain. Well, the attacker did not comp compromise your email. Your template just invited them right in. So, let's get this locked down. Step one, a name field should contain a name, not a login button that links to an attacker's fishing page. The fishing email that results is indistinguishable from your legitimate ones because your infrastructure sent it to them. It's your domain. It's your sender reputation. It's your SPF record all confirming that it was real. So, one form field that accepts markup turns your entire email system into a fishing platform for attackers. So, direct your AI to sanitize every user input before it enters any template at all. Strip the HTML, escape special characters. That's a win. Step two, your template engine allows raw HTML insertion. User content should never use that path. Data gets displayed, markup gets executed. So, a password reset email that renders user input as HTML is an email and a attacker can turn into anything they want. So, you need to direct your AI to render user content as plain text, never as raw HTML. That's a win. And step three, send an email with angle brackets, link tags, and script tags in every input field. If any of them render as a clickable link instead of a plain text, your template is fully injectable. This test will take you 30 seconds. And the alternative is finding out when a customer clicks a fishing link that contain a domain that you sent them. So, direct your AI to test every single template. Your domain reputation is your business reputation, and one injectable template burns both to the ground. That's not a win. Get it fixed.

</div>
