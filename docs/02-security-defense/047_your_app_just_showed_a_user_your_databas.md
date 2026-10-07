# Episode 047: Your app just showed a user your database name, your server

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcybEeAEhP8/) |

---

## 🚨 1. The Incident & Attack Vector
Your app just showed a user your database name, your server file path, and the query that failed.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Returns raw database error stack traces and internal file paths to users upon unhandled server exceptions. | Sanitizes error responses into generic user messages while routing full diagnostic stack traces to centralized Sentry trackers. |

---

## 💡 3. Root Cause & Architectural Principle
They accidentally clicked on a broken link. Your AI built error handling. Great.

---

## ⚡ 4. Hardening Action Checklist
- [ ] separate your error responses by environment.
- [ ] route every error to centralized logging, not to the user screen.
- [ ] build custom error pages that reveal nothing.

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
> **Production Heuristic:** Your users found a bug. Do not let the bug report write itself.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI built app just showed a user your database name, your server file path, and their query that failed. And they were not trying to hack you. They accidentally clicked on a broken link. Your AI built error handling. Great. Detailed stack traces, full database queries, and internal file paths. However, you shipped it to production, and now your users are seeing the same data. So, an attacker does not need to probe your system. Your error pages are doing the reconnaissance for them. So, let's get it cleaned up. Step one, separate your error responses by environment. Development shows the full stack trace. Production shows a generic message. Your users should never see an error that contains a file path, a query string, or a database name, or even a package version. So, direct your AI to implement environmentaware error handling so that it returns detailed errors only in development and returns generic userfriendly responses in production. That's definitely a win. Step two, route every error to centralized logging, not to the user screen. Every error your app throws should be captured, timestamped, and searchable in your monitoring system. No doubt about it. The user sees a clean error page. You see the full detail in your logs. So, direct your AI to implement structured error logging that captures the full stack trace request context and the user session data in your monitoring tool without exposing any of it to the client. That's also a win. And step three, build custom error pages that reveal nothing. So your 404 or your 500 or your timeout page, every one of them should be branded, helpful, and architecturally silent. So direct your AI to build custom error pages for every common error code. so that it gives the user a clear next step without revealing any server side details. Those users who found a bug, do not let the bug write itself or the report. That's not a win.

</div>
