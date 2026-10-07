# Episode 060: Your AI agent fetches any URL a user submits

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DceYRVpCFKG/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI agent fetches any URL a user submits.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Allows AI agents to fetch arbitrary user-supplied URLs without validation, opening critical Server-Side Request Forgery (SSRF) bypasses. | Blocks internal VPC subnets, loopback addresses (`127.0.0.1`), and cloud metadata endpoints (`169.254.169.254`) from agent requests. |

---

## 💡 3. Root Cause & Architectural Principle
Your AI agent has the same network access that your server has. It can see internal databases, admin panels, and cloud credentials. So, when a user gives it a URL to fetch, your agent does not ask whether that URL belongs to you or to someone trying to rob you.

---

## ⚡ 4. Hardening Action Checklist
- [ ] your agent needs a boundary.
- [ ] a single validation check.
- [ ] your error messages are giving away the map.

---

## 💻 5. Hardened Production Implementation
```sql
-- migrations/001_row_level_security.sql
ALTER TABLE user_documents ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy ON user_documents
  FOR ALL
  USING (tenant_id = current_setting('app.current_tenant_id', true)::uuid)
  WITH CHECK (tenant_id = current_setting('app.current_tenant_id', true)::uuid);
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Your agent works for you. Make sure it only talks to who you approve.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI agent fetches URLs from user inputs. So, a hacker just used it to map every service running inside your network. Your AI agent has the same network access that your server has. It can see internal databases, admin panels, and cloud credentials. So, when a user gives it a URL to fetch, your agent does not ask whether that URL belongs to you or to someone trying to rob you. It fetches it from inside your perimeter and it hands the response back. So, an attacker just used your own infrastructure to bypass your own firewall. Let's get ahead of it. Step one, your agent needs a boundary. Right now, it'll fetch anything from anywhere. Internal services, cloud credential endpoints, admin dashboards. It does not know the difference between a legitimate request and an attack. So, direct your AI to restrict all outbound fetches to an approved list of external domains. and block any requests targeting your internal network altogether. That's a win. Step two, a single validation check. That is not enough. Attackers use techniques that pass your domain check on the first look and redirect to an internal target on the actual fetch. So, your agent validates the front door and walks right through the back. So, direct your AI to pin every URL to a single resolved address and revalidate on every redirect. This is so the destination cannot change between the check and the fetch. That's a win. And step three, your error messages are giving away the map. Every failed fetch returns a different error. Connection refused means a host exists. Timeout means a service is listening. So an attacker reads those differences and builds a blueprint of your internal network without ever touching it directly. So direct your AI to return one generic error for all failed fetches and log the details where Only your team can see them. So, your AI AI agent has the keys to every room in your building, right? Make sure strangers cannot tell which doors they open. That's the win.

</div>
