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
| **#074** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Your AI pushed 47 files to production in one commit'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Your AI pushed 47 files to production in one commit'. |
| **#092** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'AI Directed Engineering gets you to launch'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'AI Directed Engineering gets you to launch'. |
| **#096** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Every business on the planet is now a software company'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Every business on the planet is now a software company'. |
| **#135** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Every push goes straight to production'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Every push goes straight to production'. |
| **#137** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in '92% of developers use AI daily'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for '92% of developers use AI daily'. |
| **#142** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Your first production incident is coming'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Your first production incident is coming'. |
| **#143** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'You got that big meeting. Your product works. Your demo is'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'You got that big meeting. Your product works. Your demo is'. |
| **#158** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'The Friday deploy superstition reveals your architecture,'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'The Friday deploy superstition reveals your architecture,'. |
| **#169** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'A $20 self-hosted runner runs unlimited minutes'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'A $20 self-hosted runner runs unlimited minutes'. |
| **#172** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'GitHub Actions free tier. 2,000 minutes'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'GitHub Actions free tier. 2,000 minutes'. |
| **#173** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Every DevOps page on the internet is still out here'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Every DevOps page on the internet is still out here'. |
| **#189** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'In deployment a canary release pushes to a small group first'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'In deployment a canary release pushes to a small group first'. |
| **#200** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Self-hosted or managed'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Self-hosted or managed'. |
| **#204** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Your deployment takes forty-five minutes'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Your deployment takes forty-five minutes'. |
| **#209** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Three deployment models'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Three deployment models'. |
| **#217** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Three hundred dependencies in your App'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Three hundred dependencies in your App'. |
| **#231** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Repository Branching Strategy'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Repository Branching Strategy'. |
| **#233** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'AI breaks traditional CICD'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'AI breaks traditional CICD'. |
| **#235** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Nine checks before you hit deploy'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Nine checks before you hit deploy'. |
| **#239** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Supabase gets you to production'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Supabase gets you to production'. |
| **#245** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'The wait is over'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'The wait is over'. |
| **#251** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'AI writes the code'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'AI writes the code'. |
| **#253** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in '1K users = features'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for '1K users = features'. |
| **#256** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Ship to 5% first'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Ship to 5% first'. |
| **#268** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'You don’t need a DevOps team'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'You don’t need a DevOps team'. |
| **#278** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Day 7 of 13 covering the full tech stack!'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Day 7 of 13 covering the full tech stack!'. |
| **#279** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'One environment'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'One environment'. |
| **#283** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Layer 5 of 13!'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Layer 5 of 13!'. |
| **#289** | Builds frontend components handling only the happy path, showing blank screens or infinite spinners on network failure. | Implements all 4 mandatory UI states (Loading skeleton, Error with interactive Retry, Empty guidance, and Success) for every async view. |
| **#291** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Your app only knows the happy path'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Your app only knows the happy path'. |
| **#294** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Dev, staging, production, all in the same place your laptop'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Dev, staging, production, all in the same place your laptop'. |
| **#297** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Your app works in the demo. It works when you show your'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Your app works in the demo. It works when you show your'. |
| **#300** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'You tested it on your machine. Perfection!'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'You tested it on your machine. Perfection!'. |
| **#301** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Hit deploy. It’s broken'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Hit deploy. It’s broken'. |
| **#305** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in '847 dependencies'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for '847 dependencies'. |
| **#315** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Deploy. Works'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Deploy. Works'. |
| **#316** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in '47 packages'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for '47 packages'. |
| **#317** | Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'The demo works'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'The demo works'. |

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
