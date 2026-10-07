# Episode 070: Every time a new client signs up, your developer forks the

> **Category:** Frontend Architecture & API Hygiene (معماری فرانت‌اند، طراحی واسط و بهداشت API)  
> **Production Layer:** Layer 1  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DcQ8u02Cj1A/](https://www.instagram.com/reel/DcQ8u02Cj1A/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Every time a new client signs up for your multi-tenant system, you fork the entire repository. New branch, new deployment, new set of environmental variables. Client number four wanted dashboard in dark mode.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
Client number four wanted dashboard in dark mode. Client number seven wanted to export CSVs instead of PDFs. And client number 11 wants to skip onboarding entirely.

---

## ⚡ 3. Hardening Action Checklist
- [ ] wanted dashboard in dark mode. Client number seven wanted to export CSVs instead of PDFs.
- [ ] feature flag scoped per tenant. A feature flag is not a global onoff switch.
- [ ] tenant configuration inheritance with override layers. So start with a base configuration every tenant shares.
- [ ] tenant aware routing at the application boundary. The application must know which tenant is making the request before it touches any logic.

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

Every time a new client signs up for your multi-tenant system, you fork the entire repository. New branch, new deployment, new set of environmental variables. Client number four wanted dashboard in dark mode. Client number seven wanted to export CSVs instead of PDFs. And client number 11 wants to skip onboarding entirely. So your AI copied the codebase and started customizing. But now you have 11 versions of your product and you cannot remember which client runs which branch. So that's no longer a product. That's actually 11 products wearing the exact same name. Here's how you're going to direct your AI to serve all of those clients without forking your product for each and everyone. Step one, feature flag scoped per tenant. A feature flag is not a global onoff switch. It's a per tenant configuration. Client number seven gets those CSV exports. Client four gets dark mode. And everyone else gets the default. One codebase evaluates the tenant context and renders the right experience. So directory AI to implement tenant scoped feature flags where every configurable behavior is controlled by tenant ID not by code branches. That's a win. Step two, tenant configuration inheritance with override layers. So start with a base configuration every tenant shares. Layer tenant specific overrides on top of that client. 11 overrides the onboarding flow. Everyone else inherits the default. So when you update the base, every tenant gets the update unless they have an explicit override. So direct your AI to build a configuration system with base defaults and per tenant overrides that merge at runtime. That's a win. And step three, tenant aware routing at the application boundary. The application must know which tenant is making the request before it touches any logic. subdomain, header, jot claim. That identity drives which configuration loads, which features will activate, which branding will render. So, direct your AI to implement tenant resolution middleware that identifies the tenant on every single request and then it injects the tenant context before any business logic executes. One codebase, 11 clients, zero forks. So, directory AI to build it that way from day one.

</div>
