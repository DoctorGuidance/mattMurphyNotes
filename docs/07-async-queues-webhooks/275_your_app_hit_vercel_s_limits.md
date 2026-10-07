# Episode 275: Your app hit Vercel’s limits

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Async Queues & Webhooks |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYzc-WUAOlA/) |

---

## 🚨 1. The Incident & Attack Vector
Your app hit Vercel’s limits.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Executes long-running video or AI processing pipelines inside serverless functions, hitting hard Vercel execution limits. | Offloads long-running processing tasks to dedicated long-lived container workers (Fly/ECS) decoupled via message queues. |

---

## 💡 3. Root Cause & Architectural Principle
That's not a bug. That's your app telling you it's time for a bigger house. So here are the three things you can do right now to fix it.

---

## ⚡ 4. Hardening Action Checklist
- [ ] know the limits you're hitting.
- [ ] know what the next tools in line are.
- [ ] split your stack.

---

## 💻 5. Hardened Production Implementation
```sql
-- migrations/002_composite_indexes.sql
-- Eliminate table scans and guarantee unique constraints
CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS idx_users_org_email 
  ON users (organization_id, LOWER(email));

-- Covering index for frequent filtered lookups
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_orders_customer_status_created 
  ON orders (customer_id, status) INCLUDE (total_amount, created_at);
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** That’s a graduation. Railway, Render, and Fly exist for exactly this moment.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Someone this week commented on here and said that their app keeps hitting the 10second function timeout on Versel's basic hobby plan. Right? That's not a bug. That's your app telling you it's time for a bigger house. So here are the three things you can do right now to fix it. Step one, know the limits you're hitting. Versel gives you 10 second timeouts and serverless only execution. For a landing page, that's fine. But the moment your app starts processing files and running background, jobs. You're fighting the platform instead of building your product. Let's get it moving forward. Step two, know what the next tools in line are. Railway is great and it gives you persistent servers, longunning background jobs, cron tasks, and websockets. Render does a great job, too, and adds managed services like Postgress and Redis. Fly.io puts your app on servers closer to your users worldwide. These aren't harder than Versel. They're just built for different problems, and they solve them really well. Step three, split your stack. Keep your front end on Versel. Move your backend and your background jobs and processing to railway or render. It would make a big difference. Your front end talks to your backend over HTTPS. They don't have to live in the same place. And that's what every production app does eventually whether you know it or not. So, Versell isn't bad. It's just not the only tool. And knowing when to graduate is what separates a project from a product. Now, you know.

</div>
