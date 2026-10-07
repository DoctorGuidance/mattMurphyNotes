# Episode 064: You shipped your web app as a mobile app

> **Category:** Frontend Architecture & API Hygiene (معماری فرانت‌اند، طراحی واسط و بهداشت API)  
> **Production Layer:** Layer 1  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DcZOrpQCcZW/](https://www.instagram.com/reel/DcZOrpQCcZW/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
You just shipped your web app as a mobile app and every API key is visible in the devices local storage. Capacitor wraps your web app in a native shell. So everything that was in the browser is now on the device.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
So everything that was in the browser is now on the device. Local storage session tokens, API keys, and web view cache. All of it sitting in the app's data directory where any rooted device or forensic tool can read it.

---

## ⚡ 3. Hardening Action Checklist
- [ ] move secrets out of client side storage and I mean API keys, tokens, and credentials. They do not belong in local storage on any mobile device.
- [ ] certificate pinning on every API call. Without certificate pinning, any proxy can intercept your app's traffic.
- [ ] deep link validation. Your app registers URL schemes.

---

## 💻 4. Hardened Implementation Code / Config
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

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

You just shipped your web app as a mobile app and every API key is visible in the devices local storage. Capacitor wraps your web app in a native shell. So everything that was in the browser is now on the device. Local storage session tokens, API keys, and web view cache. All of it sitting in the app's data directory where any rooted device or forensic tool can read it. So you did not ship a mobile app. You shipped your entire client side architect ure to a device you do not control. So here it's how we're going to fix it. Step one, move secrets out of client side storage and I mean API keys, tokens, and credentials. They do not belong in local storage on any mobile device. They belong in a platform secure keychain. Whether it's keychain on iOS or key store on Android, those are a win. Direct your AI to migrate all sensitive credentials from local storage to the platform's native secure storage using a capacitor secure storage. plugin. That's a win. Step two, certificate pinning on every API call. Without certificate pinning, any proxy can intercept your app's traffic. So, a user on a compro compromised network hands their session token to an attacker. So, direct your AI to implement certificate pinning on all API endpoints. So, the app will reject any connection not signed by your expected certificate. That's a win. And step three, deep link validation. Your app registers URL schemes. Without validation, a malicious app can register the same scheme and intercept authentication callbacks, password reset links, or even payment confirmations. So, direct your AI to implement deep link validation that verifies the origin and signature of every incoming deep link before processing it. Your web app had a browser protecting it. Your mobile app doesn't. So, fix the gaps capacitor left open for you.

</div>
