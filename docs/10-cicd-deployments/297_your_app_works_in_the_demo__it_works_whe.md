# Episode 297: Your app works in the demo. It works when you show your

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Testing, Staging & CI/CD (`تست، محیط‌های کاری، CI/CD و خط لوله استقرار`) |
| **Target Production Layer** | Layer 7 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYZ1EeNgGIu/) |

---

## 🚨 1. The Incident & Attack Vector
Your app works in the demo. It works when you show your friends. But it’s not a product. It’s a demo pretending to be a product. Here’s how to close the gap: • Give it to 5 strangers — if they can’t figure it out in 30 seconds, it’s not ready • Break it on purpose — find the crashes before your users do • Add the boring stuff — error messages, loading states, password reset A demo impresses people. A product serves people. Ship the product. -MM

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |

---

## 💡 3. Root Cause & Architectural Principle
It works when you show your family and your friends on your laptop, right? But it's not actually a product. It's a demo pretending to be a product.

---

## ⚡ 4. Hardening Action Checklist
- [ ] give it to five people that you didn't build it for.
- [ ] break it on purpose a bunch.
- [ ] add all the boring stuff.

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
> **Production Heuristic:** A demo impresses people. A product serves people. Ship the product.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Sure, that cool app you've been telling everybody about works on your computer. Works in a cool little demo. It works when you show your family and your friends on your laptop, right? But it's not actually a product. It's a demo pretending to be a product. So, let's turn it into a product. Here's how you make that change. Number one, give it to five people that you didn't build it for. Not your friends, not your co-founder, not even your mom. Five strangers who fit your target user. Just watch them use it. Don't explain anything to them. Don't help out. If they can't figure it out in 30 seconds, it's not ready for production. Trust me. A demo needs context. A product never does. Number two, break it on purpose a bunch. Enter a blank form. Type a,000 characters. Type 10,000 characters. Hit submit 47 times. Open it on a phone. Whatever you didn't think it would do, your users will do in the first hour anyway. So, if your app crashes when someone does something, totally unexpected. You shipped a prototype, not a product. Find the brakes before they do. Number three, add all the boring stuff. Error messages, loading states, empty states, password resets, terms of service pages. None of this is exciting. Not even a little bit. But all of it is required. The gap between a demo and a product is 100 boring things done, right? That's what separates builders from your friend with a little hobby on his phone, right? A demo impresses people. A product services people. You have to serve people with a product you can ship.

</div>
