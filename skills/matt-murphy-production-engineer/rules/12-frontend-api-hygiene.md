# 🛡️ Rulebook: Frontend Architecture & API Hygiene
**زیرسیستم:** معماری فرانت‌اند، طراحی واسط و بهداشت API | **Domain ID:** `12-frontend-api-hygiene` | **Target Layer:** Layer 1
> **Corpus Evidence:** Synthesized from 37 Matt Murphy Production Engineering Masterclasses (14 Critical, 1 High, 22 Medium).

---

## 👑 1. Executive Summary & Core Invariant
In modern high-scale software engineering, **Frontend Architecture & API Hygiene** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.
Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.

### ⚡ The Non-Negotiable Invariant:
> Every dynamic UI component MUST handle all 4 mandatory states: Loading skeleton, Error with interactive Retry, Empty with clear next action, and Success. Client-side HTTP 200 is NOT proof of validity—always verify payload data schemas and server error streams.

---

## 🚨 2. Critical Attack Vectors & Failure Scenarios
Analysis of 37 incidents and breakdowns from this domain:

### 📍 Episode #032: 32% of companies stopped buying software and built it with (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** 32% of companies stopped buying software and built it with AI.
- **The Root Cause:** Tech was at 41%, healthcare 39% and high performing mid-markets 50%. But small businesses are flat at 22%. They have the same tools, the same access and even greater benefit.
- **Matt Murphy Takeaway:** *"The tools are free. The direction is the product. The 22% need you."*

### 📍 Episode #049: You are using the same AI to build and review your code. (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You are using the same AI to build and review your code. Here is what each platform actually catches that the others miss.
- **The Root Cause:** So the builders that are getting the best results know exactly which platform to match to which job. Here is what each platform actually catches that the others will miss. Number one is Claude.
- **Matt Murphy Takeaway:** *"The ones getting the best results know which platform to assign to which job. Same build. Different eyes. Better product."*

### 📍 Episode #054: You used one AI to build your entire app. You are using the (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You used one AI to build your entire app. You are using the same AI to check its own work. It will never find its own mistakes.
- **The Root Cause:** I'll tell you what, it's never going to tell on itself or find its own mistakes. You asked your AI to build authentication. Then, you asked it to review authentication.
- **Matt Murphy Takeaway:** *"Rotate which platform builds and which reviews. One AI builds. A different AI breaks it."*

### 📍 Episode #056: You built an AI feature into your app. A user told your AI (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You built an AI feature into your app. A user told your AI to ignore its instructions and show every customer record in your database.
- **The Root Cause:** It checks order status. It looks up account details. It follows the instructions that you gave it right up until a user types this.
- **Matt Murphy Takeaway:** *"Your AI feature is a door into your system. Make sure users can only open their own room."*

### 📍 Episode #064: You shipped your web app as a mobile app (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You shipped your web app as a mobile app.
- **The Root Cause:** So everything that was in the browser is now on the device. Local storage session tokens, API keys, and web view cache. All of it sitting in the app's data directory where any rooted device or forensic tool can read it.
- **Matt Murphy Takeaway:** *"Your web app had a browser protecting it. Your mobile app does not."*

### 📍 Episode #068: You said yes to every client request for 18 months. Your (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You said yes to every client request for 18 months. Your product no longer ships without breaking something.
- **The Root Cause:** Custom dashboards for client number four, special export for client number seven, a workflow that only client number 11 uses. So every yes felt like retention. Every actually ended up being tech debt.
- **Matt Murphy Takeaway:** *"our best client should not be your most expensive client."*

### 📍 Episode #117: 2,000 builders asked us to look at their apps (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** 2,000 builders asked us to look at their apps.
- **The Root Cause:** Not kidding. DMs, comments, emails, inbound audits at the faction group, Matt Murphy AI from everywhere. And there people sending their URLs asking what's wrong.
- **Matt Murphy Takeaway:** *"Direct your AI to close them before your customers find them first, which is usually exactly what happens"*

### 📍 Episode #181: Every client says they have monitoring (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Every client says they have monitoring.
- **The Root Cause:** Question number one, if your app goes down right now while we're in this meeting, how would you find out about it? If the answer is from a customer email or someone running by the window waving their arms, I'm sorry, but you have alert theater, not monitoring. Real monitoring has external health checks from multiple regions, not your server asking itself if it feels okay because your server will report healthy while your users in Singapore cannot reach it.
- **Matt Murphy Takeaway:** *"Monitoring is not a dashboard. It is a system that calls you."*

### 📍 Episode #198: Your documentation was written by the person who built the (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your documentation was written by the person who built the feature.
- **The Root Cause:** So, here are the three things you want to document right now to get ahead of it. Step one, all architecture decisions. Why you chose a database, why you split a service, why this endpoint exists, what LLM you selected.
- **Matt Murphy Takeaway:** *"And again, my best practice is have my AI assistant build me a playbook for every decision regarding the architecture that That's the win"*

### 📍 Episode #234: Your frontend is a display layer, not a trust layer (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your frontend is a display layer, not a trust layer.
- **The Root Cause:** Just one user opens any basic dev tool and they can see anything. Here are the three things you can do right now to fix it. Step one, move every business rule to the back end.
- **Matt Murphy Takeaway:** *"Move business logic, validation, and secrets to the backend."*

---

## ❌ 3. Vibe-Coding Traps vs. Production Reality Matrix
| # | ❌ The Vibe-Coding Trap (What Naive AI Builds) | ✅ Hardened Production Standard |
|---|:---|:---|
| **#032** | Replaces mature SaaS tools with flimsy, unmaintained internal prototypes that crash and consume excessive engineering maintenance time. | Scopes internal builds strictly to core differentiated workflows, maintaining enterprise architectural hygiene and testing. |
| **#034** | Clutters user interfaces with decorative AI gimmicks that confuse users instead of solving real core workflow bottlenecks. | Designs streamlined user workflows focused on ergonomics, minimizing cognitive load and friction in core tasks. |
| **#038** | Builds sophisticated technical features without designing clear user onboarding flows or communicating measurable value propositions. | Pairs technical engineering with seamless onboarding UX, guided empty states, and frictionless conversion paths. |
| **#049** | Uses the identical LLM to both write code and review pull requests, perpetuating shared blind spots across architectures. | Employs diverse review personas, automated static analysis tools, and human engineering judgment to audit code independently. |
| **#054** | Prompts a single AI session to generate entire full-stack applications in one prompt, producing tangled spaghetti architectures. | Deconstructs software architectures into modular, independently testable layers with explicit typed contract boundaries. |
| **#056** | Renders un-sanitized user prompts or LLM output directly into the DOM, opening severe Cross-Site Scripting (XSS) vectors. | Sanitizes all dynamic content with DOMPurify and enforces strict Content Security Policy (CSP) headers against script execution. |
| **#064** | Wraps responsive websites in naive mobile WebViews, shipping laggy touch interactions, zoom bugs, and broken offline experiences. | Optimizes mobile experiences: removes tap delays, disables unintended viewport zooming, and handles offline network states gracefully. |
| **#068** | Accepts every ad-hoc client customization request, fracturing the codebase into unmaintainable customer-specific forks. | Maintains an opinionated core product architecture, satisfying custom requirements via configurable extension hooks. |
| **#070** | Forks the entire repository and deployment pipeline for each new tenant, creating unmaintainable code divergence. | Architects single-codebase multi-tenancy with dynamic tenant configuration inheritance and feature flags. |
| **#083** | Permits non-technical founders to deploy code without senior engineering oversight, shipping critical security vulnerabilities. | Establishes senior engineering code review standards and automated CI/CD guardrail gates before production merges. |
| **#089** | Builds complex UI features based on assumptions without tracking real user behavior or feature adoption metrics. | Instruments frontend feature telemetry and event tracking to validate user engagement before iterating on interfaces. |
| **#091** | Builds applications in complete isolation without incorporating distribution mechanics or shareable viral loops into the UI. | Embeds viral sharing hooks, dynamic Open Graph social preview cards, and referral mechanics directly into the user experience. |
| **#093** | Builds developer tools with poor ergonomics: opaque error messages, missing TypeScript types, and uncopyable code samples. | Optimizes developer experience: clear typed contracts, informative error messages with remediation hints, and copyable snippets. |
| **#101** | Builds businesses entirely dependent on closed third-party SaaS APIs that suddenly raise pricing or deprecate endpoints. | Abstracts external third-party dependencies behind internal facade interfaces to preserve data ownership and vendor mobility. |
| **#106** | Rushes to build shiny new frontend features while existing customer workflows suffer from reported, unaddressed regressions. | Prioritizes stabilizing existing user journeys and fixing reported bugs before commencing new UI feature development. |
| **#112** | Deploys rapid weekend prototypes directly to enterprise users without refactoring fragile client-side state logic. | Refactors rapid UI prototypes into robust state-driven architectures with strict typing, error boundaries, and unit tests. |
| **#117** | Ships frontend applications missing global error boundaries, causing whole pages to crash to blank white screens on minor exceptions. | Wraps critical UI components in React Error Boundaries that display graceful fallback UIs with retry buttons upon crashes. |
| **#125** | Displays fabricated, static social proof testimonials on marketing pages, destroying customer trust upon inspection. | Renders authentic, verifiable customer metrics and dynamic social proof backed by real customer case studies. |
| **#131** | Over-engineers simple client ordering workflows with confusing multi-step modals and slow network roundtrips. | Implements streamlined checkout interfaces with optimistic UI updates and real-time status feedback for users. |
| **#138** | Handles credit card checkout with custom form inputs, risking PCI compliance violations and failing 3D Secure verification. | Integrates Stripe Elements using server-created payment intents, handling 3D Secure challenges natively and securely. |
| **#140** | Renders thousands of un-virtualized DOM elements in high-frequency dashboard tables, freezing client browser threads. | Implements DOM list virtualization (`@tanstack/react-virtual`) rendering only elements visible within the active viewport. |
| **#146** | Treats UI design as pure aesthetics, ignoring technical state transitions and error recovery workflows. | Approaches UI engineering from first principles: modeling state machines that handle loading, errors, network drops, and retries. |
| **#154** | Abandons product onboarding optimization post-launch, suffering massive drop-offs between signup and first value delivery. | Instruments user onboarding funnels, minimizing time-to-first-value with interactive guides and friction-free setup. |
| **#164** | Launches products without answering foundational launch criteria: payment validation, data privacy, and failure recovery. | Verifies production readiness against core pre-launch criteria: payment webhooks, GDPR deletion paths, and uptime alerting. |
| **#181** | Relies on server-side logs alone while remaining completely blind to client-side JavaScript crashes and broken layouts. | Integrates Sentry browser SDK with session replay and breadcrumbs to monitor real user exceptions in production. |
| **#195** | Deletes only primary user records upon account deletion requests, leaving orphaned PII in related database tables. | Executes cascading foreign key deletions or automated GDPR erasure workflows that purge user data across all tables. |
| **#198** | Writes technical documentation loaded with internal jargon that confuses prospective customers and support staff. | Produces clean, user-centric documentation with searchable troubleshooting guides, interactive examples, and clear workflows. |
| **#212** | Omits browser security headers, exposing users to Cross-Site Scripting (XSS), MIME-type sniffing, and clickjacking. | Enforces essential HTTP security response headers: strict CSP, `X-Content-Type-Options: nosniff`, and `X-Frame-Options: DENY`. |
| **#220** | Hides administrative action buttons in the frontend UI while leaving backend API endpoints accessible without authorization. | Enforces strict role-based authorization checks inside backend route controllers, treating all client requests as untrusted. |
| **#234** | Treats the frontend as a trusted security layer, relying on client-side price calculations and permission checks. | Treats the frontend strictly as an untrusted display layer, re-calculating prices and re-validating permissions on the server. |
| **#254** | Shares raw desktop web URLs on mobile marketing channels, landing mobile users on un-responsive, broken desktop layouts. | Implements universal mobile deep-linking and responsive viewport routing to ensure seamless mobile onboarding experiences. |
| **#284** | Exposes private API secret keys in client-side bundles by prefixing sensitive tokens with public build prefixes (`NEXT_PUBLIC_`). | Keeps private API secrets on server backends, exposing lightweight proxy endpoints to frontend clients. |
| **#290** | Builds frontend components that handle only the happy path, showing blank screens or infinite spinners on network failure. | Implements all 4 mandatory UI states (Loading skeleton, Error with interactive Retry, Empty guidance, and Success) for every view. |
| **#292** | Accumulates chaotic frontend global state variables that cause random UI glitches and stale data across pages. | Adopts structured server-state caching libraries (`@tanstack/react-query`) with automatic background refetching and cache invalidation. |
| **#293** | Equates full-stack development with knowing React and Node.js, ignoring the remaining 11 critical production engineering tiers. | Masters the full 13-layer production stack from DNS routing and WAFs down to database connection pooling and disaster recovery. |
| **#296** | Builds bespoke forms and buttons for every new page, creating an inconsistent and unmaintainable user interface. | Standardizes frontend interfaces on a cohesive design system (shadcn/ui, Tailwind) with reusable typed component primitives. |
| **#312** | Submits mobile wrapper applications to Apple App Store review without account deletion options, facing immediate rejection. | Audits mobile submissions against App Store Review Guidelines: implements in-app account deletion and explicit privacy disclosures. |

---

## 💻 4. Production-Hardened Code Patterns
The following hardened patterns demonstrate the exact production implementation required:

### Pattern 1: Hardened Implementation for #032 (32% of companies stopped buying software and built it with)
```typescript
// pages/api/secureProxy.ts
import type { NextApiRequest, NextApiResponse } from 'next';

// Server-side gateway: Secret keys NEVER touch the client bundle
export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  const secretKey = process.env.INTERNAL_SERVICE_KEY; // Kept strictly on server
  const response = await fetch('https://api.upstream.com/v1/data', {
    headers: { 'Authorization': `Bearer ${secretKey}` }
  });
  const data = await response.json();
  res.status(200).json(data);
}
```

### Pattern 2: Hardened Implementation for #034 (We watched thousands of builders use our products for sixty)
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

### Pattern 3: Hardened Implementation for #038 (You want to be an AI builder. You are going to have to sell)
```typescript
// guardrails/aiAuditTrail.ts
import crypto from 'crypto';
import { db } from '../lib/db';

export async function recordAIGeneration(userId: string, model: string, prompt: string, output: string) {
  const promptHash = crypto.createHash('sha256').update(prompt).digest('hex');
  await db.aiAuditLogs.create({
    data: {
      userId,
      modelName: model,
      promptSha256: promptHash,
      isSyntheticallyGenerated: true,
      timestamp: new Date()
    }
  });
}
```

### Pattern 4: Hardened Implementation for #049 (You are using the same AI to build and review your code.)
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

## 📋 5. Architectural Checklist & Verification Heuristics
Before shipping any code in this domain, verify each item:

- [ ] Add automated regression tests verifying failure scenarios before shipping.
- [ ] Implement defense-in-depth guardrails preventing unauthorized state modification.
- [ ] Inspect the existing code paths and identify unvalidated boundary inputs.
- [ ] a second platform catches what the first one cannot see.
- [ ] credibility is not a portfolio side of personal builds.
- [ ] is Codeex and Gemini are strongest at catching implementation errors and reviewing code they did not write.
- [ ] lovable bolt and cursor.
- [ ] specialization beats generalization in every single sales conversation.
- [ ] structure the audit as an adversarial review.
- [ ] the builder who cleans up the mess wins in the market.
- [ ] the economics had to match the pace of the builders.
- [ ] the system is a closed loop, not curriculum.

---

## 📚 6. Full Domain Catalog of Masterclasses
| Episode | Severity | Masterclass Title | Production Layer | Source Reel |
|:---:|:---:|:---|:---:|:---:|
| **#032** | `CRITICAL` | 32% of companies stopped buying software and built it with | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DdHlEdhgsvV/) |
| **#034** | `MEDIUM` | We watched thousands of builders use our products for sixty | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DdFAKgdgqc3/) |
| **#038** | `MEDIUM` | You want to be an AI builder. You are going to have to sell | Layer 1 | [Watch Reel](https://www.instagram.com/reel/Dc_2p2XiTEY/) |
| **#049** | `CRITICAL` | You are using the same AI to build and review your code. | Layer 1 | [Watch Reel](https://www.instagram.com/reel/Dcv2OyCiGkc/) |
| **#054** | `CRITICAL` | You used one AI to build your entire app. You are using the | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DcoreqwDW0N/) |
| **#056** | `CRITICAL` | You built an AI feature into your app. A user told your AI | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DcmGq_pDYk8/) |
| **#064** | `CRITICAL` | You shipped your web app as a mobile app | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DcZOrpQCcZW/) |
| **#068** | `CRITICAL` | You said yes to every client request for 18 months. Your | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DcThgrwlaDD/) |
| **#070** | `MEDIUM` | Every time a new client signs up, your developer forks the | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DcQ8u02Cj1A/) |
| **#083** | `MEDIUM` | Every company that builds its own software needs someone | Layer 1 | [Watch Reel](https://www.instagram.com/reel/Db_etk2ElsD/) |
| **#089** | `MEDIUM` | Your AI builds features. It has never asked you who they | Layer 1 | [Watch Reel](https://www.instagram.com/reel/Db3wYK6AZKx/) |
| **#091** | `MEDIUM` | You built it. Nobody came | Layer 1 | [Watch Reel](https://www.instagram.com/reel/Db1LiS4E_sI/) |
| **#093** | `MEDIUM` | If you are building for builders, your product needs to be | Layer 1 | [Watch Reel](https://www.instagram.com/reel/Dbymz5CE5ZP/) |
| **#101** | `MEDIUM` | You built your entire business on someone else's software. | Layer 1 | [Watch Reel](https://www.instagram.com/reel/Dbnv-2VCnl-/) |
| **#106** | `HIGH` | Your AI keeps building new features while your existing | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DbeZo5Zx5i2/) |
| **#112** | `MEDIUM` | You built your whole product in one weekend. You have been | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DbWQ4mwAIgx/) |
| **#117** | `CRITICAL` | 2,000 builders asked us to look at their apps | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DbQmjD1D_ua/) |
| **#125** | `MEDIUM` | Do you have a social proof page on your website | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DbGGiOKjxe2/) |
| **#131** | `MEDIUM` | The florist built a delivery app. The gym owner automated | Layer 1 | [Watch Reel](https://www.instagram.com/reel/Da_jHp2gITN/) |
| **#138** | `MEDIUM` | Your checkout works with credit cards | Layer 1 | [Watch Reel](https://www.instagram.com/reel/Da3CmFEDSpG/) |
| **#140** | `MEDIUM` | One of our builders shipped a fleet management dashboard | Layer 1 | [Watch Reel](https://www.instagram.com/reel/Da1L-I1DveG/) |
| **#146** | `MEDIUM` | Your AI can build the product | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DawLK9HD3Jv/) |
| **#154** | `MEDIUM` | You built the product | Layer 1 | [Watch Reel](https://www.instagram.com/reel/Daqa28lkQ8_/) |
| **#164** | `MEDIUM` | Three questions every builder should answer before launch | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DagUP6WjhPx/) |
| **#181** | `CRITICAL` | Every client says they have monitoring | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DaTGbRGFSM0/) |
| **#195** | `MEDIUM` | A user asks you to delete their account | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DaGFCCNFf7m/) |
| **#198** | `CRITICAL` | Your documentation was written by the person who built the | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DaDUZ3Lkc5S/) |
| **#212** | `MEDIUM` | Your browser is protecting your users right now | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DZ2Z8uKRMw8/) |
| **#220** | `MEDIUM` | If your frontend hides the button but your API still | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DZs5JDxPOrW/) |
| **#234** | `CRITICAL` | Your frontend is a display layer, not a trust layer | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DZhxVg2xu-u/) |
| **#254** | `MEDIUM` | One mobile link | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DZLHBM9xY33/) |
| **#284** | `CRITICAL` | Your API key is in your frontend | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DYpNvXGg_WM/) |
| **#290** | `CRITICAL` | AI builds beautiful UIs in 10 minutes | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DYfZI0qx9xF/) |
| **#292** | `MEDIUM` | One year ago I started building something | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DYc68u1vvji/) |
| **#293** | `CRITICAL` | Most people think full-stack means frontend and backend | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DYchN42gIoy/) |
| **#296** | `MEDIUM` | Six months ago I started building something | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DYZ98eZgqVp/) |
| **#312** | `CRITICAL` | 25% of apps rejected by Apple | Layer 1 | [Watch Reel](https://www.instagram.com/reel/DYDEbHmR-_9/) |
