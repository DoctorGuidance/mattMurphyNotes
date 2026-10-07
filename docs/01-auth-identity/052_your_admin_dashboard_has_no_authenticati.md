# درس 052: درس 052: Your admin dashboard has no authentication

> **عنوان انگلیسی:** Your admin dashboard has no authentication  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcrQPBHG0_I/)  

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
// Standard Hardening Snippet for Episode 052
// Domain: Authentication & Identity
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 052 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your admin dashboard has no authentication because your AI assumed it was internal only. Well, it's not. It is on the public internet. So, your AI built an admin panel so you could manage your users, view orders, and update the settings, right? Well, it put it at back/admin or back slashdashboard, whatever it is. No login screen, no access control. It assumed only you would know the URL. Well, every automated scanner on the internet has already found it. Right now, anyone who types domain followed by backslashadmin can see every user in your system, every transaction in your database, and every setting you can change. Some of them, they can even change them themselves. So, we need to shut it down. Step one, your admin panel is accessible to anyone who can guess the URL. There's no authentication between the public internet and most of your sensitive controls. So, direct your AI to add authentication to every admin route immed mediately. No admin page should render without a verified session from a user with explicit admin privileges. Period. Not a regular user session. An admin session with rolebased verification. That's definitely a win. Step two, your admin routes are predictable paths, right? Every scanner on Earth is checking for back slashadmin back slash dashboard back slashmanage or back slashbackend or admin, right? So if your admin panel is at any of those it's already been found. Direct your AI to move your admin routes to a non-guessable path and implement rate limiting on login attempts to block brute force attacks on those. That's a win. And step three, your admin panel has no audit trail. You do not know who's accessed it, when they accessed it, or what they changed. If someone has already been in your admin panel, you have no way to know what they saw, or what they modified. So, Directory AI to implement an audit log that records every admin action, every login attempt, every data change with timestamps and user identification. That's definitely a win. Your admin panel is the keys to your entire business. Right now, you left those keys sitting on the sidewalk for anyone to pick up.


</div>
