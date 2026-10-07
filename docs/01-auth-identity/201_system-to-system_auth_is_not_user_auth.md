# Episode 201: System-to-system auth is not user auth

> **Category:** Authentication & Identity (احراز هویت و مدیریت نشست‌ها)  
> **Production Layer:** Layer 4  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DaAwzEqFWpT/](https://www.instagram.com/reel/DaAwzEqFWpT/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your API talks to three other services. Each one requires authentication. None of them are users logging in though.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
None of them are users logging in though. Here are the three things you got to get right. Step one, service to service off is not user off.

---

## ⚡ 3. Hardening Action Checklist
- [ ] service to service off is not user off. There is no login screen, no session cookies, no password reset flow.
- [ ] shared secrets are just a starting point. An API key in an environment variable works until that variable leaks.
- [ ] mutual TLS verifies both sides. ides the client proves itself to the server.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Secure HttpOnly Cookie Issuance
res.cookie('session_token', token, {
  httpOnly: true,                               // Inaccessible to client JS
  secure: process.env.NODE_ENV === 'production', // HTTPS only
  sameSite: 'lax',                              // CSRF protection
  path: '/',
  maxAge: 15 * 60 * 1000                        // 15-minute short-lived
});
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your API talks to three other services. Each one requires authentication. None of them are users logging in though. Here are the three things you got to get right. Step one, service to service off is not user off. There is no login screen, no session cookies, no password reset flow. One service proves to another that it has permission to make that request. The mechanism is different, but the stakes are definitely higher. A compromised service token does not affect one account, it affects all accounts. Step two, shared secrets are just a starting point. An API key in an environment variable works until that variable leaks. An environment variable leaks, they leak in logs, in error messages, and stack traces. So, rotate your secrets on a schedule, not after an incident. The rotation plan you build before the breach is the one that will save you, and that's a win. Step three, mutual TLS verifies both sides. ides the client proves itself to the server. The server proves itself to the client. No token to steal, no secret to rotate. The identity lives in the certificate. For high trust internal communications, MTLS removes the API key from the equation altogether. Your services trust each other. Make them prove it though.

</div>
