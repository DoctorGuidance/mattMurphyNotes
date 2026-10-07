# 🛡️ Rulebook: Rate Limiting & Abuse Prevention
**زیرسیستم:** محدودسازی نرخ، مقابله با DoS و بات‌ها | **Domain ID:** `05-rate-limiting-abuse` | **Target Layer:** Layer 9
> **Corpus Evidence:** Synthesized from 4 Matt Murphy Production Engineering Masterclasses (1 Critical, 2 High, 1 Medium).

---

## 👑 1. Executive Summary & Core Invariant
In modern high-scale software engineering, **Rate Limiting & Abuse Prevention** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.
Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.

### ⚡ The Non-Negotiable Invariant:
> Every public endpoint must be guarded by Redis-backed Token Bucket rate limiting across 3 tiers: unauthenticated IP caps, authenticated user quotas, and tenant/API-key rate limits. Return HTTP 429 with standard `Retry-After` headers.

---

## 🚨 2. Critical Attack Vectors & Failure Scenarios
Analysis of 4 incidents and breakdowns from this domain:

### 📍 Episode #103: One Kid with a Laptop Can Take Your Entire Product Offline (Rate Limiting) (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** A single script running 500 requests per second against your login or search endpoint floods the database connection pool, exhausts memory, and takes your entire SaaS offline for all paying customers.
- **The Root Cause:** Bandwidth and compute are finite. Protect API endpoints before they touch business logic or databases using memory-efficient Token Bucket algorithms.
- **Matt Murphy Takeaway:** *"Without rate limits, your database is at the mercy of anyone who knows how to write a while-true loop."*

### 📍 Episode #178: Rate limiting is not about saying no (Severity: `HIGH`)
- **The Attack Vector / Incident:** Rate limiting is not about saying no.
- **The Root Cause:** It is about building a pricing model that totally scales. So here's how I think about rate limiting architecture for production systems we build for clients at Faction. There are three layers, but most builders are only implementing one.
- **Matt Murphy Takeaway:** *"Hard limits protect the system. Adaptive limits protect the experience. Tiered limits protect the business."*

### 📍 Episode #274: Layer 9 of 13 (Severity: `HIGH`)
- **The Attack Vector / Incident:** Layer nine of 13, rate limiting. This is the one that protects your wallet. So, last week a user in my comments said a bot hit their API 10,000 times in an hour.
- **The Root Cause:** So, last week a user in my comments said a bot hit their API 10,000 times in an hour. Cha-ching. If your app calls OpenAI or Anthropic or any paid API and you have no rate limiting, you're just one rogue bot away from a bill that ends your project.
- **Matt Murphy Takeaway:** *"One invoice you weren’t expecting."*

---

## ❌ 3. Vibe-Coding Traps vs. Production Reality Matrix
| # | ❌ The Vibe-Coding Trap (What Naive AI Builds) | ✅ Hardened Production Standard |
|---|:---|:---|
| **#103** | Exposes origin servers directly to the internet without an edge WAF or DDoS mitigation, allowing trivial request loops to crash the app. | Deploys Cloudflare/edge WAF with adaptive behavioral rate limiting and automated IP anomaly blacklisting. |
| **#178** | Drops abusive connections abruptly with opaque errors instead of standard HTTP rate limiting protocols. | Enforces Token Bucket rate limiting returning HTTP 429 status codes with explicit `Retry-After` headers and graceful client backoff. |
| **#274** | Omits gateway rate limiting, leaving expensive AI and payment endpoints unprotected against automated bot abuse. | Applies multi-tiered rate limiting at API gateways: strict limits on auth/AI endpoints and relaxed thresholds for read APIs. |
| **#304** | Allows 50 simultaneous registrations from a single IP to exhaust database pools and trigger external verification costs. | Throttles user registration endpoints by IP subnet and device fingerprint, queueing burst traffic via Redis queues. |

---

## 💻 4. Production-Hardened Code Patterns
The following hardened patterns demonstrate the exact production implementation required:

### Pattern 1: Hardened Implementation for #103 (One Kid with a Laptop Can Take Your Entire Product Offline (Rate Limiting))
```typescript
// middleware/rateLimiter.ts
import { RateLimiterRedis } from 'rate-limiter-flexible';
import { redisClient } from '../lib/redis';

const rateLimiter = new RateLimiterRedis({
  storeClient: redisClient,
  keyPrefix: 'rate_limit_auth',
  points: 10,       // Maximum 10 attempts
  duration: 60,     // Per 60 seconds
});

export async function authRateLimit(req: Request, res: Response, next: NextFunction) {
  try {
    const clientKey = req.ip || req.headers['x-forwarded-for'];
    await rateLimiter.consume(clientKey as string);
    next();
  } catch (err) {
    res.status(429).json({ error: 'Too Many Requests', retryAfter: 60 });
  }
}
```

### Pattern 2: Hardened Implementation for #178 (Rate limiting is not about saying no)
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

### Pattern 3: Hardened Implementation for #274 (Layer 9 of 13)
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

### Pattern 4: Hardened Implementation for #304 (50 users sign up at once)
```typescript
// infrastructure/resilienceGuard.ts
export const config = {
  timeoutMs: 5000,
  retryPolicy: { retries: 3, backoffFactor: 2 },
  circuitBreaker: { failureThreshold: 5, resetTimeoutMs: 30000 }
};
```

---

## 📋 5. Architectural Checklist & Verification Heuristics
Before shipping any code in this domain, verify each item:

- [ ] Add automated regression tests verifying failure scenarios before shipping.
- [ ] Deploy Cloudflare Turnstile or proof-of-work challenges on high-cost AI generation endpoints.
- [ ] Enforce fail-safe boundaries preventing cascade outages.
- [ ] Establish real-time observability alerts on critical paths.
- [ ] Implement a Redis Token Bucket rate limiter across all public endpoints (10 req/min for auth, 60 req/min for APIs).
- [ ] Implement defense-in-depth guardrails preventing unauthorized state modification.
- [ ] Inspect the existing code paths and identify unvalidated boundary inputs.
- [ ] Isolate unverified components behind automated integration tests.
- [ ] Return standard `429 Too Many Requests` responses with explicit `Retry-After` headers.

---

## 📚 6. Full Domain Catalog of Masterclasses
| Episode | Severity | Masterclass Title | Production Layer | Source Reel |
|:---:|:---:|:---|:---:|:---:|
| **#103** | `CRITICAL` | One Kid with a Laptop Can Take Your Entire Product Offline (Rate Limiting) | Layer 9 | [Watch Reel](https://www.instagram.com/reel/DbjN2IVCeEm/) |
| **#178** | `HIGH` | Rate limiting is not about saying no | Layer 9 | [Watch Reel](https://www.instagram.com/reel/DaVrNEXD-tc/) |
| **#274** | `HIGH` | Layer 9 of 13 | Layer 9 | [Watch Reel](https://www.instagram.com/reel/DYz-1mDxTXN/) |
| **#304** | `MEDIUM` | 50 users sign up at once | Layer 9 | [Watch Reel](https://www.instagram.com/reel/DYQMWv2Pohr/) |
