# Episode 224: You added indexes and your app is still slow

> **Category:** Database & Storage Engineering (پایگاه‌داده، روابط، ایندکس و پایداری داده)  
> **Production Layer:** Layer 3  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DZp7APuRdvP/](https://www.instagram.com/reel/DZp7APuRdvP/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your app is running slow. You added indexes. It's still slow because you're guessing where the problem is.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
It's still slow because you're guessing where the problem is. Here are the three things you use right now to figure it out. Step one, explain, analyze.

---

## ⚡ 3. Hardening Action Checklist
- [ ] explain, analyze. Stop assuming which query is the bottleneck.
- [ ] pg_stat_ statements. This tracks every query your application runs.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// PostgreSQL Connection Pooling Configuration
// DATABASE_URL routed through PgBouncer / Supavisor:
DATABASE_URL="postgresql://user:pass@db.pooler.supabase.com:6543/postgres?pgbouncer=true"
DIRECT_URL="postgresql://user:pass@db.supabase.com:5432/postgres" // For schema migrations
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your app is running slow. You added indexes. It's still slow because you're guessing where the problem is. Here are the three things you use right now to figure it out. Step one, explain, analyze. Stop assuming which query is the bottleneck. Use explain analyze and it'll show you exactly what the database is doing. Sequential scans, nested loops, index scans it chose not to use. The database has a plan for every query. You just haven't looked at it. If you do, that'll be a win. Step two, pg_stat_ statements. This tracks every query your application runs. How many times, how long each one takes, which one consumes the most total time. Your slowest query might only run once. Your most expensive query runs 10,000 times a day and takes 40 milliseconds each. That's an extra 400 seconds of database time for every query. Find those expensive ones first and that'll be a win. Step three. Connection pooling. Your database accepts a limited number of connections. When every request opens a new connection, you hit that ceiling before you hit the traffic. PG Bouncer shows you how many connections are used and where they are wasted. Stop guessing. Start measuring. Get that database cleaned up and it'll go fast.

</div>
