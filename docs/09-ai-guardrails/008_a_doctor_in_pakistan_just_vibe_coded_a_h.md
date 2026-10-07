# Episode 008: A doctor in Pakistan just vibe coded a HIPAA-compliant

> **Category:** AI Guardrails, LLM Security & Compliance (مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی)  
> **Production Layer:** Layer 2  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DdroHsllR2T/](https://www.instagram.com/reel/DdroHsllR2T/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
A doctor in Pakistan from my builder's community just vibecoded a fully compliant hospital management system. It has multi-tenant architecture, role- security, prescription integration. And he's not an engineer.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
And he's not an engineer. He's a physician at a public hospital where he built this from his desk. So multi-tenant, five permission levels, super admin, organization admin, staff, medical team, patient portal, he's got them all.

---

## ⚡ 3. Hardening Action Checklist
- [ ] Postgress rowle security so every tenants's data is isolated at the database level not the application level database level and he integrated e-rescription through shcript added two-actor authentication with SMS and authenticator app realtime error tracking through better stack hippa and papa compliant hosting on liquid web with assigned baa then he sent me a message right I use your videos to improve my app including security and reliability.
- [ ] This is a production healthcare software handling real patient data built by a doctor who used my content and directed his AI to build what he could not find on the market to solve the problem.
- [ ] Every single day, I open messages from builders in our community who took a fix it, a security audit, or a single tutorial of mine in a real and turned it into into a product.

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

A doctor in Pakistan from my builder's community just vibecoded a fully compliant hospital management system. It has multi-tenant architecture, role- security, prescription integration. And he's not an engineer. He's a physician at a public hospital where he built this from his desk. So multi-tenant, five permission levels, super admin, organization admin, staff, medical team, patient portal, he's got them all. Postgress rowle security so every tenants's data is isolated at the database level not the application level database level and he integrated e-rescription through shcript added two-actor authentication with SMS and authenticator app realtime error tracking through better stack hippa and papa compliant hosting on liquid web with assigned baa then he sent me a message right I use your videos to improve my app including security and reliability. I'll take it. This isn't a demo. This is not a weekend project. This is a production healthcare software handling real patient data built by a doctor who used my content and directed his AI to build what he could not find on the market to solve the problem. And he's not alone. Every single day, I open messages from builders in our community who took a fix it, a security audit, or a single tutorial of mine in a real and turned it into into a product. Not engineers, operators, founders, physicians, professionals who needed software that did not exist. And then they built it for themselves because nobody was building it for them. This is what AI directed engineering actually looks like in the real world. It's not replacing developers. It's enabling the people who understand the problem better than any developer ever could. So the doctor who knows which workflow kills time or the operator who knows which process breaks or the founder who has lived inside of the gap. The best software is not built by people who know how to write code. It's built by people who know what needs to exist and be fixed. That is the win.

</div>
