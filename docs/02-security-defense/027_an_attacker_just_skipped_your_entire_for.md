# Episode 027: An attacker just skipped your entire form and sent raw data

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdOvuLgiUiv/) |

---

## 🚨 1. The Incident & Attack Vector
An attacker just skipped your entire form and sent raw data to your API.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Relies solely on frontend HTML form validation attributes, trusting raw HTTP requests submitted directly to API handlers. | Enforces identical server-side input schema validation using Zod/Valibot on all incoming API request payloads. |

---

## 💡 3. Root Cause & Architectural Principle
So your AI validated everything in the browser, but none of it runs on the server. So your AI added ZOD validation to your forms, required fields, email format, password length, right? Well, it catches everything in the browser, but the server accepts the raw request body without checking it at all.

---

## ⚡ 4. Hardening Action Checklist
- [ ] your form validates on the client.
- [ ] an attacker adds fields your form does not have an is admin flag or a roll override or a price override.
- [ ] every API endpoint is accessible without your front end.

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
> **Production Heuristic:** The form catches mistakes. The server catches attacks.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI just let an attacker skip your entire form and send raw data straight to your API. Empty strings, negative prices, garbage in every single field. So your AI validated everything in the browser, but none of it runs on the server. So your AI added ZOD validation to your forms, required fields, email format, password length, right? Well, it catches everything in the browser, but the server accepts the raw request body without checking it at all. So, client validation is a user experience feature. Server validation is a security control. Your AI built one and skipped the other. Let's get it fixed. Number one, your form validates on the client. Your server does not. An attacker sends a request directly to your endpoint. Your form never sees it. Your server processes it without a question. And your database stores whatever arrived. So, Zod runs anywhere JavaScript runs. So your AI treated it as a front-end tool. You need to direct your AI to run the same schema on the server. That's the win. Step two, an attacker adds fields your form does not have an is admin flag or a roll override or a price override. Your server passes the full request body to your database without stripping anything unexpected. So if your schema defines 10 fields and the request contains 11, the 11th should not exist. in your system at all. So direct your AI to reject unknown fields from every single request. And number three, every API endpoint is accessible without your front end. Invalid values, extra fields. If the server accepts them, the validation is cosmetic. Your server must enforce the same rules your form does independently. So direct your AI to test every route by sending a request without the form. The form catches the mistakes. The server catches attacks. That's something you want to get your hands around for the win.

</div>
