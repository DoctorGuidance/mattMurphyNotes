# 🛡️ Rulebook: Observability & Error Tracking
**زیرسیستم:** مشاهده‌پذیری، لاگ ساختاریافته و رهگیری خطا | **Domain ID:** `06-observability-logs` | **Target Layer:** Layer 12
> **Corpus Evidence:** Synthesized from 16 Matt Murphy Production Engineering Masterclasses (7 Critical, 1 High, 8 Medium).

---

## 👑 1. Executive Summary & Core Invariant
In modern high-scale software engineering, **Observability & Error Tracking** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.
Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.

### ⚡ The Non-Negotiable Invariant:
> Zero opaque console.logs in production. All logs must be structured JSON containing timestamps, correlation IDs (`x-request-id`), severity levels, and sanitized contexts. PII and secrets must be scrubbed at the logging boundary.

---

## 🚨 2. Critical Attack Vectors & Failure Scenarios
Analysis of 16 incidents and breakdowns from this domain:

### 📍 Episode #150: Your monitoring says green (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your monitoring says green.
- **The Root Cause:** Let's start with the patterns your monitoring is missing. Your dashboards say 99% uptime, right? Error rates are below the thresholds.
- **Matt Murphy Takeaway:** *"Read it like a dashboard."*

### 📍 Episode #163: Customer A logged in and saw customer B's data (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Customer A logged in and saw customer B's data.
- **The Root Cause:** Customer A has logged into your multi-tenant SAS and saw customer B's data, their revenue numbers, their customer list, their private messages. Not good. Here's what actually happens next.
- **Matt Murphy Takeaway:** *"Not after the support ticket arrives."*

### 📍 Episode #180: Your error tracker catches errors your code throws (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your error tracker catches errors your code throws.
- **The Root Cause:** Here are the three things you want to add right now to fix it. Step one, business metric alerting. Your infrastructure metrics say the server is healthy.
- **Matt Murphy Takeaway:** *"Monitor what your tools were never built to see."*

### 📍 Episode #183: Your error tracker catches errors your code throws (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your error tracker catches errors your code throws.
- **The Root Cause:** Here are the three things you want to add right now to fix it. Step one, business metric alerting. Your infrastructure metrics say the server is healthy.
- **Matt Murphy Takeaway:** *"Monitor what your tools were never built to see."*

### 📍 Episode #205: Silent 2 AM Server Crashes: Unhandled Promise Rejections (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** An asynchronous background task throws an unhandled rejection at 2 AM. The Node.js event loop terminates immediately. The server crashes silently with no log entries, leaving customers facing 502 Bad Gateway until morning.
- **The Root Cause:** Asynchronous runtimes require proactive error budgeting. Capture unhandled exceptions globally, report structured context to monitoring systems, and restart gracefully.
- **Matt Murphy Takeaway:** *"An unhandled promise rejection in production is a ticking time bomb. Capture it globally or let your users tell you when you're down."*

### 📍 Episode #267: Tech Stack Layer 12 (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Layer 12 of 13, error tracking and logs. This is the one that tells you what's broken before your users do. So, if your only debugging strategy is refreshing the page, your app isn't in production.
- **The Root Cause:** So, if your only debugging strategy is refreshing the page, your app isn't in production. It's just a shiny demo. So, right now, most of you have no idea what's happening inside your app.
- **Matt Murphy Takeaway:** *"Refreshing the page isn’t a debugging strategy."*

### 📍 Episode #295: Hit F12 on your live app (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Hit F12 on your live app.
- **The Root Cause:** Hit F12. Click on sources. Now search for the word key.
- **Matt Murphy Takeaway:** *"You left the vault open."*

### 📍 Episode #303: Your app crashes and you have no idea (Severity: `HIGH`)
- **The Attack Vector / Incident:** I told you your app crashes and you don't know why
- **The Root Cause:** I told you your app crashes and you don't know why
- **Matt Murphy Takeaway:** *"More tips and tricks coming tomorrow"*

---

## ❌ 3. Vibe-Coding Traps vs. Production Reality Matrix
| # | ❌ The Vibe-Coding Trap (What Naive AI Builds) | ✅ Hardened Production Standard |
|---|:---|:---|
| **#023** | Logs unstructured text or swallows exceptions silently in 'I need to tell you something that's going to make you', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |
| **#071** | Logs unstructured text or swallows exceptions silently in 'Your status page says operational. Your customers are', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |
| **#121** | Logs unstructured text or swallows exceptions silently in 'You have 6,000 users and fewer of them come back every week', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |
| **#128** | Logs unstructured text or swallows exceptions silently in 'Your user clicked delete my account', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |
| **#150** | Logs unstructured text or swallows exceptions silently in 'Your monitoring says green', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |
| **#163** | Logs unstructured text or swallows exceptions silently in 'Customer A logged in and saw customer B's data', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |
| **#180** | Monitors only hard thrown exceptions in code while missing silent functional failures like payment webhooks returning 200 on failure. | Instruments business-level telemetry and anomaly alerts tracking webhook ingestion rates and business outcome drop-offs. |
| **#183** | Assumes error trackers catch every production failure without deploying end-to-end synthetic canary health checks. | Deploys automated synthetic transaction canaries verifying payment webhook pipelines end-to-end around the clock. |
| **#199** | Logs unstructured text or swallows exceptions silently in 'Your logs say everything and tell you nothing', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |
| **#205** | Leaves uncaught exceptions and unhandled promise rejections unhandled in Node.js, crashing the server process silently. | Registers global process handlers for uncaughtException and unhandledRejection, logging context to Sentry with graceful restart. |
| **#250** | Logs unstructured text or swallows exceptions silently in 'Flat rate', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |
| **#267** | Logs unstructured text or swallows exceptions silently in 'Tech Stack Layer 12', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |
| **#295** | Logs unstructured text or swallows exceptions silently in 'Hit F12 on your live app', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |
| **#303** | Logs unstructured text or swallows exceptions silently in 'Your app crashes and you have no idea', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |
| **#313** | Logs unstructured text or swallows exceptions silently in 'Something broke. Users noticed before you did', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |
| **#321** | Logs unstructured text or swallows exceptions silently in 'App breaks', creating monitoring blind spots in production. | Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry. |

---

## 💻 4. Production-Hardened Code Patterns
The following hardened patterns demonstrate the exact production implementation required:

### Pattern 1: Hardened Implementation for #023 (I need to tell you something that's going to make you)
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

### Pattern 2: Hardened Implementation for #071 (Your status page says operational. Your customers are)
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

### Pattern 3: Hardened Implementation for #121 (You have 6,000 users and fewer of them come back every week)
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

### Pattern 4: Hardened Implementation for #128 (Your user clicked delete my account)
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
- [ ] a data retention policy engine.
- [ ] a defined error budget per critical endpoint.
- [ ] a retention schedule mapped to your actual obligations.
- [ ] an audit trail that proves you followed the policy.
- [ ] an automated dropoff alert.
- [ ] burn rate alerting that catches trends before they become outages.
- [ ] business cost attribution on every single incident.
- [ ] to understanding it better.
- [ ] usage event tracking on your core features.

---

## 📚 6. Full Domain Catalog of Masterclasses
| Episode | Severity | Masterclass Title | Production Layer | Source Reel |
|:---:|:---:|:---|:---:|:---:|
| **#023** | `MEDIUM` | I need to tell you something that's going to make you | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DdXBw5CCWyS/) |
| **#071** | `MEDIUM` | Your status page says operational. Your customers are | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DcO7fDEj9eg/) |
| **#121** | `MEDIUM` | You have 6,000 users and fewer of them come back every week | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DbLW867jzzG/) |
| **#128** | `MEDIUM` | Your user clicked delete my account | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DbDv862jzKb/) |
| **#150** | `CRITICAL` | Your monitoring says green | Layer 12 | [Watch Reel](https://www.instagram.com/reel/Das4Jx8glN_/) |
| **#163** | `CRITICAL` | Customer A logged in and saw customer B's data | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DaiaXxhGx1Z/) |
| **#180** | `CRITICAL` | Your error tracker catches errors your code throws | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DaTdfIAjBkp/) |
| **#183** | `CRITICAL` | Your error tracker catches errors your code throws | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DaRl8xpkdmS/) |
| **#199** | `MEDIUM` | Your logs say everything and tell you nothing | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DaCLbB1khUp/) |
| **#205** | `CRITICAL` | Silent 2 AM Server Crashes: Unhandled Promise Rejections | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DZ8HOqlgZy5/) |
| **#250** | `MEDIUM` | Flat rate | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DZP2LwegIXN/) |
| **#267** | `CRITICAL` | Tech Stack Layer 12 | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DY7iptdRsB0/) |
| **#295** | `CRITICAL` | Hit F12 on your live app | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DYaNabIR0KG/) |
| **#303** | `HIGH` | Your app crashes and you have no idea | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DYR8zObgVsw/) |
| **#313** | `MEDIUM` | Something broke. Users noticed before you did | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DYAwPCav_eC/) |
| **#321** | `MEDIUM` | App breaks | Layer 12 | [Watch Reel](https://www.instagram.com/reel/DXuq33Sjzgh/) |
