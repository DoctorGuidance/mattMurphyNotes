# Episode 044: Your API uses the user ID in the URL to load their data

> **Category:** Authentication & Identity (احراز هویت و مدیریت نشست‌ها)  
> **Production Layer:** Layer 4  
> **Official Instagram Reel:** [https://www.instagram.com/reel/Dc1jZHyiWz0/](https://www.instagram.com/reel/Dc1jZHyiWz0/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your API is using the user ID and the URL to load the data. So you change the number and you see someone else's account algether. So your AI yeah built your API endpoints.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
So your AI yeah built your API endpoints. Your front end sends the logged in user's ID and gets their data right back. But your API never checks whether the person making the request is actually the right user.

---

## ⚡ 3. Hardening Action Checklist
- [ ] verify ownership on every API request. Every endpoint that returns user specific data must check the authenticated user's identity against the resource they are requesting.
- [ ] stop using sequential IDs in your URLs. User 1, user 2, user 3, or order 1, 10,002, 10,00
- [ ] audit every endpoint that takes an ID as a parameter. Your AI built dozens of endpoints.

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

Your API is using the user ID and the URL to load the data. So you change the number and you see someone else's account algether. So your AI yeah built your API endpoints. Your front end sends the logged in user's ID and gets their data right back. But your API never checks whether the person making the request is actually the right user. So your authorization is in the URL and your URL is one guess away from every other user's data. Let's get this handled. Step one, verify ownership on every API request. Every endpoint that returns user specific data must check the authenticated user's identity against the resource they are requesting. So if user 12 requests user 15's data, the server returns a 403. So direct your AI to add ownership verification middleware so that it compares the authenticated session user against the resource owner on every protected endpoint. That's a win. Step two, stop using sequential IDs in your URLs. User 1, user 2, user 3, or order 1, 10,002, 10,003. Sequential IDs make enumeration trivial. An attacker writes a loop and downloads every user's data in minutes. So, direct your AI to replace sequential integer IDs with UYU IDs and all API endpoints and database references. That's a win. And step three, audit every endpoint that takes an ID as a parameter. Your AI built dozens of endpoints. Every one of them accepts an ID in the URL, query string, or a request body, a potential access control failure. So, direct your AI to list every endpoint so that it accepts a resource identifier, verify ownership checks exist on each one, and flag any endpoint where a user can access resources that do not belong to them. Your API should not trust the URL. It should Trust the user session. That's your win.

</div>
