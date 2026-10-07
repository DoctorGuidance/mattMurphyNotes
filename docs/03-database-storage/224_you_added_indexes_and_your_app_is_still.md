# Episode 224: You added indexes and your app is still slow

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Database & Storage Engineering (`پایگاه‌داده، روابط، ایندکس و پایداری داده`) |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZp7APuRdvP/) |

---

## 🚨 1. The Incident & Attack Vector
You added indexes and your app is still slow.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Adds random single-column indexes without analyzing query patterns, bloating disk overhead while queries remain slow. | Designs composite multi-column indexes matching exact `WHERE`, `JOIN`, and `ORDER BY` clauses following leftmost prefix rules. |

---

## 💡 3. Root Cause & Architectural Principle
It's still slow because you're guessing where the problem is. Here are the three things you use right now to figure it out. Step one, explain, analyze.

---

## ⚡ 4. Hardening Action Checklist
- [ ] explain, analyze.
- [ ] pg_stat_ statements.

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
> **Production Heuristic:** Start measuring.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your app is running slow. You added indexes. It's still slow because you're guessing where the problem is. Here are the three things you use right now to figure it out. Step one, explain, analyze. Stop assuming which query is the bottleneck. Use explain analyze and it'll show you exactly what the database is doing. Sequential scans, nested loops, index scans it chose not to use. The database has a plan for every query. You just haven't looked at it. If you do, that'll be a win. Step two, pg_stat_ statements. This tracks every query your application runs. How many times, how long each one takes, which one consumes the most total time. Your slowest query might only run once. Your most expensive query runs 10,000 times a day and takes 40 milliseconds each. That's an extra 400 seconds of database time for every query. Find those expensive ones first and that'll be a win. Step three. Connection pooling. Your database accepts a limited number of connections. When every request opens a new connection, you hit that ceiling before you hit the traffic. PG Bouncer shows you how many connections are used and where they are wasted. Stop guessing. Start measuring. Get that database cleaned up and it'll go fast.

</div>
