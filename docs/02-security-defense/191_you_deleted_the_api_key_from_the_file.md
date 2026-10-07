# Episode 191: You deleted the API key from the file

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaJQlPhFeqw/) |

---

## 🚨 1. The Incident & Attack Vector
You deleted the API key from the file.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Removes exposed secrets from source code via git commits without purging historical commits or revoking compromised keys. | Revokes leaked credentials immediately at the provider, rotates secrets, and purges git commit history with BFG Repo-Cleaner. |

---

## 💡 3. Root Cause & Architectural Principle
However, the old key is still in your git history, and git history never goes away. Here are the three things you can check right now to see if you're safe. Step one, scan your history.

---

## ⚡ 4. Hardening Action Checklist
- [ ] scan your history.
- [ ] environment variables are not secrets management.
- [ ] rotate on schedule.

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
> **Production Heuristic:** Every commit is permanent.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

So your API key is sitting in your repository again. You committed it 3 months ago, rotated it maybe last week. However, the old key is still in your git history, and git history never goes away. Here are the three things you can check right now to see if you're safe. Step one, scan your history. Every commit you have ever made is totally searchable. A secret you committed and deleted in the next commit still exists in the diff. Tools scan your entire git history for patterns that look like keys, tokens, and credentials all day long. Run one today. The results will absolutely surprise you. Step two, environment variables are not secrets management. AMV file works locally. In production, it becomes a total liability. Environment variables live in plain text. Anyone with server access can read them. So, a secrets manager encrypts at rest, controls access by role, and logs every read. The difference between a variable and a managed secret is an audit trail. That's the win. Step three, rotate on schedule. Not after a breach, but before one. If your key is not changed in 6 months, you're betting that nobody found it. Rotation is not paranoia, it's policy. And trust me, somebody found it. Your secrets are only secret if you treat them that way. So, you got to get in front of them.

</div>
