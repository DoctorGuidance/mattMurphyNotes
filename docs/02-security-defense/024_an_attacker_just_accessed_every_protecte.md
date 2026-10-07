# Episode 024: An attacker just accessed every protected page in your app

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdWeKvGDz5k/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI set up next.js middleware to check authentication, right? But an attacker just accessed every protected page in your app without logging in at all because the attacker's request never hit next.js. So your AI added authentication in middleware, one file, every route protected, right?

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
So your AI added authentication in middleware, one file, every route protected, right? But middleware does not run on every single request type. So some pass can bypass it entirely.

---

## ⚡ 4. Hardening Action Checklist
- [ ] next.js middleware matches routes using your matcher config. If API routes are excluded from the matcher, every API endpoint is unprotected.
- [ ] a trailing slash a double encoded character or a path prefix changes how the matcher evaluates in a request. Right?
- [ ] middleware runs at the edge before your server. Your AI may check that a cookie exists without validating it against your session store.

---

## 💻 5. Hardened Production Implementation
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

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Never deploy unverified AI-generated code directly to production without testing failure modes.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI set up next.js middleware to check authentication, right? But an attacker just accessed every protected page in your app without logging in at all because the attacker's request never hit next.js. So your AI added authentication in middleware, one file, every route protected, right? But middleware does not run on every single request type. So some pass can bypass it entirely. One off layer with gaps is no off layer. at all. So, let's get it locked down. Number one, next.js middleware matches routes using your matcher config. If API routes are excluded from the matcher, every API endpoint is unprotected. So, your AI built to check for your page navigation, but an attacker calls the API endpoint directly. The middleware never fires and so the response comes back with all the data. So, directory AI to verify the middleware matcher includes every route that requires authentication. That's a win. Number two, a trailing slash a double encoded character or a path prefix changes how the matcher evaluates in a request. Right? So when your middleware does not recognize the variation it's seeing, the request passes right on through. So the route resolves and returns protected data on that request. So you need to direct your AI to test every protected route with path variations and confirm Confirm the middleware intercepts each one. That's a win. And step three, middleware runs at the edge before your server. Your AI may check that a cookie exists without validating it against your session store. So where an AI expired or forged cookie passes through, the real validation must happen server side. So direct your AI to add server side authorization checks on every API route and server component independent of the middleware. middleware. It's a convenience layer. And if it's your only authorization check, it's your weakest one. So, let's get it fixed.

</div>
