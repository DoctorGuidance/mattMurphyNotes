# Episode 022: Your user's full database record is in their browser right

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdZDAYDkr3A/) |

---

## 🚨 1. The Incident & Attack Vector
Your user's full database record is in their browser right now.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Passes raw database entity objects directly into React Server Components, serializing sensitive fields to the browser wire. | Transforms database results into explicit Data Transfer Objects (DTOs), stripping internal fields before serializing props. |

---

## 💡 3. Root Cause & Architectural Principle
The payload contains all 20. Your AI fetched an entire row and let next.js serialize it. So your AI queried the database inside a server component and pass the result as props.

---

## ⚡ 4. Hardening Action Checklist
- [ ] React server components serialize every prop into a wire format the browser parses to build the page.
- [ ] nested components inherit the same props.
- [ ] the RSC payload.

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
> **Production Heuristic:** Audit every Server Component that receives database results. Your UI is a window. The payload is the wall behind it.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI put your user's full database record in the browser right now. Your React server component displays three fields. The payload contains all 20. Your AI fetched an entire row and let next.js serialize it. So your AI queried the database inside a server component and pass the result as props. Well, the component renders a name, an email, and a profile photo. So the browser received the password hash, the internal RO flag and the billing token alongside it. So the server components render on the server, right? But the data they use still travels to the browser. So let's get it fixed. Number one, React server components serialize every prop into a wire format the browser parses to build the page. So your AI passed the full database row because the query was simpler. The component only displays three fields, but the payload will contain all of them that you send. So, an attacker opens the network tab and reads what your UI chose not to show. So, direct your AI to select only the fields the component renders, never a full row. That's a win. Number two, nested components inherit the same props. So, your AI passes the full user object to a parent and three child components each take what they need. So the full object serializes once every field is in the payload. But a leak at the parent level exposes data to every child. So direct your AI to create a data transfer object at each component boundary with only the required fields there. And number three, the RSC payload. It's not HTML. It is a structured format any attacker can parse and extract at scale. 20 users loading the page means 20 full records are being exposed. So direct your AI to audit every server component that receives database results and verify no sensitive field reaches the wire format. Your UI is a window, folks. The payload, it's the wall behind it. If sensitive data is in the wall, someone is definitely going to look. So you got to get it locked down.

</div>
