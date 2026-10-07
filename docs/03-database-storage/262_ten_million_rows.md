# Episode 262: Ten million rows

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Database & Storage Engineering (`پایگاه‌داده، روابط، ایندکس و پایداری داده`) |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZDUWLJRpZ8/) |

---

## 🚨 1. The Incident & Attack Vector
Your database has 10 million rows. Queries that took 20 milliseconds now take four to 5 seconds. Adding indexes is not fixing it anymore.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Filters tenant data in frontend or application code, leaking records across accounts on missed WHERE clauses. | Enforces Row-Level Security (RLS) directly in PostgreSQL, guaranteeing zero cross-tenant data leakage. |

---

## 💡 3. Root Cause & Architectural Principle
Adding indexes is not fixing it anymore. Your single Postgress instance has hit its ceiling. Here are three things you can do right now to fix it.

---

## ⚡ 4. Hardening Action Checklist
- [ ] shard by tenant.
- [ ] use Situs for transparent sharding.
- [ ] start with logical partitioning before physical.

---

## 💻 5. Hardened Production Implementation
```typescript
// lib/dbPool.ts
import { Pool } from 'pg';

export const dbPool = new Pool({
  connectionString: process.env.DATABASE_POOL_URL, // PgBouncer transaction pool
  max: 20,                                         // Strict ceiling per serverless container
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 5000,
});
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** When single Postgres is not enough.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your database has 10 million rows. Queries that took 20 milliseconds now take four to 5 seconds. Adding indexes is not fixing it anymore. Your single Postgress instance has hit its ceiling. Here are three things you can do right now to fix it. Step one, shard by tenant. If you built multi-tenency with an org ID column, you already have natural shard key. Each large tenant gets their own database. Small tenants share a poolled instance. Superbase lets you spin up isolated projects per tenant. Route at the application layer based on the org ID. Step two, use Situs for transparent sharding. Situs extends Postgress with distributed tables. You pick a distribution column, usually tenant ID or user ID. Situs handles routing queries to the right shard automatically. Your application code does not change. Same SQL same OM data lives on multiple nodes. Step three, start with logical partitioning before physical. Postgress native partitioning splits one table into partitions by range or list. Partition your events table by month. Partition your user data by region. The database prunes partitions at query time. Scans only touch relevant data. Indexes first, partition second, full sharding third. Do not jump to shard. because you saw a conference talk about it. Jump to sharding because your monitoring proved that you needed it. So tell me, what is your row count looking like right now? Share it in the comments.

</div>
