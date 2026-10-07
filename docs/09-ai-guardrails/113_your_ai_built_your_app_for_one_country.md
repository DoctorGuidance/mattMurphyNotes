# درس 113: درس 113: Your AI built your app for one country

> **عنوان انگلیسی:** Your AI built your app for one country  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DbVvJBgDv7n/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه AI Guardrails, LLM Security & Compliance و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به AI Guardrails, LLM Security & Compliance در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 113
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 113 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI built your app for one country, but your customers live in 12 countries. Right now, someone in Logos is trying to pay you, and your payment processor is rejecting their card. Someone in Mumbai is looking at a date picker that makes no sense because your AI hard-coded the American date format. And someone in London is getting your support emails at 3:00 a.m. because your AI scheduled everything in American Central time. So, your AI built for the country you live in. That's great. But your business does not live in one country. Here are the three things you're going to direct your AI to fix before your international customers stop trying at all. Step one, multicurrency payment support. Your AI connected Stripe with one currency. Stripe supports 135 currencies natively. So, your AI will never turn it on because you never told it your customers live outside your zone in the United States. So, direct your AI to enable automatic currency conversion at checkout. So, a customer in Kenya sees Kenyon shillings and a customer in the UK sees pounds. The integration takes you an afternoon. The customers you are losing take their money somewhere else permanently. So, step two, local aare formatting across your entire application. Dates, times, numbers, currencies, and addresses. Every one of these displays differently depending on where your customers live. So your AI hard-coded American formatting because that's what the tutorials use and that's where you live. But you need to direct your AI to implement localal detection and format every userfacing data point based on the customer's actual location. One wrong date format tells an international customer this product was not built for them. And step three, time zone aware scheduling. For every automated communication, emails, notifications, reminders, subscription, renewals, all of them should fire relative to your customer's time zone, not yours. So, direct your AI to store each user's time zone at sign up and reference it for every scheduled event in the system. A renewal reminder at 3:00 a.m. is not a reminder at all. It's just noise. So, your AI built a product for your time zone, your currency in your language, and it did great. But your customers do not agree to any of those limitations. So, direct your AI to build for where your customers are actually living. And that's a win.


</div>
