# 🗄️ Rule 02: Database Engineering, Indexes & RLS

> **Based on Matt Murphy Masterclasses:** Episodes 003, 005, 174, 192, 211, 287, 288

---

## 1. Connection Pooling Guardrail (Lesson 211)
- Never instantiate direct PostgreSQL connections inside serverless handlers (AWS Lambda, Vercel Serverless Functions).
- Route all connections through **PgBouncer** or **Supavisor** using transaction pooling mode (`?pgbouncer=true` or port 6543).

```env
# ✅ Correct pooled configuration:
DATABASE_URL="postgresql://user:pass@db.pooler.supabase.com:6543/postgres?pgbouncer=true"
DIRECT_URL="postgresql://user:pass@db.supabase.com:5432/postgres" # Only for migrations
```

---

## 2. Row Level Security (RLS) Mandate (Lesson 005, 104)
When using Supabase or PostgreSQL:
```sql
-- Enable RLS on every multi-tenant table
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;

-- Strict tenant isolation policy
CREATE POLICY tenant_isolation_policy ON documents
  FOR ALL
  USING (tenant_id = (current_setting('app.current_tenant_id', true))::uuid);
```

---

## 3. Indexing Strategy (Lesson 287)
- Never deploy a migration without inspecting query plans (`EXPLAIN ANALYZE`).
- Foreign key columns must ALWAYS have an index to prevent full-table sequential scans during JOINs and CASCADE deletions.
