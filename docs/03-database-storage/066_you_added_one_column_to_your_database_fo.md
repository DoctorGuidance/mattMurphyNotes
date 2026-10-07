# Episode 066: You added one column to your database for one client. Every

> **Category:** Database & Storage Engineering (پایگاه‌داده، روابط، ایندکس و پایداری داده)  
> **Production Layer:** Layer 3  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DcWGRX2G2l8/](https://www.instagram.com/reel/DcWGRX2G2l8/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
You added one column to your database for one client. Now every other client's queries have slowed down by 40%. So one client wanted a custom field on every single record and a new column in the shared schema that only they were using.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
So one client wanted a custom field on every single record and a new column in the shared schema that only they were using. So now every query, every migration, every backup and every restore carries a custom field that 99% of the clients never asked for or see. So one client's feature requ trust just became every client's technical debt and every client is paying for it in performance.

---

## ⚡ 3. Hardening Action Checklist
- [ ] per tenant schema extensions without shared schema pollution. A metadata table or JSON B column scoped to a tenant that holds custom fields.
- [ ] tenant isolated compute for heavy or custom workloads. When one tenant runs a report that scans millions of rows, that work workload should not be competing for resources with every other tenant in real time.
- [ ] tenant scoped migration pass. A schema change for one tenant cannot require downtime for all of your tenants.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Strict Tenant & User-Scoped Query
const record = await prisma.document.findFirst({
  where: {
    id: req.params.id,
    tenantId: req.user.tenantId // Mandatory tenant isolation
  }
});
if (!record) throw new NotFoundError('Access denied or record not found');
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

You added one column to your database for one client. Now every other client's queries have slowed down by 40%. So one client wanted a custom field on every single record and a new column in the shared schema that only they were using. So now every query, every migration, every backup and every restore carries a custom field that 99% of the clients never asked for or see. So one client's feature requ trust just became every client's technical debt and every client is paying for it in performance. You cannot say no to the revenue. We get it. But you said yes in the wrong way. And now tenant specific schema changes compound with every single release. Here's what tier 3 multi-tenant isolation really looks like. Step one, per tenant schema extensions without shared schema pollution. A metadata table or JSON B column scoped to a tenant that holds custom fields. The base schema stays clean. Tenant specific data lives in an extension layer that can grow without affecting anyone else. So direct your AI to implement a tenant extension model where custom fields are stored outside the core schema and joined at query time only for the requesting tenant. That's a win. Number two, tenant isolated compute for heavy or custom workloads. When one tenant runs a report that scans millions of rows, that work workload should not be competing for resources with every other tenant in real time. So isolate heavy compute into tenant scoped workers or cues. Direct your AI to implement workload isolation so one tenants's expensive operations cannot degrade the performance for all of the others. And step three tenant scoped migration pass. A schema change for one tenant cannot require downtime for all of your tenants. Migrations that affect the extension layer run per tenant. So migrations that affect the core schema are backwards compatible. Direct your AI to build a migration strategy that separates core schema changes from tenant specific changes. This way, no single tenants evolution forces a systemwide deployment. Say yes to your client, but say it with your architecture. It's the best way to go.

</div>
