# 🛡️ Rulebook: Application Security & Defense
**Architectural Domain:** Application Security & Defense | **Domain ID:** `02-security-defense` | **Target Layer:** Layer 8
> **Corpus Evidence:** Synthesized from 49 Matt Murphy Production Engineering Masterclasses (30 Critical, 6 High, 13 Medium).

---

## 👑 1. Executive Summary & Core Invariant
In modern high-scale software engineering, **Application Security & Defense** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.
Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.

### ⚡ The Non-Negotiable Invariant:
> Zero secrets in client code or frontend bundles. No wildcard CORS (`*`) on authenticated APIs. Clickjacking frames must be blocked via CSP `frame-ancestors 'none'`. All user inputs crossing system boundaries must be strictly sanitized and parameterized to prevent injection.

---

## 🚨 2. Critical Attack Vectors & Failure Scenarios
Analysis of 49 incidents and breakdowns from this domain:

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
| **#011** | Hardcodes unpinned Redis dependency libraries without tracking critical security CVEs or upstream license forks. | Pins exact dependency versions with hash integrity locks and automates Dependabot/Snyk security vulnerability scanning in CI. |
| **#015** | Omits iframe clickjacking protection headers, allowing phishing sites to embed the authenticated UI inside transparent frames. | Enforces `X-Frame-Options: DENY` and `Content-Security-Policy: frame-ancestors 'none'` on all authenticated HTTP responses. |
| **#016** | Retains existing session identifiers across authentication transitions (Session Fixation), enabling session hijacking. | Regenerates session IDs on every privilege change using `req.session.regenerate()` with Secure, HttpOnly, and SameSite flags. |
| **#017** | Accepts unvalidated redirect destinations in query parameters, enabling attackers to route users to external phishing portals. | Validates post-action redirect paths against an explicit relative route allowlist, rejecting scheme-relative URLs (`//`). |
| **#018** | Issues permanent, multi-use password reset tokens without expiration or post-consumption invalidation. | Enforces 15-minute token TTLs, single-use invalidation, and throttles password reset dispatches to 3 requests per hour. |
| **#020** | Leaves GraphQL introspection endpoints enabled in production, giving attackers a complete structural blueprint of the API. | Disables GraphQL schema introspection in production environments and enforces strict query depth/complexity limits. |
| **#022** | Passes raw database entity objects directly into React Server Components, serializing sensitive fields to the browser wire. | Transforms database results into explicit Data Transfer Objects (DTOs), stripping internal fields before serializing props. |
| **#024** | Relies exclusively on edge middleware route matchers for authorization, leaving endpoints exposed to URL normalization bypasses. | Enforces defense-in-depth authorization checks inside individual route handlers and database queries, not just at middleware boundaries. |
| **#026** | Sends transactional emails without SPF, DKIM, and DMARC DNS records, enabling attackers to spoof domain emails. | Configures strict SPF, DKIM 2048-bit keys, and DMARC `p=reject` policies to ensure verifiable domain email authentication. |
| **#027** | Relies solely on frontend HTML form validation attributes, trusting raw HTTP requests submitted directly to API handlers. | Enforces identical server-side input schema validation using Zod/Valibot on all incoming API request payloads. |
| **#033** | Concatenates user search input directly into raw database query strings, opening critical SQL/NoSQL injection vulnerabilities. | Uses parameterized queries and typed ORM builders exclusively, treating all user inputs as non-executable literal data. |
| **#035** | Allows users to pass arbitrary role fields in signup or profile updates, allowing self-promotion to administrator status. | Isolates role assignments to dedicated internal administrative workflows, stripping role fields from public mutation schemas. |
| **#037** | Implements OAuth authorization code exchanges without validating PKCE code verifiers or cross-site state parameters. | Enforces PKCE (RFC 7636) code challenges and cryptographically signed state parameters on all third-party OAuth integrations. |
| **#047** | Returns raw database error stack traces and internal file paths to users upon unhandled server exceptions. | Sanitizes error responses into generic user messages while routing full diagnostic stack traces to centralized Sentry trackers. |
| **#055** | Communicates with mobile app backends over unencrypted HTTP or without TLS certificate pinning, exposing mobile traffic to interception. | Enforces HTTPS with TLS 1.3 and implements certificate pinning in mobile apps to prevent man-in-the-middle proxy inspection. |
| **#057** | Leaves VPS root SSH access enabled with default passwords and open administrative ports on public IP addresses. | Hardens Linux VPS hosts: disables root SSH, enforces key-based authentication, configures UFW firewalls, and enables Fail2ban. |
| **#058** | Installs unvetted npm packages that execute malicious postinstall scripts or exfiltrate `process.env` credentials at runtime. | Audits dependencies using `npm audit`, runs untrusted packages in restricted sandboxes, and verifies lockfile integrity in CI. |
| **#059** | Echoes back incoming request origins in `Access-Control-Allow-Origin` headers, rendering CORS protections completely useless. | Validates incoming origins against an explicit static allowlist before setting access control response headers. |
| **#065** | Accepts state-modifying POST requests without Cross-Site Request Forgery (CSRF) tokens on cookie-authenticated sessions. | Implements Double Submit Cookie patterns or SameSite=Strict cookie policies to neutralize cross-site request forgery. |
| **#069** | Leaves authentication endpoints vulnerable to credential stuffing attacks by allowing 14,000 un-throttled login requests. | Deploys IP-based and username-based Token Bucket rate limiters backed by Redis with progressive delays and CAPTCHA gates. |
| **#078** | Feeds un-redacted multi-tenant databases into customer-facing LLMs, leaking peer customer data through prompt completions. | Enforces strict data masking, tenant isolation filters, and prompt boundaries before feeding context into LLM generation. |
| **#080** | Allows logins from unprecedented geolocations without requiring step-up verification or alerting account owners. | Calculates risk scores based on IP reputation, device fingerprints, and impossible travel velocity, requiring step-up MFA challenges. |
| **#082** | Postpones founder-led video distribution until after product launch, launching to zero audience and zero distribution velocity. | Builds distribution channels and founder video cadences simultaneously alongside product engineering before launch day. |
| **#086** | Grants autonomous AI agents unrestricted read/write database credentials, risking catastrophic hallucinated record destruction. | Restricts AI agents to least-privilege read-only replicas and scopes mutation capabilities through hardened API contracts. |
| **#105** | Exposes private database credentials, Stripe secret keys, and third-party tokens by committing them to public git repositories. | Automates secret scanning in CI with Gitleaks/Trufflehog and stores production credentials exclusively in environment vaults. |
| **#132** | Treats APIs solely as frontend data conduits without recognizing them as the primary attack surface requiring continuous defense. | Architects APIs with defense-in-depth: edge rate limiting, schema validation, least-privilege scoping, and audit telemetry. |
| **#167** | Operates without community peer review or senior engineering oversight, shipping known security anti-patterns into production. | Subject architectures to structured peer audits, threat modeling, and senior production engineering code reviews. |
| **#175** | Allows AI coding assistants to execute unsanitized bash commands or file modifications directly on local developer machines. | Runs untrusted AI-generated terminal scripts inside containerized developer sandboxes with constrained network access. |
| **#187** | Installs unverified Model Context Protocol (MCP) servers with unrestricted file system and environment variable access. | Audits MCP server source code, applies least-privilege operating system permissions, and restricts tool execution capabilities. |
| **#191** | Removes exposed secrets from source code via git commits without purging historical commits or revoking compromised keys. | Revokes leaked credentials immediately at the provider, rotates secrets, and purges git commit history with BFG Repo-Cleaner. |
| **#215** | Deploys web applications to production without running automated dynamic application security testing (DAST) tools. | Integrates OWASP ZAP dynamic vulnerability scanning into CI/CD pipelines to detect injection and header flaws before release. |
| **#219** | Builds ad-hoc security mechanisms in application code instead of leveraging battle-tested security framework primitives. | Standardizes security defenses on proven industry frameworks, avoiding brittle custom security implementations. |
| **#226** | Relies on free unmaintained security plugins that introduce transitive vulnerabilities and silent security failures. | Audits and minimizes third-party security plugins, adopting native framework defenses with active security maintenance. |
| **#227** | Leaves public repositories unmonitored for accidental secret commits, allowing automated crawler bots to steal keys in seconds. | Installs pre-commit Git hooks (TruffleHog/git-secrets) that block commits containing API keys, private certificates, or tokens. |
| **#244** | Stores AI provider API keys in raw `.env` files committed to repository roots and packaged into Docker build artifacts. | Injects AI provider credentials at runtime via secure secret managers (AWS SSM/Doppler) without baking them into images. |
| **#249** | Postpones vulnerability scanning until after security incidents occur, lacking continuous automated compliance verification. | Runs automated container, dependency, and dynamic endpoint vulnerability scans on every merge to production branches. |
| **#260** | Maintains the identical static production API secret key for months without rotation schedules or breach contingency plans. | Automates 90-day secret rotation pipelines supporting dual-key grace periods to prevent service disruption during rotation. |
| **#261** | Shares database user credentials across multiple microservices, granting lateral access if any single service is breached. | Provisions distinct database credentials and scoped schema permissions for every microservice to enforce defense-in-depth. |
| **#273** | Deploys code under the naive assumption that lack of reported attacks implies adequate production security posture. | Adopts zero-trust architectural principles: assumes breach, verifies explicitly, and limits blast radius at every boundary. |
| **#282** | Copies code snippets directly from LLMs into production without validating cryptographic safety or input boundaries. | Audits every AI-generated component against secure coding guidelines, enforcing strict validation and sanitization. |
| **#306** | Launches production applications without performing structured pre-launch security audits against standard threat vectors. | Verifies production readiness against a comprehensive 47-point security checklist covering identity, data, and compute. |
| **#318** | Ignores newly disclosed Common Vulnerabilities and Exposures (CVEs) in deployed production dependencies. | Configures continuous CVE monitoring with automated pull requests (Dependabot) and emergency security patch protocols. |
| **#322** | Merges high-velocity AI-generated pull requests without automated static analysis security testing (SAST) gates. | Blocks PR merges failing automated Semgrep/SonarQube SAST gates designed to catch insecure AI coding patterns. |
| **#326** | Flat Docker/VPC network where all services share credentials, communicate without tokens, and have unrestricted egress. | Microsegmented subnets with Calico/Docker network isolation, mandatory mTLS tokens, and egress firewalls. |
| **#327** | Setting Access-Control-Allow-Origin: * or echoing req.headers.origin blindly with allowCredentials: true. | Explicit domain allowlist, strict regex matching for trusted origins, and credentials set exclusively for verified peers. |

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
| **#326** | `CRITICAL` | Flat Network Blast Radius: Microsegmentation, mTLS & Least Privilege | Layer 8 | [Watch Reel](https://www.instagram.com/reel/326/) |
| **#327** | `CRITICAL` | The Wildcard CORS Breach: Explicit Allowlists & Safe Credential Handling | Layer 8 | [Watch Reel](https://www.instagram.com/reel/327/) |
