# Episode 169: A $20 self-hosted runner runs unlimited minutes

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Testing, Staging & CI/CD (`تست، محیط‌های کاری، CI/CD و خط لوله استقرار`) |
| **Target Production Layer** | Layer 7 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DabfLrfF-OA/) |

---

## 🚨 1. The Incident & Attack Vector
A $20 self-hosted runner runs unlimited minutes.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Relies on unverified AI code assumptions without failure handling or production boundaries in Testing, Staging & CI/CD. | Applies hardened architectural patterns, strict input boundaries, and automated monitoring for Testing, Staging & CI/CD. |

---

## 💡 3. Root Cause & Architectural Principle
Step one, self-hosted runners. GitHub actions let you bring your own compute. It's a $20 per month server and it runs unlimited minutes.

---

## ⚡ 4. Hardening Action Checklist
- [ ] self-hosted runners.
- [ ] conditional pipelines.
- [ ] monitor your usage before it surprises you.

---

## 💻 5. Hardened Production Implementation
```typescript
// config/productionHardening.ts
export const productionConfig = {
  timeoutMs: 8000,
  maxPayloadBytes: 1024 * 1024, // 1MB payload ceiling
  headers: {
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains'
  }
};
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** CI that scales does not surprise you on day 19.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your CI/CD pipeline just exceeded the free tier midsprint. Here are three things you're going to change right now to fix it. Step one, self-hosted runners. GitHub actions let you bring your own compute. It's a $20 per month server and it runs unlimited minutes. So that same pipeline that cost $1,200 in overrun charges now runs for $20 on your own machine. Yeah, you manage the server and you manage the runner software. and you manage the updates. But for teams that are burning through CI minutes, the math takes 5 seconds to figure out. It's a win. Step two, conditional pipelines. Not every commit needs every single test. A change to your readme does not need integration tests. A change to your marketing page does not need your back-end build. Pathbased triggers run only the stages that match the change files. Fewer stages, fewer minutes, same safety. Most Teams run the full suite on every push. That's not thorough, that's wasteful. Step three, monitor your usage before it surprises you. GitHub shows you your minute consumption and settings. Check it weekly. Set a team alert at 75% of your monthly allocation. When the alert fires, you have time to optimize and fix. When the pipeline stops, you have no time for anything. So, the CI that scales is not the one with the most features. It's the one that does not surprise you on day 19. in the middle of that sprint.

</div>
