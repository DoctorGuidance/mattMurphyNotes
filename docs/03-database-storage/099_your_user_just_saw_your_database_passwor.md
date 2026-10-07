# درس 099: درس 099: Your user just saw your database password on their screen

> **عنوان انگلیسی:** Your user just saw your database password on their screen  
> **حوزه معماری:** پایگاه‌داده، روابط، ایندکس و پایداری داده (Database & Storage Engineering)  
> **لایه پروداکشن:** لایه 3 (Database & Storage)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DbqUuqlk7L6/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث پایگاه‌داده، روابط، ایندکس و پایداری داده است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Database & Storage Engineering و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Database & Storage Engineering در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 099
// Domain: Database & Storage Engineering
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 099 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your user just saw your database password on their screen. Your app crashed. Instead of a friendly error message, it dumped a raw stack trace with your database connection string, your framework versions, and the exact line of code that failed. That's not a bug, people. That is your AI showing the world exactly how to break into your application. So, here are the three things you're going to direct your AI to do right now to fix it. Number one, split your error handling into two layers. A public layer that shows your user a clean, helpful message and a private layer that logs the full technical detail on your server where only you can see it. Your AI built a handler that does both jobs. That is not efficiency. That is a security hole disguised as a feature. The moment you separate what your user sees from what your server records is the moment your app starts behaving like a product instead of a prototype. That's a win. Step two, catch errors at every boundary. Not just your login form, your API routes, your background jobs, your web hook receivers, your payment call backs. Every uncaught error is a stack trace waiting to leak. Directory AI to set up automated testing that catches these before your users do. Unit test with something like vi test or endtoend test with something like playright. Your AI knows how to configure both. turn them on, but it'll never do it unless you ask it to. Step three, build an error logging pipeline. Timestamps, user sessions, routes, inputs, stack traces, all of it. All private, all searchable. When something breaks at 2 a.m., you trace it in minutes, not 3 hours of guessing what happened. Your users should never see your internals, your logs. They should see everything. That is the difference between a product and a total liability. So, get Get out there and make it a win.


</div>
