# Episode 117: 2,000 builders asked us to look at their apps

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Frontend Architecture & API Hygiene |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbQmjD1D_ua/) |

---

## 🚨 1. The Incident & Attack Vector
2,000 builders asked us to look at their apps.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Ships frontend applications missing global error boundaries, causing whole pages to crash to blank white screens on minor exceptions. | Wraps critical UI components in React Error Boundaries that display graceful fallback UIs with retry buttons upon crashes. |

---

## 💡 3. Root Cause & Architectural Principle
Not kidding. DMs, comments, emails, inbound audits at the faction group, Matt Murphy AI from everywhere. And there people sending their URLs asking what's wrong.

---

## ⚡ 4. Hardening Action Checklist
- [ ] no error handling beyond the default.
- [ ] no environment separation.
- [ ] no audit trail on sensitive actions.

---

## 💻 5. Hardened Production Implementation
```typescript
// pages/api/secureProxy.ts
import type { NextApiRequest, NextApiResponse } from 'next';

// Server-side gateway: Secret keys NEVER touch the client bundle
export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const secretKey = process.env.INTERNAL_SERVICE_KEY; // Kept strictly on server
  const response = await fetch('https://api.upstream.com/v1/data', {
    headers: { 'Authorization': `Bearer ${secretKey}` }
  });
  const data = await response.json();
  res.status(200).json(data);
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Direct your AI to close them before your customers find them first, which is usually exactly what happens

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Over 2,000 builders have had us look at their app and the same three things are broken and almost every single one. 2,000 requests. Not kidding. DMs, comments, emails, inbound audits at the faction group, Matt Murphy AI from everywhere. And there people sending their URLs asking what's wrong. The pattern was so consistent it was almost heartbreaking. They all built something that works. None of them built anything that protects it. Here's are the three things that were missing in almost every single app that we've reviewed. Number one, no error handling beyond the default. Their AI built the feature. When the feature works, it works beautifully, right? But when it fails, the user gets a white screen or a stack trace or a generic 500 error that means nothing to anyone. No graceful error messages, no fallback states, no way for the user to understand what happened or what to do next. Your AI builds the happy path. It never builds the unhappy path and your users live most of their life on the unhappy path way more than you think. Number two, no environment separation. Development and production are running in the same database, same API keys, same configuration altogether. One wrong query in development and your production users are going to feel it instantly. I saw apps where test users named ASDF were sitting in the same tables as all the paying customers and your AI does not know the difference between a test environment and a live one. Same for users. So unless you tell it they need to be separate, they aren't going to be. And number three, no audit trail on sensitive actions. Users upgrading plans, changing email addresses, deleting data, modifying permissions, none of it is logged. When a customer says, "I did not authorize that charge," you have no record of what happened. When a team member accidentally deletes a record, You have no way to trace it back. And your AI, it built the actions, just never built the receipts. Over 2,000 apps we've seen, same three gaps almost every time. Direct your AI to close them before your customers find them first, which is usually exactly what happens.

</div>
