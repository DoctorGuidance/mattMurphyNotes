# Episode 288: Your frontend talks to the database directly

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Database & Storage Engineering (`پایگاه‌داده، روابط، ایندکس و پایداری داده`) |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYiSfwGP2D9/) |

---

## 🚨 1. The Incident & Attack Vector
Your frontend talks to the database directly.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Leaves endpoints open without rate limiting, allowing scrapers or brute-force bots to drain resources. | Implements token bucket rate limiting at gateway level, throttling abusive IPs with exponential backoff. |

---

## 💡 3. Root Cause & Architectural Principle
That's a security hole with UI. Layer two of 13 is where your app's brain lives. Business logic, data validation, rate limiting, request authentication.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Inspect the existing code paths and identify unvalidated boundary inputs.
- [ ] Implement defense-in-depth guardrails preventing unauthorized state modification.
- [ ] Add automated regression tests verifying failure scenarios before shipping.

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
> **Production Heuristic:** It's time to lock it up so you can ship

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your app calls the database from the front end. That's not an architecture strategy. That's a security hole with UI. Layer two of 13 is where your app's brain lives. Business logic, data validation, rate limiting, request authentication. Without a proper backend, your front end talks to the database directly and your secrets live directly in your browser. Your logic can be inspected by anyone at that point. The AI builds you a front that calls Superbase directly works great for a demo, but that's terrible for production. There's no input validation. There's no rate limiting. There's no business rules enforcement. A user can send a thousand requests in a second, your app is going to process all of them. A user sends malformed data, your app's just going to store it. And a user manipulates the client side code, your app trusts it. Layer 2 is not glamorous. It's the bouncer at the door. And right now, your door is wide open. It's time to lock it up so you can ship.

</div>
