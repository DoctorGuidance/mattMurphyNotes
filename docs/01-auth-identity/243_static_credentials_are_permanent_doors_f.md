# Episode 243: Static credentials are permanent doors for attackers

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Authentication & Identity (`احراز هویت و مدیریت نشست‌ها`) |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZXhEL2RVRu/) |

---

## 🚨 1. The Incident & Attack Vector
Static credentials are permanent doors for attackers.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Deploys static, hardcoded API secret keys that remain unchanged across environments for years, maximizing breach blast radiuses. | Enforces automated secret rotation using cloud secret managers and issues short-lived ephemeral credentials to services. |

---

## 💡 3. Root Cause & Architectural Principle
If they leak, every query in your system is compromised until you change them manually. Here are three things you can do right now to fix it. Step one, deploy a secrets engine that generates credentials on demand.

---

## ⚡ 4. Hardening Action Checklist
- [ ] deploy a secrets engine that generates credentials on demand.
- [ ] configure per service credential scoping.
- [ ] enable audit logging on every secret access.

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
> **Production Heuristic:** Dynamic secrets expire before anyone can live there.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your database credentials are completely static. Same username and password for the last 6 months. If they leak, every query in your system is compromised until you change them manually. Here are three things you can do right now to fix it. Step one, deploy a secrets engine that generates credentials on demand. Hashy Corpse Vault or Infysical or your cloud provider's native manager. Whatever it is, the difference from basic secrets management Dynamic secrets are created per session and auto expire. That's a win. Your app requests those credentials. Vault generates a unique set. They live for 1 hour, then they die. No permanent credentials to steal. Like I said, that's a win. Step two, configure per service credential scoping. Your API server gets readr access to the tables it needs. Your analytics service gets read only rights. And your background worker gets access to job Q and nothing else. Least privilege enforced by the secrets engine, not by trust. That's a win. Step three, enable audit logging on every secret access. Who requested credentials? When from which IP address for which service, right? When something goes wrong, you have the full trail to audit, not a guess, a complete log. Dynamic secrets, scoped assets, audit trail, so your blast radius shrinks from infinite to just that one session. So, Oh, how are you managing database credentials right now? Be honest in the comments.

</div>
