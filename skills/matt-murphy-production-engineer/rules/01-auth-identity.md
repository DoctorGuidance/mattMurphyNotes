# 🛡️ Rulebook: Authentication & Identity
**زیرسیستم:** احراز هویت و مدیریت نشست‌ها | **Domain ID:** `01-auth-identity` | **Target Layer:** Layer 4
> **Corpus Evidence:** Synthesized from 30 Matt Murphy Production Engineering Masterclasses (11 Critical, 3 High, 16 Medium).

---

## 👑 1. Executive Summary & Core Invariant
In modern high-scale software engineering, **Authentication & Identity** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.
Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.

### ⚡ The Non-Negotiable Invariant:
> Authentication tokens must NEVER touch `localStorage` or `sessionStorage`. All sessions must rely on `HttpOnly; Secure; SameSite=Lax` cookies with short-lived access tokens (10-15m) and rotating refresh token families. Every entity lookup MUST be composite-scoped (`tenant_id` + `user_id`) to mathematically eliminate IDOR.

---

## 🚨 2. Critical Attack Vectors & Failure Scenarios
Analysis of 30 incidents and breakdowns from this domain:

### 📍 Episode #043: Your AI Stored Your Authentication Token in LocalStorage (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your AI built your authentication system. Server returns a JWT; frontend stores it in `localStorage`. That token represents your user's identity, sitting in a storage location that every script on your page (including third-party chat widgets and analytics) can silently read.
- **The Root Cause:** Client-side storage is for public UI state, not security tokens. Protect credentials behind browser cookie flags that prevent JavaScript access.
- **Matt Murphy Takeaway:** *"Your auth token is your user's key to the building. Stop leaving it on the counter where any script can copy it."*

### 📍 Episode #044: IDOR: Your API Uses the ID in the URL to Load Data (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** A user visits `/api/invoices/1042`. They change the URL to `1043` and view another company's financial records. The backend trusted the ID in the URL without checking if the authenticated tenant actually owns that resource.
- **The Root Cause:** Never treat client-provided route parameters as an authorization assertion. Direct-object queries must strictly scope to the authenticated user's organization.
- **Matt Murphy Takeaway:** *"An ID in a URL is an address, not an authorization badge. Always verify ownership at the query level."*

### 📍 Episode #048: You added Sign in with Google. Your AI left the redirect (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You added Sign in with Google. Your AI left the redirect wide open.
- **The Root Cause:** So, your AI, it built ooth flow, right? Log in with Google, get a token, redirect back to your app. But the redirect, that URL is not locked to your domain.
- **Matt Murphy Takeaway:** *"Your users trust that login button. Make sure it only works for you."*

### 📍 Episode #050: You added a chat widget to your site. It can read every (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You added a chat widget to your site. It can read every password your users type on every page.
- **The Root Cause:** But now it can read every password your users are typing on every single page. So your AI dropped in a script tag, one line, instant customer support widget in the corner of every page. But that script runs with the same privileges as your own code.
- **Matt Murphy Takeaway:** *"Implement a Content Security Policy. You control your code. Control who else gets to run theirs next to it."*

### 📍 Episode #118: You picked your auth provider because it was free (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You picked your auth provider because it was free.
- **The Root Cause:** They're going to ask you these four questions. Do you support SAML? Do you support SSO into their identity provider?
- **Matt Murphy Takeaway:** *"So direct your AI to evaluate that gap before your next enterprise conversation or don't sell any enterprise deals"*

### 📍 Episode #124: A user logged in six months ago (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** A user logged in six months ago.
- **The Root Cause:** Someone opened it and your app was still logged in. So your database is wide open on a stranger's screen right now. And your AI, it built authentication, but it never built session management.
- **Matt Murphy Takeaway:** *"So, you need to direct your AI to close them tonight"*

### 📍 Episode #160: Your AI added Google Sign-In (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your AI added Google Sign-In.
- **The Root Cause:** Here are the three things you're going to direct your AI to do right now to fix it. Step one, silent token refresh. Your access token expires every 60 minutes.
- **Matt Murphy Takeaway:** *"Keeping users logged in safely is the orchestration nobody teaches."*

### 📍 Episode #201: System-to-system auth is not user auth (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** System-to-system auth is not user auth.
- **The Root Cause:** None of them are users logging in though. Here are the three things you got to get right. Step one, service to service off is not user off.
- **Matt Murphy Takeaway:** *"Three trust boundaries."*

### 📍 Episode #206: The vulnerability that lets anyone forge a token exists in (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** The vulnerability that lets anyone forge a token exists in your stack right now.
- **The Root Cause:** Here are the three things you check right now to see if you have it. Step one, algorithm none. Some Jot libraries accept a token with the algorithm set to none.
- **Matt Murphy Takeaway:** *"Check the algorithm."*

### 📍 Episode #243: Static credentials are permanent doors for attackers (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Static credentials are permanent doors for attackers.
- **The Root Cause:** If they leak, every query in your system is compromised until you change them manually. Here are three things you can do right now to fix it. Step one, deploy a secrets engine that generates credentials on demand.
- **Matt Murphy Takeaway:** *"Dynamic secrets expire before anyone can live there."*

---

## ❌ 3. Vibe-Coding Traps vs. Production Reality Matrix
| # | ❌ The Vibe-Coding Trap (What Naive AI Builds) | ✅ Hardened Production Standard |
|---|:---|:---|
| **#040** | Passes raw `req.body` directly into ORM update methods, allowing attackers to inject `isAdmin: true` via mass assignment. | Enforces strict input allowlists using Zod schemas (`.strict()`), rejecting any non-whitelisted or administrative fields. |
| **#043** | Stores JWT authentication tokens in client-side `localStorage` or `sessionStorage` accessible to any malicious script (XSS). | Stores session tokens in `HttpOnly; Secure; SameSite=Lax` cookies completely inaccessible to JavaScript. |
| **#044** | Queries database solely by resource ID from URL parameter (`/api/invoices/:id`), allowing any user to access another tenant's records (IDOR). | Enforces composite scoping on every query (`WHERE id = :id AND tenant_id = :tenant_id AND user_id = :user_id`) to mathematically eliminate IDOR. |
| **#048** | Leaves OAuth redirect URIs open or wildcarded without validating the cryptographic `state` parameter, enabling login hijacking. | Locks OAuth redirect URIs strictly to registered endpoints, validates CSRF state parameters, and requests minimal required scopes. |
| **#050** | Embeds unvetted third-party JavaScript chat widgets globally without Content Security Policy (CSP) isolation, exposing user keystrokes. | Restricts third-party scripts via strict CSP script-src directives, sandboxes iframe widgets, and audits external DOM access. |
| **#052** | Exposes administrative dashboards on public route paths without multi-factor authentication (MFA) or network IP gating. | Gates admin routes behind SSO/MFA, enforces IP allowlisting via VPN/Tailscale, and logs all administrative actions to audit tables. |
| **#067** | Implements naive authentication in 'Your app got featured on Product Hunt. 4,000 signups in 48', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Your app got featured on Product Hunt. 4,000 signups in 48'. |
| **#090** | Deploys code directly from developer laptops to production on launch day without automated staging regression pipelines. | Gates all production releases behind automated CI/CD staging verification, database migration smoke tests, and canary rollouts. |
| **#118** | Selects consumer authentication providers lacking SAML SSO or SCIM provisioning, blocking enterprise security compliance. | Architects auth abstraction supporting enterprise SAML SSO, automated SCIM user lifecycle management, and domain directory syncing. |
| **#124** | Issues indefinite session tokens without server-side invalidation or inactivity timeout checks, leaving stale sessions permanently open. | Enforces rolling session timeouts, short-lived access tokens (15m), and instant server-side revocation on password/security events. |
| **#136** | Implements naive authentication in 'They survived the first 48 hours', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'They survived the first 48 hours'. |
| **#139** | Implements naive authentication in 'Your AI generated a feature in 20 minutes', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Your AI generated a feature in 20 minutes'. |
| **#141** | Implements naive authentication in 'Your AI handles 70% of support', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Your AI handles 70% of support'. |
| **#145** | Implements naive authentication in 'Your security kicks users out every 15 minutes', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Your security kicks users out every 15 minutes'. |
| **#157** | Implements naive authentication in 'Your AI loaded scripts from 14 domains', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Your AI loaded scripts from 14 domains'. |
| **#160** | Implements naive authentication in 'Your AI added Google Sign-In', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Your AI added Google Sign-In'. |
| **#161** | Implements naive authentication in '60% of signups never return after day two', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for '60% of signups never return after day two'. |
| **#165** | Implements naive authentication in 'Your user reported a bug', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Your user reported a bug'. |
| **#194** | Implements naive authentication in 'RBAC is not a feature', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'RBAC is not a feature'. |
| **#201** | Implements naive authentication in 'System-to-system auth is not user auth', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'System-to-system auth is not user auth'. |
| **#206** | Verifies JWT tokens using libraries that accept the insecure `none` algorithm or fails to enforce strict signing key verification. | Enforces asymmetric algorithm validation (RS256/ES256), explicitly rejects tokens with `alg: none`, and validates audience/issuer claims. |
| **#213** | Implements naive authentication in 'Self-hosted auth is not a philosophy', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Self-hosted auth is not a philosophy'. |
| **#218** | Implements naive authentication in 'Clerk or Auth0', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Clerk or Auth0'. |
| **#228** | Implements naive authentication in 'A token that never expires is not auth', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'A token that never expires is not auth'. |
| **#230** | Implements naive authentication in 'Every hour you spend building auth is an hour you did not', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Every hour you spend building auth is an hour you did not'. |
| **#243** | Implements naive authentication in 'Static credentials are permanent doors for attackers', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Static credentials are permanent doors for attackers'. |
| **#276** | Implements naive authentication in 'Tech Stack Layer 8 of 13', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Tech Stack Layer 8 of 13'. |
| **#285** | Implements naive authentication in 'Day 4 of 13!', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Day 4 of 13!'. |
| **#308** | Implements naive authentication in 'Vibe-coded apps have one thing in common. The auth is broken', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for 'Vibe-coded apps have one thing in common. The auth is broken'. |
| **#314** | Implements naive authentication in '1 user Login works', failing to protect session boundaries or validate identity claims. | Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for '1 user Login works'. |

---

## 💻 4. Production-Hardened Code Patterns
The following hardened patterns demonstrate the exact production implementation required:

### Pattern 1: Hardened Implementation for #040 (CodeRabbit reviewed your code and found zero issues)
```typescript
// schemas/userUpdate.ts
import { z } from 'zod';

// Explicitly whitelist allowed user fields - NEVER allow role, isAdmin, or accountStatus
export const updateUserProfileSchema = z.object({
  name: z.string().min(2).max(50),
  avatarUrl: z.string().url().optional(),
  bio: z.string().max(250).optional()
}).strict(); // Rejects any unknown or injected administrative properties
```

### Pattern 2: Hardened Implementation for #043 (Your AI Stored Your Authentication Token in LocalStorage)
```typescript
// auth/cookieSession.ts
import { Response } from 'express';

export function issueAuthCookie(res: Response, token: string) {
  res.cookie('auth_token', token, {
    httpOnly: true,                               // Completely blocks JS access
    secure: process.env.NODE_ENV === 'production', // HTTPS only
    sameSite: 'lax',                              // Mitigates CSRF
    path: '/',
    maxAge: 15 * 60 * 1000                        // 15-minute short expiry
  });
}
```

### Pattern 3: Hardened Implementation for #044 (IDOR: Your API Uses the ID in the URL to Load Data)
```typescript
// services/invoiceService.ts
export async function getInvoice(invoiceId: string, authenticatedTenantId: string) {
  // ❌ VULNERABLE: const inv = await db.invoice.findUnique({ where: { id: invoiceId } });
  // ✅ SECURE: Strict Tenant Scoping
  const invoice = await db.invoice.findFirst({
    where: {
      id: invoiceId,
      tenantId: authenticatedTenantId // Enforce tenant isolation
    }
  });
  if (!invoice) throw new NotFoundError('Invoice not found or access denied');
  return invoice;
}
```

### Pattern 4: Hardened Implementation for #048 (You added Sign in with Google. Your AI left the redirect)
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

- [ ] Add immediate server-side revocation so compromised sessions can be terminated instantly.
- [ ] Enable database-level Row Level Security (RLS) as an un-bypassable guardrail.
- [ ] Enforce composite scoping with `tenant_id` on every database query.
- [ ] Move all authentication tokens out of `localStorage` and into `HttpOnly; Secure; SameSite=Lax` cookies.
- [ ] Replace sequential integer IDs with cryptographically random UUIDv7 or NanoIDs.
- [ ] Shorten access token lifespans to 10–15 minutes and implement rotating refresh tokens.
- [ ] audit every third party script on your site and what it can access.
- [ ] enforce a state parameter on every OOTH request.
- [ ] lock your redirect URL to exact registered URLs.
- [ ] scope your token request to the minimum permissions your app actually needs.
- [ ] separate user endpoints from admin endpoints.
- [ ] whitelist allowed fields on every right endpoint.

---

## 📚 6. Full Domain Catalog of Masterclasses
| Episode | Severity | Masterclass Title | Production Layer | Source Reel |
|:---:|:---:|:---|:---:|:---:|
| **#040** | `HIGH` | CodeRabbit reviewed your code and found zero issues | Layer 4 | [Watch Reel](https://www.instagram.com/reel/Dc808nfFdi-/) |
| **#043** | `CRITICAL` | Your AI Stored Your Authentication Token in LocalStorage | Layer 4 | [Watch Reel](https://www.instagram.com/reel/Dc3kkckjyYV/) |
| **#044** | `CRITICAL` | IDOR: Your API Uses the ID in the URL to Load Data | Layer 4 | [Watch Reel](https://www.instagram.com/reel/Dc1jZHyiWz0/) |
| **#048** | `CRITICAL` | You added Sign in with Google. Your AI left the redirect | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DcwZzLckxZ4/) |
| **#050** | `CRITICAL` | You added a chat widget to your site. It can read every | Layer 4 | [Watch Reel](https://www.instagram.com/reel/Dct1A_WDsrP/) |
| **#052** | `HIGH` | Your admin dashboard has no authentication | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DcrQPBHG0_I/) |
| **#067** | `MEDIUM` | Your app got featured on Product Hunt. 4,000 signups in 48 | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DcUFF39Eu04/) |
| **#090** | `MEDIUM` | Your product on launch day is not your product. It is your | Layer 4 | [Watch Reel](https://www.instagram.com/reel/Db3MvKXgYMd/) |
| **#118** | `CRITICAL` | You picked your auth provider because it was free | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DbOpQ2mDrD1/) |
| **#124** | `CRITICAL` | A user logged in six months ago | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DbGolYUFbnV/) |
| **#136** | `MEDIUM` | They survived the first 48 hours | Layer 4 | [Watch Reel](https://www.instagram.com/reel/Da5cIxGDdca/) |
| **#139** | `MEDIUM` | Your AI generated a feature in 20 minutes | Layer 4 | [Watch Reel](https://www.instagram.com/reel/Da2uC94Da2K/) |
| **#141** | `MEDIUM` | Your AI handles 70% of support | Layer 4 | [Watch Reel](https://www.instagram.com/reel/Da02icHj2ss/) |
| **#145** | `HIGH` | Your security kicks users out every 15 minutes | Layer 4 | [Watch Reel](https://www.instagram.com/reel/Daxv0QLgG8B/) |
| **#157** | `MEDIUM` | Your AI loaded scripts from 14 domains | Layer 4 | [Watch Reel](https://www.instagram.com/reel/Danl3ysjuQ8/) |
| **#160** | `CRITICAL` | Your AI added Google Sign-In | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DallI-2D9Q7/) |
| **#161** | `MEDIUM` | 60% of signups never return after day two | Layer 4 | [Watch Reel](https://www.instagram.com/reel/Dak14uIihkT/) |
| **#165** | `MEDIUM` | Your user reported a bug | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DafuL1lggp3/) |
| **#194** | `MEDIUM` | RBAC is not a feature | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DaGcgHaiq3i/) |
| **#201** | `CRITICAL` | System-to-system auth is not user auth | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DaAwzEqFWpT/) |
| **#206** | `CRITICAL` | The vulnerability that lets anyone forge a token exists in | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DZ71CFgmeVk/) |
| **#213** | `MEDIUM` | Self-hosted auth is not a philosophy | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DZ0ck8DvVKa/) |
| **#218** | `MEDIUM` | Clerk or Auth0 | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DZu8mdaR7A4/) |
| **#228** | `MEDIUM` | A token that never expires is not auth | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DZm7yPZxxlC/) |
| **#230** | `MEDIUM` | Every hour you spend building auth is an hour you did not | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DZk6Q0yRF7h/) |
| **#243** | `CRITICAL` | Static credentials are permanent doors for attackers | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DZXhEL2RVRu/) |
| **#276** | `MEDIUM` | Tech Stack Layer 8 of 13 | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DYxb9K-RC7n/) |
| **#285** | `MEDIUM` | Day 4 of 13! | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DYnJUm9xKMN/) |
| **#308** | `CRITICAL` | Vibe-coded apps have one thing in common. The auth is broken | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DYLIVYbvPdO/) |
| **#314** | `MEDIUM` | 1 user Login works | Layer 4 | [Watch Reel](https://www.instagram.com/reel/DX_2cLYgf7q/) |
