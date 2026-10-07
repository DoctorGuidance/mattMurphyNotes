# درس 064: درس 064: You shipped your web app as a mobile app

> **عنوان انگلیسی:** You shipped your web app as a mobile app  
> **حوزه معماری:** معماری فرانت‌اند، طراحی واسط و بهداشت API (Frontend Architecture & API Hygiene)  
> **لایه پروداکشن:** لایه 1 (UI & Accessibility)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcZOrpQCcZW/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث معماری فرانت‌اند، طراحی واسط و بهداشت API است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Frontend Architecture & API Hygiene و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Frontend Architecture & API Hygiene در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 064
// Domain: Frontend Architecture & API Hygiene
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 064 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

You just shipped your web app as a mobile app and every API key is visible in the devices local storage. Capacitor wraps your web app in a native shell. So everything that was in the browser is now on the device. Local storage session tokens, API keys, and web view cache. All of it sitting in the app's data directory where any rooted device or forensic tool can read it. So you did not ship a mobile app. You shipped your entire client side architect ure to a device you do not control. So here it's how we're going to fix it. Step one, move secrets out of client side storage and I mean API keys, tokens, and credentials. They do not belong in local storage on any mobile device. They belong in a platform secure keychain. Whether it's keychain on iOS or key store on Android, those are a win. Direct your AI to migrate all sensitive credentials from local storage to the platform's native secure storage using a capacitor secure storage. plugin. That's a win. Step two, certificate pinning on every API call. Without certificate pinning, any proxy can intercept your app's traffic. So, a user on a compro compromised network hands their session token to an attacker. So, direct your AI to implement certificate pinning on all API endpoints. So, the app will reject any connection not signed by your expected certificate. That's a win. And step three, deep link validation. Your app registers URL schemes. Without validation, a malicious app can register the same scheme and intercept authentication callbacks, password reset links, or even payment confirmations. So, direct your AI to implement deep link validation that verifies the origin and signature of every incoming deep link before processing it. Your web app had a browser protecting it. Your mobile app doesn't. So, fix the gaps capacitor left open for you.


</div>
