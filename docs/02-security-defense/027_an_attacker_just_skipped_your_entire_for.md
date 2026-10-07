# Episode 027: An attacker just skipped your entire form and sent raw data

> **Category:** Application Security & Defense (امنیت نرم‌افزار، حملات و دفاع لایه‌ای)  
> **Production Layer:** Layer 8  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DdOvuLgiUiv/](https://www.instagram.com/reel/DdOvuLgiUiv/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your AI just let an attacker skip your entire form and send raw data straight to your API. Empty strings, negative prices, garbage in every single field. So your AI validated everything in the browser, but none of it runs on the server.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
So your AI validated everything in the browser, but none of it runs on the server. So your AI added ZOD validation to your forms, required fields, email format, password length, right? Well, it catches everything in the browser, but the server accepts the raw request body without checking it at all.

---

## ⚡ 3. Hardening Action Checklist
- [ ] your form validates on the client. Your server does not.
- [ ] an attacker adds fields your form does not have an is admin flag or a roll override or a price override. Your server passes the full request body to your database without stripping anything unexpected.
- [ ] every API endpoint is accessible without your front end. Invalid values, extra fields.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #027
// Domain: 02-security-defense
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #027 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #027');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your AI just let an attacker skip your entire form and send raw data straight to your API. Empty strings, negative prices, garbage in every single field. So your AI validated everything in the browser, but none of it runs on the server. So your AI added ZOD validation to your forms, required fields, email format, password length, right? Well, it catches everything in the browser, but the server accepts the raw request body without checking it at all. So, client validation is a user experience feature. Server validation is a security control. Your AI built one and skipped the other. Let's get it fixed. Number one, your form validates on the client. Your server does not. An attacker sends a request directly to your endpoint. Your form never sees it. Your server processes it without a question. And your database stores whatever arrived. So, Zod runs anywhere JavaScript runs. So your AI treated it as a front-end tool. You need to direct your AI to run the same schema on the server. That's the win. Step two, an attacker adds fields your form does not have an is admin flag or a roll override or a price override. Your server passes the full request body to your database without stripping anything unexpected. So if your schema defines 10 fields and the request contains 11, the 11th should not exist. in your system at all. So direct your AI to reject unknown fields from every single request. And number three, every API endpoint is accessible without your front end. Invalid values, extra fields. If the server accepts them, the validation is cosmetic. Your server must enforce the same rules your form does independently. So direct your AI to test every route by sending a request without the form. The form catches the mistakes. The server catches attacks. That's something you want to get your hands around for the win.

</div>
