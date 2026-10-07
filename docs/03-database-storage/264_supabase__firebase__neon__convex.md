# درس 264: درس 264: Supabase. Firebase. Neon. Convex

> **عنوان انگلیسی:** Supabase. Firebase. Neon. Convex  
> **حوزه معماری:** پایگاه‌داده، روابط، ایندکس و پایداری داده (Database & Storage Engineering)  
> **لایه پروداکشن:** لایه 3 (Database & Storage)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZALI2bRljh/)  

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
// Standard Hardening Snippet for Episode 264
// Domain: Database & Storage Engineering
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 264 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

I've gotten the same question three different ways this week from 20 different people. Should I use Superbase or Firebase? Should I use Convex instead? What about Neon? Well, there's no universal answer about databases, but there is a universal framework. So, here are the three things you can do right now to figure it out. Step one, match your database to your data shape. If your data is relational, meaning uh users have orders, orders have items, and items belong in C categories, you need Postgress. Well, Superbase and Neon both run Postgress under the hood from the factory. That's a win. But if your data is document shaped, meaning each record is a self-contained blob of JSON, Firebase and Convex might make more sense. In Convex on mobile apps, definitely a win. So, don't fight your data shape. Step two, evaluate the ecosystem, not just the database. Superbase gives you off storage and real time out of the box, right? Neon gives you serverless, Postgress with database branching. Firebase gives you Google's infrastructure and tight mobile integration and the database engine matters less than the tooling around it. Right? Pick the one where you write the least amount of custom code. Step three, plan your exit before your build. Superbase and neon run standard Postgress. You can leave anytime. Firebase and convex though use proprietary models. So if you want to leave, you're rewriting your entire data layer. No matter what you pick, the best database is the one you understand fully, you can afford, and you can leave when you need to.


</div>
