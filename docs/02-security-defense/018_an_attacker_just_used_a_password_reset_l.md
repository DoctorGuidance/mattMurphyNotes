# Episode 018: An attacker just used a password reset link from four

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdeMk-bFdui/) |

---

## 🚨 1. The Incident & Attack Vector
An attacker just used a password reset link from four months ago.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Issues permanent, multi-use password reset tokens without expiration or post-consumption invalidation. | Enforces 15-minute token TTLs, single-use invalidation, and throttles password reset dispatches to 3 requests per hour. |

---

## 💡 3. Root Cause & Architectural Principle
Uh-oh. Your user change their password twice since then, but the old link still logs them in. So, your AI built a password reset flow.

---

## ⚡ 4. Hardening Action Checklist
- [ ] an attacker who accesses an old email, a forwarded message, a breached inbox finds every reset link ever sent.
- [ ] a reset token that works more than once lets an attacker use it after the legitimate user already has.
- [ ] an attacker who finds the reset endpoint can request thousands of tokens per minute.

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
> **Production Heuristic:** Your password reset is a door. Your AI built it without a lock.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Did an attacker just use a password reset link from four months ago to hack your app? That token still works. Uh-oh. Your user change their password twice since then, but the old link still logs them in. So, your AI built a password reset flow. It generates a token, sends an email, and lets the user set a new password, but the token never expires, and the token is never invalidated after use. So, a reset token without an expiration is a permanent key to your account. Let's get it locked down. Step one, an attacker who accesses an old email, a forwarded message, a breached inbox finds every reset link ever sent. Each one still works because your AI never set a time limit. Four months later, a token is still valid. The user has changed their password, updated their security settings, enabled two-factor authentication, but none of it matters because the old link bypasses all of that. So, direct your AI to set every password reset token to expire within 15 minutes. That's a win. Step two, a reset token that works more than once lets an attacker use it after the legitimate user already has. So, the user clicks the link, resets the password, and moves on, right? Well, the attacker clicks the same link an hour later and resets it again. The user has no idea what just happened. So, directory AI to invalidate every reset token immediately after the first use. In step three, an attacker who finds the reset endpoint can request thousands of tokens per minute. Each one is a valid entry point. Each one lands in the inbox the attacker may have access to. Without rate limiting, your reset flow is a token factory. So, direct your AI to Limit reset requests to three per email address per hour. That's a win. Your your password reset has a door, folks. Your AI built it without a lock, without a timer, and without a limit. Time to lock it down for good.

</div>
