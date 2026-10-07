# Episode 077: You put Cloudflare in front of your app

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Caching & Edge Performance (`کشینگ، توزیع لبه و پرفورمنس سیستمی`) |
| **Target Production Layer** | Layer 10 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DcHNH00EZ1T/) |

---

## 🚨 1. The Incident & Attack Vector
You put Cloudflare in front of your app.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Implements caching without invalidation strategies or tenant namespaces in 'You put Cloudflare in front of your app', risking stale or leaked data. | Employs tenant-scoped cache keys with distributed mutex locks (anti-dogpile) and mutation-driven invalidation. |

---

## 💡 3. Root Cause & Architectural Principle
Cloudflare only protects you if all traffic is flowing through it. The moment someone finds your real IP, they skip everything. that you set up.

---

## ⚡ 4. Hardening Action Checklist
- [ ] your origin IP is leaking.
- [ ] your origin server still accepts connections from the entire internet.
- [ ] your SSL is probably set to flexible.

---

## 💻 5. Hardened Production Implementation
```typescript
// middleware/cors.ts
import cors from 'cors';

const ALLOWED_ORIGINS = ['https://app.company.com', 'https://portal.company.com'];

export const secureCors = cors({
  origin: (origin, callback) => {
    if (!origin || ALLOWED_ORIGINS.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Blocked by CORS policy: unauthorized origin'));
    }
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
});
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Cloudflare is not a switch you flip. It is an architecture you configure.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

You put Cloudflare in front of your app, but an attacker found your server's real IP and went right around it. All your W rules, all your DDoS protection, your bot filtering, your rate limiting, all of it bypassed completely because your origin server's IP address is discoverable and your attacker just hit it directly. Cloudflare only protects you if all traffic is flowing through it. The moment someone finds your real IP, they skip everything. that you set up. Here is what your AI missed when it configured your Cloudflare. Step one, your origin IP is leaking. DNS history tools store every IP your domain has ever pointed to. If you added Cloudflare after your site was already live, your precloudflare IP is a public record. Your email headers are exposing it. Misconfigured subdomains will point straight to it. So, direct your AI to check every subdomain, every MX record. every outbound email header and every DNS history service for your origin IP. If it's discoverable anywhere, your Cloudflare setup is a locked front door with a wide openen garage door. That's not a win. Step two, your origin server still accepts connections from the entire internet. It should only accept connections from Cloudflare's IP range. So, direct your AI to configure your firewall to whitelist Cloudflare's published IP ranges and block everything else. If a request does not come through Cloudflare, it does not reach your server. Period. And number three, your SSL is probably set to flexible. That means traffic between your user and Cloudflare is encrypted, but traffic between Cloudflare and your server is not encrypted. So an attacker on the network between Cloudflare and your origin sees everything in plain text. So direct your AI to set SSL to full strict mode and install a Cloudflare origin certificate on your server. Encrypted end to end, no gaps. Cloudflare is not a switch that you flip. It is an architecture that you must configure. So, direct your AI to configure it correctly before somebody walks right around it.

</div>
