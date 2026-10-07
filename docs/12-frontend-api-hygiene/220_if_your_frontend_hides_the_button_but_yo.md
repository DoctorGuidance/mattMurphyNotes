# درس 220: درس 220: If your frontend hides the button but your API still

> **عنوان انگلیسی:** If your frontend hides the button but your API still  
> **حوزه معماری:** معماری فرانت‌اند، طراحی واسط و بهداشت API (Frontend Architecture & API Hygiene)  
> **لایه پروداکشن:** لایه 1 (UI & Accessibility)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZs5JDxPOrW/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث معماری فرانت‌اند، طراحی واسط و بهداشت API است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Frontend Architecture & API Hygiene و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Frontend Architecture & API Hygiene در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 220
// Domain: Frontend Architecture & API Hygiene
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 220 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your app has users. Some of them are admins, some of them are not. And right now, you're checking it with an if statement. Here are the three things you do right now to fix that. Step one, understand what RBAC actually is. Ro based access control. Every user gets a role. Every role gets permissions. Admin can delete. Editor can update. Viewer can read. Those are the basics. Roles are enforced. at the API layer, not the UI layer. The UI hides things for convenience. The API blocks things for security. That's the win. Step two, start with three roles always. Admin, member, viewer. That covers 90% of SAS application use cases at launch. Do not build custom permission matrix. Well, not before you have your first paying customer. Ship three roles. Add complexity when the business demands it. That's the win. And step three, enforce it everywhere. Every API route checks the role. Every server action validates the user. If your front end hides the delete button, but your API still accepts the delete request, you do not have access control. You have a suggestion and suggestions do not survive a curious user with browser console. Right? You must enforce permission or it does not exist. That's The win.


</div>
