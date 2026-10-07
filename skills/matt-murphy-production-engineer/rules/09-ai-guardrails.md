# 🛡️ Rulebook: AI Guardrails, LLM Security & Compliance
**زیرسیستم:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی | **Domain ID:** `09-ai-guardrails` | **Target Layer:** Layer 2
> **Corpus Evidence:** Synthesized from 46 Matt Murphy Production Engineering Masterclasses (6 Critical, 7 High, 33 Medium).

---

## 👑 1. Executive Summary & Core Invariant
In modern high-scale software engineering, **AI Guardrails, LLM Security & Compliance** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.
Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.

### ⚡ The Non-Negotiable Invariant:
> Comply strictly with EU AI Act Article 50: clearly watermarked and labeled Synthetic Generated Information (SGI). Separate untrusted user instructions from system prompts. Enforce strict output schema validation (e.g. Zod) and hard spending caps/circuit breakers on token usage.

---

## 🚨 2. Critical Attack Vectors & Failure Scenarios
Analysis of 46 incidents and breakdowns from this domain:

### 📍 Episode #001: Your AI Product Just Became Illegal (EU AI Act & SGI Compliance) (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** The EU AI Act went live, legally classifying all model-generated copy, avatars, and images as Synthetically Generated Information (SGI). If your application serves AI outputs without explicit disclosure, you face severe statutory fines for deceptive practices.
- **The Root Cause:** Treat synthetic generation as a regulated boundary. Separate AI-produced artifacts at the schema level and maintain an immutable write-only audit trail recording the timestamp, prompt hash, and model used.
- **Matt Murphy Takeaway:** *"Your AI doesn't read legislation—compliance is your job. An immutable generation log demonstrates compliance; absence of one demonstrates negligence."*

### 📍 Episode #036: NIST says most agents run on borrowed credentials (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** NIST says most agents run on borrowed credentials.
- **The Root Cause:** And it's not an argument against AI agents. I think they're awesome. It's an argument for directing them to operate safely.
- **Matt Murphy Takeaway:** *"Direct your agents or they direct themselves."*

### 📍 Episode #060: Your AI agent fetches any URL a user submits (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your AI agent fetches any URL a user submits.
- **The Root Cause:** Your AI agent has the same network access that your server has. It can see internal databases, admin panels, and cloud credentials. So, when a user gives it a URL to fetch, your agent does not ask whether that URL belongs to you or to someone trying to rob you.
- **Matt Murphy Takeaway:** *"Your agent works for you. Make sure it only talks to who you approve."*

### 📍 Episode #119: Your AI built a healthcare app. It has never heard of HIPAA (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your AI built a healthcare app. It has never heard of HIPAA.
- **The Root Cause:** Your AI doesn't know that. It will literally store patient data wherever it wants and it'll transmit it however it feels like it and it'll log it again wherever it wants. So, if your application touches any patient data, student health records or protected health health information, you're already subject to a federal regulation and your AI never asked a single question about it.
- **Matt Murphy Takeaway:** *"Direct your AI to fix that before your first patient walks through the door"*

### 📍 Episode #309: Founder ships on Lovable (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** So, a founder I know built an app on lovable last month
- **The Root Cause:** So, a founder I know built an app on lovable last month
- **Matt Murphy Takeaway:** *"Don't name names, just spill it in the comments"*

### 📍 Episode #310: 250,000 of you watched my videos this week, thank you, I’m (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** 250,000 of you watched my videos this week
- **The Root Cause:** 250,000 of you watched my videos this week
- **Matt Murphy Takeaway:** *"But next week we start solving"*

### 📍 Episode #025: When every news channel says the same thing on the same (Severity: `HIGH`)
- **The Attack Vector / Incident:** When every news channel says the same thing on the same day, I don't get scared. I get suspicious.
- **The Root Cause:** I've been in tech for 30 plus years. I have seen this movie before. So, let's talk about it.
- **Matt Murphy Takeaway:** *"This is not a warning. This is a business strategy. Monopolies disguised as safety are the biggest risk of all."*

### 📍 Episode #029: Two frontier models shipped last week and most builders (Severity: `HIGH`)
- **The Attack Vector / Incident:** Two frontier models shipped last week and most builders never checked the price.
- **The Root Cause:** Whether it went up or down depends on whether you noticed at all. Right. Fable 5.1 and GPT6 Astra both dropped in the same week.
- **Matt Murphy Takeaway:** *"HASHTAGS: #aidirectedengineering #claude #gpt #agents #production"*

### 📍 Episode #088: The SaaS industry is built on feature bloat. That model is (Severity: `HIGH`)
- **The Attack Vector / Incident:** The SaaS industry is built on feature bloat. That model is dying.
- **The Root Cause:** And that model is dead. Every major platform tries to solve every problem for every customer. You know who I'm talking about.
- **Matt Murphy Takeaway:** *"An AI Directed Engineer can build the 50 features you actually use for a fraction of what you pay to rent 1,000 you do not. The economics flipped. The next era gives you ownership."*

### 📍 Episode #114: The better the AI gets, the worse your code is going to be (Severity: `HIGH`)
- **The Attack Vector / Incident:** The better the AI gets, the worse your code is going to be.
- **The Root Cause:** Opus 5 is better. GPT56 is smarter. Fable is unbeatable.
- **Matt Murphy Takeaway:** *"Here is why better models are making this worse."*

---

## ❌ 3. Vibe-Coding Traps vs. Production Reality Matrix
| # | ❌ The Vibe-Coding Trap (What Naive AI Builds) | ✅ Hardened Production Standard |
|---|:---|:---|
| **#001** | Hides AI involvement or assumes users don't care; buries vague disclaimers in Terms of Service. | Enforces non-removable SGI metadata/watermarks, explicit pre-generation user consent gates, and immutable audit logs. |
| **#008** | Filters tenant data in frontend or application code, leaking records across accounts on missed WHERE clauses. | Enforces Row-Level Security (RLS) directly in PostgreSQL, guaranteeing zero cross-tenant data leakage. |
| **#013** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#014** | Stores credentials in client-side localStorage/sessionStorage vulnerable to XSS and malicious dependencies. | Stores tokens in HttpOnly, Secure, SameSite=Lax cookies completely inaccessible to JavaScript. |
| **#025** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#029** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#030** | Configures wildcard `Access-Control-Allow-Origin: *` with credentials enabled, exposing authenticated APIs. | Enforces strict origin allowlists and explicit pre-flight inspection for production APIs. |
| **#036** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#042** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#051** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#060** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#063** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#073** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#081** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#085** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#087** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#088** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#095** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#097** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#100** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#108** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#111** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#113** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#114** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#115** | Leaves endpoints open without rate limiting, allowing scrapers or brute-force bots to drain resources. | Implements token bucket rate limiting at gateway level, throttling abusive IPs with exponential backoff. |
| **#119** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#126** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#130** | Directly trusts incoming POST payload parameters without verifying cryptographic signatures. | Validates digital HMAC signature against raw request buffer and locks event IDs in Redis for idempotency. |
| **#144** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#148** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#152** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#159** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#162** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#168** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#170** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#177** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#236** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#238** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#240** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#241** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#246** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#259** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#281** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#302** | Ships demo code directly into production without verifying boundary limits or failure fallback paths. | Hardens systems with circuit breakers, exponential backoff retries, and isolated fault boundaries. |
| **#309** | Ships demo code directly into production without verifying boundary limits or failure fallback paths. | Hardens systems with circuit breakers, exponential backoff retries, and isolated fault boundaries. |
| **#310** | Ships demo code directly into production without verifying boundary limits or failure fallback paths. | Hardens systems with circuit breakers, exponential backoff retries, and isolated fault boundaries. |

---

## 💻 4. Production-Hardened Code Patterns
The following hardened patterns demonstrate the exact production implementation required:

### Pattern 1: Hardened Implementation for #001 (Your AI Product Just Became Illegal (EU AI Act & SGI Compliance))
```typescript
// middleware/aiAuditLogger.ts
import { Request, Response, NextFunction } from 'express';
import crypto from 'crypto';
import { db } from '../lib/db';

export async function recordAIGenerationLog(req: Request, model: string, prompt: string) {
  const promptHash = crypto.createHash('sha256').update(prompt).digest('hex');
  await db.aiAuditLog.create({
    data: {
      userId: req.user?.id,
      modelUsed: model,
      promptHash: promptHash,
      isSyntheticallyGenerated: true,
      timestamp: new Date(),
    }
  });
}
```

### Pattern 2: Hardened Implementation for #008 (A doctor in Pakistan just vibe coded a HIPAA-compliant)
```typescript
-- migrations/001_row_level_security.sql
ALTER TABLE user_documents ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy ON user_documents
  FOR ALL
  USING (tenant_id = current_setting('app.current_tenant_id', true)::uuid)
  WITH CHECK (tenant_id = current_setting('app.current_tenant_id', true)::uuid);
```

### Pattern 3: Hardened Implementation for #013 (A member failed an exam because her AI argued with the)
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

### Pattern 4: Hardened Implementation for #014 (A founder asked how a solo builder keeps up with compliance)
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

- [ ] AI compliance platforms have collapsed the cost of ongoing monitoring.
- [ ] Add automated regression tests verifying failure scenarios before shipping.
- [ ] Create an immutable audit log table recording timestamp, model version, and SHA-256 prompt hash for every generation.
- [ ] Embed non-removable SGI metadata and visible UI disclosures on all synthetic text, audio, and media.
- [ ] Implement a hard affirmative consent gate before any raw user input touches an LLM endpoint.
- [ ] Implement defense-in-depth guardrails preventing unauthorized state modification.
- [ ] Inspect the existing code paths and identify unvalidated boundary inputs.
- [ ] set a 90-day compliance calendar.
- [ ] standards exist because someone already made the mistake.
- [ ] the model sees the code in front of it.
- [ ] three documents cannot wait until you have revenue.
- [ ] when your AI argues with the standard, that is the moment you are being tested not by the exam, by the work itself.

---

## 📚 6. Full Domain Catalog of Masterclasses
| Episode | Severity | Masterclass Title | Production Layer | Source Reel |
|:---:|:---:|:---|:---:|:---:|
| **#001** | `CRITICAL` | Your AI Product Just Became Illegal (EU AI Act & SGI Compliance) | Layer 2 | [Watch Reel](https://www.instagram.com/reel/Dblxs5jinu-/) |
| **#008** | `MEDIUM` | A doctor in Pakistan just vibe coded a HIPAA-compliant | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DdroHsllR2T/) |
| **#013** | `MEDIUM` | A member failed an exam because her AI argued with the | Layer 2 | [Watch Reel](https://www.instagram.com/reel/Ddl66hIAIkY/) |
| **#014** | `MEDIUM` | A founder asked how a solo builder keeps up with compliance | Layer 2 | [Watch Reel](https://www.instagram.com/reel/Ddj5rEuCSpf/) |
| **#025** | `HIGH` | When every news channel says the same thing on the same | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DdUc_1qClhy/) |
| **#029** | `HIGH` | Two frontier models shipped last week and most builders | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DdMK_2Cj09R/) |
| **#030** | `MEDIUM` | Thousands of people scraped your prompt this week and you | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DdKJvRxjm6M/) |
| **#036** | `CRITICAL` | NIST says most agents run on borrowed credentials | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DdCbUuPFMA9/) |
| **#042** | `MEDIUM` | They call me grandpa AI in the comments | Layer 2 | [Watch Reel](https://www.instagram.com/reel/Dc4IJo3EWLB/) |
| **#051** | `MEDIUM` | You have 47 skills loaded into your AI right now. Half of | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DctRagnk9uk/) |
| **#060** | `CRITICAL` | Your AI agent fetches any URL a user submits | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DceYRVpCFKG/) |
| **#063** | `MEDIUM` | AWS just killed Bedrock Agents. Renamed it to Classic. | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DcbP4U7G6QK/) |
| **#073** | `MEDIUM` | GitHub just showed you exactly where your AI money goes | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DcMWtOgEgaE/) |
| **#081** | `MEDIUM` | Your customers are using a product that has never been | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DcCDhdAiqOZ/) |
| **#085** | `MEDIUM` | MCP is a dead end. Your agent can build its own | Layer 2 | [Watch Reel](https://www.instagram.com/reel/Db856-FiqP7/) |
| **#087** | `MEDIUM` | Your AI is running on six-month-old instructions. That is | Layer 2 | [Watch Reel](https://www.instagram.com/reel/Db6VI3WFqKD/) |
| **#088** | `HIGH` | The SaaS industry is built on feature bloat. That model is | Layer 2 | [Watch Reel](https://www.instagram.com/reel/Db5xi3yEg4w/) |
| **#095** | `MEDIUM` | Your AI agent forgot what it was doing halfway through the | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DbwB5V_EvJS/) |
| **#097** | `MEDIUM` | Your idea is not your moat. Your ability to execute is | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DbtdHYklNf3/) |
| **#100** | `MEDIUM` | Half of you said you do not care about the EU. Got it | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DboLRcsl9ag/) |
| **#108** | `MEDIUM` | Your AI built an app that 1.3 billion people cannot use | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DbaxXyTgbRR/) |
| **#111** | `MEDIUM` | Your next customer might not be a human | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DbYgfWbDWW2/) |
| **#113** | `MEDIUM` | Your AI built your app for one country | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DbVvJBgDv7n/) |
| **#114** | `HIGH` | The better the AI gets, the worse your code is going to be | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DbTtQrCiJZz/) |
| **#115** | `HIGH` | Your AI built your app in a weekend. A security auditor | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DbTF4zkEegn/) |
| **#119** | `CRITICAL` | Your AI built a healthcare app. It has never heard of HIPAA | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DbOGY9aEY0-/) |
| **#126** | `MEDIUM` | The LLMs were never built for what you are using them for | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DbEmNbZE_2X/) |
| **#130** | `MEDIUM` | Your AI built a product. It did not register a business | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DbBCtEGiaMM/) |
| **#144** | `HIGH` | Starting this week every fix script on Instagram has a | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DayGrh5DzUz/) |
| **#148** | `MEDIUM` | Your user clicked delete my account. Now what | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DavJP42gfEJ/) |
| **#152** | `MEDIUM` | Google launched a free AI agents course | Layer 2 | [Watch Reel](https://www.instagram.com/reel/Daq9JyhiZT9/) |
| **#159** | `MEDIUM` | Your AI built the app | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DamFvyUj3U0/) |
| **#162** | `MEDIUM` | Your AI built an API that trusts every request it receives | Layer 2 | [Watch Reel](https://www.instagram.com/reel/Dai-n_LjPMS/) |
| **#168** | `MEDIUM` | Your checkout takes 12 seconds because your AI built the | Layer 2 | [Watch Reel](https://www.instagram.com/reel/Dac-EGTAq7Q/) |
| **#170** | `MEDIUM` | Cursor hit $2B ARR | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DabL4W6DEHs/) |
| **#177** | `MEDIUM` | Your AI built the app | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DaWCNkViYbI/) |
| **#236** | `MEDIUM` | Stop eyeballing your AI outputs | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DZf8_d7PpQZ/) |
| **#238** | `MEDIUM` | Raw AI output should never touch your users | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DZdbRXmv_lb/) |
| **#240** | `MEDIUM` | Agent memory is not one big context dump | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DZa1S1mAYCI/) |
| **#241** | `MEDIUM` | Two multi-agent patterns | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DZaJ_faRdcV/) |
| **#246** | `HIGH` | Your AI app does not need one model | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DZU438dxu9_/) |
| **#259** | `MEDIUM` | Not software engineering | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DZGpm6StEZS/) |
| **#281** | `MEDIUM` | No privacy policy | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DYrvI-fAPC2/) |
| **#302** | `MEDIUM` | We’re building a community of builders, operators, and vibe | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DYSumgevjjU/) |
| **#309** | `CRITICAL` | Founder ships on Lovable | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DYIG09qxms4/) |
| **#310** | `CRITICAL` | 250,000 of you watched my videos this week, thank you, I’m | Layer 2 | [Watch Reel](https://www.instagram.com/reel/DYFlrvbBehK/) |
