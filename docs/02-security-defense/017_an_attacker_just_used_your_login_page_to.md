# Episode 017: An attacker just used your login page to send your users to

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdewD5fFOjE/) |

---

## 🚨 1. The Incident & Attack Vector
An attacker just used your login page to send your users to a phishing site.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |

---

## 💡 3. Root Cause & Architectural Principle
The destination comes from a URL parameter your server never validates. A redirect after login is most trusted moment in your application. So an attacker knows how to exploit that trust completely.

---

## ⚡ 4. Hardening Action Checklist
- [ ] your login URL includes a parameter.
- [ ] an attacker who cannot use an external URL tries a relative path that resolves unexpectedly, like a double slash at the start, a backslash, an encoded character.
- [ ] your logout flow has the same vulnerability.

---

## 💻 5. Hardened Production Implementation
```typescript
// guardrails/aiAuditTrail.ts
import crypto from 'crypto';
import { db } from '../lib/db';

export async function recordAIGeneration(userId: string, model: string, prompt: string, output: string) {
  const promptHash = crypto.createHash('sha256').update(prompt).digest('hex');
  await db.aiAuditLogs.create({
    data: {
      userId,
      modelName: model,
      promptSha256: promptHash,
      isSyntheticallyGenerated: true,
      timestamp: new Date()
    }
  });
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Your login page is your user's front door.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI built a return to feature. After login, the user redirects to the page they came from. The destination comes from a URL parameter your server never validates. A redirect after login is most trusted moment in your application. So an attacker knows how to exploit that trust completely. Here's the three steps you're going to take to fix it. Step one, your login URL includes a parameter. liked return to or redirect. An attacker crafts a link pointing to your real login page with the redirect set to their fishing site. That's not a win. The user sees your real form, types their real password, and after authentication, your server sends them to the attacker's page. No reason to suspect anything because they just logged in for real from their perspective. So, Directory AI to validate every redirect URL. against an allow list of your domains. Step two, an attacker who cannot use an external URL tries a relative path that resolves unexpectedly, like a double slash at the start, a backslash, an encoded character. URL parsing treats these differently than your validation does. The redirect passes the check and sends the user off of your site. So, direct your AI to parse the redirect URL and reject anything that resolves outside your application, including protocol relative and encoded variance. Right, that's a win. And step three, your logout flow has the same vulnerability. A redirect after logout sends the user to a fishing login page that looks just like yours. So, the user thinks they were logged out and logs back in on the attacker's page. It's time to direct your AI to audit every every redirect in your authentication flow, not just login. That is definitely a win because your login page is your users's front door, right? And an attacker just put a fake hallway behind it and they're trying to get all your users. Don't let it happen. Get it locked up.

</div>
