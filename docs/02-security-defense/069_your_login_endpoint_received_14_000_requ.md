# Episode 069: Your login endpoint received 14,000 requests last night.

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcRgRM2jjuv/) |

---

## 🚨 1. The Incident & Attack Vector
Your login endpoint received 14,000 requests last night and none of them were your users. Credential stuffing bots hitting your login 200 requests per minute. Scrapers on your pricing page every 3 seconds and automated scanners probing every route for potential vulnerabilities.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
Scrapers on your pricing page every 3 seconds and automated scanners probing every route for potential vulnerabilities. All of it sailing right through Cloudflare, hitting your origin, consuming your compute, and spiking your bill. You have a security layer in front of your application and it's doing nothing because your AI never configured it correctly.

---

## ⚡ 4. Hardening Action Checklist
- [ ] rate limiting rules on authentication endpoints. Your login, registration, and password reset endpoints should never accept more than a defined number of requests per IP per minute.
- [ ] bot management rules on high-v value pages. Your pricing page, your checkout flow, your API documentation.
- [ ] custom WFT rules, known attack patterns, SQL injection attempts and query strings, XSS payloads and form fields, path traversal and URLs. Cloudflare's WFT can catch these at the edge and drop the request before your application ever sees it.

---

## 💻 5. Hardened Production Implementation
```typescript
// Redis Token Bucket Rate Limiter
import { RateLimiterRedis } from 'rate-limiter-flexible';
const rateLimiter = new RateLimiterRedis({
  storeClient: redisClient,
  points: 10,   // 10 requests
  duration: 60, // per 60 seconds
});
await rateLimiter.consume(req.ip);
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Never deploy unverified AI-generated code directly to production without testing failure modes.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your login endpoint received 14,000 requests last night and none of them were your users. Credential stuffing bots hitting your login 200 requests per minute. Scrapers on your pricing page every 3 seconds and automated scanners probing every route for potential vulnerabilities. All of it sailing right through Cloudflare, hitting your origin, consuming your compute, and spiking your bill. You have a security layer in front of your application and it's doing nothing because your AI never configured it correctly. Happens to the best of us. Step one, rate limiting rules on authentication endpoints. Your login, registration, and password reset endpoints should never accept more than a defined number of requests per IP per minute. Not at your application level, at the edge before the request ever reaches your server. So, direct your AI to configure Cloudflare rate limiting rules that block or challenge any IP exceeding thresholds on authentication routes. That is definitely a win. Step two, bot management rules on high-v value pages. Your pricing page, your checkout flow, your API documentation. Bots hit these pages thousands of times every day. Cloudflare can identify automated traffic by behavior fingerprint and challenge or block it before it touches your origin. So, direct your AI to configure bot management rules. that protect high-V value routes from automated scraping and reconnaissance. And number three, custom WFT rules, known attack patterns, SQL injection attempts and query strings, XSS payloads and form fields, path traversal and URLs. Cloudflare's WFT can catch these at the edge and drop the request before your application ever sees it. So direct your AI to deploy custom WFT rules that block the OASP top 10 attack patterns at the Cloudflare edge. You're paying for a wall. Configure it as a wall.

</div>
