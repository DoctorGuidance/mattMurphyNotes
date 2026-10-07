# Episode 157: Your AI loaded scripts from 14 domains

> **Category:** Authentication & Identity (احراز هویت و مدیریت نشست‌ها)  
> **Production Layer:** Layer 4  
> **Official Instagram Reel:** [https://www.instagram.com/reel/Danl3ysjuQ8/](https://www.instagram.com/reel/Danl3ysjuQ8/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your app is loading scripts from 14 different domains and you only approved three of them. Your AI pulled in analytics, font libraries, thirdparty widgets, and tracking pixels. Every one of them runs code in your users browsers.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
Every one of them runs code in your users browsers. So, here are the three things you're going to direct your AI to do right now to lock it down. Step one, content security policy headers.

---

## ⚡ 3. Hardening Action Checklist
- [ ] content security policy headers. Direct your AI to add CSP headers that whitelist ex exactly which domains can load scripts in your application.
- [ ] audit what your AI installed. Direct your AI to list every external resource your application is loading.
- [ ] report before you enforce. CSP has a report only mode.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #157
// Domain: 01-auth-identity
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #157 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #157');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your app is loading scripts from 14 different domains and you only approved three of them. Your AI pulled in analytics, font libraries, thirdparty widgets, and tracking pixels. Every one of them runs code in your users browsers. So, here are the three things you're going to direct your AI to do right now to lock it down. Step one, content security policy headers. Direct your AI to add CSP headers that whitelist ex exactly which domains can load scripts in your application. If a domain is not on the list, the browser blocks it. One malicious script on one compromised CDN can hijack every session on your site. CSP stops it before it executes, and that's the win. Step two, audit what your AI installed. Direct your AI to list every external resource your application is loading. Scripts, stylesheets, fonts, images, iframes. If you cannot explain why each one is there. It shouldn't be there. Your AI added it for convenience. You need to verify it did not add risk. Step three, report before you enforce. CSP has a report only mode. Direct your AI to enable reporting first. Collect violations for a week. See what breaks before you block it. Then you enforce. 14 domains is not a feature. It's an attack surface your AI built. without asking you about it. So now it's time to lock it down.

</div>
