# Episode 190: You wrote RLS policies

> **Category:** Multi-Tenancy & Data Isolation (معماری چندمستأجره و جداسازی قطعی داده‌ها)  
> **Production Layer:** Layer 8  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DaLDSqRgaBG/](https://www.instagram.com/reel/DaLDSqRgaBG/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
You just spent two long hours writing rowle security policies, beautiful rules, tenant isolation, role-based access on every single table. And then you built an API route that queries the database with the service ro key. The service ro key bypasses every RS policy you just wrote.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
The service ro key bypasses every RS policy you just wrote. Every single one of them. Your front end calls an API endpoint.

---

## ⚡ 3. Hardening Action Checklist
- [ ] A database policy that protects nothing because the application code walks right around around it every time.

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

You just spent two long hours writing rowle security policies, beautiful rules, tenant isolation, role-based access on every single table. And then you built an API route that queries the database with the service ro key. The service ro key bypasses every RS policy you just wrote. Every single one of them. Your front end calls an API endpoint. That endpoint connects to the database as a service role. The service role sees everything. every tenant, every row, every table, every time. So your RLS policies are performing for an audience of nobody. The attacker does not go through the front door where your policies are watching. They find the API route where your service key already opened every lock in the building for them. 45% of vibecoded applications that we review have a security vulnerability. And this one, they seem to all share. A database policy that protects nothing because the application code walks right around around it every time. Your security, it's not your policies. Your security is every path to the data. And right now, one of those critical paths has the door fully unlocked. I just dropped the fix to this in the free faction community. The link is in my bio. Come check it out.

</div>
