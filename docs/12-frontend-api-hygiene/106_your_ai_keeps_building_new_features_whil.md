# درس 106: درس 106: Your AI keeps building new features while your existing

> **عنوان انگلیسی:** Your AI keeps building new features while your existing  
> **حوزه معماری:** معماری فرانت‌اند، طراحی واسط و بهداشت API (Frontend Architecture & API Hygiene)  
> **لایه پروداکشن:** لایه 1 (UI & Accessibility)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DbeZo5Zx5i2/)  

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
// Standard Hardening Snippet for Episode 106
// Domain: Frontend Architecture & API Hygiene
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 106 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI keeps building new features while your existing features are totally broken and you keep letting it because building feels like progress. Something breaks, a payment flow fails, your onboarding drops people at step three. Instead of fixing it, you ask your AI to build the next feature. Guess what? Been there, done that. Because new features feel like momentum, and there's a lot of dopamine in the AI system. Fixing feels like you're going backwards. Here are three reasons that your instinct is destroying your product. Step one, every new feature stacked on a broken foundation makes the foundation more fragile. Your AI will happily add a notification system on top of an offflow that drops sessions. It will build a reporting dashboard that queries a database that has no indexes. So, your AI builds what you ask for, but it never asks whether the thing underneath it can hold the weight of what you're building. Step two, Your customers are not asking for new features. They are asking for the current ones to work perfectly. Go read your support inbox. The signal is not, I wish this had more features. It never is. The signal is this does not work the way I expected. New features attract customers. Sure, broken features lose them fast. And losing is more expensive than delaying. Step three, direct your AI to run a feature health audit before it builds anything new. What is live? What is broken? What has active users versus zero adoption? Broken and used gets fixed first. Broken and unused gets killed. Only after the foundation is solid do you build the next thing. Your AI will build forever if you let it. But your job as an AIdirected engineer is to tell it when to stop building and start fixing.


</div>
