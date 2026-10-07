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
| **#004** | Allows public-facing marketing or CMS containers to communicate directly with internal production database subnets. | Isolates container networks into private VPC subnets, requiring mutual TLS (mTLS) and read-only roles for peripheral tools. |
| **#005** | Configures wildcard `Access-Control-Allow-Origin: *` with credentials enabled to silence development CORS errors in production. | Restricts CORS headers to an explicit whitelist of trusted production domains and validates preflight request origins. |
| **#007** | Relies purely on edge WAF rules while concatenating raw strings in application SQL queries, exposing data to injection bypasses. | Enforces parameterized queries via ORM/prepared statements and validates all endpoint inputs using strict Zod schemas. |
| **#009** | Issues long-lived, un-throttled magic login links with open redirect parameters, enabling token theft and phishing redirection. | Issues short-lived (5-10m) single-use magic tokens, locks redirect URLs to whitelisted domains, and rate limits email dispatch. |
| **#011** | Hardcodes unpinned Redis dependency libraries without tracking critical security CVEs or upstream license forks. | Pins cache infrastructure versions to actively maintained community forks (e.g. Valkey) and audits CVE advisories. |
| **#015** | Omits framing protection headers, allowing attackers to transparently embed application forms inside malicious iframes (Clickjacking). | Configures `X-Frame-Options: DENY` and CSP `frame-ancestors 'none'` to block unauthorized iframe embedding across all routes. |
| **#016** | Trusts client-reported timestamps and device clocks for time-sensitive business logic and session expiration. | Computes all lease durations, expirations, and financial timestamps strictly using authoritative server-synchronized UTC clocks. |
| **#017** | Accepts unvalidated URL redirect parameters on login/logout routes (`?redirect=...`), bouncing users to external phishing domains. | Enforces strict destination allowlisting for redirect URLs, rejecting external protocols, double slashes, and path traversal. |
| **#018** | Disables TLS certificate verification (`rejectUnauthorized: false`) in database or internal API connections to bypass cert errors. | Provisions valid CA certificate bundles for all internal database and microservice connections with strict TLS verification. |
| **#020** | Leaves GraphQL introspection queries enabled in production, giving attackers a complete structural schema of private entities. | Disables GraphQL schema introspection in production environments and enforces strict query depth and complexity limits. |
| **#022** | Passes raw database entity objects directly into React Server Components, serializing sensitive fields to the browser wire. | Transforms database results into explicit Data Transfer Objects (DTOs), stripping internal fields before serializing props. |
| **#024** | Exposes security boundaries in 'An attacker just accessed every protected page in your app', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'An attacker just accessed every protected page in your app'. |
| **#026** | Exposes security boundaries in 'An attacker sent a phishing email from your domain', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'An attacker sent a phishing email from your domain'. |
| **#027** | Exposes security boundaries in 'An attacker just skipped your entire form and sent raw data', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'An attacker just skipped your entire form and sent raw data'. |
| **#033** | Exposes security boundaries in 'An attacker just typed a crafted string into your search', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'An attacker just typed a crafted string into your search'. |
| **#035** | Exposes security boundaries in 'Someone just promoted themselves to admin in your app by', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Someone just promoted themselves to admin in your app by'. |
| **#037** | Exposes security boundaries in 'An attacker just grabbed your Google Login authorization', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'An attacker just grabbed your Google Login authorization'. |
| **#047** | Exposes security boundaries in 'Your app just showed a user your database name, your server', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Your app just showed a user your database name, your server'. |
| **#055** | Exposes security boundaries in 'Your mobile app sends every API call in plain text', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Your mobile app sends every API call in plain text'. |
| **#057** | Exposes security boundaries in 'You moved to a VPS for more control', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'You moved to a VPS for more control'. |
| **#058** | Installs untrusted npm packages without automated audit scanning or lockfile verification, allowing malicious code to exfiltrate `process.env`. | Runs automated dependency vulnerability audits (`npm audit` / Snyk), verifies lockfile checksums, and isolates process secrets. |
| **#059** | Exposes security boundaries in 'Your API is configured to accept requests from any origin', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Your API is configured to accept requests from any origin'. |
| **#065** | Runs database without automated WAL archiving, relying on nightly backups that lose up to 24 hours of customer transactions. | Implements continuous Point-In-Time Recovery (PITR) with continuous WAL streaming to offsite cloud storage. |
| **#069** | Exposes security boundaries in 'Your login endpoint received 14,000 requests last night', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Your login endpoint received 14,000 requests last night'. |
| **#078** | Exposes security boundaries in 'Your AI just answered a customer's question with data from', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Your AI just answered a customer's question with data from'. |
| **#080** | Exposes security boundaries in 'An attacker logged into your app at 3 AM from another', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'An attacker logged into your app at 3 AM from another'. |
| **#082** | Exposes security boundaries in 'You cannot learn to shoot content after your product', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'You cannot learn to shoot content after your product'. |
| **#086** | Exposes security boundaries in 'An AI agent breached a company's production database this', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'An AI agent breached a company's production database this'. |
| **#105** | Prefixes database service-role secrets or private API keys with `NEXT_PUBLIC_` or `VITE_`, leaking admin credentials into client bundles. | Keeps secret API keys strictly on server runtimes, accessing backend services through authenticated server API proxies. |
| **#132** | Exposes security boundaries in 'Your API is simultaneously a security surface, a product', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Your API is simultaneously a security surface, a product'. |
| **#167** | Exposes security boundaries in 'Today I am opening The Industry inside The Faction', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Today I am opening The Industry inside The Faction'. |
| **#175** | Exposes security boundaries in 'GitHub Copilot had a CVSS 9.6 remote code execution', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'GitHub Copilot had a CVSS 9.6 remote code execution'. |
| **#187** | Exposes security boundaries in 'Your supply chain is not just npm packages anymore', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Your supply chain is not just npm packages anymore'. |
| **#191** | Exposes security boundaries in 'You deleted the API key from the file', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'You deleted the API key from the file'. |
| **#215** | Exposes security boundaries in 'The first time I ever ran OWASP ZAP on one of my own apps', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'The first time I ever ran OWASP ZAP on one of my own apps'. |
| **#219** | Exposes security boundaries in 'I get the same DM 20-30 times a day', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'I get the same DM 20-30 times a day'. |
| **#226** | Exposes security boundaries in 'One is free', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'One is free'. |
| **#227** | Exposes security boundaries in 'Bots are scanning every public repo for API keys right now', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Bots are scanning every public repo for API keys right now'. |
| **#244** | Exposes security boundaries in 'AI Provider Secret!', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'AI Provider Secret!'. |
| **#249** | Exposes security boundaries in 'OWASP ZAP', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'OWASP ZAP'. |
| **#260** | Exposes security boundaries in 'Same API key for six months', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Same API key for six months'. |
| **#261** | Exposes security boundaries in 'Two users', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Two users'. |
| **#273** | Exposes security boundaries in 'Your app works', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Your app works'. |
| **#282** | Exposes security boundaries in 'Your app is copy-pasted from ChatGPT', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'Your app is copy-pasted from ChatGPT'. |
| **#306** | Exposes security boundaries in '47-item security checklist', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for '47-item security checklist'. |
| **#318** | Exposes security boundaries in '35 CVEs from AI code in March', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for '35 CVEs from AI code in March'. |
| **#322** | Exposes security boundaries in 'AI code 2x more issues. 3x more security vulns. $1.5', trusting client inputs or unvalidated network parameters. | Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for 'AI code 2x more issues. 3x more security vulns. $1.5'. |

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
