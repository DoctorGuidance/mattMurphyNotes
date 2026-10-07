# Episode 270: Vibe Coded Multi-Tenant Platform

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Multi-Tenancy & Data Isolation (`معماری چندمستأجره و جداسازی قطعی داده‌ها`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DY4jQHeR4Gb/) |

---

## 🚨 1. The Incident & Attack Vector
So, a follower on here told me last week that they're building a school management system. I love it. 20,000 users across 50 schools, three portals per school, admin, staff, and students.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
20,000 users across 50 schools, three portals per school, admin, staff, and students. That's a real production system, and it needs real data architecture. So, here are the three things you do right now to build it.

---

## ⚡ 4. Hardening Action Checklist
- [ ] add a tenant ID to every single table in the database. Every row in your database needs to know which organization it belongs to before before things get chaotic.
- [ ] enforce isolation at the database level, not in your app code. Use role level security so the database itself blocks cross tenant access.
- [ ] design your schema for the access you actually have, right? Students are queried by the school, attendance is queried by the date, and fees are queried by the status.

---

## 💻 5. Hardened Production Implementation
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

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Never deploy unverified AI-generated code directly to production without testing failure modes.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

So, a follower on here told me last week that they're building a school management system. I love it. 20,000 users across 50 schools, three portals per school, admin, staff, and students. That's a real production system, and it needs real data architecture. So, here are the three things you do right now to build it. Step one, add a tenant ID to every single table in the database. Every row in your database needs to know which organization it belongs to before before things get chaotic. Student table, tenant ID. Attendance table, tenant ID. Fee records, tenant ID. You get the point. Without it, one school can see another school's data. And that's not cool. Step two, enforce isolation at the database level, not in your app code. Use role level security so the database itself blocks cross tenant access. If your app has a bug and forgets a wear clause, RLS catches it. Your application code is the first line. and a defense the database. That's the last. Step three, design your schema for the access you actually have, right? Students are queried by the school, attendance is queried by the date, and fees are queried by the status. Each pattern needs its own indexes. You get it. 20,000 users across 50 schools is nothing for Postgress. Totally handles it. But the wrong schema makes even 400 users feel super slow. So multi-tenency, it's not a feature. It's an architecture decision you make before you scale, not after. Heck, you make it before you build, not after. Hope this helped.

</div>
