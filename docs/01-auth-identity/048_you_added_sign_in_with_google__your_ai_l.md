# Episode 048: You added Sign in with Google. Your AI left the redirect

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Authentication & Identity |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcwZzLckxZ4/) |

---

## 🚨 1. The Incident & Attack Vector
You added Sign in with Google. Your AI left the redirect wide open.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Accepts unvalidated `returnTo` redirect destinations after Google OAuth login, enabling phishing redirection attacks. | Validates post-authentication redirect URLs against a strict domain whitelist and enforces PKCE state parameters. |

---

## 💡 3. Root Cause & Architectural Principle
So, your AI, it built ooth flow, right? Log in with Google, get a token, redirect back to your app. But the redirect, that URL is not locked to your domain.

---

## ⚡ 4. Hardening Action Checklist
- [ ] lock your redirect URL to exact registered URLs.
- [ ] enforce a state parameter on every OOTH request.
- [ ] scope your token request to the minimum permissions your app actually needs.

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
> **Production Heuristic:** Your users trust that login button. Make sure it only works for you.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

So, your AI, it added signin with Google to your product, but your AI also left the redirect wide open. So, someone just sent your users a login link that delivers their token to a server you've never even seen. So, your AI, it built ooth flow, right? Log in with Google, get a token, redirect back to your app. But the redirect, that URL is not locked to your domain. And an attacker crafted a login link that looks exactly like you. So, the token gets redirected to their server instead of yours and your authentication worked perfectly, but it just worked for the wrong person. Let's get that tightened up. Step one, lock your redirect URL to exact registered URLs. No wild cards, no pattern matching, no open redirects. Every OOTH provider gives you a whitelist. If you redirect can point anywhere, your login can be hijacked from anywhere. So, direct your AI to audit every OOTH integration and restrict redirect URLs to exact hard-coded callback URLs registered with each provider. That's a win. Step two, enforce a state parameter on every OOTH request. The state parameter ties the login request to the user session. That's so the callback can verify the flow was initiated by your app and not by an attacker. Without it, anyone can forge an OOTH call call back. So direct your AI to generate a unique cryptographically random state value on every login request and reject any call back where that state does not match. That's also a win. And step three, scope your token request to the minimum permissions your app actually needs. So if you requested full profile access and your app only needs an email address, every stolen token gives the attacker more than it should. So direct your AI to audit every OOTH scope and reduce each to the minimum required for the feature it supports. Your users, they trust that login button, so make sure it only works for them.

</div>
