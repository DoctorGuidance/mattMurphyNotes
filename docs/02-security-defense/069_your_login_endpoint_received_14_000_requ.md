# Episode 069: Your login endpoint received 14,000 requests last night.

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcRgRM2jjuv/) |

---

## 🚨 1. The Incident & Attack Vector
Your login endpoint received 14,000 requests last night. None of them were your users. Credential stuffing, scrapers, vulnerability scanners.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Leaves authentication endpoints vulnerable to credential stuffing attacks by allowing 14,000 un-throttled login requests. | Deploys IP-based and username-based Token Bucket rate limiters backed by Redis with progressive delays and CAPTCHA gates. |

---

## 💡 3. Root Cause & Architectural Principle
Scrapers on your pricing page every 3 seconds and automated scanners probing every route for potential vulnerabilities. All of it sailing right through Cloudflare, hitting your origin, consuming your compute, and spiking your bill. You have a security layer in front of your application and it's doing nothing because your AI never configured it correctly.

---

## ⚡ 4. Hardening Action Checklist
- [ ] rate limiting rules on authentication endpoints.
- [ ] bot management rules on high-v value pages.
- [ ] custom WFT rules, known attack patterns, SQL injection attempts and query strings, XSS payloads and form fields, path traversal and URLs.

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
> **Production Heuristic:** You are paying for a wall. Configure it.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your login endpoint received 14,000 requests last night and none of them were your users. Credential stuffing bots hitting your login 200 requests per minute. Scrapers on your pricing page every 3 seconds and automated scanners probing every route for potential vulnerabilities. All of it sailing right through Cloudflare, hitting your origin, consuming your compute, and spiking your bill. You have a security layer in front of your application and it's doing nothing because your AI never configured it correctly. Happens to the best of us. Step one, rate limiting rules on authentication endpoints. Your login, registration, and password reset endpoints should never accept more than a defined number of requests per IP per minute. Not at your application level, at the edge before the request ever reaches your server. So, direct your AI to configure Cloudflare rate limiting rules that block or challenge any IP exceeding thresholds on authentication routes. That is definitely a win. Step two, bot management rules on high-v value pages. Your pricing page, your checkout flow, your API documentation. Bots hit these pages thousands of times every day. Cloudflare can identify automated traffic by behavior fingerprint and challenge or block it before it touches your origin. So, direct your AI to configure bot management rules. that protect high-V value routes from automated scraping and reconnaissance. And number three, custom WFT rules, known attack patterns, SQL injection attempts and query strings, XSS payloads and form fields, path traversal and URLs. Cloudflare's WFT can catch these at the edge and drop the request before your application ever sees it. So direct your AI to deploy custom WFT rules that block the OASP top 10 attack patterns at the Cloudflare edge. You're paying for a wall. Configure it as a wall.

</div>
