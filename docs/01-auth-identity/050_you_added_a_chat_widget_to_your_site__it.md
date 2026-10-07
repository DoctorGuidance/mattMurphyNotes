# Episode 050: You added a chat widget to your site. It can read every

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Authentication & Identity (`احراز هویت و مدیریت نشست‌ها`) |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Dct1A_WDsrP/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI added a chat widget to your site during your build. Not uncommon. But now it can read every password your users are typing on every single page.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
But now it can read every password your users are typing on every single page. So your AI dropped in a script tag, one line, instant customer support widget in the corner of every page. But that script runs with the same privileges as your own code.

---

## ⚡ 4. Hardening Action Checklist
- [ ] audit every
- [ ] implement a content security policy that restricts what external scripts can do. A CSP tells the browser which domains are allowed to execute scripts on your page.

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

Your AI added a chat widget to your site during your build. Not uncommon. But now it can read every password your users are typing on every single page. So your AI dropped in a script tag, one line, instant customer support widget in the corner of every page. But that script runs with the same privileges as your own code. It can read every form field, every keystroke, every cookie, every session token. Guess what? On every page, page, including your login page, your checkout page, your admin panel. So, you didn't install a chat widget. Your AI gave a third party full access to your entire application. Let's get it fixed. Step one, audit every third party script on your site and what it can access. Most teams cannot even list how many external scripts are loaded in their system. Analytics, chat, reviews, retargeting, AB testing, every one of them has full DOM. access by default. So, direct your AI to inventory every third party script, identify what data each can access, and then document which pages each script loads on. That's a win. Step two, remove third party scripts from every sensitive page. Your login page, your checkout page, your account settings page, your admin panel. No analytics tag needs to watch your users type their passwords. No chat widget needs to load on on your payment form. So, direct your AI to implement page level script loading that excludes thirdparty scripts from any page that handles credentials, payment data, or administrative functions. And step three, implement a content security policy that restricts what external scripts can do. A CSP tells the browser which domains are allowed to execute scripts on your page. Any script not on that list gets blocked. So, direct your AI to build a content security policy that whitelists only approved script sources and blocks inline script injection from any unauthorized origin. You control your code. Control who else gets to run theirs next to it.

</div>
