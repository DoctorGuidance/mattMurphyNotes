# 🛡️ Rulebook: Testing, Staging & CI/CD
**زیرسیستم:** تست، محیط‌های کاری، CI/CD و خط لوله استقرار | **Domain ID:** `10-cicd-deployments` | **Target Layer:** Layer 7
> **Corpus Evidence:** Synthesized from 39 Matt Murphy Production Engineering Masterclasses (9 Critical, 6 High, 24 Medium).

---

## 👑 1. Executive Summary & Core Invariant
In modern high-scale software engineering, **Testing, Staging & CI/CD** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.
Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.

### ⚡ The Non-Negotiable Invariant:
> Production parity across Dev, Staging, and Prod is absolute. Database migrations must be backward-compatible and tested for zero-downtime rollbacks before deployment. Release via automated canary/blue-green pipelines with automatic regression rollbacks.

---

## 🚨 2. Critical Attack Vectors & Failure Scenarios
Analysis of 39 incidents and breakdowns from this domain:

### 📍 Episode #142: Your first production incident is coming (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your first production incident is coming.
- **The Root Cause:** But that's not the problem. Having no support playbook for what happens after that is the problem. So here are the three things you're going to do right now to direct your AI to fix it.
- **Matt Murphy Takeaway:** *"You just have to make sure you know what to tell it to do"*

### 📍 Episode #189: In deployment a canary release pushes to a small group first (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** In deployment a canary release pushes to a small group first.
- **The Root Cause:** Then you open the gates to everybody. I just did this with my own faction community launch. Here are the three things that happened.
- **Matt Murphy Takeaway:** *"The gates are open."*

### 📍 Episode #209: Three deployment models (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Three deployment models.
- **The Root Cause:** Same goal, but completely different cost curves. Here are the three things you need to know. Step one, Verscell was built for front-end frameworks.
- **Matt Murphy Takeaway:** *"Match the hosting to the stage."*

### 📍 Episode #231: Repository Branching Strategy (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Repository Branching Strategy.
- **The Root Cause:** Let's talk about it. Here are the three things you need to know right now about branching repositories. Step one, your main branch is always production.
- **Matt Murphy Takeaway:** *"Your main branch is always production — treat it that way."*

### 📍 Episode #235: Nine checks before you hit deploy (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Nine checks before you hit deploy.
- **The Root Cause:** Here are the three things you can do right now to prevent it. Step one, verify all of your safety nets. Your environment variables are loaded from your secrets manager, not hardcoded.
- **Matt Murphy Takeaway:** *"Fifteen minutes saves you days."*

### 📍 Episode #245: The wait is over (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You wanted to know more about the faction community? I got something for you. You want to know more about Matt Murphy.ai, the website, it's live right now.
- **The Root Cause:** You want to know more about Matt Murphy.ai, the website, it's live right now. Now, the website and the community, they are symbiotic, but they are also not exactly the same. And this is an important message for everybody out there.
- **Matt Murphy Takeaway:** *"But game On people, less rock"*

### 📍 Episode #294: Dev, staging, production, all in the same place your laptop (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Dev, staging, production, all in the same place: your laptop.
- **The Root Cause:** When you break something, you break it in production. And when you try to fix something at 11:00 p.m. at night, you're fixing it in a live production database while real users are using it.
- **Matt Murphy Takeaway:** *"You’re testing and breaking everything live."*

### 📍 Episode #305: 847 dependencies (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** I told you your vibe coded app has 847 dependencies and you installed maybe seven of them
- **The Root Cause:** I told you your vibe coded app has 847 dependencies and you installed maybe seven of them
- **Matt Murphy Takeaway:** *"More tips and tricks coming tomorrow"*

### 📍 Episode #316: 47 packages (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your AI generated app uses 47 different packages and you can name maybe three of them
- **The Root Cause:** Your AI generated app uses 47 different packages and you can name maybe three of them
- **Matt Murphy Takeaway:** *"Drop it below in the comments"*

### 📍 Episode #002: Full Tech Stack Recap! (Severity: `HIGH`)
- **The Attack Vector / Incident:** Full Tech Stack Recap!
- **The Root Cause:** And most vibe coders, they have two front end and a database, sometimes off. But that leaves 10 plus layers completely missing. And those 10 layers that are missing separate a demo from a real product.
- **Matt Murphy Takeaway:** *"The full production stack. Here’s every layer, one more time."*

---

## ❌ 3. Vibe-Coding Traps vs. Production Reality Matrix
| # | ❌ The Vibe-Coding Trap (What Naive AI Builds) | ✅ Hardened Production Standard |
|---|:---|:---|
| **#002** | Treats production software as a single monolith without architectural boundaries across layers, causing cascading outages. | Enforces strict isolation across all 13 production layers from edge UI to disaster recovery with automated verification gates. |
| **#074** | Pushes 47 disparate code files directly to production in a single un-reviewed commit, making bug isolation impossible. | Breaks feature changes into small, atomic pull requests protected by feature flags and automated CI verification gates. |
| **#092** | Uses AI coding tools to bypass staging environments, deploying unverified prototype code straight to paying users. | Enforces automated CI/CD staging environments where AI-authored code passes automated regression tests before production release. |
| **#096** | Treats business software as disposable weekend scripts without continuous integration, automated builds, or rollback plans. | Adopts enterprise CI/CD standards: automated test pipelines, reproducible Docker builds, and instant canary rollback capabilities. |
| **#135** | Pushes code commits directly to production branches without branch protection rules, automated tests, or review gates. | Enforces protected main branches requiring green CI build checks, automated linting, and peer approvals before deployment. |
| **#137** | Allows developers to merge AI-generated code without automated security testing, flooding codebases with security anti-patterns. | Integrates automated static analysis (SAST) and secret scanning into pull request pipelines to verify all AI-generated code. |
| **#142** | Waits for the first major production outage before writing operational runbooks, panicking when user databases crash. | Authors clear incident response runbooks with documented rollback steps, database failover procedures, and on-call escalation paths. |
| **#143** | Demos software using carefully manicured local databases, watching the product crash when exposed to real production data. | Enforces environment parity between staging and production, testing releases against realistic, anonymized production datasets. |
| **#158** | Fears Friday deployments due to missing test suites and lack of automated rollback capabilities. | Builds automated regression test suites and zero-downtime blue/green deployment pipelines that make deployments routine any day. |
| **#169** | Burns expensive managed cloud CI runner minutes on long build matrices instead of using cost-effective dedicated runners. | Deploys dedicated self-hosted CI runners on fixed-cost compute instances ($20/mo), achieving unlimited pipeline execution. |
| **#172** | Exhausts GitHub Actions free tier minutes mid-month due to un-cached dependency installations and serial test execution. | Implements dependency caching (`actions/cache`), Docker layer caching, and parallelized test jobs to cut CI runtimes by 70%. |
| **#173** | Follows over-engineered enterprise DevOps dogma for early-stage prototypes, stalling feature delivery for months. | Adopts pragmatic trunk-based development with ephemeral preview environments, balancing engineering velocity with reliability. |
| **#189** | Deploys updates simultaneously to 100% of production traffic, exposing all users immediately to uncaught regressions. | Implements canary deployments: routes 5% of production traffic to new versions, monitoring error metrics before full rollout. |
| **#200** | Makes infrastructure hosting decisions based on internet hype rather than calculating operational maintenance and egress costs. | Evaluates hosting trade-offs systematically: balancing managed convenience against self-hosted control and compute margins. |
| **#204** | Suffers 45-minute deployment build times caused by un-cached monolithic Docker builds and sequential test execution. | Optimizes Docker build pipelines with multi-stage BuildKit caching and parallel test matrix jobs, cutting deploy time to 4 minutes. |
| **#209** | Adopts high-risk deployment models without understanding coupling between application code and database schema states. | Selects deployment patterns (Rolling, Blue/Green, Canary) aligned with backward-compatible database schema migrations. |
| **#217** | Pulls in 300 unvetted third-party npm dependencies, creating a massive attack surface for supply chain compromises. | Audits the dependency tree, removes redundant packages, and pins exact versions with lockfile integrity verification. |
| **#231** | Maintains long-lived diverging feature branches for weeks, causing nightmare merge conflicts and broken deployments. | Practices trunk-based development with short-lived feature branches (<24h) and feature flags for incomplete capabilities. |
| **#233** | Allows high-velocity AI code generation to overwhelm traditional manual PR review processes, creating code review backlogs. | Automates PR review triage with AI linters, automated test suites, and strict architectural boundary checkers. |
| **#235** | Hits the deploy button without verifying database migrations, environment variables, or build health. | Automates a strict 9-point pre-flight deployment checklist in CI: schema check, secret scans, build verification, and smoke tests. |
| **#239** | Applies database schema changes via the Supabase web dashboard in production, causing environmental drift from local code. | Manages Supabase schema migrations as versioned SQL migration files committed to Git and applied via CI pipelines. |
| **#245** | Postpones CI/CD pipeline automation until late in product development, suffering manual deployment errors every week. | Establishes automated git-push CI/CD pipelines from Day 1 of development, making production releases effortless. |
| **#251** | Allows AI to generate large production components without writing unit tests, accumulating silent architectural debt. | Mandates test-driven verification for AI-generated code, requiring unit and integration tests before merging changes. |
| **#253** | Continues rushing new features after reaching 1,000 active users while ignoring database query degradation and stability. | Shifts focus at 1k users from feature addition to operational reliability: index optimization, caching, and regression testing. |
| **#256** | Rolls out major application updates to all users at once, risking widespread customer churn during regressions. | Automates phased rollouts (5% -> 25% -> 100%) with automated rollbacks triggered if error rates exceed 0.1%. |
| **#268** | Hires dedicated DevOps teams prematurely for simple prototypes, wasting capital on unnecessary infrastructure overhead. | Leverages developer-friendly platform-as-a-service primitives (Railway, Fly, Vercel) with Git-driven deployment automation. |
| **#278** | Operates microservices with inconsistent release pipelines, resulting in version mismatches and broken API contracts. | Standardizes CI/CD release pipeline definitions across all repositories using reusable GitHub Actions workflow templates. |
| **#279** | Develops directly against production databases, risking accidental table drops and catastrophic customer data corruption. | Enforces strict three-tier environment isolation (Dev, Staging, Production) with isolated database clusters and credentials. |
| **#283** | Treats Layer 5 Staging Parity as optional, testing migrations on production databases during live customer traffic. | Mandates staging dry-runs for all database migrations and configuration updates prior to production execution. |
| **#289** | Rely on paying users to discover broken workflows in production due to lack of automated regression testing. | Deploys automated Playwright end-to-end integration test suites in CI verifying critical user journeys before every release. |
| **#291** | Tests software only on the happy path, releasing code that crashes on empty database states or network timeouts. | Tests edge cases, network timeouts, invalid inputs, and dirty data conditions in CI before approving pull requests. |
| **#294** | Runs development, staging, and production setups all locally on developer laptops, suffering 'works on my machine' bugs. | Containerizes applications using Docker Compose and mirrors cloud infrastructure in isolated staging environments. |
| **#297** | Prepares investor demos using pristine sanitized data, hiding severe database deadlocks and slow queries under dirty inputs. | Fuzz-tests staging environments with dirty, realistic production datasets to uncover unhandled errors prior to launch. |
| **#300** | Deploys code under the assumption that local macOS/Windows execution guarantees identical behavior on Linux production hosts. | Enforces reproducible Docker builds that compile and execute code inside identical Linux container runtimes across all stages. |
| **#301** | Deploys code blindly with manual git pulls on servers, suffering deployment outages with zero understanding of changes. | Adopts immutable preview deployments (Vercel/Netlify) and atomic deployment rollouts to eliminate deployment roulette. |
| **#305** | Accumulates 847 transitive npm dependencies, ignoring known security CVEs and supply chain injection risks. | Runs automated `npm audit` gates in CI and schedules monthly dependency pruning to eliminate unmaintained libraries. |
| **#315** | Deploys non-deterministic build artifacts that work or break randomly depending on upstream package updates. | Enforces deterministic builds using pinned package lockfiles, base Docker image SHAs, and reproducible artifact caches. |
| **#316** | Installs dozens of redundant utility packages, inflating frontend bundle sizes and slowing page load speeds. | Audits bundle sizes using Webpack/Vite bundle analyzers, replacing heavy external packages with native JavaScript APIs. |
| **#317** | Relies on polished pitch deck demos while skipping resilience testing, watching software fail when real users enter unpredicted inputs. | Runs automated chaos engineering and edge-case fuzzing against application APIs prior to opening public user access. |

---

## 💻 4. Production-Hardened Code Patterns
The following hardened patterns demonstrate the exact production implementation required:

### Pattern 1: Hardened Implementation for #002 (Full Tech Stack Recap!)
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

### Pattern 2: Hardened Implementation for #074 (Your AI pushed 47 files to production in one commit)
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

### Pattern 3: Hardened Implementation for #092 (AI Directed Engineering gets you to launch)
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

### Pattern 4: Hardened Implementation for #096 (Every business on the planet is now a software company)
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

---

## 📋 5. Architectural Checklist & Verification Heuristics
Before shipping any code in this domain, verify each item:

- [ ] Add automated regression tests verifying failure scenarios before shipping.
- [ ] Implement defense-in-depth guardrails preventing unauthorized state modification.
- [ ] Inspect the existing code paths and identify unvalidated boundary inputs.
- [ ] automated checks that run before any merge.
- [ ] branch protection on main.
- [ ] build a staging environment.
- [ ] direct your AI to map every conversion point in your buying journey.
- [ ] every step between discovery and purchase is an engineering problem.
- [ ] small scoped commits that you can trace and reverse.
- [ ] the AI conveyor belt is a shared environment where your team builds drop onto a production pipeline.
- [ ] the builders who treat their salesunnel like they treat their codebase win.
- [ ] your staff builds what they know.

---

## 📚 6. Full Domain Catalog of Masterclasses
| Episode | Severity | Masterclass Title | Production Layer | Source Reel |
|:---:|:---:|:---|:---:|:---:|
| **#002** | `HIGH` | Full Tech Stack Recap! | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DZAw8CcRXM6/) |
| **#074** | `MEDIUM` | Your AI pushed 47 files to production in one commit | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DcLzI-pFJlM/) |
| **#092** | `MEDIUM` | AI Directed Engineering gets you to launch | Layer 7 | [Watch Reel](https://www.instagram.com/reel/Db0n5e6DAUl/) |
| **#096** | `MEDIUM` | Every business on the planet is now a software company | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DbveZVplEYz/) |
| **#135** | `MEDIUM` | Every push goes straight to production | Layer 7 | [Watch Reel](https://www.instagram.com/reel/Da51JT3DSQi/) |
| **#137** | `MEDIUM` | 92% of developers use AI daily | Layer 7 | [Watch Reel](https://www.instagram.com/reel/Da3gktKj0oX/) |
| **#142** | `CRITICAL` | Your first production incident is coming | Layer 7 | [Watch Reel](https://www.instagram.com/reel/Da0QC2EDfG3/) |
| **#143** | `MEDIUM` | You got that big meeting. Your product works. Your demo is | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DayW9qUEVyF/) |
| **#158** | `MEDIUM` | The Friday deploy superstition reveals your architecture, | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DanRJ1EjMnJ/) |
| **#169** | `MEDIUM` | A $20 self-hosted runner runs unlimited minutes | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DabfLrfF-OA/) |
| **#172** | `MEDIUM` | GitHub Actions free tier. 2,000 minutes | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DaaYDrMkbpW/) |
| **#173** | `MEDIUM` | Every DevOps page on the internet is still out here | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DaYjVYPPpZx/) |
| **#189** | `CRITICAL` | In deployment a canary release pushes to a small group first | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DaLm59JFDJF/) |
| **#200** | `HIGH` | Self-hosted or managed | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DaBItqrFHiF/) |
| **#204** | `MEDIUM` | Your deployment takes forty-five minutes | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DZ8txA_mRAp/) |
| **#209** | `CRITICAL` | Three deployment models | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DZ44VWrxdvI/) |
| **#217** | `MEDIUM` | Three hundred dependencies in your App | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DZvd_LOvbRH/) |
| **#231** | `CRITICAL` | Repository Branching Strategy | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DZkd5y_xpqP/) |
| **#233** | `MEDIUM` | AI breaks traditional CICD | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DZiVwxixLrb/) |
| **#235** | `CRITICAL` | Nine checks before you hit deploy | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DZgXTkptNR6/) |
| **#239** | `MEDIUM` | Supabase gets you to production | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DZcoN1gRCgL/) |
| **#245** | `CRITICAL` | The wait is over | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DZVPbw9x7Bw/) |
| **#251** | `HIGH` | AI writes the code | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DZN3Z3IPD9a/) |
| **#253** | `MEDIUM` | 1K users = features | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DZLl1dfvSdm/) |
| **#256** | `MEDIUM` | Ship to 5% first | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DZKp4rPAasV/) |
| **#268** | `HIGH` | You don’t need a DevOps team | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DY7OKr4xruV/) |
| **#278** | `MEDIUM` | Day 7 of 13 covering the full tech stack! | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DYuyZmkRXye/) |
| **#279** | `MEDIUM` | One environment | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DYuVqaeRi8q/) |
| **#283** | `MEDIUM` | Layer 5 of 13! | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DYpc9DkghA8/) |
| **#289** | `MEDIUM` | Your users are your QA team | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DYhc3KSA_D1/) |
| **#291** | `MEDIUM` | Your app only knows the happy path | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DYfDSOzgC-x/) |
| **#294** | `CRITICAL` | Dev, staging, production, all in the same place your laptop | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DYcYahVgw_I/) |
| **#297** | `HIGH` | Your app works in the demo. It works when you show your | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DYZ1EeNgGIu/) |
| **#300** | `MEDIUM` | You tested it on your machine. Perfection! | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DYVJUa3xSOu/) |
| **#301** | `HIGH` | Hit deploy. It’s broken | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DYUiLhrNY9o/) |
| **#305** | `CRITICAL` | 847 dependencies | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DYPXmX3AXQS/) |
| **#315** | `MEDIUM` | Deploy. Works | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DX9avyogIVx/) |
| **#316** | `CRITICAL` | 47 packages | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DX7VHJORcWV/) |
| **#317** | `MEDIUM` | The demo works | Layer 7 | [Watch Reel](https://www.instagram.com/reel/DX2OR7nRQIP/) |
