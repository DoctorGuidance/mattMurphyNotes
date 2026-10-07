# Episode 155: Your first enterprise customer sent a procurement checklist

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Cloud Infrastructure & FinOps (`معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaqKoflEgzB/) |

---

## 🚨 1. The Incident & Attack Vector
Your first enterprise customer sent a procurement checklist.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Leaves serverless functions or compute instances unmonitored without timeouts or egress alarms in 'Your first enterprise customer sent a procurement checklist'. | Enforces hard function timeouts (15-30s), egress bandwidth controls, and automated cloud spending kill-switches. |

---

## 💡 3. Root Cause & Architectural Principle
Their IT team just sent over a procurement checklist. Line one, do you support single sign on via SAML and OIDC? You have Google signin and an email password, but I don't think that's SSO.

---

## ⚡ 4. Hardening Action Checklist
- [ ] SSO is not optional for the enterprise.
- [ ] SAML is a protocol your AI needs to learn fast.
- [ ] plan for multi-tenant SSO.

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
> **Production Heuristic:** The enterprise deal starts with three letters. SSO!

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your first enterprise customer wants to buy your product. That's a win. Their IT team just sent over a procurement checklist. Line one, do you support single sign on via SAML and OIDC? You have Google signin and an email password, but I don't think that's SSO. Here are the three things you need to understand right now to fix it. Step one, SSO is not optional for the enterprise. Their employees log in through one corporate identity provider every day. Octa, Azure AD, Google Workspace. If your app cannot authenticate through their provider, their IT team will not approve the purchase at all. You're out of there. This is not a feature request. It is a gate and a bare minimum to get in the door. Step two, SAML is a protocol your AI needs to learn fast. Direct your AI to implement SAML 2.0 or OIDC integration. The handshake, the assertion, the attribute mapping, the session management, your AI can build it all, but you have to know to ask for it before the checklist arrives from the client. And step three, plan for multi-tenant SSO. Each customer uses a different identity provider. Customer A uses Octa, customer B uses Azure AD. Direct your AI to build tenants specific SSO configurations. One integration pattern per tenant credentials. The potential enterprise deals that can change your business. Start with three letters every single time. S O That's the win.

</div>
