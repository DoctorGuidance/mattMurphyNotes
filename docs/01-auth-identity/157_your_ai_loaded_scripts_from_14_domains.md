# Episode 157: Your AI loaded scripts from 14 domains

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Authentication & Identity (`احراز هویت و مدیریت نشست‌ها`) |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Danl3ysjuQ8/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI loaded scripts from 14 domains.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |

---

## 💡 3. Root Cause & Architectural Principle
Every one of them runs code in your users browsers. So, here are the three things you're going to direct your AI to do right now to lock it down. Step one, content security policy headers.

---

## ⚡ 4. Hardening Action Checklist
- [ ] content security policy headers.
- [ ] audit what your AI installed.
- [ ] report before you enforce.

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
> **Production Heuristic:** So now it's time to lock it down

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your app is loading scripts from 14 different domains and you only approved three of them. Your AI pulled in analytics, font libraries, thirdparty widgets, and tracking pixels. Every one of them runs code in your users browsers. So, here are the three things you're going to direct your AI to do right now to lock it down. Step one, content security policy headers. Direct your AI to add CSP headers that whitelist ex exactly which domains can load scripts in your application. If a domain is not on the list, the browser blocks it. One malicious script on one compromised CDN can hijack every session on your site. CSP stops it before it executes, and that's the win. Step two, audit what your AI installed. Direct your AI to list every external resource your application is loading. Scripts, stylesheets, fonts, images, iframes. If you cannot explain why each one is there. It shouldn't be there. Your AI added it for convenience. You need to verify it did not add risk. Step three, report before you enforce. CSP has a report only mode. Direct your AI to enable reporting first. Collect violations for a week. See what breaks before you block it. Then you enforce. 14 domains is not a feature. It's an attack surface your AI built. without asking you about it. So now it's time to lock it down.

</div>
