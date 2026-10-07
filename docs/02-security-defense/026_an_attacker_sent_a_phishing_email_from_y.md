# Episode 026: An attacker sent a phishing email from your domain

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdPTYpBAiuY/) |

---

## 🚨 1. The Incident & Attack Vector
An attacker sent a phishing email from your domain.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends transactional emails without SPF, DKIM, and DMARC DNS records, enabling attackers to spoof domain emails. | Configures strict SPF, DKIM 2048-bit keys, and DMARC `p=reject` policies to ensure verifiable domain email authentication. |

---

## 💡 3. Root Cause & Architectural Principle
It was your own email system, but your AI let them in through a name field. So, your AI integrated resend for transactional emails and drops user input into the template. No sanitization.

---

## ⚡ 4. Hardening Action Checklist
- [ ] a name field should contain a name, not a login button that links to an attacker's fishing page.
- [ ] your template engine allows raw HTML insertion.
- [ ] send an email with angle brackets, link tags, and script tags in every input field.

---

## 💻 5. Hardened Production Implementation
```typescript
// middleware/rateLimiter.ts
import { RateLimiterRedis } from 'rate-limiter-flexible';
import { redisClient } from '../lib/redis';
import { Request, Response, NextFunction } from 'express';

const limiter = new RateLimiterRedis({
  storeClient: redisClient,
  keyPrefix: 'rl_global',
  points: 10,       // Max 10 requests
  duration: 60,     // Per 60 seconds
  blockDuration: 60 // Block for 60s if exceeded
});

export async function rateLimitMiddleware(req: Request, res: Response, next: NextFunction) {
  try {
    await limiter.consume(req.ip);
    next();
  } catch (err) {
    res.status(429).json({ error: 'Rate limit exceeded. Try again in 60s.' });
  }
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Your domain reputation is your business reputation.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

An attacker just sent a fishing email from your domain. SPF passed, DKIM passed, Demar passed. It was your own email system, but your AI let them in through a name field. So, your AI integrated resend for transactional emails and drops user input into the template. No sanitization. So, an attacker types HTML into a form field and resend delivers it from your verified domain. Well, the attacker did not comp compromise your email. Your template just invited them right in. So, let's get this locked down. Step one, a name field should contain a name, not a login button that links to an attacker's fishing page. The fishing email that results is indistinguishable from your legitimate ones because your infrastructure sent it to them. It's your domain. It's your sender reputation. It's your SPF record all confirming that it was real. So, one form field that accepts markup turns your entire email system into a fishing platform for attackers. So, direct your AI to sanitize every user input before it enters any template at all. Strip the HTML, escape special characters. That's a win. Step two, your template engine allows raw HTML insertion. User content should never use that path. Data gets displayed, markup gets executed. So, a password reset email that renders user input as HTML is an email and a attacker can turn into anything they want. So, you need to direct your AI to render user content as plain text, never as raw HTML. That's a win. And step three, send an email with angle brackets, link tags, and script tags in every input field. If any of them render as a clickable link instead of a plain text, your template is fully injectable. This test will take you 30 seconds. And the alternative is finding out when a customer clicks a fishing link that contain a domain that you sent them. So, direct your AI to test every single template. Your domain reputation is your business reputation, and one injectable template burns both to the ground. That's not a win. Get it fixed.

</div>
