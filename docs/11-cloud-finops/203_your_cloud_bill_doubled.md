# Episode 203: Your cloud bill doubled

> **Category:** Cloud Infrastructure & FinOps (معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه)  
> **Production Layer:** Layer 6  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DZ-KjLZEcwV/](https://www.instagram.com/reel/DZ-KjLZEcwV/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your cloud bill doubled last month. You're not exactly sure which service is causing it. And you're not alone.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
And you're not alone. So, here are the three things you're going to check right now to figure it out. Step one, check your idle resources.

---

## ⚡ 3. Hardening Action Checklist
- [ ] check your idle resources. That staging environment you spun up 3 months ago, it's still running.
- [ ] rightize it. Your production server runs on an instance built for traffic you don't have yet.
- [ ] data going into the cloud is free, but data coming out is not egress fees. So every API response, every image served, every web hook payload.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #203
// Domain: 11-cloud-finops
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #203 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #203');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your cloud bill doubled last month. You're not exactly sure which service is causing it. And you're not alone. So, here are the three things you're going to check right now to figure it out. Step one, check your idle resources. That staging environment you spun up 3 months ago, it's still running. Or the database replica you created for a load test that's still accepting connections. Uh-oh. What about the storage bucket from a feature you never shipped still acrewing charges daily? I'm telling you, cloud providers, they do not remind you, they bill you forever. So, audit what is running, kill what is not. That's the win. Step two, rightize it. Your production server runs on an instance built for traffic you don't have yet. Overprovisioning, yeah, it feels safe, but it's also really expensive. Most applications run at about 15% utilization on hardware sized for the full 100%. So, make sure you match the resources to the actual load, not the load you hope to have. Step three, data going into the cloud is free, but data coming out is not egress fees. So every API response, every image served, every web hook payload. If your architecture moves data between regions or between providers, the bill is growing quietly. So you have to know where your data travels, folks. Your cloud bill is not a mystery. It is a mirror of your architecture decisions.

</div>
