# Episode 320: 10 users fine

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Database & Storage Engineering (`پایگاه‌داده، روابط، ایندکس و پایداری داده`) |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DXwtOTDA-gx/) |

---

## 🚨 1. The Incident & Attack Vector
10 users, everything's fine. 100 users, things are slowing down around here.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes database stability under 10 users translates linearly to production loads without index optimization or connection limits. | Pre-calculates query latency under scale using realistic benchmarks and optimizes queries before onboarding production users. |

---

## 💡 3. Root Cause & Architectural Principle
10 users, everything's fine. 100 users, things are slowing down around here.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Isolate unverified components behind automated integration tests.
- [ ] Enforce fail-safe boundaries preventing cascade outages.
- [ ] Establish real-time observability alerts on critical paths.

---

## 💻 5. Hardened Production Implementation
```sql
-- migrations/003_scaling_indexes.sql
-- Scale from 10 users to 10,000 concurrent users without database locks
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_active_sessions_lookup 
  ON sessions (user_id, expires_at) 
  WHERE expires_at > NOW();
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Maybe, maybe not

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

10 users, everything's fine. 100 users, things are slowing down around here. Thousand users, everything crashes to the ground. This is the scaling cliff. And vibe coded apps hit it real hard. Here's why. AI generated code optimizes for works, not for works at scale. That database query that takes 50 milliseconds with 100 rows takes 30 seconds with 100,000 rows. And that API call you can make on every page load fine with 10 users, death spiral with a thousand. The code isn't wrong. It just wasn't designed to scale. And here's what productionready scaling looks like in a vibe coded app. Database queries with proper indexing. Not select from everything, but targeted queries that stay fast as data grows. A clear caching strategy. Don't compute the same thing a thousand times over. Compute it once. Cache it once. Serve it fast. Fast async processing for heavy operations. Don't make users wait while you send emails or generate reports. Cue it up. Process it in the background. And load testing before launch. Not we'll see what happens, but actual simulated traffic. Find the cliffs before your new users do. When we finish a vibe coded project at Faction, we stress test for scale because launch day surprises are the most expensive kind. What's the most users your app has handled at once? Was it smooth? Did it hit a cliff? Have you crashed? Maybe, maybe not. Tell me below.

</div>
