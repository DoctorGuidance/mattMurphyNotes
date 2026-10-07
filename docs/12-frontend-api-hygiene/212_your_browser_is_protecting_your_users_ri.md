# Episode 212: Your browser is protecting your users right now

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Frontend Architecture & API Hygiene (`معماری فرانت‌اند، طراحی واسط و بهداشت API`) |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZ2Z8uKRMw8/) |

---

## 🚨 1. The Incident & Attack Vector
Your browser is protecting your users right now.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes successful network responses and relies solely on frontend validation for business state in 'Your browser is protecting your users right now'. | Implements all 4 UI states, treats client state as untrusted, and verifies payload schemas on both client and server. |

---

## 💡 3. Root Cause & Architectural Principle
Step one, cores cross origin resource sharing. When your front end calls your API on a different domain, the browser blocks it by default. That is not a bug.

---

## ⚡ 4. Hardening Action Checklist
- [ ] cores cross origin resource sharing.
- [ ] CSP, content security policies.
- [ ] set both.

---

## 💻 5. Hardened Production Implementation
```typescript
// middleware/cors.ts
import cors from 'cors';

const ALLOWED_ORIGINS = ['https://app.company.com', 'https://portal.company.com'];

export const secureCors = cors({
  origin: (origin, callback) => {
    if (!origin || ALLOWED_ORIGINS.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Blocked by CORS policy: unauthorized origin'));
    }
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
});
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Trust the browser.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your browser is protecting your users right now and you probably have no idea how. Here are the three things you need to understand right now about browser protection. Step one, cores cross origin resource sharing. When your front end calls your API on a different domain, the browser blocks it by default. That is not a bug. That is a security feature in your favor. Without cores, any website could make requests your API using your user's cookies. When you set force to allow everything. You told the browser, you trust everyone. I don't trust everyone. That's not a configuration. That is surrender, not the win. Step two, CSP, content security policies. This tells the browser what is allowed to run on your page. Without CSP, an injected script tag can load anything from anywhere. With CSP, even if they inject the tag, the browser blocks the execution completely. CSP does not prevent an attack. It prevents the damage. That's a win. Step three, set both. Most builders skip security headers because the app works without them. And it does work. It also works for attackers. 5 minutes of configuration between your users and your entire category of attacks will change. Configure the headers. Trust the browser. That's the only way to rock.

</div>
