# Episode 221: Application-level filtering is a prayer

> **Category:** Multi-Tenancy & Data Isolation (معماری چندمستأجره و جداسازی قطعی داده‌ها)  
> **Production Layer:** Layer 8  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DZslOCNRDNh/](https://www.instagram.com/reel/DZslOCNRDNh/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your application, it's got a bug. A query returns data that it should not have and the user sees another customer's records. In most applications, nothing can stop this.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
In most applications, nothing can stop this. But rowle security certainly will. Here are the three things you need to know right now about RLS.

---

## ⚡ 3. Hardening Action Checklist
- [ ] RLS is a database level firewall. You write the policy.
- [ ] this is not the same as filtering in your application code. One missed wear clause and you have a data leak.
- [ ] Superbase makes RLS accessible. You enable it per table and every query respects the policy.

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

Your application, it's got a bug. A query returns data that it should not have and the user sees another customer's records. In most applications, nothing can stop this. But rowle security certainly will. Here are the three things you need to know right now about RLS. Step one, RLS is a database level firewall. You write the policy. The user can only see rows where the tenant ID matches their own ID. Every query passes through a policy first. If the row does not belong to the user does not exist. Step two, this is not the same as filtering in your application code. One missed wear clause and you have a data leak. RLS means the database itself enforces this rule. Even if the application code is wrong, the data stays protected. That is the difference between a policy and a prayer and that's a win. Step three, Superbase makes RLS accessible. You enable it per table and every query respects the policy. see automatically. For anything where one user should never see another user's information, RLS is not a feature, it's the foundation. So, always make sure to protect the data at the source.

</div>
