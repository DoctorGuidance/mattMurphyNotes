# درس 216: درس 216: Images do not belong in database columns

> **عنوان انگلیسی:** Images do not belong in database columns  
> **حوزه معماری:** پایگاه‌داده، روابط، ایندکس و پایداری داده (Database & Storage Engineering)  
> **لایه پروداکشن:** لایه 3 (Database & Storage)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZxfOW9xsFD/)  

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
// Standard Hardening Snippet for Episode 216
// Domain: Database & Storage Engineering
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 216 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your users are uploading images. You store them in the database. Your database is now doing two jobs it was never designed to do at the exact same time. Here are the three things you're going to do to your database right now to fix it. Step one, move files out of the database. Images, PDFs, videos. None of these belong in a database column. They belong in object storage. Object storage is built for these files specifically. Databases are built for rows. Mixing them is how a $200 a month database becomes an $800 a month database. No reason at all. Step two, serve files from a CDN. When someone loads a profile picture, that request should never hit your origin server. It should hit the CDN node closest to your end user. Faster delivery, lower bandwidth cost. The user gets the file in milliseconds instead of seconds. You know what? That's a win. Step three, separate your data model completely. Your database stores a URL that points to the file, not the file itself. A string column instead of a blob column holding 10 megabytes. This is not optimization. This is the standard and the way you should be building. Every production system separates storage from data. The ones that don't just haven't hit the wall yet. So, make sure you store smart for the win every time.


</div>
