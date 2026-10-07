# 🛡️ Rulebook: Database & Storage Engineering
**زیرسیستم:** پایگاه‌داده، روابط، ایندکس و پایداری داده | **Domain ID:** `03-database-storage` | **Target Layer:** Layer 3
> **Corpus Evidence:** Synthesized from 33 Matt Murphy Production Engineering Masterclasses (7 Critical, 9 High, 17 Medium).

---

## 👑 1. Executive Summary & Core Invariant
In modern high-scale software engineering, **Database & Storage Engineering** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.
Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.

### ⚡ The Non-Negotiable Invariant:
> Direct database connections in serverless or high-concurrency environments are strictly prohibited; PgBouncer / Supavisor connection pooling is mandatory. Every query column in `WHERE`, `JOIN`, or `ORDER BY` must be covered by a B-Tree or composite index. Relational integrity via Foreign Keys is required.

---

## 🚨 2. Critical Attack Vectors & Failure Scenarios
Analysis of 33 incidents and breakdowns from this domain:

### 📍 Episode #003: 50 Users Sign Up and Crash Your Database (Connection Pooling & Caching) (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** 50 users sign up concurrently. The server opens 50 unmanaged database connections. PostgreSQL reaches its connection limit, queries queue up, and the entire app displays the blank screen of death.
- **The Root Cause:** Databases have strict hardware connection limits. Multiplex database connections through a connection pooler (PgBouncer/Supavisor) and protect read-heavy queries with an in-memory caching tier.
- **Matt Murphy Takeaway:** *"If your database breaks in a load test, you fix it quietly. If it breaks in production, you lose customers loudly."*

### 📍 Episode #045: Your AI put your database credentials in a Next.js Server (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your AI put your database credentials in a Next.js Server Action.
- **The Root Cause:** Your AI built your Nex.js. It wrote server functions that query your database directly, but it put server logic and client components in the exact same file. So Nex.js analyzed the imports, decided your server dependencies belonged on the client side, and included your database connection string in the code.
- **Matt Murphy Takeaway:** *"Your server functions run on the server. Your credentials should stay there."*

### 📍 Episode #099: Your user just saw your database password on their screen (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your user just saw your database password on their screen.
- **The Root Cause:** Instead of a friendly error message, it dumped a raw stack trace with your database connection string, your framework versions, and the exact line of code that failed. That's not a bug, people. That is your AI showing the world exactly how to break into your application.
- **Matt Murphy Takeaway:** *"Split your error handling. Catch errors at every boundary. Build a logging pipeline. Fix it today."*

### 📍 Episode #193: You changed a field name (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You changed a field name.
- **The Root Cause:** That's not a win. So, here are the three things you're going to do right now to fix it. Step one, define the contract clearly.
- **Matt Murphy Takeaway:** *"Your API had no contract and no versioning."*

### 📍 Episode #232: Everyone is shopping for a vector database (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Everyone is shopping for a vector database.
- **The Root Cause:** Here are the three things you need to know right now. Step one, PG vector exists. One extension turns your existing Postgress database into a vector store.
- **Matt Murphy Takeaway:** *"Postgres just quietly became all of them."*

### 📍 Episode #288: Your frontend talks to the database directly (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your frontend talks to the database directly.
- **The Root Cause:** That's a security hole with UI. Layer two of 13 is where your app's brain lives. Business logic, data validation, rate limiting, request authentication.
- **Matt Murphy Takeaway:** *"It's time to lock it up so you can ship"*

### 📍 Episode #298: Your app works great (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Your app works great.
- **The Root Cause:** Well, here's how you're going to fix it. Number one, abstract your API calls. Never call an API directly from your main code.
- **Matt Murphy Takeaway:** *"Don’t build your house on rented land. Own the foundation, rent the features."*

### 📍 Episode #053: Your database has been doing a full table scan on every (Severity: `HIGH`)
- **The Attack Vector / Incident:** Your database has been doing a full table scan on every request since launch.
- **The Root Cause:** So your AI wrote the queries, right? They worked, pages loaded, data showed up. What you did not see is that every query was reading every row in the table to find the one row it needed.
- **Matt Murphy Takeaway:** *"Fix it before your hosting provider fixes it for you."*

### 📍 Episode #066: You added one column to your database for one client. Every (Severity: `HIGH`)
- **The Attack Vector / Incident:** You added one column to your database for one client. Every other client's queries slowed down by 40%.
- **The Root Cause:** So one client wanted a custom field on every single record and a new column in the shared schema that only they were using. So now every query, every migration, every backup and every restore carries a custom field that 99% of the clients never asked for or see. So one client's feature requ trust just became every client's technical debt and every client is paying for it in performance.
- **Matt Murphy Takeaway:** *"Say yes to your biggest client. Say it architecturally."*

### 📍 Episode #079: Your database just lost 14 hours of customer data (Severity: `HIGH`)
- **The Attack Vector / Incident:** Your database just lost 14 hours of customer data.
- **The Root Cause:** Everything users did today. Every transaction, every upload, every message, every account change gone. Because your AI set up nightly backups, but your database failed at 2 p.m.
- **Matt Murphy Takeaway:** *"Your backup is not your recovery plan. Your tested plan is."*

---

## ❌ 3. Vibe-Coding Traps vs. Production Reality Matrix
| # | ❌ The Vibe-Coding Trap (What Naive AI Builds) | ✅ Hardened Production Standard |
|---|:---|:---|
| **#003** | Creates a new database connection per HTTP request without pooling; queries identical data on every render. | Routes traffic through transaction poolers (PgBouncer) allowing 50 requests to share 10 connections; caches hot data in Redis. |
| **#045** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#053** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#066** | Filters tenant data in frontend or application code, leaking records across accounts on missed WHERE clauses. | Enforces Row-Level Security (RLS) directly in PostgreSQL, guaranteeing zero cross-tenant data leakage. |
| **#072** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#079** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#094** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#099** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#149** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#151** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#153** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#174** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#176** | Sends raw user input straight to LLMs and streams unverified model outputs directly to client browsers. | Applies schema validation, prompt sanitization, consent gates, and immutable audit logs with SGI metadata. |
| **#192** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#193** | Relies on unverified AI code assumptions without failure handling or production boundaries in Database & Storage Engineering. | Applies hardened architectural patterns, strict input boundaries, and automated monitoring for Database & Storage Engineering. |
| **#196** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#210** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#211** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#216** | Configures wildcard `Access-Control-Allow-Origin: *` with credentials enabled, exposing authenticated APIs. | Enforces strict origin allowlists and explicit pre-flight inspection for production APIs. |
| **#224** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#229** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#232** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#237** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#252** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#262** | Filters tenant data in frontend or application code, leaking records across accounts on missed WHERE clauses. | Enforces Row-Level Security (RLS) directly in PostgreSQL, guaranteeing zero cross-tenant data leakage. |
| **#264** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#265** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#272** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#277** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#287** | Relies on default primary keys without composite or covering indexes, causing sequential full-table scans. | Defines covering and composite indexes matching exact query access patterns with foreign key constraints. |
| **#288** | Leaves endpoints open without rate limiting, allowing scrapers or brute-force bots to drain resources. | Implements token bucket rate limiting at gateway level, throttling abusive IPs with exponential backoff. |
| **#298** | Leaves endpoints open without rate limiting, allowing scrapers or brute-force bots to drain resources. | Implements token bucket rate limiting at gateway level, throttling abusive IPs with exponential backoff. |
| **#320** | Assumes database queries that worked with 10 users will scale without indexes under concurrent load. | Optimizes connection pool transactions and implements partial indexes targeting active workloads. |

---

## 💻 4. Production-Hardened Code Patterns
The following hardened patterns demonstrate the exact production implementation required:

### Pattern 1: Hardened Implementation for #003 (50 Users Sign Up and Crash Your Database (Connection Pooling & Caching))
```typescript
// lib/db.ts - Prisma Connection Pooling Configuration
import { PrismaClient } from '@prisma/client';

// Always route app queries through PgBouncer connection string
const prisma = new PrismaClient({
  datasources: {
    db: {
      url: process.env.DATABASE_URL_POOLED, // e.g. postgresql://...?pgbouncer=true
    },
  },
});
export default prisma;
```

### Pattern 2: Hardened Implementation for #045 (Your AI put your database credentials in a Next.js Server)
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

### Pattern 3: Hardened Implementation for #053 (Your database has been doing a full table scan on every)
```typescript
-- migrations/002_composite_indexes.sql
-- Eliminate table scans and guarantee unique constraints
CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS idx_users_org_email 
  ON users (organization_id, LOWER(email));

-- Covering index for frequent filtered lookups
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_customer_status_created 
  ON orders (customer_id, status) INCLUDE (total_amount, created_at);
```

### Pattern 4: Hardened Implementation for #066 (You added one column to your database for one client. Every)
```typescript
-- migrations/001_row_level_security.sql
ALTER TABLE user_documents ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy ON user_documents
  FOR ALL
  USING (tenant_id = current_setting('app.current_tenant_id', true)::uuid)
  WITH CHECK (tenant_id = current_setting('app.current_tenant_id', true)::uuid);
```

---

## 📋 5. Architectural Checklist & Verification Heuristics
Before shipping any code in this domain, verify each item:

- [ ] Add a Redis/Upstash caching layer for any data that changes less frequently than once per minute.
- [ ] Enable connection pooling on the database (Supabase pooler port 6543 or PgBouncer in transaction mode).
- [ ] Run automated load tests using k6 or Artillery before launch to discover connection bottlenecks in staging.
- [ ] install the serveronly package and mark every sensitive file.
- [ ] per tenant schema extensions without shared schema pollution.
- [ ] scan your deployed code for leaked secrets.
- [ ] separate server logic and client components into different files.
- [ ] tenant isolated compute for heavy or custom workloads.
- [ ] tenant scoped migration pass.
- [ ] you have no visibility into which queries are slow.
- [ ] your AI never added indexes to your database.
- [ ] your queries are pulling more data than your pages actually need.

---

## 📚 6. Full Domain Catalog of Masterclasses
| Episode | Severity | Masterclass Title | Production Layer | Source Reel |
|:---:|:---:|:---|:---:|:---:|
| **#003** | `CRITICAL` | 50 Users Sign Up and Crash Your Database (Connection Pooling & Caching) | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DYkAobpgwjI/) |
| **#045** | `CRITICAL` | Your AI put your database credentials in a Next.js Server | Layer 3 | [Watch Reel](https://www.instagram.com/reel/Dc0_yCoHNXv/) |
| **#053** | `HIGH` | Your database has been doing a full table scan on every | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DcqspRtHPGB/) |
| **#066** | `HIGH` | You added one column to your database for one client. Every | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DcWGRX2G2l8/) |
| **#072** | `MEDIUM` | Your database has two versions of every record right now | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DcOX9AdERD2/) |
| **#079** | `HIGH` | Your database just lost 14 hours of customer data | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DcEoX9xCZ8Q/) |
| **#094** | `MEDIUM` | Your AI built your database. It never planned for the day | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DbyDJomAkQv/) |
| **#099** | `CRITICAL` | Your user just saw your database password on their screen | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DbqUuqlk7L6/) |
| **#149** | `MEDIUM` | MCP crossed 97M monthly downloads. 19,000 servers | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DatgvgjkmS_/) |
| **#151** | `MEDIUM` | Your database changed | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DasnI0OlWM3/) |
| **#153** | `HIGH` | The database you started with is not the one you need | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DaqooTiEUY4/) |
| **#174** | `MEDIUM` | Three backup decisions you make right now | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DaYW16Ojg1C/) |
| **#176** | `MEDIUM` | It's the Fourth of July | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DaX0eVMjoVf/) |
| **#192** | `MEDIUM` | Your database has a backup | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DaI4bPSlUBj/) |
| **#193** | `CRITICAL` | You changed a field name | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DaIUwXBlLf_/) |
| **#196** | `MEDIUM` | Your database answers the same question a thousand times a | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DaEXXLvEf6L/) |
| **#210** | `MEDIUM` | Convex is blowing up | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DZ3G-nTPl9F/) |
| **#211** | `MEDIUM` | Prisma protects you from the database | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DZ20J4SRMkE/) |
| **#216** | `MEDIUM` | Images do not belong in database columns | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DZxfOW9xsFD/) |
| **#224** | `HIGH` | You added indexes and your app is still slow | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DZp7APuRdvP/) |
| **#229** | `MEDIUM` | Half of the questions in my DMs are about this topic | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DZlTwapPlLC/) |
| **#232** | `CRITICAL` | Everyone is shopping for a vector database | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DZisZ_9v0RW/) |
| **#237** | `HIGH` | Your database is doing the same work on every request | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DZfT4d5AiWg/) |
| **#252** | `HIGH` | 50 users | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DZNMhyvxyha/) |
| **#262** | `MEDIUM` | Ten million rows | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DZDUWLJRpZ8/) |
| **#264** | `MEDIUM` | Supabase. Firebase. Neon. Convex | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DZALI2bRljh/) |
| **#265** | `HIGH` | Tech Stack Layer 13 of 13 | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DY-UCtORgDS/) |
| **#272** | `MEDIUM` | Your database doesn’t have to live with your app | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DY1-cZaRlSD/) |
| **#277** | `MEDIUM` | Your app was written by AI | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DYwyDG3xBlg/) |
| **#287** | `MEDIUM` | 47 columns | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DYklzbex7me/) |
| **#288** | `CRITICAL` | Your frontend talks to the database directly | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DYiSfwGP2D9/) |
| **#298** | `CRITICAL` | Your app works great | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DYXGdH4AtnZ/) |
| **#320** | `HIGH` | 10 users fine | Layer 3 | [Watch Reel](https://www.instagram.com/reel/DXwtOTDA-gx/) |
