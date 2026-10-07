# Episode 045: Your AI put your database credentials in a Next.js Server

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Database & Storage Engineering (`پایگاه‌داده، روابط، ایندکس و پایداری داده`) |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/Dc0_yCoHNXv/) |

---

## 🚨 1. The Incident & Attack Vector
Your AI put your database credentials in a next.js server action. So the build process shipped them to every user's browser. Your AI built your Nex.js.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
Your AI built your Nex.js. It wrote server functions that query your database directly, but it put server logic and client components in the exact same file. So Nex.js analyzed the imports, decided your server dependencies belonged on the client side, and included your database connection string in the code.

---

## ⚡ 4. Hardening Action Checklist
- [ ] install the serveronly package and mark every sensitive file. This package creates a build error if any server code is accidentally included in what ships to the browser.
- [ ] separate server logic and client components into different files. A single file that exports both server functions and browserfacing components is a boundary your AI should have never crossed.
- [ ] scan your deployed code for leaked secrets. Every JavaScript file your app delivers is totally public.

---

## 💻 5. Hardened Production Implementation
```typescript
// Hardened Production Configuration - Episode #045
// Domain: 03-database-storage
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #045 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #045');
  }
  return true;
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Never deploy unverified AI-generated code directly to production without testing failure modes.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your AI put your database credentials in a next.js server action. So the build process shipped them to every user's browser. Your AI built your Nex.js. It wrote server functions that query your database directly, but it put server logic and client components in the exact same file. So Nex.js analyzed the imports, decided your server dependencies belonged on the client side, and included your database connection string in the code. It delivers to your users's browser. So your production secrets are in view source right now. That's not a win. So let's fix it. Step one, install the serveronly package and mark every sensitive file. This package creates a build error if any server code is accidentally included in what ships to the browser. So direct your AI to add the serveron import to every file that touches your database, your API keys or any of your credentials. If the build succeeds after adding it, your secrets are not exposed. That's a win. Step two, separate server logic and client components into different files. A single file that exports both server functions and browserfacing components is a boundary your AI should have never crossed. So, direct your AI to move every server function into dedicated files so that they share no exports with anything that renders in the browser. and verify no server import chain reaches a client entry point. That's a win. And step three, scan your deployed code for leaked secrets. Every JavaScript file your app delivers is totally public. So direct your AI to run a production build and search the output for your database host name, your API keys, your connection string, and every value in your environmental variables. Any match means that secrets are already visible to every user who open developer tools on your site. So your server functions run on the server. Your credentials should also stay there. That's the win.

</div>
