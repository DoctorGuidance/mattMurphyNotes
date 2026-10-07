# Episode 228: A token that never expires is not auth

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Authentication & Identity (`احراز هویت و مدیریت نشست‌ها`) |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZm7yPZxxlC/) |

---

## 🚨 1. The Incident & Attack Vector
A token that never expires is not auth.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Stores credentials in client-side localStorage/sessionStorage vulnerable to XSS and malicious dependencies. | Stores tokens in HttpOnly, Secure, SameSite=Lax cookies completely inaccessible to JavaScript. |

---

## 💡 3. Root Cause & Architectural Principle
That is a wide open door for trouble. So, here are the three things you're going to do right now to fix it. Step one, understand what a session actually is.

---

## ⚡ 4. Hardening Action Checklist
- [ ] understand what a session actually is.
- [ ] set expiration and rotation.
- [ ] implement logout properly.

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
> **Production Heuristic:** It is an open door.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

When your users log in, a token gets created and that token lives forever. That is not Oth, folks. That is a wide open door for trouble. So, here are the three things you're going to do right now to fix it. Step one, understand what a session actually is. When a user logs in, your system creates a unique token. That token proves who they are on every single request they make. Jot files, session cookies, whatever the mechanism, right? If that token never expires, anyone who steals it owns that account forever. No password change fixes it. No logout will fix it. The token is the key, and you hand it out a key that never stops working. That's not a win. Step two, set expiration and rotation. Access tokens should be short-lived. 15 minutes, 30 minutes, not 30 days. Refresh tokens extend the session without asking the user to log in again. So when the access token expires, the refresh token gets a brand new one and the refresh token itself continues to rotate. So every time it is used, the old one dies and a new one is born. So if someone steals the old token, it's already dead. That's a win. So clerk handles this automatically. Superbase handles this automatically. But if you built off yourself, you need to handle this yourself. Step three, implement logout properly. Logout does not mean delete. the cookie from the browser. Log out means invalidating the session on the server completely. If your logout only clears the front end, the token still works. Anyone who captured it can still make authenticated requests. Server side sessions invalidation is the only logout that's going to count. So, make sure you close the door behind you for no new visitors. That's a win.

</div>
