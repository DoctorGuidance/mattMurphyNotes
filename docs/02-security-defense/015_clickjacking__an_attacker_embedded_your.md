# Episode 015: Clickjacking: An Attacker Embedded Your App Inside Their Iframe

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdjWI7CDKC3/) |

---

## 🚨 1. The Incident & Attack Vector
An attacker embeds your authenticated dashboard inside a transparent iframe on their phishing website. When users click an innocent-looking button on the overlay, they unknowingly trigger actions (like deleting accounts or transferring funds) inside your app.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Omits frame-protection headers, allowing any malicious web page to embed your application. | Emits `X-Frame-Options: DENY` and CSP `frame-ancestors 'none'` to block unauthorized framing at the browser level. |

---

## 💡 3. Root Cause & Architectural Principle
Browsers protect against UI redressing only when instructed by the origin server. Explicitly forbid framing using standard security response headers.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Set `X-Frame-Options: DENY` on all HTTP responses.
- [ ] Configure modern Content Security Policy with `frame-ancestors 'none'`.
- [ ] Verify framing protection on all sensitive action pages and settings views.

---

## 💻 5. Hardened Production Implementation
```typescript
// middleware/securityHeaders.ts
import { Request, Response, NextFunction } from 'express';

export function frameProtectionHeaders(req: Request, res: Response, next: NextFunction) {
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('Content-Security-Policy', "frame-ancestors 'none'");
  next();
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** If you don't forbid iframes, someone else will design the UI your users actually click on.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your users are clicking buttons on your app while looking at an attacker's website. All because an attacker embedded an entire application inside of your website. Purchases, transfers, permission changes, all triggered by invisible clicks. So, your AI deployed your application without the one thing that prevents framing. So, any website can load your app inside of an invisible iframe and overlay their own buttons on top of yours. So users can't attack what they can't see, but an attacker makes them click what they cannot see. And that's the trick. We need to get it shut down. Step one, the attacker builds a page with a prize, a game, or a form. Behind it, your application loads in a transparent iframe. So the user clicks what they think is an attacker's button in a game, but they're actually clicking your app, a purchase confirmation, a permission grant, or a password change. They never see your application at all. Their browser executed the action because they are already logged into your system. So, direct your AI to add the X-Frame options header and set deny on every single response. That's a win. Step two, X-Frame options is the legacy protection content security policy frame. Ancestors is the modern replacement and gives you more control. Try it out. You can allow your own domain to frame itself while blocking everyone else. Both headers should be present because older browsers only support X-frame options. So direct your AI to set both headers. X-frame options deny and content security policy frame ancestors to self. That's the win. And three, your application may intentionally use Iframes for embedded widgets, payment forms or third party integrations. Those iframes, they need framing. Your main application doesn't. So your AI may have skipped the header because one feature requires framing and the blanket restriction would have broken it. So direct your AI to set frame ancestors on a per route basis. This allows framing only on the specific endpoints that require it. One header, two versions, every resp. response. That's all it takes for a win.

</div>
