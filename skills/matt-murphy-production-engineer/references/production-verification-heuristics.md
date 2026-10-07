# 🔬 Production Verification Heuristics & Diagnostic Questions
> Deep diagnostic questions and verification gates for every layer of the modern production stack.

---

### Layer 01: UI & Accessibility Hygiene
- [ ] **Diagnostic Check:** Are all 4 UI states (Loading skeleton, Error with Retry, Empty state, Success) fully implemented and tested?
- [ ] **Diagnostic Check:** Is user input debounced on search/filter to prevent event loop saturation?
- [ ] **Diagnostic Check:** Are touch targets at least 44x44px with WCAG 4.5:1 color contrast ratio?
- [ ] **Diagnostic Check:** Does the UI prevent multi-click duplicate submissions by disabling buttons on pending state?

### Layer 02: APIs & Business Logic
- [ ] **Diagnostic Check:** Is the frontend treated strictly as a display layer, with 100% of validation re-enforced on the server?
- [ ] **Diagnostic Check:** Are API endpoints protected by request timeouts (e.g. 5-10s) using AbortController or server timeouts?
- [ ] **Diagnostic Check:** Do state-mutating requests accept and verify an Idempotency-Key header to prevent duplicate side effects?
- [ ] **Diagnostic Check:** Are HTTP 200 responses verified to contain actual valid data rather than wrapped error strings?

### Layer 03: Database & Storage Engineering
- [ ] **Diagnostic Check:** Is connection pooling (PgBouncer, Supavisor) active for all database access, especially serverless functions?
- [ ] **Diagnostic Check:** Does every WHERE, JOIN, and ORDER BY column have an explicit B-tree or composite index?
- [ ] **Diagnostic Check:** Are foreign keys explicitly defined with CASCADE or SET NULL policies to prevent orphaned records?
- [ ] **Diagnostic Check:** Has an automated Point-In-Time Recovery (PITR) restore drill been executed within the last 30 days?

### Layer 04: Auth & Identity Security
- [ ] **Diagnostic Check:** Are authentication tokens stored exclusively in HttpOnly, Secure, SameSite=Lax cookies, NEVER in localStorage?
- [ ] **Diagnostic Check:** Do direct object queries include composite scoping: `WHERE id = :id AND tenant_id = :tenant_id` (Anti-IDOR)?
- [ ] **Diagnostic Check:** Are access tokens short-lived (10-15 minutes) with rotating refresh token families?
- [ ] **Diagnostic Check:** Are OAuth flows protected by state parameter validation and PKCE code challenge verification?

### Layer 05: Staging & Environment Parity
- [ ] **Diagnostic Check:** Is the staging database running the identical major.minor database version and extensions as production?
- [ ] **Diagnostic Check:** Are environment variables strictly segregated between preview, staging, and production environments?
- [ ] **Diagnostic Check:** Are external APIs (Stripe, Twilio, OpenAI) using isolated sandbox credentials in staging?

### Layer 06: Cloud & Compute Reliability
- [ ] **Diagnostic Check:** Are serverless functions bounded by hard execution timeouts (e.g. 15-30s) to prevent runaway billing?
- [ ] **Diagnostic Check:** Are egress data paths monitored to prevent unexpected NAT Gateway bandwidth charges?
- [ ] **Diagnostic Check:** Are auto-scaling groups configured with hard maximum instance limits and billing alert thresholds?

### Layer 07: CI/CD & Release Safety
- [ ] **Diagnostic Check:** Does every release pipeline run automated unit and regression tests prior to artifact creation?
- [ ] **Diagnostic Check:** Are database migrations applied in a backward-compatible manner (expand-and-contract pattern)?
- [ ] **Diagnostic Check:** Is an automated rollback runbook configured for canary/blue-green deployment failures?

### Layer 08: Security & Row-Level Defense
- [ ] **Diagnostic Check:** Is Row Level Security (RLS) enabled on all tables containing multi-user or multi-tenant records?
- [ ] **Diagnostic Check:** Are all API keys, database credentials, and service roles excluded from client bundles and git commits?
- [ ] **Diagnostic Check:** Is CORS strictly configured with an explicit domain whitelist rather than wildcard `*`?
- [ ] **Diagnostic Check:** Are clickjacking framing attacks blocked via `X-Frame-Options: DENY` or CSP `frame-ancestors 'none'`?

### Layer 09: Rate Limiting & Abuse Prevention
- [ ] **Diagnostic Check:** Is Redis-backed Token Bucket rate limiting applied to all public, auth, and LLM endpoints?
- [ ] **Diagnostic Check:** Are rate limits tiered across IP caps (unauthenticated), user sessions, and tenant API keys?
- [ ] **Diagnostic Check:** Does the rate limiter return HTTP 429 with explicit `Retry-After` response headers?

### Layer 10: Caching & CDN Edge Strategy
- [ ] **Diagnostic Check:** Are cached keys explicitly namespaced by tenant ID (`tenant:{id}:key`) to prevent data leakage?
- [ ] **Diagnostic Check:** Is Dogpile / Thundering Herd stampede prevented using distributed mutex locks?
- [ ] **Diagnostic Check:** Is cache invalidation hooked into database mutations rather than relying purely on time-to-live (TTL)?

### Layer 11: Connection Pooling & Resource Limits
- [ ] **Diagnostic Check:** Is the application pool size configured strictly below the database server's max connection capacity?
- [ ] **Diagnostic Check:** Are connection timeouts configured to fail fast rather than hanging threads indefinitely?
- [ ] **Diagnostic Check:** Are database connections properly closed/released back to the pool in finally blocks?

### Layer 12: Observability & Error Tracing
- [ ] **Diagnostic Check:** Are all server logs formatted as structured JSON with ISO timestamps, log levels, and context?
- [ ] **Diagnostic Check:** Is an `x-request-id` correlation token propagated across all microservices and database queries?
- [ ] **Diagnostic Check:** Are stack traces captured and grouped in Sentry or equivalent error monitoring with PII stripped?
- [ ] **Diagnostic Check:** Are health check probes (`/health/live` and `/health/ready`) separated and monitored?

### Layer 13: Disaster Recovery & Redundancy
- [ ] **Diagnostic Check:** Are automated database backups verified with automated spin-up test restores?
- [ ] **Diagnostic Check:** Is the RTO (Recovery Time Objective) and RPO (Recovery Point Objective) explicitly defined and tested?
- [ ] **Diagnostic Check:** Is critical object storage (S3) configured with cross-region replication or versioning against ransomware?

