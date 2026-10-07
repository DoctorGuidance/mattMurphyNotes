# درس 070: درس 070: Every time a new client signs up, your developer forks the

> **عنوان انگلیسی:** Every time a new client signs up, your developer forks the  
> **حوزه معماری:** معماری فرانت‌اند، طراحی واسط و بهداشت API (Frontend Architecture & API Hygiene)  
> **لایه پروداکشن:** لایه 1 (UI & Accessibility)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcQ8u02Cj1A/)  

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
// Standard Hardening Snippet for Episode 070
// Domain: Frontend Architecture & API Hygiene
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 070 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Every time a new client signs up for your multi-tenant system, you fork the entire repository. New branch, new deployment, new set of environmental variables. Client number four wanted dashboard in dark mode. Client number seven wanted to export CSVs instead of PDFs. And client number 11 wants to skip onboarding entirely. So your AI copied the codebase and started customizing. But now you have 11 versions of your product and you cannot remember which client runs which branch. So that's no longer a product. That's actually 11 products wearing the exact same name. Here's how you're going to direct your AI to serve all of those clients without forking your product for each and everyone. Step one, feature flag scoped per tenant. A feature flag is not a global onoff switch. It's a per tenant configuration. Client number seven gets those CSV exports. Client four gets dark mode. And everyone else gets the default. One codebase evaluates the tenant context and renders the right experience. So directory AI to implement tenant scoped feature flags where every configurable behavior is controlled by tenant ID not by code branches. That's a win. Step two, tenant configuration inheritance with override layers. So start with a base configuration every tenant shares. Layer tenant specific overrides on top of that client. 11 overrides the onboarding flow. Everyone else inherits the default. So when you update the base, every tenant gets the update unless they have an explicit override. So direct your AI to build a configuration system with base defaults and per tenant overrides that merge at runtime. That's a win. And step three, tenant aware routing at the application boundary. The application must know which tenant is making the request before it touches any logic. subdomain, header, jot claim. That identity drives which configuration loads, which features will activate, which branding will render. So, direct your AI to implement tenant resolution middleware that identifies the tenant on every single request and then it injects the tenant context before any business logic executes. One codebase, 11 clients, zero forks. So, directory AI to build it that way from day one.


</div>
