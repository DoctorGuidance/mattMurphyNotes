# Episode 155: Your first enterprise customer sent a procurement checklist

> **Category:** Cloud Infrastructure & FinOps (معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه)  
> **Production Layer:** Layer 6  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DaqKoflEgzB/](https://www.instagram.com/reel/DaqKoflEgzB/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your first enterprise customer wants to buy your product. That's a win. Their IT team just sent over a procurement checklist.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
Their IT team just sent over a procurement checklist. Line one, do you support single sign on via SAML and OIDC? You have Google signin and an email password, but I don't think that's SSO.

---

## ⚡ 3. Hardening Action Checklist
- [ ] SSO is not optional for the enterprise. Their employees log in through one corporate identity provider every day.
- [ ] SAML is a protocol your AI needs to learn fast. Direct your AI to implement SAML
- [ ] plan for multi-tenant SSO. Each customer uses a different identity provider.

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

Your first enterprise customer wants to buy your product. That's a win. Their IT team just sent over a procurement checklist. Line one, do you support single sign on via SAML and OIDC? You have Google signin and an email password, but I don't think that's SSO. Here are the three things you need to understand right now to fix it. Step one, SSO is not optional for the enterprise. Their employees log in through one corporate identity provider every day. Octa, Azure AD, Google Workspace. If your app cannot authenticate through their provider, their IT team will not approve the purchase at all. You're out of there. This is not a feature request. It is a gate and a bare minimum to get in the door. Step two, SAML is a protocol your AI needs to learn fast. Direct your AI to implement SAML 2.0 or OIDC integration. The handshake, the assertion, the attribute mapping, the session management, your AI can build it all, but you have to know to ask for it before the checklist arrives from the client. And step three, plan for multi-tenant SSO. Each customer uses a different identity provider. Customer A uses Octa, customer B uses Azure AD. Direct your AI to build tenants specific SSO configurations. One integration pattern per tenant credentials. The potential enterprise deals that can change your business. Start with three letters every single time. S O That's the win.

</div>
