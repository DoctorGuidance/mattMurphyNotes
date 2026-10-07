# Episode 120: Your app went down and your customers think you stole their

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Cloud Infrastructure & FinOps (`معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbL-9-3kT8H/) |

---

## 🚨 1. The Incident & Attack Vector
Your app went down and your customers think you stole their money. Six hours of downtime.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |

---

## 💡 3. Root Cause & Architectural Principle
And this is all because your AI never built you a status system. Here are three things you direct your AI to build before your next outage becomes a trust crisis. Step one, a public status page on a separate domain altogether, not hosted on your main infrastructure.

---

## ⚡ 4. Hardening Action Checklist
- [ ] a public status page on a separate domain altogether, not hosted on your main infrastructure.
- [ ] a scheduled maintenance announcement system.
- [ ] an incident communication workflow.

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
> **Production Heuristic:** So direct your AI to build it before your next outage cost you more than just a little bit of downtime

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your app went down when you were asleep and now your customers think you stole their money. 6 hours of downtime, no status page, no status updates, no maintenance announcement, no communication to the users of any kind. And this is all because your AI never built you a status system. Here are three things you direct your AI to build before your next outage becomes a trust crisis. Step one, a public status page on a separate domain altogether, not hosted on your main infrastructure. Because when your app goes down, your status page goes down with it. So your AI can deploy a standalone status page in 20 minutes on a completely separate host. The difference between the site is down and I have no idea why. And we know and we are trying to fix it is the difference between a chargeback and patience. Right? And that's a win if you get it right. Step two, a scheduled maintenance announcement system. Every application needs downtime. The Builders who announce maintenance windows in advance, they look professional. The builders who take their app down at 2 p.m. on a Tuesday afternoon with no warning look pretty amateur. So, your AI can build an automated notification system that emails active users before scheduled downtime and posts it to your status page so your customers do not mind downtime. They don't mind it at all. They mind surprises and time that they had set aside that you didn't notify them. And step three, an incident communication workflow. When an outage hits, you need a status page update with defined intervals, email notifications to active subscribers, and an estimated restoration time, even if it's just a guess. Silence during an outage is what turns technical problems into a reputation and revenue problem. Your AI can build the entire workflow with templates preloaded and triggers fully automated, but it'll never build it on its own because it does not know that silence is the fastest way to lose every customer you earned. So your AI built a product and never built the system. It tells your customers the product is still alive even when it isn't. So direct your AI to build it before your next outage cost you more than just a little bit of downtime.

</div>
