# Episode 124: A user logged in six months ago

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Authentication & Identity (`احراز هویت و مدیریت نشست‌ها`) |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbGolYUFbnV/) |

---

## 🚨 1. The Incident & Attack Vector
A user logged in six months ago.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Issues long-lived session tokens that never expire, leaving accounts vulnerable if client devices are lost or stolen. | Enforces rotating refresh tokens with 7-day idle timeouts, 30-day absolute expirations, and remote session revocation. |

---

## 💡 3. Root Cause & Architectural Principle
Someone opened it and your app was still logged in. So your database is wide open on a stranger's screen right now. And your AI, it built authentication, but it never built session management.

---

## ⚡ 4. Hardening Action Checklist
- [ ] session expiration with a defined timeline.
- [ ] concurrent session limits.
- [ ] is instant session revocation.

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
> **Production Heuristic:** So, you need to direct your AI to close them tonight

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

A user who logged in 6 months ago still has full access to your entire application right now. They lost their laptop at a coffee shop 3 months ago. Someone opened it and your app was still logged in. So your database is wide open on a stranger's screen right now. And your AI, it built authentication, but it never built session management. And sessions that never expire and tokens that live forever are open doors everywhere in your system. So here are the three things you direct your AI to build before someone walks through a door you forgot to close. Step one, session expiration with a defined timeline. Right now, your sessions live forever because most frameworks ship that way and your AI use the default. A banking app and a note-taking app do not get the same session window. You decide the lifetime based on what your application touches. Financial data, hours or less. Low-risk content, days or less. That is an engineering decision and it's yours to make. All right, step two, concurrent session limits. Right now, one user can be logged in on 15 devices and you would just never know because when credentials get stolen, the attacker rides an existing session while the real user has no idea someone else is in their account. So, your AI can cap active sessions per user. Most builders do not know this is even possible. And step three is instant session revocation. When a user changes their password, every active session for that user needs to die right then. Not on the next token refresh, not eventually, right now. Without it, a user who changes their password still has an attacker sitting inside an active session on another device. The password change was a false sense of security. Your AI built the lock on the front door. It left every window in the house wide open. So, you need to direct your AI to close them tonight.

</div>
