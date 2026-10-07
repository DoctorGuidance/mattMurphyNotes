# 🛡️ Rulebook: Caching & Edge Performance
**زیرسیستم:** کشینگ، توزیع لبه و پرفورمنس سیستمی | **Domain ID:** `04-caching-performance` | **Target Layer:** Layer 10
> **Corpus Evidence:** Synthesized from 12 Matt Murphy Production Engineering Masterclasses (3 Critical, 1 High, 8 Medium).

---

## 👑 1. Executive Summary & Core Invariant
In modern high-scale software engineering, **Caching & Edge Performance** is not a cosmetic detail or an afterthought—it is a critical reliability boundary.
Naive 'vibe-coding' implementations frequently collapse under concurrency, expose catastrophic security holes, or run up thousands of dollars in unexpected bills.

### ⚡ The Non-Negotiable Invariant:
> Never cache without a deterministic invalidation strategy. Prevent Dogpile/Thundering Herd stampedes using distributed mutex locks or probabilistic early expiration. All cached keys must be tenant-namespaced (`tenant:{id}:key`) to prevent cross-tenant data leaks.

---

## 🚨 2. Critical Attack Vectors & Failure Scenarios
Analysis of 12 incidents and breakdowns from this domain:

### 📍 Episode #077: You put Cloudflare in front of your app (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** You put Cloudflare in front of your app.
- **The Root Cause:** Cloudflare only protects you if all traffic is flowing through it. The moment someone finds your real IP, they skip everything. that you set up.
- **Matt Murphy Takeaway:** *"Cloudflare is not a switch you flip. It is an architecture you configure."*

### 📍 Episode #104: A customer just called you. They are looking at someone (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** A customer just called you. They are looking at someone else's revenue dashboard. Their invoices. Their customer list. Their monthly revenue. Your AI cached a query result without scoping it to the tenant.
- **The Root Cause:** So, your AI set up caching to speed up your app, but it never scoped the cache to the appropriate tenant. So, customer A loaded their dashboard and the result got cached. Customer B loaded the same page and boom, your cash served customer A's financial data instantly to customer B.
- **Matt Murphy Takeaway:** *"One cached query. Two customers. Zero trust left in your product. Your database security is irrelevant if your cache layer bypasses it."*

### 📍 Episode #171: Nobody decides to build a caching strategy (Severity: `CRITICAL`)
- **The Attack Vector / Incident:** Nobody decides to build a caching strategy.
- **The Root Cause:** Somebody adds redis. The app gets faster. Everybody moves on.
- **Matt Murphy Takeaway:** *"Caching is not a performance feature. It is a business decision about how wrong your data is allowed to be."*

### 📍 Episode #271: Tech Stack Layer 10 of 13 (Severity: `HIGH`)
- **The Attack Vector / Incident:** Tech Stack Layer 10 of 13.
- **The Root Cause:** And your users, they don't care. They just see slow. And no one likes slow.
- **Matt Murphy Takeaway:** *"Your bill knows all about it."*

---

## ❌ 3. Vibe-Coding Traps vs. Production Reality Matrix
| # | ❌ The Vibe-Coding Trap (What Naive AI Builds) | ✅ Hardened Production Standard |
|---|:---|:---|
| **#012** | Sends identical repetitive prompts to expensive cloud LLMs on every request without caching deterministic model completions. | Caches deterministic LLM completions in Redis using prompt hashes as cache keys, drastically slashing API costs and latency. |
| **#019** | Re-computes semantic similarity and vector lookups for identical queries instead of leveraging semantic cache layers. | Deploys semantic vector caching (GPTCache/Redis) to return cached completions for semantically equivalent user questions. |
| **#039** | Ships frequent code updates without versioning cache keys, serving stale legacy assets and crashing frontend clients. | Incorporates git commit deployment hashes into cache keys and asset URLs (`Cache-Busting`) to guarantee immediate cache updates. |
| **#077** | Puts Cloudflare in front of an application with naive default cache settings, accidentally caching dynamic user sessions at the edge. | Configures explicit `Cache-Control: private, no-store` on authenticated routes while caching purely static assets at the CDN edge. |
| **#104** | Caches database query results using global static keys without tenant scoping, leaking Customer A's dashboard to Customer B. | Prefixes all cache keys with tenant and user boundaries (`cache:tenant_{id}:user_{id}:dashboard`) to prevent cross-tenant data leaks. |
| **#116** | Hits primary databases directly for high-traffic public profile pages, buckling under sudden viral social media traffic spikes. | Serves high-read public pages from distributed edge caches with stale-while-revalidate policies, shielding backend origins. |
| **#171** | Adds ad-hoc in-memory caching variables across controllers, causing inconsistent state across multiple server instances. | Standardizes on centralized Redis clusters with explicit TTLs and event-driven cache invalidation patterns (Cache-Aside). |
| **#186** | Designs write-heavy workloads with aggressive read-caching architectures, causing cache thrashing and lock contention. | Analyzes application read-write ratios to pick optimal caching topologies: Write-Through for reads vs append buffers for writes. |
| **#197** | Caches rapidly mutating transactional states like inventory balances, causing overselling and financial reconciliation bugs. | Restricts caching to static, reference, or read-heavy data while reading volatile transactional state directly from ACID databases. |
| **#214** | Adds Redis without connection pooling or serialization optimizations, spending more time in network roundtrips than SQL queries. | Implements connection pooling, binary serialization (MessagePack/Protobuf), and batch pipelining for Redis interactions. |
| **#263** | Deploys single-region backends serving global users, imposing 300ms network round-trip latencies on overseas customers. | Distributes static content and read replicas via edge networks and global CDNs to achieve sub-50ms latency worldwide. |
| **#271** | Treats Layer 10 Caching as a band-aid for broken database indexes rather than a deliberate architectural tier. | Hardens database indexes first, then layers Redis caching with strict TTLs and distributed mutex locks against dogpiling. |

---

## 💻 4. Production-Hardened Code Patterns
The following hardened patterns demonstrate the exact production implementation required:

### Pattern 1: Hardened Implementation for #012 (The CEO of the most influential AI company on the planet)
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

### Pattern 2: Hardened Implementation for #019 (Everyone asked the same question this week)
```typescript
-- migrations/002_composite_indexes.sql
-- Eliminate table scans and guarantee unique constraints
CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS idx_users_org_email 
  ON users (organization_id, LOWER(email));

-- Covering index for frequent filtered lookups
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_customer_status_created 
  ON orders (customer_id, status) INCLUDE (total_amount, created_at);
```

### Pattern 3: Hardened Implementation for #039 (Your AI shipped three products this quarter)
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

### Pattern 4: Hardened Implementation for #077 (You put Cloudflare in front of your app)
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
- [ ] a weekly content audit system that tells you exactly what's working and what to kill.
- [ ] caching is not the only shared layer leaking.
- [ ] distribution is the new moat.
- [ ] one product that converts at 5% beats 10 that converted zero.
- [ ] test this before your customer figures it out.
- [ ] your SSL is probably set to flexible.
- [ ] your database security is irrelevant if your cache layer completely bypasses it.
- [ ] your origin IP is leaking.
- [ ] your origin server still accepts connections from the entire internet.

---

## 📚 6. Full Domain Catalog of Masterclasses
| Episode | Severity | Masterclass Title | Production Layer | Source Reel |
|:---:|:---:|:---|:---:|:---:|
| **#012** | `MEDIUM` | The CEO of the most influential AI company on the planet | Layer 10 | [Watch Reel](https://www.instagram.com/reel/DdmeiTlACNc/) |
| **#019** | `MEDIUM` | Everyone asked the same question this week | Layer 10 | [Watch Reel](https://www.instagram.com/reel/DdcLYmyCCXH/) |
| **#039** | `MEDIUM` | Your AI shipped three products this quarter | Layer 10 | [Watch Reel](https://www.instagram.com/reel/Dc9Rv5LksSj/) |
| **#077** | `CRITICAL` | You put Cloudflare in front of your app | Layer 10 | [Watch Reel](https://www.instagram.com/reel/DcHNH00EZ1T/) |
| **#104** | `CRITICAL` | A customer just called you. They are looking at someone | Layer 10 | [Watch Reel](https://www.instagram.com/reel/DbimVuCkZqi/) |
| **#116** | `MEDIUM` | Zero to 50,000+ followers in 90 days | Layer 10 | [Watch Reel](https://www.instagram.com/reel/DbQzWwMlS-F/) |
| **#171** | `CRITICAL` | Nobody decides to build a caching strategy | Layer 10 | [Watch Reel](https://www.instagram.com/reel/Daa2AoBkiC3/) |
| **#186** | `MEDIUM` | Read-write ratio determines the architecture | Layer 10 | [Watch Reel](https://www.instagram.com/reel/DaOZMI2CCGx/) |
| **#197** | `MEDIUM` | Not Everything Should Be Cached | Layer 10 | [Watch Reel](https://www.instagram.com/reel/DaDuf2DFSP-/) |
| **#214** | `MEDIUM` | You added Redis and your app got faster | Layer 10 | [Watch Reel](https://www.instagram.com/reel/DZz3QjsAx7r/) |
| **#263** | `MEDIUM` | Your app is fast in Virginia | Layer 10 | [Watch Reel](https://www.instagram.com/reel/DZCzQPpRI8d/) |
| **#271** | `HIGH` | Tech Stack Layer 10 of 13 | Layer 10 | [Watch Reel](https://www.instagram.com/reel/DY2nroEvto_/) |
