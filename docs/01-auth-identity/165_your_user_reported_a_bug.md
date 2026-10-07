# درس 165: درس 165: Your user reported a bug

> **عنوان انگلیسی:** Your user reported a bug  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DafuL1lggp3/)  

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
// Standard Hardening Snippet for Episode 165
// Domain: Authentication & Identity
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 165 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your user reported a bug. You asked them to describe it. They just said everything stopped working. So, that's not necessarily a great bug report. It's definitely a cry for help. Here are the three things you direct your AI to do right now to fix it. Step one, session replays. Direct your AI to integrate session replays into your application. That way, every user session is fully recorded. So, every click, every scroll, every error, when a user reports a bug, You don't have to ask what happened. You watch what happened from their screen in real time. That's a win. Step two, connect replay to error tracking. Direct your AI to link session replays directly to error events. So when Sentry catches an exception, the replay is attached automatically. You see the error and the user experience that caused it side by side. No guessing, no reproducing. It's all right there. And step three, Flag rage clicks. A user who clicks the same button seven times in 3 seconds is not patient. They're stuck. Direct your AI to detect rage clicks and flag them as UX failures before a support ticket is filed. So stop asking users to describe bugs. Start watching what they experienced. That is orchestration and that is the win.


</div>
