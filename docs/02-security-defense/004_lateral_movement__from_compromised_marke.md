# Episode 004: Lateral Movement: From Compromised Marketing Tool to Production Database

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Dd1Xt-zETRJ/) |

---

## 🚨 1. The Incident & Attack Vector
An attacker exploits a known vulnerability in a third-party marketing container. Because all containers share an unsegmented flat Docker network, the attacker pivots to the admin API and reads database credentials from environment variables.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Runs all services (marketing, admin API, database) inside a single flat network where everything trusts everything. | Strict network segmentation: marketing cannot reach database networks; internal service calls require mTLS or auth tokens. |

---

## 💡 3. Root Cause & Architectural Principle
Zero-trust network architecture: Network location does not equal authorization. Apply network isolation and the principle of least privilege so a breach in one container isolates the damage.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Segment your container networks so front-facing marketing tools cannot physically reach database subnets.
- [ ] Require service tokens or mutual TLS (mTLS) for all internal service-to-service API calls.
- [ ] Apply least-privilege permissions: containers that only serve marketing content must have read-only roles.

---

## 💻 5. Hardened Production Implementation
```typescript
# docker-compose.prod.yml - Network Segmentation
version: '3.8'
networks:
  public_net:
  private_net:
    internal: true # No direct route to public internet or marketing

services:
  marketing_tool:
    image: marketing:latest
    networks: [public_net] # Cannot reach private_net

  database:
    image: postgres:16
    networks: [private_net] # Completely isolated
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** One breach should give an attacker one compromised container—never your entire infrastructure.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI deployed multiple services on the same network. The marketing dashboard, the admin API, and the production database all communicate freely. A vulnerability in one gives access to them all. So, a network where everything trusts everything is one breach away from losing everything. It's time to do something about it. Step one, your marketing tool has a known vulnerability. An attacker exploits it and gains a shell on that container. From there, they can reach the admin API because both services share a network with no segmentation. So the admin API connects to the production database with credentials that are stored in environment variables that an attacker can now read. So one compromised marketing widget escalated to full database access. So direct your AI to segment your network so each service can only reach the specific services that it needs. Marketing can't reach the database. The admin API cannot reach marketing and that that's a win. Step two, service to service communication inside your network happens without authentication. So any process on the network can call any internal endpoint. An attacker who compromises one service makes unauthenticated requests to every other service. So direct your AI to require mutual TLS or service tokens for every internal API call. No internal request should be trusted because of its network location alone. Never. And number three, your AI deployed every service with the same permissions. The marketing container has the same network access as the database container. If a service does not need to reach the internet, should not be able to. If it does not need to write of the database, its credentials should be read only. So direct your AI to apply the principle of least privilege to every container, service account, and network rule. One breach should give an attacker one service, not your entire operation. And that is a win.

</div>
