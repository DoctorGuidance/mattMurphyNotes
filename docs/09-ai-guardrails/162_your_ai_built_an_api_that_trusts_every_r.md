# Episode 162: Your AI built an API that trusts every request it receives

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Dai-n_LjPMS/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI built an API that trusts every request it receives.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Sends unvalidated user inputs straight to LLMs without budget caps or injection defenses in 'Your AI built an API that trusts every request it receives'. | Applies prompt sanitization, structured output validation (Zod), spend ceilings, and SGI metadata compliance. |

---

## 💡 3. Root Cause & Architectural Principle
A request with a missing field gets processed. A request with a malicious payload gets processed. Everything your API receives, your AI trusts.

---

## ⚡ 4. Hardening Action Checklist
- [ ] input validation on every route.
- [ ] sanitization.
- [ ] rate awareness at the middleware level.

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
> **Production Heuristic:** That is AI-Directed orchestration.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI built an API that processes every single request it receives. No validation, no sanitization, no rejection. A request with a missing field gets processed. A request with a malicious payload gets processed. Everything your API receives, your AI trusts. Here are the three things you need to direct your AI to do right now to fix it. Step one, input validation on every route. Direct your AI to validate the shape of every request before it touches your business logic. Wrong type rejected. Missing field rejected. Unexpected field stripped. If the request does not match the schema, it never reaches your database. And that's a win. Step two, sanitization. Direct your AI to clean every string input before processing. A user who types a script tag into a form field is either confused or possibly attacking you. Either way, your API should not execute it. And step three, rate awareness at the middleware level. Direct your AI to track request patterns per user per endpoint. A user hitting the same endpoint 50 times per second, they aren't using your app. They're probing it. Your middleware catches the pattern before your business logic ever sees it. So you always follow this rule. Trust nothing and validate everything. That is how you orchestrate an API.

</div>
