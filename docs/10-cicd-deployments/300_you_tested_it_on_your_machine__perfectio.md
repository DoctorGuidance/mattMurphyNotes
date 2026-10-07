# درس 300: درس 300: You tested it on your machine. Perfection!

> **عنوان انگلیسی:** You tested it on your machine. Perfection!  
> **حوزه معماری:** تست، محیط‌های کاری، CI/CD و خط لوله استقرار (Testing, Staging & CI/CD)  
> **لایه پروداکشن:** لایه 7 (CI/CD & Pipelines)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DYVJUa3xSOu/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث تست، محیط‌های کاری، CI/CD و خط لوله استقرار است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Testing, Staging & CI/CD و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Testing, Staging & CI/CD در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 300
// Domain: Testing, Staging & CI/CD
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 300 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

So, I saw that you shipped your app that you tested on your machine on your account with your data. Of course, it works perfectly. But now, somebody with a six-year-old Android opens your app and boom, the layout breaks. The images don't load. The form submits twice. Or someone else signs up with a name that has an apostrophe in it. Your database throws an error. Their account doesn't even exist anymore. Uh-oh. Or a third person opens it on Safari. Safari. Yeah, I said Safari and half the features won't work. Turns out you didn't actually test your app. You demoed your app to yourself and it worked great. But the real QA team sounds like those are your users and they're not sending you bug reports. They're sending you uninstalls. So the people who find your bugs shouldn't also be the people that are paying for the system. The fix to this issue is definitely coming next week. Follow along so you don't miss a thing.


</div>
