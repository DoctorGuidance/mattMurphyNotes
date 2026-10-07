# Episode 163: Customer A logged in and saw customer B's data

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Observability & Error Tracking |
| **Target Production Layer** | Layer 12 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DaiaXxhGx1Z/) |

---

## 🚨 1. The Incident & Attack Vector
Customer A logged in and saw customer B's data.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Fails to alert engineers when cross-tenant data leaks occur, learning about privacy breaches from furious customer emails. | Instruments anomaly detection alerts on unexpected tenant ID mismatches and immediately terminates suspicious sessions. |

---

## 💡 3. Root Cause & Architectural Principle
Customer A has logged into your multi-tenant SAS and saw customer B's data, their revenue numbers, their customer list, their private messages. Not good. Here's what actually happens next.

---

## ⚡ 4. Hardening Action Checklist
- [ ] the technical damage.
- [ ] the legal damage.
- [ ] what are you going to do about it?

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
> **Production Heuristic:** Not after the support ticket arrives.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

So, let me tell you how a Wednesday morning goes wrong. Your support inbox has a ticket that says, "I'm seeing someone else's dashboard. Customer A has logged into your multi-tenant SAS and saw customer B's data, their revenue numbers, their customer list, their private messages. Not good. Here's what actually happens next. Step one, the technical damage. Your tenant isolation has a gap in the system. A query with the missing wear clause or a caching layer that served the wrong tenants data because the cache key did not include the tenant context. The technical fix might take your AI an hour once you identify the root cause, but the technical fix is the smallest part of this entire story. Step two, the legal damage. Customer B's data was exposed to customer A. Now you have a legal obligation to notify customer B that their data was viewed by an unauthorized party. If customer B is in healthcare, you have a potential HIPPA violation and a fine. If you're in finance, a regulatory reporting requirement. And if you're in Europe, a GDPR breach notification filed within 72 hours. Customer A may have screenshotted the data before you fixed it. You cannot unsee what has been seen. And customer B does not care that it was a bug. They care that their private data was visible. to a stranger and they will ask these three questions. How long was this happening for? Who else could have seen my data? And number three, what are you going to do about it? If you cannot answer the first two almost immediately, your monitoring was not built for this business. Step three, the trust damage. Customer B leaves. That's a given. But the real damage is when customer A tells their whole network. They post it publicly and untended isolation failure becomes a reputation event for your whole product. Competitors, they'll screenshot it. Your sales team will hear about it on every call for the next 6 months. The companies that survive this are not the ones who fixed it the fastest. They are the ones who directed their AI to build tenant isolation as a business requirement from day one. Not as a technical afterthought the day after it broke, but a separate tenant and test and boundary architecture from the very first day. So, direct your AI to build monitoring that alerts the moment a tenant sees another tenants's data. Because by the time a customer tells you, the damage is already done and so are you.

</div>
