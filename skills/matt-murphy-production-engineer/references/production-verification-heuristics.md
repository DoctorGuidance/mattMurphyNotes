# 🔬 Production Verification Heuristics & 13-Layer Diagnostic Manual
> Comprehensive diagnostic questions, failure modes, code smells, and verification gates across all 13 production engineering layers.

---

## 🏛️ Layer 01: UI & Accessibility Hygiene
- **💥 Operational Failure Mode:** User experience collapse, silent input loss, client-side lag, and accessibility lawsuits.
- **⚡ Non-Negotiable Invariant:** UI components must handle all four states; input handlers must never block the event loop; interfaces must satisfy WCAG 2.1 AA.
- **📚 Matt Murphy Masterclasses:** Lessons 067, 136, 161, 289, 291

### 🔍 Diagnostic Checklist:
- [ ] Are all 4 mandatory UI states implemented: Loading skeleton, Error with interactive retry, Empty state with clear next action, and Success state?
- [ ] Is user input on search/filter/autocomplete inputs strictly debounced (300-500ms) to prevent event loop starvation and API floods?
- [ ] Are touch targets sized at least 44x44px with a minimum color contrast ratio of 4.5:1 against backgrounds?
- [ ] Are submit buttons automatically disabled and marked with pending spinners on form submission to prevent duplicate multi-click requests?
- [ ] Are long lists virtualized (react-window/virtualizer) to avoid rendering thousands of DOM nodes simultaneously?

### 🔎 Code Smells & Verification Commands:
> `Grep for `onChange` calling async functions without debounce; grep for naked `<button>` without `disabled={isSubmitting}`; check for missing `<ErrorBoundary>` wrappers.`

---

## 🏛️ Layer 02: APIs & Business Logic
- **💥 Operational Failure Mode:** Unauthorized state modification, mass assignment, unhandled network timeouts, and blind client trust.
- **⚡ Non-Negotiable Invariant:** The frontend is strictly a display layer; 100% of business logic and validation must be re-verified on the server.
- **📚 Matt Murphy Masterclasses:** Lessons 040, 104, 115, 288, 298

### 🔍 Diagnostic Checklist:
- [ ] Are all inbound request bodies validated using strict runtime schemas (Zod `.strict()`), rejecting unknown or injected fields like `isAdmin`?
- [ ] Are external API calls and outbound fetches bounded by explicit timeouts (5-10s) using AbortController to prevent server hang?
- [ ] Do state-mutating requests accept and verify an `Idempotency-Key` header to eliminate duplicate side effects on retries?
- [ ] Are HTTP 200 responses verified to contain actual payload data rather than wrapped error strings (`{ status: 200, error: 'failed' }`)?
- [ ] Is business logic isolated in service layers rather than embedded in route handlers or client components?

### 🔎 Code Smells & Verification Commands:
> `Grep for `fetch(` without `signal`; search for `req.body` passed directly into ORM queries without Zod parse; check for missing HTTP 400 error handlers.`

---

## 🏛️ Layer 03: Database & Storage Engineering
- **💥 Operational Failure Mode:** Connection pool exhaustion, sequential table scans, lost customer data, and slow queries.
- **⚡ Non-Negotiable Invariant:** Zero unindexed queries in production; relational integrity enforced at the database engine; tested continuous recovery.
- **📚 Matt Murphy Masterclasses:** Lessons 003, 045, 065, 174, 192, 211, 216

### 🔍 Diagnostic Checklist:
- [ ] Is connection pooling (PgBouncer or Supavisor) enabled for all database access, especially in serverless runtimes?
- [ ] Does every column participating in `WHERE`, `JOIN`, or `ORDER BY` have an explicit B-tree or composite index?
- [ ] Are Foreign Keys explicitly declared with appropriate `ON DELETE CASCADE` or `SET NULL` policies?
- [ ] Are media assets and binary blobs offloaded to Object Storage (S3) instead of stored in database columns?
- [ ] Has a Point-In-Time Recovery (PITR) restore drill been successfully executed and timed within the last 30 days?
- [ ] Are all multi-step balance or credit mutations wrapped inside atomic ACID database transactions (`$transaction`)?

### 🔎 Code Smells & Verification Commands:
> `Run `EXPLAIN ANALYZE` on top queries; check for port 5432 vs 6543 pooler in serverless DB URLs; grep for `data:image/` strings stored in database fields.`

---

## 🏛️ Layer 04: Auth & Identity Security
- **💥 Operational Failure Mode:** Account takeover, session hijacking, IDOR data exposure, and credential stuffing.
- **⚡ Non-Negotiable Invariant:** Zero auth tokens in localStorage; mandatory composite scoping on direct object lookups; short-lived access credentials.
- **📚 Matt Murphy Masterclasses:** Lessons 043, 044, 048, 118, 124, 160, 206

### 🔍 Diagnostic Checklist:
- [ ] Are authentication tokens stored exclusively in `HttpOnly; Secure; SameSite=Lax` cookies, NEVER in localStorage or sessionStorage?
- [ ] Do direct object queries include composite scoping: `WHERE id = :id AND tenant_id = :tenant_id AND user_id = :user_id` (Anti-IDOR)?
- [ ] Are access tokens short-lived (10-15 minutes) accompanied by server-managed rotating refresh token families?
- [ ] Are OAuth flows protected by state parameter validation and PKCE code challenge verification?
- [ ] Does the JWT verification logic explicitly reject tokens signed with `alg: none` and enforce asymmetric algorithms (RS256)?
- [ ] Is password hashing configured with Argon2id or bcrypt (cost factor >= 12) rather than legacy MD5/SHA algorithms?

### 🔎 Code Smells & Verification Commands:
> `Grep for `localStorage.setItem('token'` or `getItem('jwt'`; grep for `findUnique({ where: { id } })` without tenant check; grep for `jwt.decode` without verify.`

---

## 🏛️ Layer 05: Staging & Environment Parity
- **💥 Operational Failure Mode:** Bugs that work in staging but crash in production; leaked production credentials.
- **⚡ Non-Negotiable Invariant:** Dev, Staging, and Production environments must share identical engine versions, configurations, and isolated credentials.
- **📚 Matt Murphy Masterclasses:** Lessons 090, 119, 137, 281

### 🔍 Diagnostic Checklist:
- [ ] Is the staging database running the identical major.minor database engine version and extensions as production?
- [ ] Are environment variables strictly segregated between preview, staging, and production environments?
- [ ] Are external integrations (Stripe, Twilio, OpenAI) using isolated sandbox credentials in staging?
- [ ] Are seed scripts and mock data prohibited from running against production databases?

### 🔎 Code Smells & Verification Commands:
> `Verify `NODE_ENV` configuration; check `.env.production` is excluded from git; test staging migrations before running on prod.`

---

## 🏛️ Layer 06: Cloud & Compute Reliability
- **💥 Operational Failure Mode:** Runaway cloud billing, hanging serverless invocations, and memory saturation crashes.
- **⚡ Non-Negotiable Invariant:** Every cloud resource must be bounded by hard execution timeouts, memory caps, and budget alarms with automated kill-switches.
- **📚 Matt Murphy Masterclasses:** Lessons 010, 021, 134, 182, 280

### 🔍 Diagnostic Checklist:
- [ ] Are serverless functions bounded by hard execution timeouts (15-30s) to prevent runaway concurrency billing?
- [ ] Are compute containers configured with explicit memory and CPU resource limits to avoid OOM killer cascade?
- [ ] Are cloud egress data paths monitored to prevent unexpected NAT Gateway bandwidth charges?
- [ ] Are billing alert thresholds and automated budget alarms configured in AWS/GCP/Vercel with alert notifications?

### 🔎 Code Smells & Verification Commands:
> `Inspect `vercel.json` or `serverless.yml` for `maxDuration`; verify NAT Gateway egress CloudWatch metrics; verify billing alarm triggers.`

---

## 🏛️ Layer 07: CI/CD & Release Safety
- **💥 Operational Failure Mode:** Production downtime during deployments, broken database migrations, and inability to rollback.
- **⚡ Non-Negotiable Invariant:** Releases must be automated, zero-downtime, backward-compatible, and instantly reversible.
- **📚 Matt Murphy Masterclasses:** Lessons 040, 058, 090, 177, 287

### 🔍 Diagnostic Checklist:
- [ ] Does every deployment pipeline run automated unit and regression tests prior to building artifacts?
- [ ] Are database migrations applied using the expand-and-contract pattern to ensure backward compatibility?
- [ ] Is an automated canary or blue-green deployment strategy configured with automatic rollback on error spike?
- [ ] Are dependency versions pinned and checked against lockfile checksums before packaging?

### 🔎 Code Smells & Verification Commands:
> `Review GitHub Actions / CI workflow steps; test rollback of migrations on staging; verify lockfile integrity in CI.`

---

## 🏛️ Layer 08: Security & Row-Level Defense
- **💥 Operational Failure Mode:** Data leaks between organizations, exposed private keys, clickjacking, and XSS.
- **⚡ Non-Negotiable Invariant:** Zero secret leaks in client bundles; database Row Level Security (RLS) active on all multi-tenant tables; strict CORS allowlists.
- **📚 Matt Murphy Masterclasses:** Lessons 004, 005, 014, 015, 066, 105, 276

### 🔍 Diagnostic Checklist:
- [ ] Is Row Level Security (RLS) enabled on every PostgreSQL table containing multi-tenant or multi-user records?
- [ ] Are API keys, database credentials, and service roles excluded from client bundles (`NEXT_PUBLIC_` / `VITE_` audits)?
- [ ] Is CORS strictly configured with an explicit domain whitelist rather than wildcard `*` on authenticated APIs?
- [ ] Are clickjacking framing attacks blocked via `X-Frame-Options: DENY` or CSP `frame-ancestors 'none'`?
- [ ] Are untrusted user HTML payloads sanitized with DOMPurify before rendering?

### 🔎 Code Smells & Verification Commands:
> `Grep for `NEXT_PUBLIC_.*SECRET` or `SERVICE_ROLE`; grep for `Access-Control-Allow-Origin: *`; verify `ALTER TABLE ... ENABLE ROW LEVEL SECURITY;`.`

---

## 🏛️ Layer 09: Rate Limiting & Abuse Prevention
- **💥 Operational Failure Mode:** Denial of service, credential stuffing, scraping, and unexpected LLM token bills.
- **⚡ Non-Negotiable Invariant:** All public and authenticated routes must be throttled by multi-tier token bucket rate limiting backed by Redis.
- **📚 Matt Murphy Masterclasses:** Lessons 052, 103, 104, 215

### 🔍 Diagnostic Checklist:
- [ ] Is Redis-backed Token Bucket rate limiting applied to all public, auth, and LLM endpoints?
- [ ] Are rate limits tiered across unauthenticated IP caps, authenticated user sessions, and enterprise tenant keys?
- [ ] Does the rate limiter return standard HTTP 429 status codes with explicit `Retry-After` headers?
- [ ] Are brute-force login attempts penalized with exponential backoff delays?

### 🔎 Code Smells & Verification Commands:
> `Inspect middleware registration on `/api/auth/*` and `/api/generate`; test curl burst requests to verify 429 response.`

---

## 🏛️ Layer 10: Caching & CDN Edge Strategy
- **💥 Operational Failure Mode:** Thundering herd cache stampedes, stale data served to users, and cross-tenant cache leaks.
- **⚡ Non-Negotiable Invariant:** Cache keys must be tenant-namespaced; stampedes prevented with distributed mutex locks; cache invalidation event-driven.
- **📚 Matt Murphy Masterclasses:** Lessons 003, 011, 019, 055, 080

### 🔍 Diagnostic Checklist:
- [ ] Are cached keys explicitly namespaced by tenant ID (`tenant:{id}:key`) to prevent cross-tenant data leaks?
- [ ] Is Dogpile / Thundering Herd stampede prevented using distributed mutex locks or probabilistic early expiration?
- [ ] Is cache invalidation hooked into database mutations rather than relying purely on time-to-live (TTL)?
- [ ] Are public static assets served through a CDN with immutable cache headers and content hashing?

### 🔎 Code Smells & Verification Commands:
> `Inspect Redis cache key format; test cache stampede behavior under simulated load; check Cache-Control headers on static assets.`

---

## 🏛️ Layer 11: Connection Pooling & Resource Limits
- **💥 Operational Failure Mode:** Database connection exhaustion (`too many clients`), server freezing, and thread lock.
- **⚡ Non-Negotiable Invariant:** Application connection pools must be sized below database engine capacity; connections released in finally blocks.
- **📚 Matt Murphy Masterclasses:** Lessons 003, 174, 203, 275

### 🔍 Diagnostic Checklist:
- [ ] Is the application pool size configured strictly below the database server's maximum connection capacity?
- [ ] Are connection acquisition timeouts configured to fail fast rather than hanging threads indefinitely?
- [ ] Are database connections properly closed/released back to the pool in finally blocks?
- [ ] Are long-running analytical queries routed to a read replica rather than the primary transactional pool?

### 🔎 Code Smells & Verification Commands:
> `Check `max_connections` in PostgreSQL config; review pool settings in Prisma/TypeORM/Drizzle; verify replica routing.`

---

## 🏛️ Layer 12: Observability & Error Tracing
- **💥 Operational Failure Mode:** Silent production outages, unmonitored exceptions, and inability to trace customer errors.
- **⚡ Non-Negotiable Invariant:** Structured JSON logs with correlation IDs; centralized exception capture with PII scrubbing; health check probes.
- **📚 Matt Murphy Masterclasses:** Lessons 002, 180, 183, 205, 289

### 🔍 Diagnostic Checklist:
- [ ] Are all server logs formatted as structured JSON with ISO timestamps, severity levels, and sanitized contexts?
- [ ] Is an `x-request-id` correlation token generated at the edge and propagated across all services and DB queries?
- [ ] Are stack traces captured and grouped in Sentry with sensitive customer PII scrubbed at the logging boundary?
- [ ] Are global handlers registered for `uncaughtException` and `unhandledRejection` with graceful process restart?
- [ ] Are separate `/health/live` (liveness) and `/health/ready` (readiness) probes monitored by infrastructure orchestrators?

### 🔎 Code Smells & Verification Commands:
> `Grep for raw `console.log(`; check for Sentry initialization; test process crash behavior under simulated uncaught error.`

---

## 🏛️ Layer 13: Disaster Recovery & Redundancy
- **💥 Operational Failure Mode:** Catastrophic unrecoverable data loss, ransomware lockouts, and extended downtime.
- **⚡ Non-Negotiable Invariant:** Backups must be continuous, offsite, immutable, and regularly verified via automated restore drills.
- **📚 Matt Murphy Masterclasses:** Lessons 065, 174, 180, 290

### 🔍 Diagnostic Checklist:
- [ ] Are automated database backups verified with automated spin-up test restores at least monthly?
- [ ] Is the Recovery Time Objective (RTO) and Recovery Point Objective (RPO) explicitly defined and tested against SLAs?
- [ ] Is critical object storage (S3) configured with cross-region replication and object versioning against deletion?
- [ ] Is an emergency runbook documented for DNS failover and database failover during cloud provider outages?

### 🔎 Code Smells & Verification Commands:
> `Inspect automated PITR restore drill logs; verify S3 versioning and MFA delete configuration; review disaster recovery runbook.`

---

