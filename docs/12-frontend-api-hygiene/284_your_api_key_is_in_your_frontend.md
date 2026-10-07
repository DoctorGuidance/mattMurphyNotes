# درس 284: درس 284: Your API key is in your frontend

> **عنوان انگلیسی:** Your API key is in your frontend  
> **حوزه معماری:** معماری فرانت‌اند، طراحی واسط و بهداشت API (Frontend Architecture & API Hygiene)  
> **لایه پروداکشن:** لایه 1 (UI & Accessibility)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DYpNvXGg_WM/)  

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
// Standard Hardening Snippet for Episode 284
// Domain: Frontend Architecture & API Hygiene
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 284 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Last week, I told you to hit F12 and search for the word key. If you found your API key sitting in your front-end JavaScript, that message was for you. Every visitor to your app, they can see it, too. Here's how you lock it down in 15 minutes. Step one, move all secrets to server side environment variables. Not in your code, not in your config file that ships to the browser, not in thev file that's committed to git, server side only. Vers has an EMV vase. Netlfi has an EMV vase. Railway, Render, Fly, they all have them. Put your keys there. Delete them from your code. Step two, create a proxy API route. Your front end should never call an external API directly. Instead, front end calls your server. Your server calls the API. The key lives on the server. The browser never sees it. One route, one file, 15 lines of code. Your secrets are invisible. Step three, rotate every key that was ever in your front end. Even if you just moved it, even if you think no one saw it, your git history remembers everything. If a key was ever committed, it's already been scraped. Go to open AI, go to Stripe, generate new keys, update your EMV vars. Old keys, dead keys out. Get them out. How many of your keys are still in your frontend code right now? Be honest. Drop it in the comments.


</div>
