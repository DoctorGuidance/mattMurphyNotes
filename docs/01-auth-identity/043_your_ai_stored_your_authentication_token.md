# Episode 043: Your AI Stored Your Authentication Token in LocalStorage

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Authentication & Identity (`احراز هویت و مدیریت نشست‌ها`) |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Dc3kkckjyYV/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI built your authentication system. Server returns a JWT; frontend stores it in `localStorage`. That token represents your user's identity, sitting in a storage location that every script on your page (including third-party chat widgets and analytics) can silently read.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Stores JWTs in `localStorage` or `sessionStorage` accessible to any script via `window.localStorage`. | Stores tokens in `HttpOnly; Secure; SameSite=Lax` cookies completely invisible to JavaScript. |

---

## 💡 3. Root Cause & Architectural Principle
Client-side storage is for public UI state, not security tokens. Protect credentials behind browser cookie flags that prevent JavaScript access.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Move all authentication tokens out of `localStorage` and into `HttpOnly; Secure; SameSite=Lax` cookies.
- [ ] Shorten access token lifespans to 10–15 minutes and implement rotating refresh tokens.
- [ ] Add immediate server-side revocation so compromised sessions can be terminated instantly.

---

## 💻 5. Hardened Production Implementation
```typescript
// auth/cookieSession.ts
import { Response } from 'express';

export function issueAuthCookie(res: Response, token: string) {
  res.cookie('auth_token', token, {
    httpOnly: true,                               // Completely blocks JS access
    secure: process.env.NODE_ENV === 'production', // HTTPS only
    sameSite: 'lax',                              // Mitigates CSRF
    path: '/',
    maxAge: 15 * 60 * 1000                        // 15-minute short expiry
  });
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Your auth token is your user's key to the building. Stop leaving it on the counter where any script can copy it.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI stored your authentication token in local storage. Now any script on your page can steal it and log in as your user. So your AI built your login system. User authenticates. Server sends back to a jot file. Front end stores it in local storage. That token is your user's identity and it is sitting in a storage location that every script on your page can read. So that chat widget you added last week can read your users off tokens right now. Here's how we're going to fix it. Number one, move your tokens out of local storage and into HTTPON cookies. An HTTPon cookie cannot be read by JavaScript. It travels with every request automatically and is invisible to any script running on your page. So, direct your AI to refactor authentication flow. So, it stores the jot in a secure HTTPON same site cookie instead of local storage. That's a win. Number two, Set token expiration short and implement refresh tokens. A stolen jot that lasts 30 days is an open door for 30 days. A token that expires in 15 minutes limits that damage window. So direct your AI to implement short-lived access tokens with a secure refresh token rotation that issues a new pair on each refresh. That's a win. And number three, add token revocation. If a user changes their password or reports a compromised account, every active token for that user should die immediately. So, directory AI to implement a token revocation list or a per user user token version, right? So that it invalidates all existing tokens when the user's security state changes. Your off token is your user's key to the building. Stop leaving it on the counter where anyone can copy it. And that is a win.

</div>
