# Episode 005: An Attacker Read Your User's Private Data via Permissive CORS

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Ddyy2G3kwC7/) |

---

## 🚨 1. The Incident & Attack Vector
An AI scaffolding tool configured CORS with `Access-Control-Allow-Origin: *`. An authenticated user visits an attacker's website; the malicious site sends a fetch request to your API with credentials, and the browser happily returns the user's private data.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Configures wildcard `Access-Control-Allow-Origin: *` with credentials enabled to silence development CORS errors in production. | Restricts CORS headers to an explicit whitelist of trusted production domains and validates preflight request origins. |

---

## 💡 3. Root Cause & Architectural Principle
CORS is the browser's defense perimeter protecting your users. Never trust every origin on the public internet on authenticated endpoints.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Remove all wildcard `*` values from `Access-Control-Allow-Origin` in production.
- [ ] Implement an explicit whitelist checking against your trusted web app domains.
- [ ] Ensure credentials flag (`credentials: true`) is only enabled on strictly whitelisted domains.

---

## 💻 5. Hardened Production Implementation
```typescript
// middleware/cors.ts
import cors from 'cors';

const ALLOWED_ORIGINS = ['https://app.yourdomain.com', 'https://yourdomain.com'];

export const secureCors = cors({
  origin: (origin, callback) => {
    if (!origin || ALLOWED_ORIGINS.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Blocked by CORS policy'));
    }
  },
  credentials: true,
});
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Your API shouldn't trust every domain on the internet just to silence a local console error.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI configured cores on your API. The browser asked which origins are allowed and your server said all of them. So an attacker just read your user's private data from a completely different website. Your course policy allowed it. So your API trusts every origin on the internet because your AI set access control allow origin to the wild card. An API that trusts every origin trusts the Attackers origin too. So here are three steps to get it fixed. Step one, the wildcard header tells every browser that any website can read responses from your API. So an attacker hosts a page that makes requests to your API using your user's cookies. The browser sends the credentials. Your API returns the data and the attacker's page reads it. So your user never leaves the attacker's website. You need to direct your AI to Replace the wild card with an explicit allow list of your own domains. That is the win. Step two, your AI may have added access control allow credentials alongside the wild card. This tells the browser to include cookies with cross origin requests. The wild card with credentials is the most dangerous course configuration possible. Don't do it. Every website on the internet can make authenticated requests. to your API and read the full response. So, direct your AI to set credentials to true only when the origin header matches your allow list. That's a win. And step three, your API reflects the origin header back as the access control allow origin value without checking it. This is functionally identical to a wild card, but passes automated scans that flag wild cards. So, an attacker that's their origin, your API echoes it back and the browser fully trusts it. So direct your AI to validate the origin header against a hard-coded allow list before reflecting it. Your API has a guest list. Right now everyone is on it and that is not a win.

</div>
