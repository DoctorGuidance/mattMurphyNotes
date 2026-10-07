# Episode 301: Hit deploy. It’s broken

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `HIGH` |
| **Architectural Domain** | Testing, Staging & CI/CD (`تست، محیط‌های کاری، CI/CD و خط لوله استقرار`) |
| **Target Production Layer** | Layer 7 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYUiLhrNY9o/) |

---

## 🚨 1. The Incident & Attack Vector
When you hit deploy, you refresh and it's broken, and then you hit deploy again and it works and you have no idea what has changed

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Deploys code directly to production without environment parity, automated regression testing, or rollback plans in 'Hit deploy. It’s broken'. | Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for 'Hit deploy. It’s broken'. |

---

## 💡 3. Root Cause & Architectural Principle
When you hit deploy, you refresh and it's broken, and then you hit deploy again and it works and you have no idea what has changed

---

## ⚡ 4. Hardening Action Checklist
- [ ] preview deploys before going live.
- [ ] one thing at a time.
- [ ] know your roll back.

---

## 💻 5. Hardened Production Implementation
```json
// vercel.json - Preview Deployment & Instant Rollback Strategy
{
  "github": {
    "silent": true,
    "autoJobCancelation": true
  },
  "buildCommand": "npm run build:check",
  "cleanUrls": true
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** In fact, more tips and tricks coming tomorrow

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

When you hit deploy, you refresh and it's broken, and then you hit deploy again and it works and you have no idea what has changed. That's not engineering. That's gambling. And here's how you stop praying and start shipping. Number one, preview deploys before going live. Versel and Netlifi both do this for free. Great platforms. Every time you push code, it builds a preview URL for you to check out, a live version of your app. with the new changes that nobody sees but you. Super powerful. Click around, test it, make sure everything works, then push it to production. You'd test drive a car right before you bought it. Well, test drive your deploy before shipping it. Your customers will appreciate it. Number two, one thing at a time. Stop shipping 47 changes in one deploy because when it breaks, and it's going to break, you have no idea which of those 47 changes caused the break. All commits, small deploys. Each one does one particular thing. If it breaks, you know exactly what broke, exactly how to fix it, right? This alone eliminates 80% of deployment headaches, and you don't want one. Number three, know your roll back. Before you hit deploy, know exactly how to undo it step by step. One click, under 60 seconds, full roll back. Versel has instant roll back on the previous deploy because when your app is down and your users are leaving, you're going to want that button. And you don't want to be googling how to roll back for the first time when it's happening. So ship with confidence, not with cross fingers. Every deploy should be totally boring. In fact, more tips and tricks coming tomorrow.

</div>
