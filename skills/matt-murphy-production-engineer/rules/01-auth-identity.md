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
| **#040** | Accepts unrestricted request body payloads in user update endpoints, enabling privilege escalation via `isAdmin: true` mass assignment. | Enforces strict Zod schema whitelisting on update endpoints and strips sensitive role/permission fields at the controller layer. |
| **#043** | Stores JWT authentication tokens in browser LocalStorage, leaving sessions vulnerable to complete theft via Cross-Site Scripting (XSS). | Stores authentication tokens exclusively in HttpOnly, Secure, SameSite=Lax cookies completely inaccessible to JavaScript. |
| **#044** | Fetches user records directly by sequential URL parameters (`/api/users/:id`) without validating requesting user ownership (IDOR). | Enforces ownership verification on every database query (`where: { id, tenantId, userId }`) and replaces sequential IDs with UUIDv4. |
| **#048** | Accepts unvalidated `returnTo` redirect destinations after Google OAuth login, enabling phishing redirection attacks. | Validates post-authentication redirect URLs against a strict domain whitelist and enforces PKCE state parameters. |
| **#050** | Embeds third-party chat widgets directly in the main DOM, allowing unverified scripts to read authenticated session state. | Isolates third-party widgets inside sandboxed iframes with restricted permissions and zero direct access to parent cookies. |
| **#052** | Deploys internal administrative dashboards without authentication, assuming security through obscure unguessable URLs. | Enforces enterprise Single Sign-On (SSO), mandatory hardware MFA, and IP-restricted VPN gateways for all administrative tools. |
| **#067** | Spawns direct database session queries for every user request during traffic surges, crashing under authentication connection saturation. | Caches validated session tokens in distributed Redis clusters with 60-second TTLs to shield the database from connection spikes. |
| **#090** | Launches authentication flows without telemetry, remaining blind to user drop-offs and broken third-party OAuth providers. | Instruments conversion funnels and automated alerts on authentication failure spikes across all social login providers. |
| **#118** | Selects identity providers solely on free-tier limits without evaluating data exportability or custom domain SSO capabilities. | Selects auth providers based on tenant isolation, SAML/OIDC compliance, and zero-downtime user credential export policies. |
| **#124** | Issues long-lived session tokens that never expire, leaving accounts vulnerable if client devices are lost or stolen. | Enforces rotating refresh tokens with 7-day idle timeouts, 30-day absolute expirations, and remote session revocation. |
| **#136** | Forces lengthy multi-step registration forms upfront, causing 70% of prospective users to abandon the authentication funnel. | Adopts progressive profiling with frictionless passwordless magic links, collecting extended metadata only after user activation. |
| **#139** | Allows user profile update endpoints to modify email and phone identifiers without sending verification challenges. | Requires re-authentication and automated one-time confirmation challenges before altering primary identity attributes. |
| **#141** | Permits automated AI support workflows to execute account actions based on unauthenticated user-supplied email claims. | Verifies cryptographic session signatures and tenant scopes before allowing AI agents to trigger administrative or billing operations. |
| **#145** | Forces abrupt user logouts every 15 minutes by failing to implement silent background token renewal flows. | Implements seamless background token refresh using rotating refresh tokens without interrupting active user sessions. |
| **#157** | Loads external JavaScript tracking scripts directly onto authentication pages, risking credential harvesting via script tampering. | Enforces strict Content Security Policy (CSP) blocking third-party scripts on all login and password reset routes. |
| **#160** | Trusts Google Sign-In identity payloads without verifying the `email_verified: true` claim, risking account takeover. | Validates issuer, audience, and the `email_verified` boolean claim on every external OAuth identity token before account linkage. |
| **#161** | Fails to detect credential stuffing attacks by logging failed logins as normal application events without threshold alarms. | Monitors failed login ratios per IP and user account, triggering progressive delays, CAPTCHAs, and security alerts. |
| **#165** | Swallows authentication exceptions in frontend error boundaries, leaving users on unresponsive screens without error feedback. | Catches authentication exceptions explicitly, clearing invalid tokens and redirecting to login with explanatory context. |
| **#194** | Restricts administrative actions solely by hiding UI buttons on the client while leaving underlying API endpoints unprotected. | Decouples permissions from roles and enforces granular authorization checks on every backend controller and database query. |
| **#201** | Uses human user session cookies and interactive login flows for automated machine-to-machine microservice integrations. | Enforces dedicated service-to-service authentication using mutual TLS (mTLS) or OAuth2 client credentials with scoped tokens. |
| **#206** | Verifies JWT tokens using libraries that accept the insecure `none` algorithm or fails to enforce strict signing key verification. | Enforces asymmetric algorithm validation (RS256/ES256), explicitly rejects tokens with `alg: none`, and validates audience/issuer claims. |
| **#213** | Deploys self-hosted authentication instances without dedicated security maintenance, falling behind critical vulnerability patches. | Establishes automated vulnerability scanning and immediate patch deployment pipelines for all self-hosted identity engines. |
| **#218** | Migrates between auth vendors on impulsive whim without accounting for user credential migration friction and webhook divergence. | Abstracts authentication interfaces behind internal adapter contracts to enable vendor transitions without rewriting business code. |
| **#228** | Generates permanent personal access tokens that cannot be selectively revoked, creating permanent backdoors if leaked. | Issues scoped personal access tokens with mandatory expiration dates and instant cryptographic revocation capabilities. |
| **#230** | Builds proprietary cryptographic password hashing and session management algorithms from scratch, inviting subtle implementation flaws. | Leverages hardened, audited open-source authentication frameworks and standard password hashing primitives (Argon2id). |
| **#243** | Deploys static, hardcoded API secret keys that remain unchanged across environments for years, maximizing breach blast radiuses. | Enforces automated secret rotation using cloud secret managers and issues short-lived ephemeral credentials to services. |
| **#276** | Treats Layer 8 Identity as an isolated feature rather than an architectural foundation integrated across all 13 production tiers. | Propagates validated identity contexts through edge middleware, service meshes, and database row-level security boundaries. |
| **#285** | Skips formal session invalidation on user password changes, leaving previously authenticated devices active indefinitely. | Revokes all active refresh tokens and invalidates existing session caches immediately upon successful password resets. |
| **#308** | Accepts unverified client-supplied user identifiers in backend mutations, allowing users to alter peer account settings. | Extracts authenticated user identities strictly from verified server-side session cookies, ignoring client body ID inputs. |
| **#314** | Relies on in-memory session arrays in multi-instance deployments, causing random logouts when requests hit different server nodes. | Backs user sessions with centralized Redis clusters or stateless encrypted JWT cookies to ensure seamless multi-node scaling. |

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
