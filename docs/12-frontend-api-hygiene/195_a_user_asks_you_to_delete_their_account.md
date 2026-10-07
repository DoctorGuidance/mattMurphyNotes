# Episode 195: A user asks you to delete their account

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Frontend Architecture & API Hygiene (`معماری فرانت‌اند، طراحی واسط و بهداشت API`) |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaGFCCNFf7m/) |

---

## 🚨 1. The Incident & Attack Vector
A user asks you to delete their account.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Deletes only primary user records upon account deletion requests, leaving orphaned PII in related database tables. | Executes cascading foreign key deletions or automated GDPR erasure workflows that purge user data across all tables. |

---

## 💡 3. Root Cause & Architectural Principle
Here are the three things you reconcile right now to protect yourself. Step one, know exactly what you collect. Most applications collect more than the team ever realizes.

---

## ⚡ 4. Hardening Action Checklist
- [ ] know exactly what you collect.
- [ ] consent is not a checkbox.
- [ ] data retention.

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
> **Production Heuristic:** Their data is in six other tables.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your privacy policy says you do not sell user data, but your analytics send it to four different thirdparty services that do. A regulator will know the difference. Here are the three things you reconcile right now to protect yourself. Step one, know exactly what you collect. Most applications collect more than the team ever realizes. IP addresses and logs, device fingerprints and analytics, location data from API calls. If you cannot list every piece of personal data in your application touches your privacy policy is fiction. Audit the data map where it goes. That's the win. Step two, consent is not a checkbox. A banner that says we use cookies and a button that says accept is not informed consent. Users should understand what they're agreeing to in plain language before the data moves anywhere. The regulation is not about the checkbox. It is about whether the user undersod the deal altogether. Step three, data retention. Your user deleted their account. Their data still lives in your database, in all of your backups, in your analytics, and in your logs. Deletion is not a button click. It is an architectural decision. Know where user data lives. Build the deletion pipeline before someone asks about it. Privacy is not a legal page. It is a system. Build it to keep yourself from getting sued.

</div>
