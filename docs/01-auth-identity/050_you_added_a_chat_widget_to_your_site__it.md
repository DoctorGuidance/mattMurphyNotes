# درس 050: درس 050: You added a chat widget to your site. It can read every

> **عنوان انگلیسی:** You added a chat widget to your site. It can read every  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/Dct1A_WDsrP/)  

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
// Standard Hardening Snippet for Episode 050
// Domain: Authentication & Identity
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 050 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI added a chat widget to your site during your build. Not uncommon. But now it can read every password your users are typing on every single page. So your AI dropped in a script tag, one line, instant customer support widget in the corner of every page. But that script runs with the same privileges as your own code. It can read every form field, every keystroke, every cookie, every session token. Guess what? On every page, page, including your login page, your checkout page, your admin panel. So, you didn't install a chat widget. Your AI gave a third party full access to your entire application. Let's get it fixed. Step one, audit every third party script on your site and what it can access. Most teams cannot even list how many external scripts are loaded in their system. Analytics, chat, reviews, retargeting, AB testing, every one of them has full DOM. access by default. So, direct your AI to inventory every third party script, identify what data each can access, and then document which pages each script loads on. That's a win. Step two, remove third party scripts from every sensitive page. Your login page, your checkout page, your account settings page, your admin panel. No analytics tag needs to watch your users type their passwords. No chat widget needs to load on on your payment form. So, direct your AI to implement page level script loading that excludes thirdparty scripts from any page that handles credentials, payment data, or administrative functions. And step three, implement a content security policy that restricts what external scripts can do. A CSP tells the browser which domains are allowed to execute scripts on your page. Any script not on that list gets blocked. So, direct your AI to build a content security policy that whitelists only approved script sources and blocks inline script injection from any unauthorized origin. You control your code. Control who else gets to run theirs next to it.


</div>
