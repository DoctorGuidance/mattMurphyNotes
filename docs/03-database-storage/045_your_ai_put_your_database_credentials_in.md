# درس 045: درس 045: Your AI put your database credentials in a Next.js Server

> **عنوان انگلیسی:** Your AI put your database credentials in a Next.js Server  
> **حوزه معماری:** پایگاه‌داده، روابط، ایندکس و پایداری داده (Database & Storage Engineering)  
> **لایه پروداکشن:** لایه 3 (Database & Storage)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/Dc0_yCoHNXv/)  

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
// Standard Hardening Snippet for Episode 045
// Domain: Database & Storage Engineering
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 045 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI put your database credentials in a next.js server action. So the build process shipped them to every user's browser. Your AI built your Nex.js. It wrote server functions that query your database directly, but it put server logic and client components in the exact same file. So Nex.js analyzed the imports, decided your server dependencies belonged on the client side, and included your database connection string in the code. It delivers to your users's browser. So your production secrets are in view source right now. That's not a win. So let's fix it. Step one, install the serveronly package and mark every sensitive file. This package creates a build error if any server code is accidentally included in what ships to the browser. So direct your AI to add the serveron import to every file that touches your database, your API keys or any of your credentials. If the build succeeds after adding it, your secrets are not exposed. That's a win. Step two, separate server logic and client components into different files. A single file that exports both server functions and browserfacing components is a boundary your AI should have never crossed. So, direct your AI to move every server function into dedicated files so that they share no exports with anything that renders in the browser. and verify no server import chain reaches a client entry point. That's a win. And step three, scan your deployed code for leaked secrets. Every JavaScript file your app delivers is totally public. So direct your AI to run a production build and search the output for your database host name, your API keys, your connection string, and every value in your environmental variables. Any match means that secrets are already visible to every user who open developer tools on your site. So your server functions run on the server. Your credentials should also stay there. That's the win.


</div>
