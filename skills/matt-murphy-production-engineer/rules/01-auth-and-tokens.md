# 🔐 Rule 01: Authentication, Tokens & IDOR Defense

> **Based on Matt Murphy Masterclasses:** Episodes 043, 044, 048, 118, 124, 145, 194, 201, 206, 213, 218, 228, 230

---

## 1. Storage Guardrail: Insecure Storage Ban
```typescript
// ❌ CRITICAL VULNERABILITY (Lesson 043):
// Storing JWT in localStorage or sessionStorage exposes the token to any script or XSS.
localStorage.setItem('auth_token', token);

// ✅ PRODUCTION STANDARD:
// Issue HttpOnly, Secure, SameSite=Lax cookie from the server.
res.cookie('auth_token', token, {
  httpOnly: true,
  secure: process.env.NODE_ENV === 'production',
  sameSite: 'lax',
  path: '/',
  maxAge: 15 * 60 * 1000 // 15 minutes short-lived
});
```

---

## 2. Query Scoping Guardrail: Anti-IDOR Invariant
```typescript
// ❌ CRITICAL VULNERABILITY (Lesson 044):
// Relying purely on the ID parameter from the URL allows any authenticated user to view other tenants' invoices.
const invoice = await prisma.invoice.findUnique({
  where: { id: req.params.invoiceId }
});

// ✅ PRODUCTION STANDARD:
// Mandatory composite scoping with tenant_id and user_id.
const invoice = await prisma.invoice.findFirst({
  where: {
    id: req.params.invoiceId,
    tenantId: req.user.tenantId, // Authenticated organization context
  }
});
if (!invoice) throw new NotFoundError('Invoice not found');
```

---

## 3. OAuth PKCE Guardrail
- Every OAuth callback must validate the `state` parameter against a signed session cookie to prevent Login CSRF.
- Native apps and Single Page Apps must use PKCE (`code_challenge` / `code_verifier`).
