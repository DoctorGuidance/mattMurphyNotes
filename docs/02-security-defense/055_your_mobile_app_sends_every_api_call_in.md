# Episode 055: Your mobile app sends every API call in plain text

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcoH5avEj3J/) |

---

## 🚨 1. The Incident & Attack Vector
Your mobile app sends every API call in plain text. So someone on the same coffee shop Wi-Fi just watched all of your users log in. So your user opens your app at a coffee shop.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
So your user opens your app at a coffee shop. Every request between the app and your server crosses the network where anyone on that Wi-Fi can read it. Login credentials, session tokens, personal data.

---

## ⚡ 4. Hardening Action Checklist
- [ ] your app is not verifying the server it's talking to. So, your AI set up the API connection but never pinned the certificate.
- [ ] sensitive data is traveling in the request body with no additional protection. Even with a secure connection, tokens and credentials sitting in plain text in the request body are one misconfiguration away from full exposure.
- [ ] your app stores credentials on the device in plain text. So your AI saved the authentication token in local storage where any other app or anyone with physical access to the device can read it.

---

## 💻 5. Hardened Production Implementation
```typescript
# Docker Compose Network Segmentation
networks:
  frontend_net:
  backend_net:
    internal: true # No direct internet access
services:
  marketing:
    networks: [frontend_net]
  database:
    networks: [backend_net] # Isolated from marketing container
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Never deploy unverified AI-generated code directly to production without testing failure modes.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your mobile app sends every API call in plain text. So someone on the same coffee shop Wi-Fi just watched all of your users log in. So your user opens your app at a coffee shop. Every request between the app and your server crosses the network where anyone on that Wi-Fi can read it. Login credentials, session tokens, personal data. An attacker running a free tool on the same network captures all of it without touching your server or your app at all. So let's get this thing locked down. Step one, your app is not verifying the server it's talking to. So, your AI set up the API connection but never pinned the certificate. An attacker on the same network can sit between your app and your server, intercept every single request, and your app will never know the difference at all. So, direct your AI to implement certificate pinning so your app only communicates with your verified server. That and it rejects any connection where the certificate kit does not match. That's a win. Step two, sensitive data is traveling in the request body with no additional protection. Even with a secure connection, tokens and credentials sitting in plain text in the request body are one misconfiguration away from full exposure. So, directory AI to encrypt sensitive fields in your API payloads independently of the transport layer that so the data is protected even if the connection is compromised. In step three, your app stores credentials on the device in plain text. So your AI saved the authentication token in local storage where any other app or anyone with physical access to the device can read it. So direct your AI to move all tokens and credentials into the platform secure storage. So they are encrypted at rest and inaccessible to other applications. And well, your app works, your connection is not secure. That's the problem. So fix that transport. layer before your users end up paying for it.

</div>
