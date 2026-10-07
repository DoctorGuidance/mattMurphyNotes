# درس 145: درس 145: Your security kicks users out every 15 minutes

> **عنوان انگلیسی:** Your security kicks users out every 15 minutes  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/Daxv0QLgG8B/)  

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
// Standard Hardening Snippet for Episode 145
// Domain: Authentication & Identity
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 145 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your security settings are kicking users out every 15 minutes, even when they're actively working. So, your definition of idle might be broken. Here are the three things you're going to direct your AI to fix right now. Step one, define meaningful activity. Mouse movement, not an activity. A tab open in the background, also not an activity. Direct your AI to track actions that prove the user is still working. Form submissions, but button clicks, API calls, page navigation. If the user is reading a long document without clicking, that also is not idle. So, build an exception for sustained focus. That's a win. Step two, warn them before you kill them. Direct your AI to show a modal 60 seconds before the session expires. Your session expires in 60 seconds. Click to stay logged in. The user who stepped away for coffee sees it when they return. The user who left the office for the day doesn't That's the win. One warning will save you hundreds of frustrated support tickets. Trust me. Step three, preserve state on reauthentication. The session expired. The user logs back in. You need to direct your AI to return them exactly where they were at. Not the homepage, not a blank dashboard, their unsaved form, their half-completed workflow, wherever they were. If reauthentication erases that work, your security just cost you a customer. Secure sessions, smart timeouts, and preserve state. Those are best practices. So, build security that protects you without punishing your users.


</div>
