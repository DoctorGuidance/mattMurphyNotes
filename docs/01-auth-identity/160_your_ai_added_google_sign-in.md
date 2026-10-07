# Episode 160: Your AI added Google Sign-In

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Authentication & Identity (`احراز هویت و مدیریت نشست‌ها`) |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DallI-2D9Q7/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI added Google Sign-In.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Implements naive authentication in 'Your AI added Google Sign-In', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Your AI added Google Sign-In'. |

---

## 💡 3. Root Cause & Architectural Principle
Here are the three things you're going to direct your AI to do right now to fix it. Step one, silent token refresh. Your access token expires every 60 minutes.

---

## ⚡ 4. Hardening Action Checklist
- [ ] silent token refresh.
- [ ] graceful refresh failure.
- [ ] token rotations.

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
> **Production Heuristic:** Keeping users logged in safely is the orchestration nobody teaches.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your users get logged out every hour right in the middle of their important work and your app keeps dumping them to a login screen. So your AI did add Google Signin, but it did not handle the token life cycle. Here are the three things you're going to direct your AI to do right now to fix it. Step one, silent token refresh. Your access token expires every 60 minutes. Direct your AI to refresh it in the background before it expires. This way, the user never sees a login screen and the refresh happens invisibly. If your AI is only handling the initial login and ignores the refresh, every session has a 1 hour ceiling and that's not a win for your users. Step two, graceful refresh failure. The refresh token, it expires. The session, it's totally over. And so you need to direct your AI to redirect the login to the user's state preserved. Not a blank page, not a lost draft. not a cleared cart. Return them right where they were after reauthentication. That's a win. And step three, token rotations. Direct your AI to rotate refresh tokens on every use. A stolen refresh token that works forever is a permanent backdoor. A rotated token, it works once. Reuse flags a compromise. Login is always easy. So, keeping users safely logged in is the AIdirected orchestration that nobody else is teaching but the fact

</div>
