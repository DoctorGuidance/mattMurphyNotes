# Episode 119: Your AI built a healthcare app. It has never heard of HIPAA

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbOGY9aEY0-/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI built a healthcare app. It has never heard of HIPAA.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Deploys healthcare applications processing Protected Health Information (PHI) to non-compliant clouds without BAAs or audit logs. | Executes Business Associate Agreements (BAAs), isolates PHI in dedicated encrypted partitions, and audits access trails. |

---

## 💡 3. Root Cause & Architectural Principle
Your AI doesn't know that. It will literally store patient data wherever it wants and it'll transmit it however it feels like it and it'll log it again wherever it wants. So, if your application touches any patient data, student health records or protected health health information, you're already subject to a federal regulation and your AI never asked a single question about it.

---

## ⚡ 4. Hardening Action Checklist
- [ ] encryption at rest and in transit on every field that contains protected health information, not just your database, your backups, your logs, your exports.
- [ ] access controls with audit logging on every record that contains PHI.
- [ ] a business associate agreement with every third-party service that touches that data.

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
> **Production Heuristic:** Direct your AI to fix that before your first patient walks through the door

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI built a healthcare app, but it's never heard of HIPPA. One complaint to the Office for Civil Rights triggers an investigation that starts at $100 per violation and scales all the way up to $2 million. Your AI doesn't know that. It will literally store patient data wherever it wants and it'll transmit it however it feels like it and it'll log it again wherever it wants. So, if your application touches any patient data, student health records or protected health health information, you're already subject to a federal regulation and your AI never asked a single question about it. So, here are the three things you direct your AI to build right now if your app is touching health data. Step one, encryption at rest and in transit on every field that contains protected health information, not just your database, your backups, your logs, your exports. Your AI may have encrypted that database, but left PHI sitting in plain text in your application log. One log file is all it takes for a pretty significant fine. Step two, access controls with audit logging on every record that contains PHI. Who accessed it? When, from where, and what did they do with it? HIPPO requires you to produce this on demand. Your AI built role based access, but it did not build the paper trail that proves what touched what. And step three, a business associate agreement with every third-party service that touches that data. your hosting provider, your email service, your analytics platform. If they can see protected health information, they need a BAA on file. Your AI integrated six services and signed zero agreements. One of those services has a breach and you're liable because you have no contract that defines the obligations. So, yeah, your AI builds fast, but it does not build compliant. Direct your AI to fix that before your first patient walks through the door.

</div>
