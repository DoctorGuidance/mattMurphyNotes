# درس 190: درس 190: You wrote RLS policies

> **عنوان انگلیسی:** You wrote RLS policies  
> **حوزه معماری:** معماری چندمستأجره و جداسازی قطعی داده‌ها (Multi-Tenancy & Data Isolation)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DaLDSqRgaBG/)  

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
// Standard Hardening Snippet for Episode 190
// Domain: Multi-Tenancy & Data Isolation
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 190 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

You just spent two long hours writing rowle security policies, beautiful rules, tenant isolation, role-based access on every single table. And then you built an API route that queries the database with the service ro key. The service ro key bypasses every RS policy you just wrote. Every single one of them. Your front end calls an API endpoint. That endpoint connects to the database as a service role. The service role sees everything. every tenant, every row, every table, every time. So your RLS policies are performing for an audience of nobody. The attacker does not go through the front door where your policies are watching. They find the API route where your service key already opened every lock in the building for them. 45% of vibecoded applications that we review have a security vulnerability. And this one, they seem to all share. A database policy that protects nothing because the application code walks right around around it every time. Your security, it's not your policies. Your security is every path to the data. And right now, one of those critical paths has the door fully unlocked. I just dropped the fix to this in the free faction community. The link is in my bio. Come check it out.


</div>
