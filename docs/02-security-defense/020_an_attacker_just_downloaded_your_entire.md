# درس 020: درس 020: An attacker just downloaded your entire API schema

> **عنوان انگلیسی:** An attacker just downloaded your entire API schema  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdbnwpOiEZJ/)  

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
// Standard Hardening Snippet for Episode 020
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 020 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI just let an attacker download your entire API schema. Every query, every mutation, every type and relationship in your database. So your AI deployed a GraphQL endpoint and left introspection enabled. When your AI set up Apollo server or GraphQL API, introspection is enabled by default. In development, it powers autocomplete and documentation. But in production, it hands an attacker a complete map of your back end. And a map of every door is the first thing a burglar wants. So let's get all those doors locked down. Number one, introspection returns your full schema on a single request. Every type name, every field, every argument, every relationship. So an attacker does not guess your API service. They read it. Your mutations reveal what actions exist. Your types reveal what data exists. Your field names reveal your database structure. So direct your AI to disable introspection in production with one configuration flag. That's a win. Number two, an attacker who knows your schema crafts queries that request deeply nested relationships. A query that joins users to orders to payments to addresses five levels deep, right? Well, that can return gigabytes of data in single request and crash your server completely. So your AI never set a depth limit. So direct your AI to enforce a maximum query depth and complexity score on every single request. And number three, even with introspection disabled, an attacker can reconstruct your schema by sending queries and observing which ones succeed and which ones fail. So field suggestions and error messages reveal valid field names one at a time. So your AI left field suggestion enabled in your production error responses. So direct your AI to disable field suggestions and return generic error messages that reveal nothing about your schema. This way your API documentation is for your developers only and your schema is for your application. An attacker should have access to neither of them. That's the win.


</div>
