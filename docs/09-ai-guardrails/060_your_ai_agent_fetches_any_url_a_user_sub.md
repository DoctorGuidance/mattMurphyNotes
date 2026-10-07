# Episode 060: Your AI agent fetches any URL a user submits

> **Category:** AI Guardrails, LLM Security & Compliance (مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی)  
> **Production Layer:** Layer 2  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DceYRVpCFKG/](https://www.instagram.com/reel/DceYRVpCFKG/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your AI agent fetches URLs from user inputs. So, a hacker just used it to map every service running inside your network. Your AI agent has the same network access that your server has.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
Your AI agent has the same network access that your server has. It can see internal databases, admin panels, and cloud credentials. So, when a user gives it a URL to fetch, your agent does not ask whether that URL belongs to you or to someone trying to rob you.

---

## ⚡ 3. Hardening Action Checklist
- [ ] your agent needs a boundary. Right now, it'll fetch anything from anywhere.
- [ ] a single validation check. That is not enough.
- [ ] your error messages are giving away the map. Every failed fetch returns a different error.

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

Your AI agent fetches URLs from user inputs. So, a hacker just used it to map every service running inside your network. Your AI agent has the same network access that your server has. It can see internal databases, admin panels, and cloud credentials. So, when a user gives it a URL to fetch, your agent does not ask whether that URL belongs to you or to someone trying to rob you. It fetches it from inside your perimeter and it hands the response back. So, an attacker just used your own infrastructure to bypass your own firewall. Let's get ahead of it. Step one, your agent needs a boundary. Right now, it'll fetch anything from anywhere. Internal services, cloud credential endpoints, admin dashboards. It does not know the difference between a legitimate request and an attack. So, direct your AI to restrict all outbound fetches to an approved list of external domains. and block any requests targeting your internal network altogether. That's a win. Step two, a single validation check. That is not enough. Attackers use techniques that pass your domain check on the first look and redirect to an internal target on the actual fetch. So, your agent validates the front door and walks right through the back. So, direct your AI to pin every URL to a single resolved address and revalidate on every redirect. This is so the destination cannot change between the check and the fetch. That's a win. And step three, your error messages are giving away the map. Every failed fetch returns a different error. Connection refused means a host exists. Timeout means a service is listening. So an attacker reads those differences and builds a blueprint of your internal network without ever touching it directly. So direct your AI to return one generic error for all failed fetches and log the details where Only your team can see them. So, your AI AI agent has the keys to every room in your building, right? Make sure strangers cannot tell which doors they open. That's the win.

</div>
