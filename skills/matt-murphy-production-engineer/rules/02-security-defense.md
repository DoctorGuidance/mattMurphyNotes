# 🛡️ Rulebook: Application Security & Defense
**زیرسیستم:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای | **Domain ID:** `02-security-defense` | **Target Layer:** Layer 8
> **Corpus Evidence:** Synthesized from 47 Matt Murphy Production Engineering Masterclasses (28 Critical, 6 High, 13 Medium).

---

## 👑 1. Executive Summary & Core Invariant
In modern high-scale software engineering, **Application Security & Defense** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.
Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.

### ⚡ The Non-Negotiable Invariant:
> Zero secrets in client code or frontend bundles. No wildcard CORS (`*`) on authenticated APIs. Clickjacking frames must be blocked via CSP `frame-ancestors 'none'`. All user inputs crossing system boundaries must be strictly sanitized and parameterized to prevent injection.

---

## 🚨 2. Critical Attack Vectors & Failure Scenarios
Analysis of 47 incidents and breakdowns from this domain:

### 📍 Episode #004: Lateral Movement: From Compromised Marketing Tool to Production Database (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** An attacker exploits a known vulnerability in a third-party marketing container. Because all containers share an unsegmented flat Docker network, the attacker pivots to the admin API and reads database credentials from environment variables.
- **The Root Cause:** Zero-trust network architecture: Network location does not equal authorization. Apply network isolation and the principle of least privilege so a breach in one container isolates the damage.
- **Matt Murphy Takeaway:** *"One breach should give an attacker one compromised container—never your entire infrastructure."*

### 📍 Episode #005: An Attacker Read Your User's Private Data via Permissive CORS (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** An AI scaffolding tool configured CORS with `Access-Control-Allow-Origin: *`. An authenticated user visits an attacker's website; the malicious site sends a fetch request to your API with credentials, and the browser happily returns the user's private data.
- **The Root Cause:** CORS is the browser's defense perimeter protecting your users. Never trust every origin on the public internet on authenticated endpoints.
- **Matt Murphy Takeaway:** *"Your API shouldn't trust every domain on the internet just to silence a local console error."*

### 📍 Episode #009: An attacker intercepted your magic link and landed inside (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** An attacker intercepted your magic link and landed inside your user's dashboard.
- **The Root Cause:** So, the user enters their email, your server, generates a signed token, embeds it in a URL, and emails it out. The user clicks and authenticates the URL includes a redirect parameter your AI never locked down. So let's get it locked down.
- **Matt Murphy Takeaway:** *"Your magic link removes the password. It should not remove the security."*

### 📍 Episode #018: An attacker just used a password reset link from four (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** An attacker just used a password reset link from four months ago.
- **The Root Cause:** Uh-oh. Your user change their password twice since then, but the old link still logs them in. So, your AI built a password reset flow.
- **Matt Murphy Takeaway:** *"Your password reset is a door. Your AI built it without a lock."*

### 📍 Episode #022: Your user's full database record is in their browser right (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your user's full database record is in their browser right now.
- **The Root Cause:** The payload contains all 20. Your AI fetched an entire row and let next.js serialize it. So your AI queried the database inside a server component and pass the result as props.
- **Matt Murphy Takeaway:** *"Audit every Server Component that receives database results. Your UI is a window. The payload is the wall behind it."*

### 📍 Episode #024: An attacker just accessed every protected page in your app (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** An attacker just accessed every protected page in your app without logging in.
- **The Root Cause:** So your AI added authentication in middleware, one file, every route protected, right? But middleware does not run on every single request type. So some pass can bypass it entirely.
- **Matt Murphy Takeaway:** *"Middleware is a convenience layer. If it is your only check, it is your weakest one."*

### 📍 Episode #026: An attacker sent a phishing email from your domain (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** An attacker sent a phishing email from your domain.
- **The Root Cause:** It was your own email system, but your AI let them in through a name field. So, your AI integrated resend for transactional emails and drops user input into the template. No sanitization.
- **Matt Murphy Takeaway:** *"Your domain reputation is your business reputation."*

### 📍 Episode #033: An attacker just typed a crafted string into your search (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** An attacker just typed a crafted string into your search field and your database returned every user's credentials.
- **The Root Cause:** Your AI dropped into raw SQL and removed every protection that Prisma provides. So, your AI needed a complex join or a search feature. Prisma's standard methods could not handle it.
- **Matt Murphy Takeaway:** *"The ORM is not the vulnerability. The one place your AI bypassed it is."*

### 📍 Episode #035: Someone just promoted themselves to admin in your app by (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Someone just promoted themselves to admin in your app by editing one field in a JWT.
- **The Root Cause:** So your AI integrated clerk and reads the jot file to check the roles, but it never verifies the signature and it never checks the expiration. So a modified token passes your middleware without any challenge at all. Here's how you're going to direct your AI to verify every token.
- **Matt Murphy Takeaway:** *"Your auth provider did its job. Your AI never verified its work."*

### 📍 Episode #055: Your mobile app sends every API call in plain text (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your mobile app sends every API call in plain text.
- **The Root Cause:** So your user opens your app at a coffee shop. Every request between the app and your server crosses the network where anyone on that Wi-Fi can read it. Login credentials, session tokens, personal data.
- **Matt Murphy Takeaway:** *"Fix the transport before your users pay for it."*

---

## ❌ 3. Vibe-Coding Traps vs. Production Reality Matrix
| # | ❌ The Vibe-Coding Trap (What Naive AI Builds) | ✅ Hardened Production Standard |
|---|:---|:---|
| **#004** | Runs all services (marketing, admin API, database) inside a single flat network where everything trusts everything. | Strict network segmentation: marketing cannot reach database networks; internal service calls require mTLS or auth tokens. |
| **#005** | Sets CORS to wildcard `*` to eliminate developer console errors during local development. | Explicit domain whitelist for allowed origins with credentials verification; rejects unauthorized origins. |
| **#007** | Treats WAF as a substitute for secure coding; leaves default rule sets uncalibrated for application endpoints. | Defense-in-depth: parameterized queries and strict schema validation in code, combined with tuned WAF blocking rules. |
| **#009** | Leaves endpoints open without rate limiting, allowing scrapers or brute-force bots to drain resources. | Implements token bucket rate limiting at gateway level, throttling abusive IPs with exponential backoff. |
| **#011** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#015** | Omits frame-protection headers, allowing any malicious web page to embed your application. | Emits `X-Frame-Options: DENY` and CSP `frame-ancestors 'none'` to block unauthorized framing at the browser level. |
| **#016** | Stores credentials in client-side localStorage/sessionStorage vulnerable to XSS and malicious dependencies. | Stores tokens in HttpOnly, Secure, SameSite=Lax cookies completely inaccessible to JavaScript. |
| **#017** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#018** | Leaves endpoints open without rate limiting, allowing scrapers or brute-force bots to drain resources. | Implements token bucket rate limiting at gateway level, throttling abusive IPs with exponential backoff. |
| **#020** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#022** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#024** | Stores credentials in client-side localStorage/sessionStorage vulnerable to XSS and malicious dependencies. | Stores tokens in HttpOnly, Secure, SameSite=Lax cookies completely inaccessible to JavaScript. |
| **#026** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#027** | Blindly passes entire request body to ORM update methods, allowing attackers to inject `isAdmin: true` or elevated roles. | Enforces strict input allowlists using Zod schemas (`.strict()`), rejecting any non-whitelisted parameters. |
| **#033** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#035** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#037** | Configures wildcard `Access-Control-Allow-Origin: *` with credentials enabled, exposing authenticated APIs. | Enforces strict origin allowlists and explicit pre-flight inspection for production APIs. |
| **#047** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#055** | Blindly passes entire request body to ORM update methods, allowing attackers to inject `isAdmin: true` or elevated roles. | Enforces strict input allowlists using Zod schemas (`.strict()`), rejecting any non-whitelisted parameters. |
| **#057** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#058** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#059** | Configures wildcard `Access-Control-Allow-Origin: *` with credentials enabled, exposing authenticated APIs. | Enforces strict origin allowlists and explicit pre-flight inspection for production APIs. |
| **#065** | Blindly passes entire request body to ORM update methods, allowing attackers to inject `isAdmin: true` or elevated roles. | Enforces strict input allowlists using Zod schemas (`.strict()`), rejecting any non-whitelisted parameters. |
| **#069** | Configures wildcard `Access-Control-Allow-Origin: *` with credentials enabled, exposing authenticated APIs. | Enforces strict origin allowlists and explicit pre-flight inspection for production APIs. |
| **#078** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#080** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#082** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#086** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#105** | Prefixes administrative secrets with client-visible environment flags to make queries work quickly. | Strict segregation of server secrets; automated pre-commit scanners (Trufflehog) blocking secret commits. |
| **#132** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#167** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#175** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#187** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#191** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#215** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#219** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#226** | Relies on unverified AI code assumptions without failure handling or production boundaries in Application Security & Defense. | Applies hardened architectural patterns, strict input boundaries, and automated monitoring for Application Security & Defense. |
| **#227** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#244** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#249** | Filters tenant data in frontend or application code, leaking records across accounts on missed WHERE clauses. | Enforces Row-Level Security (RLS) directly in PostgreSQL, guaranteeing zero cross-tenant data leakage. |
| **#260** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#261** | Relies on unverified AI code assumptions without failure handling or production boundaries in Application Security & Defense. | Applies hardened architectural patterns, strict input boundaries, and automated monitoring for Application Security & Defense. |
| **#273** | Relies on unverified AI code assumptions without failure handling or production boundaries in Application Security & Defense. | Applies hardened architectural patterns, strict input boundaries, and automated monitoring for Application Security & Defense. |
| **#282** | Relies on unverified AI code assumptions without failure handling or production boundaries in Application Security & Defense. | Applies hardened architectural patterns, strict input boundaries, and automated monitoring for Application Security & Defense. |
| **#306** | Launches AI-generated apps with zero security checks, exposing unpatched CVEs and raw injection paths. | Executes rigorous 47-point enterprise security audit covering auth, headers, rate limits, and encryption. |
| **#318** | Launches AI-generated apps with zero security checks, exposing unpatched CVEs and raw injection paths. | Executes rigorous 47-point enterprise security audit covering auth, headers, rate limits, and encryption. |
| **#322** | Launches AI-generated apps with zero security checks, exposing unpatched CVEs and raw injection paths. | Executes rigorous 47-point enterprise security audit covering auth, headers, rate limits, and encryption. |

---

## 💻 4. Production-Hardened Code Patterns
The following hardened patterns demonstrate the exact production implementation required:

### Pattern 1: Hardened Implementation for #004 (Lateral Movement: From Compromised Marketing Tool to Production Database)
```typescript
# docker-compose.prod.yml - Network Segmentation
version: '3.8'
networks:
  public_net:
  private_net:
    internal: true # No direct route to public internet or marketing

services:
  marketing_tool:
    image: marketing:latest
    networks: [public_net] # Cannot reach private_net

  database:
    image: postgres:16
    networks: [private_net] # Completely isolated
```

### Pattern 2: Hardened Implementation for #005 (An Attacker Read Your User's Private Data via Permissive CORS)
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

### Pattern 3: Hardened Implementation for #007 (An Attacker Walked Straight Through Your Application Firewall (WAF))
```typescript
// schemas/inputValidation.ts
import { z } from 'zod';

export const userSearchSchema = z.object({
  query: z.string().min(1).max(100).regex(/^[a-zA-Z0-9 _-]+$/),
  page: z.number().int().min(1).default(1),
});
```

### Pattern 4: Hardened Implementation for #009 (An attacker intercepted your magic link and landed inside)
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

## 📋 5. Architectural Checklist & Verification Heuristics
Before shipping any code in this domain, verify each item:

- [ ] Apply least-privilege permissions: containers that only serve marketing content must have read-only roles.
- [ ] Ensure credentials flag (`credentials: true`) is only enabled on strictly whitelisted domains.
- [ ] Implement an explicit whitelist checking against your trusted web app domains.
- [ ] Implement schema validation (Zod/Valibot) on every API endpoint before processing inputs.
- [ ] Remove all wildcard `*` values from `Access-Control-Allow-Origin` in production.
- [ ] Require service tokens or mutual TLS (mTLS) for all internal service-to-service API calls.
- [ ] Segment your container networks so front-facing marketing tools cannot physically reach database subnets.
- [ ] Tune WAF rules to block abnormal payload encodings and enforce strict rate limits on search endpoints.
- [ ] Use parameterized SQL queries (Prisma/Drizzle/Prepared Statements) to make SQL injection mathematically impossible.
- [ ] an attacker who discovers the Magic Link endpoint can request thousands of links per minute for any email address.
- [ ] magic link tokens that do not expire remain valid indefinitely in users email.
- [ ] your magic link URL includes a redirect parameter that tells the application where to send the user after authentication.

---

## 📚 6. Full Domain Catalog of Masterclasses
| Episode | Severity | Masterclass Title | Production Layer | Source Reel |
|:---:|:---:|:---|:---:|:---:|
| **#004** | `CRITICAL` | Lateral Movement: From Compromised Marketing Tool to Production Database | Layer 8 | [Watch Reel](https://www.instagram.com/reel/Dd1Xt-zETRJ/) |
| **#005** | `CRITICAL` | An Attacker Read Your User's Private Data via Permissive CORS | Layer 8 | [Watch Reel](https://www.instagram.com/reel/Ddyy2G3kwC7/) |
| **#007** | `HIGH` | An Attacker Walked Straight Through Your Application Firewall (WAF) | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdtpUHxiirn/) |
| **#009** | `CRITICAL` | An attacker intercepted your magic link and landed inside | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdrEewmD01_/) |
| **#011** | `MEDIUM` | An attacker exploited a known vulnerability in your caching | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdoftC9DnTP/) |
| **#015** | `HIGH` | Clickjacking: An Attacker Embedded Your App Inside Their Iframe | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdjWI7CDKC3/) |
| **#016** | `MEDIUM` | An attacker just logged in as your user without a password | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdgxTr7AcvO/) |
| **#017** | `MEDIUM` | An attacker just used your login page to send your users to | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdewD5fFOjE/) |
| **#018** | `CRITICAL` | An attacker just used a password reset link from four | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdeMk-bFdui/) |
| **#020** | `HIGH` | An attacker just downloaded your entire API schema | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdbnwpOiEZJ/) |
| **#022** | `CRITICAL` | Your user's full database record is in their browser right | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdZDAYDkr3A/) |
| **#024** | `CRITICAL` | An attacker just accessed every protected page in your app | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdWeKvGDz5k/) |
| **#026** | `CRITICAL` | An attacker sent a phishing email from your domain | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdPTYpBAiuY/) |
| **#027** | `MEDIUM` | An attacker just skipped your entire form and sent raw data | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdOvuLgiUiv/) |
| **#033** | `CRITICAL` | An attacker just typed a crafted string into your search | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdHBY76jE2o/) |
| **#035** | `CRITICAL` | Someone just promoted themselves to admin in your app by | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdEcldEktWP/) |
| **#037** | `MEDIUM` | An attacker just grabbed your Google Login authorization | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DdB32a5lOZF/) |
| **#047** | `HIGH` | Your app just showed a user your database name, your server | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DcybEeAEhP8/) |
| **#055** | `CRITICAL` | Your mobile app sends every API call in plain text | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DcoH5avEj3J/) |
| **#057** | `CRITICAL` | You moved to a VPS for more control | Layer 8 | [Watch Reel](https://www.instagram.com/reel/Dci-Qq_j9EL/) |
| **#058** | `CRITICAL` | You installed an npm package last week. It has been sending | Layer 8 | [Watch Reel](https://www.instagram.com/reel/Dcg9G7PjY6E/) |
| **#059** | `CRITICAL` | Your API is configured to accept requests from any origin | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DcgZbSGgZ9z/) |
| **#065** | `CRITICAL` | Someone sent a forged request to your API last Tuesday | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DcYrFHSAOhJ/) |
| **#069** | `CRITICAL` | Your login endpoint received 14,000 requests last night. | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DcRgRM2jjuv/) |
| **#078** | `HIGH` | Your AI just answered a customer's question with data from | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DcGpmHHCug1/) |
| **#080** | `CRITICAL` | An attacker logged into your app at 3 AM from another | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DcEEyocD8II/) |
| **#082** | `MEDIUM` | You cannot learn to shoot content after your product | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DcBf7guDXSF/) |
| **#086** | `CRITICAL` | An AI agent breached a company's production database this | Layer 8 | [Watch Reel](https://www.instagram.com/reel/Db8WTQLke0j/) |
| **#105** | `CRITICAL` | 7 Out of 10 Audits Had API Keys Committed to Client Bundles | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DbgDhezjelJ/) |
| **#132** | `MEDIUM` | Your API is simultaneously a security surface, a product | Layer 8 | [Watch Reel](https://www.instagram.com/reel/Da-xLx0GH9f/) |
| **#167** | `MEDIUM` | Today I am opening The Industry inside The Faction | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DadSreribrB/) |
| **#175** | `HIGH` | GitHub Copilot had a CVSS 9.6 remote code execution | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DaYKQ7-E6KB/) |
| **#187** | `CRITICAL` | Your supply chain is not just npm packages anymore | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DaN7bWAm8Qm/) |
| **#191** | `CRITICAL` | You deleted the API key from the file | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DaJQlPhFeqw/) |
| **#215** | `CRITICAL` | The first time I ever ran OWASP ZAP on one of my own apps | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DZyEXA6vDXs/) |
| **#219** | `MEDIUM` | I get the same DM 20-30 times a day | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DZs7Ci8v5Yc/) |
| **#226** | `MEDIUM` | One is free | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DZnuuTpPBWi/) |
| **#227** | `CRITICAL` | Bots are scanning every public repo for API keys right now | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DZnYDewRV_h/) |
| **#244** | `CRITICAL` | AI Provider Secret! | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DZVg8UXv1rA/) |
| **#249** | `CRITICAL` | OWASP ZAP | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DZQU76-x-1G/) |
| **#260** | `CRITICAL` | Same API key for six months | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DZGYLpLPDR-/) |
| **#261** | `MEDIUM` | Two users | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DZFdS70R9Pv/) |
| **#273** | `MEDIUM` | Your app works | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DY0Q3_bP708/) |
| **#282** | `MEDIUM` | Your app is copy-pasted from ChatGPT | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DYqS9GuN8qd/) |
| **#306** | `CRITICAL` | 47-item security checklist | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DYNbDGTvGdj/) |
| **#318** | `CRITICAL` | 35 CVEs from AI code in March | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DX1owcTgr3i/) |
| **#322** | `CRITICAL` | AI code 2x more issues. 3x more security vulns. $1.5 | Layer 8 | [Watch Reel](https://www.instagram.com/reel/DWrjbaTETY7/) |
