# درس 033: درس 033: An attacker just typed a crafted string into your search

> **عنوان انگلیسی:** An attacker just typed a crafted string into your search  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdHBY76jE2o/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث امنیت نرم‌افزار، حملات و دفاع لایه‌ای است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Application Security & Defense و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Application Security & Defense در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 033
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 033 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

An attacker just typed a crafted string right into your search field and your database returned every user's credentials. That's not a win. Your AI dropped into raw SQL and removed every protection that Prisma provides. So, your AI needed a complex join or a search feature. Prisma's standard methods could not handle it. So, it wrote a raw SQL and every protection your ORM provides disappeared right then. The ORM protected you. The escape hatch does not. So, here's how you're going to direct your AI to close that gap. Number one, your AI put user input directly into a database command, a search field, a filter, or a sort parameter. Right? So, any input your users touch is now a direct line to your database with nothing standing between them. So, an attacker does not need to break into your system. They just type a crafted string to a form in your AI built and your database answers. every question that they ask, customer tables, user credentials, payment records, they have access to everything. The ORM was designed to prevent exactly this. So your AI bypassed it the moment the query got complicated, right? So direct it to use the ORM safe method for raw queries. That treats input as data, not as a part of the command. And that's a win. Number two, validate every input before it reaches any query. A search field that accepts 10,000 characters when the longest valid search is 200 is not a feature. It's an open invitation to get hacked. A price filter that accepts text is not flexible. It's exploitable. Directory add to constrain every input to the expected type and length before it touches the database layer at all. The validation should reject anything unexpected. Not try to sanitize it, reject it. That's the win. And number three, direct your AI to find Every raw query in your codebase right now, one search, every instance. Any raw query that builds itself from user input is an open door to your system. So your AI may have written one or it may have written 20. You do not know until you look. So each one is a direct channel between a form field and your entire database. Your ORM is not the vulnerability, but that one place your AI bypassed it certainly is. Go find it. Get it fixed.


</div>
