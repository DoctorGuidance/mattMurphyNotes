# درس 221: درس 221: Application-level filtering is a prayer

> **عنوان انگلیسی:** Application-level filtering is a prayer  
> **حوزه معماری:** معماری چندمستأجره و جداسازی قطعی داده‌ها (Multi-Tenancy & Data Isolation)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZslOCNRDNh/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث معماری چندمستأجره و جداسازی قطعی داده‌ها است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Multi-Tenancy & Data Isolation و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Multi-Tenancy & Data Isolation در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 221
// Domain: Multi-Tenancy & Data Isolation
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 221 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your application, it's got a bug. A query returns data that it should not have and the user sees another customer's records. In most applications, nothing can stop this. But rowle security certainly will. Here are the three things you need to know right now about RLS. Step one, RLS is a database level firewall. You write the policy. The user can only see rows where the tenant ID matches their own ID. Every query passes through a policy first. If the row does not belong to the user does not exist. Step two, this is not the same as filtering in your application code. One missed wear clause and you have a data leak. RLS means the database itself enforces this rule. Even if the application code is wrong, the data stays protected. That is the difference between a policy and a prayer and that's a win. Step three, Superbase makes RLS accessible. You enable it per table and every query respects the policy. see automatically. For anything where one user should never see another user's information, RLS is not a feature, it's the foundation. So, always make sure to protect the data at the source.


</div>
