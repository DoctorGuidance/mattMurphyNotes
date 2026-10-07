# Episode 234: Your frontend is a display layer, not a trust layer

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Frontend Architecture & API Hygiene (`معماری فرانت‌اند، طراحی واسط و بهداشت API`) |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZhxVg2xu-u/) |

---

## 🚨 1. The Incident & Attack Vector
Your frontend is a display layer, not a trust layer.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes successful network responses and relies solely on frontend validation for business state in 'Your frontend is a display layer, not a trust layer'. | Implements all 4 UI states, treats client state as untrusted, and verifies payload schemas on both client and server. |

---

## 💡 3. Root Cause & Architectural Principle
Just one user opens any basic dev tool and they can see anything. Here are the three things you can do right now to fix it. Step one, move every business rule to the back end.

---

## ⚡ 4. Hardening Action Checklist
- [ ] move every business rule to the back end.
- [ ] stop trusting client side validation.

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
> **Production Heuristic:** Move business logic, validation, and secrets to the backend.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your front end, it's making decisions it should not be making. Pricing logic and JavaScript, roll checks and React components, API keys and environment variables that ship to the browser. Just one user opens any basic dev tool and they can see anything. Here are the three things you can do right now to fix it. Step one, move every business rule to the back end. Discount calculations, feature gating, permission checks. If it decides what a user concede, do or pay, it does not belong in the client side code. The front end asks, the back end answers. That is the boundary and that is a win. Step two, stop trusting client side validation. Validate inputs on the front end for user experience. Validate them again on the back end for security. A disabled button is not access control. Anyone with a fetch request can skip your UI entirely. That's not a win. Step three. Audit what your bundle actually exposes. Run your production build. Open it up. Search for API routes, keys, internal endpoints, and config objects. If you can find any of those, so can anyone else. Environment variables prefixed with next_public or vite shipped to the browser. Know which ones. Your front end is a display layer, not a trust layer. The moment you treat it like a security boundary, you've already lost the battle.

</div>
