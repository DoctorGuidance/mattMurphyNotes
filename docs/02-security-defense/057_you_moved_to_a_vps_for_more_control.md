# Episode 057: You moved to a VPS for more control

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Dci-Qq_j9EL/) |

---

## 🚨 1. The Incident & Attack Vector
You moved to a VPS for more control.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Leaves VPS root SSH access enabled with default passwords and open administrative ports on public IP addresses. | Hardens Linux VPS hosts: disables root SSH, enforces key-based authentication, configures UFW firewalls, and enables Fail2ban. |

---

## 💡 3. Root Cause & Architectural Principle
So, firewall rules, SSH hardening, automatic patching. You never thought about any of it because someone else's platform was doing it for you. Now, you own that server and every vulnerability that lives on it.

---

## ⚡ 4. Hardening Action Checklist
- [ ] SSH hardening.
- [ ] a firewall that blocks everything you did not explicitly allow.
- [ ] automatic security updates.

---

## 💻 5. Hardened Production Implementation
```typescript
// middleware/rateLimiter.ts
import { RateLimiterRedis } from 'rate-limiter-flexible';
import { redisClient } from '../lib/redis';
import { Request, Response, NextFunction } from 'express';

const limiter = new RateLimiterRedis({
  storeClient: redisClient,
  keyPrefix: 'rl_global',
  points: 10,       // Max 10 requests
  duration: 60,     // Per 60 seconds
  blockDuration: 60 // Block for 60s if exceeded
});

export async function rateLimitMiddleware(req: Request, res: Response, next: NextFunction) {
  try {
    await limiter.consume(req.ip);
    next();
  } catch (err) {
    res.status(429).json({ error: 'Rate limit exceeded. Try again in 60s.' });
  }
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Three fixes. Five minutes each. Direct your AI to lock it down before someone else walks in.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

You moved to a VPS for more control, and I can't blame you, but you accidentally left the front door wide open when you did it. Your managed platform is handling security invisibly. So, firewall rules, SSH hardening, automatic patching. You never thought about any of it because someone else's platform was doing it for you. Now, you own that server and every vulnerability that lives on it. So, here's what your AI never configured when you set up your VPS. No. Number one, SSH hardening. Right now, your server is accepting password authentication on a default port. Every bot on the internet is trying root passwords against port 22 around the clock. So, your server is being attacked right now. You don't even know it. So, disable password authentication entirely. Switch to keybased access only and change the default SSH port. Disable root login while you're there. These are four commands that take 5 minutes and stop 9 99% of automated attacks before they start. So direct your AI to harden your SSH configuration before you do anything else on that server. That's a win. Step two, a firewall that blocks everything you did not explicitly allow. Your managed platform had invisible firewall rules. Your VPS has none. So every port wide open, every service fully reachable, and your database port is exposed to the public internet. So direct your AI to configure UFW or IP tables to deny all inbound traffic by default and allow only specific ports your application needs like SSH, HTTP or HTTPS. Nothing else gets through. And step three, automatic security updates. Your managed platform patched itself. Your VPS does not. So every unpatched vulnerability is a door someone will eventually walk through and you don't know about it. The longer you wait, the more do doors that are open. So direct your AI to configure unattended security updates so critical patches apply automatically without you having to remember to check. More control means more responsibility. No doubt about it. Your managed platform protected you from yourself. Your VPS is not going to. You got to handle it.

</div>
