# درس 032: درس 032: 32% of companies stopped buying software and built it with

> **عنوان انگلیسی:** 32% of companies stopped buying software and built it with  
> **حوزه معماری:** معماری فرانت‌اند، طراحی واسط و بهداشت API (Frontend Architecture & API Hygiene)  
> **لایه پروداکشن:** لایه 1 (UI & Accessibility)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdHlEdhgsvV/)  

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
// Standard Hardening Snippet for Episode 032
// Domain: Frontend Architecture & API Hygiene
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 032 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

One out of three companies this year stopped buying software altogether and built it in-house with AI instead. McKenzie's recent state of AI 2026 report says 32% skip purchasing software in 2026 altogether. Tech was at 41%, healthcare 39% and high performing mid-markets 50%. But small businesses are flat at 22%. They have the same tools, the same access and even greater benefit. But that 22% is is not a failure of tools. It's an absence of AI educated operators. So, let's talk about it. First, the 32% clearly had someone who could scope the problem internally, not a developer, an AI educated operator who understood their specific business needs, broke it into buildable modules, and directed their AI to build each one for their company. In doing so, they stopped renting a CRM for $2,000 a month that did 1,200 things when their business only needed 20. So, they direct ed their AI to build the 20 and owned the result. That's a win. So, the software they replaced was not complex. The decision to replace it required someone who could see the gap and direct their AI to build into it. So, again, that's a win. Secondly, the 22% of small business operators had access to the same tools and did nothing with them, mostly because they don't have time. But nobody could translate a business need into a business specification. It's stuff. So the bottleneck was never access to the models. They're all out there. It is access to someone who could effectively and safely direct their AI. And that gap is the entire market for what you can do for business owners. Every company in that 22% group is a potential client for an AIdirected operator who can scope direct and ship. And third, AI speed without AI direction is how one and a half million API keys leaked from a single app last year. Yep. The 32% who succeeded had scope verification and an operator accountable for the output. The ones who leaked all of those keys had a model and too much enthusiasm. Building is not the hard part anymore. In fact, everyone can do it. Knowing what to build in what order with what safeguards is the entire job now. The tools, they're almost free. The direction of them is the product. And the 202% out there of small businesses, they need you to learn. those tools. Those tools are free, but the direction is the product you're going to build for them.


</div>
