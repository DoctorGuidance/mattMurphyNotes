# Episode 009: An attacker intercepted your magic link and landed inside

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdrEewmD01_/) |

---

## 🚨 1. The Incident & Attack Vector
An attacker intercepted your magic link and landed inside your user's dashboard.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Issues long-lived, un-throttled magic login links with open redirect parameters, enabling token theft and phishing redirection. | Issues short-lived (5-10m) single-use magic tokens, locks redirect URLs to whitelisted domains, and rate limits email dispatch. |

---

## 💡 3. Root Cause & Architectural Principle
So, the user enters their email, your server, generates a signed token, embeds it in a URL, and emails it out. The user clicks and authenticates the URL includes a redirect parameter your AI never locked down. So let's get it locked down.

---

## ⚡ 4. Hardening Action Checklist
- [ ] your magic link URL includes a redirect parameter that tells the application where to send the user after authentication.
- [ ] magic link tokens that do not expire remain valid indefinitely in users email.
- [ ] an attacker who discovers the Magic Link endpoint can request thousands of links per minute for any email address.

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
> **Production Heuristic:** Your magic link removes the password. It should not remove the security.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI implemented magic link authentication, but an attacker just intercepted your magic link and landed inside your users's dashboard. So, your passwordless login just became a passwordless breakin and your AI built the flow without validating where the link resolves. So, the user enters their email, your server, generates a signed token, embeds it in a URL, and emails it out. The user clicks and authenticates the URL includes a redirect parameter your AI never locked down. So let's get it locked down. Step one, your magic link URL includes a redirect parameter that tells the application where to send the user after authentication. An attacker crafts a link with the redirect set to their server. The user clicks that magic link from their real email, authenticates against your real application, and your server sends their authentic ated session to the attacker's domain. So now the attacker has the session token. So you need to direct your AI to validate the redirect parameter against all allow list of your own domains before issuing a redirect at all. That is a win. Step two, magic link tokens that do not expire remain valid indefinitely in users email. So an attacker who gains access to a mailbox 6 months later finds every magic link still fully active. Each one is a valid authentication bypass. So, direct your AI to set Magic Link tokens to expire within 10 minutes and invalidate them immediately after first use. And step three, an attacker who discovers the Magic Link endpoint can request thousands of links per minute for any email address. So, each request sends a real email from your domain. This floods the targets inbox and damages your sender reputation. That's important. So direct your AI to rate limit magic link request to three per email address per hour and throttle total request per IP. Your magic link removes that password, but it should not remove all of your security. Get it fixed.

</div>
