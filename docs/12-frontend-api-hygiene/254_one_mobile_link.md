# Episode 254: One mobile link

> **Category:** Frontend Architecture & API Hygiene (معماری فرانت‌اند، طراحی واسط و بهداشت API)  
> **Production Layer:** Layer 1  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DZLHBM9xY33/](https://www.instagram.com/reel/DZLHBM9xY33/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your mobile app exists, but when someone shares a link to your content, it opens in the browser, not the app like it was supposed to. The user hits a login wall, gets confused, and leaves. You lost them because of a missing configuration file.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
You lost them because of a missing configuration file. Here are the three things you can do right now to fix it. Number one, configure Apple universal links.

---

## ⚡ 3. Hardening Action Checklist
- [ ] configure Apple universal links. Go create an apple.app site association file in your domain.
- [ ] configure Android app links. Similarly, create a digital assets link file hosted at your doommain.com.
- [ ] handle the fallback. Not every user has your app installed on their phone.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Strict Tenant & User-Scoped Query
const record = await prisma.document.findFirst({
  where: {
    id: req.params.id,
    tenantId: req.user.tenantId // Mandatory tenant isolation
  }
});
if (!record) throw new NotFoundError('Access denied or record not found');
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your mobile app exists, but when someone shares a link to your content, it opens in the browser, not the app like it was supposed to. The user hits a login wall, gets confused, and leaves. You lost them because of a missing configuration file. Here are the three things you can do right now to fix it. Number one, configure Apple universal links. Go create an apple.app site association file in your domain. Host it at your domain. com. This is a JSON file that tells iOS which URL path should open your app. No redirects. The link opens directly in your app every time. Apple verifies this file when the user installs your app. Step two, configure Android app links. Similarly, create a digital assets link file hosted at your doommain.com. Again, this JSON file tells Android which URLs open your app. Add intent filters to your Android manifest. X handles this with Expo linking package. Same URLs work on both platforms. Step three, handle the fallback. Not every user has your app installed on their phone. If the app is not installed, the link should go straight to your website. Your website shows the content plus a smart banner promoting the app install. Expo Router handles this with a single configuration. One URL, app installed, opens an app, not installed, opens in website with Install prompt. Universal links convert mobile web visitors into app users. Without them, every shared link is a dead end. Do you have any deep linking setups? What tripped you up? Tell me about it.

</div>
