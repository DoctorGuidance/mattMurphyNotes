# Episode 242: No gateway…..means your AI endpoint is an open wallet with

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Cloud Infrastructure & FinOps (`معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZYPNahPmpz/) |

---

## 🚨 1. The Incident & Attack Vector
No gateway…..means your AI endpoint is an open wallet with a public URL.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Connects frontend clients directly to AI provider endpoints without a gateway layer, creating an open wallet for billing abuse. | Deploys an AI API gateway (LiteLLM/Portkey) enforcing per-user rate limits, budget ceilings, and caching in front of model calls. |

---

## 💡 3. Root Cause & Architectural Principle
Here are the three things you do right now to fix it. Step one, put an API gateway in front of every AI endpoint. Kong, AWS API gateway, or Cloudflare's API shield all work great.

---

## ⚡ 4. Hardening Action Checklist
- [ ] put an API gateway in front of every AI endpoint.
- [ ] add request validation at the gateway layer.
- [ ] implement per user spend tracking.

---

## 💻 5. Hardened Production Implementation
```typescript
// auth/session.ts
import { Response } from 'express';

export function setSecureSessionCookie(res: Response, token: string) {
  res.cookie('session_token', token, {
    httpOnly: true,                               // Inaccessible to client JS
    secure: process.env.NODE_ENV === 'production', // HTTPS only
    sameSite: 'lax',                              // CSRF protection
    path: '/',
    maxAge: 15 * 60 * 1000                        // 15-minute rotation window
  });
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Three layers fix that.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI endpoint is totally public and anyone with a URL can send it requests and every request costs you real money. One bot, one loop, and one weekend you're not paying attention could be a four figure bill on Monday morning. Here are the three things you do right now to fix it. Step one, put an API gateway in front of every AI endpoint. Kong, AWS API gateway, or Cloudflare's API shield all work great. for this. The gateway handles authentication before requests reach your model. No valid API key. No requests processed. No tokens burned. This is not optional. This is infrastructure. That's a win. Step two, add request validation at the gateway layer. Check payload size. Reject context windows over the limit. Validate input schema before it touches the model. A 100k token prompt from A free tier user should never reach your Opus endpoint ever. The gateway blocks it, your budget survives. That's a win. Step three, implement per user spend tracking. Tag every request with the user ID and log token consumption by user. Set daily and monthly caps per user tier. And free users get 500 tokens per day. Pro users get 50,000. The gateway enforces that cap, not your application code. So gateway, validation, spend caps, those are three important layers between the internet and a big API bill. So tell me what is protecting your AI endpoints right now? Drop it in the comments.

</div>
