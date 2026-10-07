# Episode 035: Someone just promoted themselves to admin in your app by

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdEcldEktWP/) |

---

## 🚨 1. The Incident & Attack Vector
Someone just promoted themselves to admin in your app by editing one field in a JWT.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |

---

## 💡 3. Root Cause & Architectural Principle
So your AI integrated clerk and reads the jot file to check the roles, but it never verifies the signature and it never checks the expiration. So a modified token passes your middleware without any challenge at all. Here's how you're going to direct your AI to verify every token.

---

## ⚡ 4. Hardening Action Checklist
- [ ] verify the signature on every request.
- [ ] validate expiration and the issuer.
- [ ] use Clerk's serverside SDK instead of parsing manually.

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
> **Production Heuristic:** Your auth provider did its job. Your AI never verified its work.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Someone just promoted themselves to admin in your AI app by editing one field in a jot. Your server granted access because your AI never verified the signature. So your AI integrated clerk and reads the jot file to check the roles, but it never verifies the signature and it never checks the expiration. So a modified token passes your middleware without any challenge at all. Here's how you're going to direct your AI to verify every token. before it trusts a single claim. Number one, verify the signature on every request. Clerk signs every token with a key pair. Your server must validate that signature before reading any claim. Without verification, a user decodes their own jot, changes the role from member to admin, re-encodes it, and sends it right back. So, your server reads admin and grants access to every protected route in your app to that attacker. No alert, no log entry, full admin access to anyone who knows how a jot works. So your AI read the claims without checking whether the envelope was sealed. That's not a win. Step two, validate expiration and the issuer. An expired token should never grant any access. A token from a different clerk instance should never be trusted. Without these two checks, a stolen token works forever and a token from a completely different application passes your middleware without any challenge. So direct your AI to reject anything that's expired or issued by the wrong source. That is a win. And step three, use Clerk's serverside SDK instead of parsing manually. The SDK can handle signature verification, claim validation, and key rotation automatically. So every manual Jot implementation makes this exact same mistake because the short That always looks like it works to the AI, right? Well, it does work for honest users, but the moment someone modifies a token intentionally, your entire authorization layer disappears to an attacker. The SDK literally exists because this mistake happens in every manual implementation. So, your off provider did its job. Your AI never verified the work. That's not a win. Get it fixed.

</div>
