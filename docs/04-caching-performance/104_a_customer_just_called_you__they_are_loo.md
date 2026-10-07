# Episode 104: A customer just called you. They are looking at someone

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Caching & Edge Performance (`کشینگ، توزیع لبه و پرفورمنس سیستمی`) |
| **Target Production Layer** | Layer 10 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbimVuCkZqi/) |

---

## 🚨 1. The Incident & Attack Vector
A customer just called you. They are looking at someone else's revenue dashboard. Their invoices. Their customer list. Their monthly revenue. Your AI cached a query result without scoping it to the tenant.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Filters tenant data in frontend or application code, leaking records across accounts on missed WHERE clauses. | Enforces Row-Level Security (RLS) directly in PostgreSQL, guaranteeing zero cross-tenant data leakage. |

---

## 💡 3. Root Cause & Architectural Principle
So, your AI set up caching to speed up your app, but it never scoped the cache to the appropriate tenant. So, customer A loaded their dashboard and the result got cached. Customer B loaded the same page and boom, your cash served customer A's financial data instantly to customer B.

---

## ⚡ 4. Hardening Action Checklist
- [ ] your database security is irrelevant if your cache layer completely bypasses it.
- [ ] caching is not the only shared layer leaking.
- [ ] test this before your customer figures it out.

---

## 💻 5. Hardened Production Implementation
```sql
-- migrations/001_row_level_security.sql
ALTER TABLE user_documents ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy ON user_documents
  FOR ALL
  USING (tenant_id = current_setting('app.current_tenant_id', true)::uuid)
  WITH CHECK (tenant_id = current_setting('app.current_tenant_id', true)::uuid);
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** One cached query. Two customers. Zero trust left in your product. Your database security is irrelevant if your cache layer bypasses it.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

A customer just called you. They're looking at someone else's revenue dashboard on your system, their invoices, their customer list, their monthly revenue on your customer's screen right now. So, your AI set up caching to speed up your app, but it never scoped the cache to the appropriate tenant. So, customer A loaded their dashboard and the result got cached. Customer B loaded the same page and boom, your cash served customer A's financial data instantly to customer B. Here's why this happens and what you need to direct your AI to do to fix it immediately. Step one, your database security is irrelevant if your cache layer completely bypasses it. So you might have perfect rowle security on your databases. A lot of people do, but your cache sits in front of your database. So when your AI cached that query result, it cached the output after your security rules ran for customer A. So So customer B never hit the database. They get customer A's cache result served directly to them. So you need to direct your AI to scope every single cache key to the tenant ID. No exceptions. Every cache query, every cache page fragment, every cache API response must include a tenant context in that key. That's a win. Step two, caching is not the only shared layer leaking. Search indexes, background job cues, file storage pads and logging pipelines, right? Every shared service in your stack is a potential cross-tenant leak if your AI never scoped it appropriately. So, direct your AI to audit every shared layer and verify tenant isolation on every single one. If the layer does not know which tenant is serving, it should not be serving anything at all. And step three, test this before your customer figures it out. Direct your AI to build a cross-tenant access test. Log in as customer A. Load a page. Log out. Log in as customer B. Load that same page. If any data from customer A appears, your cash is leaking. This takes 10 minutes to test. The lawsuit from not testing it will take you years and a couple bucks promised. So, one cash query, two customers, and zero trust is left in your product. Direct your AI to scope every shared layer to every tenant today. And that's the win.

</div>
