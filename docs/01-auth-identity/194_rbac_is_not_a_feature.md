# درس 194: درس 194: RBAC is not a feature

> **عنوان انگلیسی:** RBAC is not a feature  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DaGcgHaiq3i/)  

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
// Standard Hardening Snippet for Episode 194
// Domain: Authentication & Identity
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 194 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

RBAC, RO based access control. Everyone says they have it. Most people have a boolean called underscore admin. Here are the three things you decide before you build it. Step one, roles versus permissions. A role is a label. Admin, editor, viewer. A permission is an action. Can create, can delete, can export. Most applications assign roles and hardcode what those roles can do. When the customer asks for a custom role, the whole system breaks. Build permissions first. Let roles be collections of those permissions. And that's the win. Step two, where enforcement happens. Your front end hides the button. Your API still accepts the request. That is not access control, folks. That's a suggestion and a security problem. Enforcement must happen at the API layer. Every route, every endpoint, the front end controls that experience. The backend controls all the access. Step three, scope. Can this user edit any document or only documents they created? Can this admin manage all teams or only their team? RBAC without scope is completely binary. You either have access or you do not. So RBAC with scope is granular. You have access to what belongs to you. The difference between a feature and architecture is whether it scales. So build the architecture right the first time.


</div>
