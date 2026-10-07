# Episode 249: OWASP ZAP

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZQU76-x-1G/) |

---

## 🚨 1. The Incident & Attack Vector
You built all the right security features. RLS is on. O is configured.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
O is configured. HTTPS is everywhere. But have you ever actually tried to hack your own app?

---

## ⚡ 4. Hardening Action Checklist
- [ ] run OWASP Zap on your app. Zap is free.
- [ ] test your own API in Burp Suite. You can intercept your own requests, change the user ID in the Jot payload, and then you need to know, can you access another user's data?
- [ ] automate security scanning and CI. Sneak or GitHub's built-in code scanning.

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

You built all the right security features. RLS is on. O is configured. HTTPS is everywhere. But have you ever actually tried to hack your own app? If not, someone else certainly will. Here are the three things you can do right now to test your security. Step one, run OWASP Zap on your app. Zap is free. It's open- source. It's one Docker command. It crawls your entire app and tests for the top 10 vulnerabilities. SQL injections, cross-sight scripting, broken authentication. The report, it's powerful and it tells you exactly where you're vulnerable. Run it against your staging environment. Why? Because you can fix things before an attacker finds them in production. That's a win. Step two, test your own API in Burp Suite. You can intercept your own requests, change the user ID in the Jot payload, and then you need to know, can you access another user's data? Change the org_ ID in the request. body. Can you read another tenants's records? Modify the role claim. Can you access admin endpoints? If any of these actually work, your authorization logic has holes in it like Swiss cheese. RLS is not enough. Your API passes unchecked parameters to the database. That's not a win. Step three, automate security scanning and CI. Sneak or GitHub's built-in code scanning. Add it to your GitHub actions workflow. Every push gets scanned for no own vulnerabilities and dependencies. Every PR gets checked for hard-coded secrets with GitG Guardian or TruffleHog. Security is not a one-time audit, folks. It's a continuous process of running on every single commit. Scan, intercept, and automate. You're not hiring a pen testing firm for $50,000. You're running the same tools they use for free. The difference, you got to run them before the breach. So, when did you last try to hack your own app? Huh? It's been too long. If you haven't tried, try it now.

</div>
