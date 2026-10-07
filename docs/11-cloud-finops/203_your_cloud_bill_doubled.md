# Episode 203: Your cloud bill doubled

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Cloud Infrastructure & FinOps (`معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه`) |
| **Target Production Layer** | Layer 6 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZ-KjLZEcwV/) |

---

## 🚨 1. The Incident & Attack Vector
Your cloud bill doubled.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Leaves serverless functions or compute instances unmonitored without timeouts or egress alarms in 'Your cloud bill doubled'. | Enforces hard function timeouts (15-30s), egress bandwidth controls, and automated cloud spending kill-switches. |

---

## 💡 3. Root Cause & Architectural Principle
And you're not alone. So, here are the three things you're going to check right now to figure it out. Step one, check your idle resources.

---

## ⚡ 4. Hardening Action Checklist
- [ ] check your idle resources.
- [ ] rightize it.
- [ ] data going into the cloud is free, but data coming out is not egress fees.

---

## 💻 5. Hardened Production Implementation
```typescript
// lib/dbPool.ts
import { Pool } from 'pg';

export const dbPool = new Pool({
  connectionString: process.env.DATABASE_POOL_URL, // PgBouncer transaction pool
  max: 20,                                         // Strict ceiling per serverless container
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 5000,
});
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** That is an architecture problem.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your cloud bill doubled last month. You're not exactly sure which service is causing it. And you're not alone. So, here are the three things you're going to check right now to figure it out. Step one, check your idle resources. That staging environment you spun up 3 months ago, it's still running. Or the database replica you created for a load test that's still accepting connections. Uh-oh. What about the storage bucket from a feature you never shipped still acrewing charges daily? I'm telling you, cloud providers, they do not remind you, they bill you forever. So, audit what is running, kill what is not. That's the win. Step two, rightize it. Your production server runs on an instance built for traffic you don't have yet. Overprovisioning, yeah, it feels safe, but it's also really expensive. Most applications run at about 15% utilization on hardware sized for the full 100%. So, make sure you match the resources to the actual load, not the load you hope to have. Step three, data going into the cloud is free, but data coming out is not egress fees. So every API response, every image served, every web hook payload. If your architecture moves data between regions or between providers, the bill is growing quietly. So you have to know where your data travels, folks. Your cloud bill is not a mystery. It is a mirror of your architecture decisions.

</div>
