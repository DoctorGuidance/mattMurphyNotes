# درس 157: درس 157: Your AI loaded scripts from 14 domains

> **عنوان انگلیسی:** Your AI loaded scripts from 14 domains  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/Danl3ysjuQ8/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث احراز هویت و مدیریت نشست‌ها است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Authentication & Identity و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Authentication & Identity در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 157
// Domain: Authentication & Identity
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 157 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your app is loading scripts from 14 different domains and you only approved three of them. Your AI pulled in analytics, font libraries, thirdparty widgets, and tracking pixels. Every one of them runs code in your users browsers. So, here are the three things you're going to direct your AI to do right now to lock it down. Step one, content security policy headers. Direct your AI to add CSP headers that whitelist ex exactly which domains can load scripts in your application. If a domain is not on the list, the browser blocks it. One malicious script on one compromised CDN can hijack every session on your site. CSP stops it before it executes, and that's the win. Step two, audit what your AI installed. Direct your AI to list every external resource your application is loading. Scripts, stylesheets, fonts, images, iframes. If you cannot explain why each one is there. It shouldn't be there. Your AI added it for convenience. You need to verify it did not add risk. Step three, report before you enforce. CSP has a report only mode. Direct your AI to enable reporting first. Collect violations for a week. See what breaks before you block it. Then you enforce. 14 domains is not a feature. It's an attack surface your AI built. without asking you about it. So now it's time to lock it down.


</div>
