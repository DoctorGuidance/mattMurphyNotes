# درس 094: درس 094: Your AI built your database. It never planned for the day

> **عنوان انگلیسی:** Your AI built your database. It never planned for the day  
> **حوزه معماری:** پایگاه‌داده، روابط، ایندکس و پایداری داده (Database & Storage Engineering)  
> **لایه پروداکشن:** لایه 3 (Database & Storage)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DbyDJomAkQv/)  

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
// Standard Hardening Snippet for Episode 094
// Domain: Database & Storage Engineering
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 094 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI built your database, but it never planned for the day you have to change it completely. So, your app is live, customers are using it, and you just realize you need to add a field, rename a column, or restructure how two tables relate to each other. So, that's a migration, and your AI has no idea how to do one without taking your app completely offline. So, here are three things you direct your AI to build before you touch any live database. Step one, a migration script that runs without downtime. Your AI will default to dropping a column and recreating it. On a live database, that means every customer query that hits that column while the migration runs either fails or returns total garbage. So, direct your AI to write migrations that add before they remove anything. New column goes up, data copies over, application switches to the new column, old column drops, only after everything is confirmed by you. That sequence is the difference between a migration and an outage. That's a win. Step two, a roll back plan written before the migration ever starts. If the migration breaks halfway through, you need to undo it right then. Not tomorrow, not after you debug it, but immediately. So, direct your AI to write the roll back script at the same time it writes the migration plan. If it cannot describe how to reverse it, the migration is not ready to run. And step three, a staging environment where you run the migration first, not on production, not on a copy you made 3 weeks ago, a current mirror of your live database where you test the exact migration with real data shapes before it touches a single customer record. So direct your AI to set this up before you run anything at all. The first time you test a migration should never be against the database your customers are depending on. Your AI built the database in minutes. Changing it safely takes engineering judgment and a little bit of time. And that is your job.


</div>
