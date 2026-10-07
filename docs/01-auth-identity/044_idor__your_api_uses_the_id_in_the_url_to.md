# Episode 044: IDOR: Your API Uses the ID in the URL to Load Data

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Authentication & Identity (`احراز هویت و مدیریت نشست‌ها`) |
| **Target Production Layer** | Layer 4 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Dc1jZHyiWz0/) |

---

## 🚨 1. The Incident & Attack Vector
A user visits `/api/invoices/1042`. They change the URL to `1043` and view another company's financial records. The backend trusted the ID in the URL without checking if the authenticated tenant actually owns that resource.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Queries database solely by resource ID from URL parameter (`/api/invoices/:id`), allowing any user to access another tenant's records (IDOR). | Enforces composite scoping on every query (`WHERE id = :id AND tenant_id = :tenant_id AND user_id = :user_id`) to mathematically eliminate IDOR. |

---

## 💡 3. Root Cause & Architectural Principle
Never treat client-provided route parameters as an authorization assertion. Direct-object queries must strictly scope to the authenticated user's organization.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Enforce composite scoping with `tenant_id` on every database query.
- [ ] Enable database-level Row Level Security (RLS) as an un-bypassable guardrail.
- [ ] Replace sequential integer IDs with cryptographically random UUIDv7 or NanoIDs.

---

## 💻 5. Hardened Production Implementation
```typescript
// services/invoiceService.ts
export async function getInvoice(invoiceId: string, authenticatedTenantId: string) {
  // ❌ VULNERABLE: const inv = await db.invoice.findUnique({ where: { id: invoiceId } });
  // ✅ SECURE: Strict Tenant Scoping
  const invoice = await db.invoice.findFirst({
    where: {
      id: invoiceId,
      tenantId: authenticatedTenantId // Enforce tenant isolation
    }
  });
  if (!invoice) throw new NotFoundError('Invoice not found or access denied');
  return invoice;
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** An ID in a URL is an address, not an authorization badge. Always verify ownership at the query level.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your API is using the user ID and the URL to load the data. So you change the number and you see someone else's account algether. So your AI yeah built your API endpoints. Your front end sends the logged in user's ID and gets their data right back. But your API never checks whether the person making the request is actually the right user. So your authorization is in the URL and your URL is one guess away from every other user's data. Let's get this handled. Step one, verify ownership on every API request. Every endpoint that returns user specific data must check the authenticated user's identity against the resource they are requesting. So if user 12 requests user 15's data, the server returns a 403. So direct your AI to add ownership verification middleware so that it compares the authenticated session user against the resource owner on every protected endpoint. That's a win. Step two, stop using sequential IDs in your URLs. User 1, user 2, user 3, or order 1, 10,002, 10,003. Sequential IDs make enumeration trivial. An attacker writes a loop and downloads every user's data in minutes. So, direct your AI to replace sequential integer IDs with UYU IDs and all API endpoints and database references. That's a win. And step three, audit every endpoint that takes an ID as a parameter. Your AI built dozens of endpoints. Every one of them accepts an ID in the URL, query string, or a request body, a potential access control failure. So, direct your AI to list every endpoint so that it accepts a resource identifier, verify ownership checks exist on each one, and flag any endpoint where a user can access resources that do not belong to them. Your API should not trust the URL. It should Trust the user session. That's your win.

</div>
