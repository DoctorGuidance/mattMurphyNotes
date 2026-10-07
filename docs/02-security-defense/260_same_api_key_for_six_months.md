# Episode 260: Same API key for six months

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZGYLpLPDR-/) |

---

## 🚨 1. The Incident & Attack Vector
Same API key for six months.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Exposes security boundaries in 'Same API key for six months', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Same API key for six months'. |

---

## 💡 3. Root Cause & Architectural Principle
And if it leaks and keys leak, every system that touches it is compromised until you rotate it manually, right? While your app is down. So here are the three things you do right now to fix it.

---

## ⚡ 4. Hardening Action Checklist
- [ ] move your secrets to a dedicated manager.
- [ ] implement dual key rotation.
- [ ] automate the rotation schedule.

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
> **Production Heuristic:** If you can't remember, it's probably time

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your API key is hardcoded in yourv file. It has been the same key for the last 6 months. And if it leaks and keys leak, every system that touches it is compromised until you rotate it manually, right? While your app is down. So here are the three things you do right now to fix it. Step one, move your secrets to a dedicated manager. Doppler, infysical or AWS secrets manager, not yourv file. Not your Versell dashboard, but a real secrets manager that gives you versioning, audit logs, and rotation APIs, your app. It fetches secrets at runtime instead of bundling them at deploy time. One command swaps a key across every environment simultaneously. Step two, implement dual key rotation. Generate a key while the old one still works. Deploy the new key to your application. Verify traffic flows on the new key, then revoke the old key. Two keys active simultaneously during the transition window. Zero downtime, zero failed request. That one's a win. Step three, automate the rotation schedule. Set a cron job or a scheduled function. Every 30 days, generate a new key, update your secrets manager, trigger redeployment, verify a health check, and revoke the old key. Clean automation. No human in the loop. No calendar reminder that you're going to forget. Manual rotation means you're only one rotation away from a breach. Automated rotation means a breach has 30-day blast radius instead of an infinite blast radius. So, when did the last time you changed your API keys? If you can't remember, it's probably time.

</div>
