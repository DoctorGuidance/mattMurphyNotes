# Episode 147: Six documents before your first paying user

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Cloud Infrastructure & FinOps |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Davh5IQjRBY/) |

---

## 🚨 1. The Incident & Attack Vector
Six documents before your first paying user.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Accepts commercial payments before establishing formal terms of service, refund policies, and dispute documentation. | Publishes clear, legally binding terms of service, acceptable use policies, and refund guidelines prior to onboarding paying users. |

---

## 💡 3. Root Cause & Architectural Principle
You know that one that no one reads. Well, that's the one that defines what your users can and cannot do, what you are liable and not liable for, and what happens when things go wrong. Your AI can draft it, but you need to direct it with your specific use.

---

## ⚡ 4. Hardening Action Checklist
- [ ] terms of service.
- [ ] privacy policy.
- [ ] data processing agreement, a DPA.

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
> **Production Heuristic:** Your AI can draft every one. But only if you know to ask.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your product's ready, your first customers are ready to pay, but before you accept a single payment, you want these six documents in place in your business or you're going to end up exposed. Doc number one, terms of service. You know that one that no one reads. Well, that's the one that defines what your users can and cannot do, what you are liable and not liable for, and what happens when things go wrong. Your AI can draft it, but you need to direct it with your specific use. case for your product, all of your data practices and your liability boundaries. A template you download from the internet protects nobody at all. Doc number two, privacy policy. This tells users what data you collect and how you use it and how they request deletion from it. If your policy says one thing and your app does another, you have a compliance violation. Not a technicality, but a sizable fine if you don't get it right. Doc number three, data processing agreement, a DPA. If you process data on behalf of another business, a DPA defines who is responsible for what. GDPR absolutely requires it. Enterprise customers will ask for it every single time. Doc number four is a refund policy. What happens when a customer wants their money back? Payment processors, they require it. Customer trust absolutely depends on it. Doc number five, this one's big. Master service agreement. If you were selling your system to a company that's going to use it. The MSA defines how you support it. SLAs's, uptime guarantees, response times, and what happens when something breaks. The MSA governs the relationship between your product and their business. It's a big deal. And doc six, it's optional, but it's important. Cyber liability insurance. When you handle someone else's data and something goes wrong, you will end up personally liable, not your LLC. I've corrected it in plenty of comments. Most Policies cost $200 to $600 a year and $200 to protect what could be a $50,000 problem. That's a big deal. Not everyone needs it on day one. I get it. But the moment you handle customer data at scale, the coverage protects what the documents alone cannot. So those six documents, none of them are code. All of them protect the business and the product underneath the code. Your AI can draft every single one of them for you, but only if you know what to ask for. Now you do.

</div>
