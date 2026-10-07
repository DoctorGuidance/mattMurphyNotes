# درس 289: درس 289: Your users are your QA team

> **عنوان انگلیسی:** Your users are your QA team  
> **حوزه معماری:** تست، محیط‌های کاری، CI/CD و خط لوله استقرار (Testing, Staging & CI/CD)  
> **لایه پروداکشن:** لایه 7 (CI/CD & Pipelines)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DYhc3KSA_D1/)  

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
// Standard Hardening Snippet for Episode 289
// Domain: Testing, Staging & CI/CD
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 289 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Last week, I told you your users are doing QA for free. Six-year-old Android phones, mobile data, apostrophes in their name, whatever it was, your app broke three different ways, right? So, here's how to find those bugs before your users do. Step one, device testing matrix. You don't need a lab. You need browser stack. It has a free tier. Sign up for it. Or just grab two old phones from your old drawer. Test on the worst device you can find with the slowest connection, the smallest screen, the oldest browser. If it works there, it'll work everywhere. Step two, edge case input testing. Put an apostrophe in every single field or put 10,000 characters in a field built for 50. Leave required fields empty and hit the submit button or paste emojis in the search bar. I'm telling you, your AI never tested these. Your users will. Step three, get five strangers to use it with zero context. Not your friends, not your co-founder, not your mom, people who have never seen your app. Hand them your phone and say nothing. Watch where they tap. Watch where they get stuck. Watch where they give up. That's your bug report from users. So, tell me, what's the dumbest bug a user ever found in your app? I got some funny ones, but comment below.


</div>
