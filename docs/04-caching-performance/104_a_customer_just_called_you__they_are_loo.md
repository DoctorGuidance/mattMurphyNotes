# درس 104: درس 104: A customer just called you. They are looking at someone

> **عنوان انگلیسی:** A customer just called you. They are looking at someone  
> **حوزه معماری:** کشینگ، توزیع لبه و پرفورمنس سیستمی (Caching & Edge Performance)  
> **لایه پروداکشن:** لایه 10 (Caching & CDN)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DbimVuCkZqi/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث کشینگ، توزیع لبه و پرفورمنس سیستمی است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Caching & Edge Performance و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Caching & Edge Performance در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 104
// Domain: Caching & Edge Performance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 104 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

A customer just called you. They're looking at someone else's revenue dashboard on your system, their invoices, their customer list, their monthly revenue on your customer's screen right now. So, your AI set up caching to speed up your app, but it never scoped the cache to the appropriate tenant. So, customer A loaded their dashboard and the result got cached. Customer B loaded the same page and boom, your cash served customer A's financial data instantly to customer B. Here's why this happens and what you need to direct your AI to do to fix it immediately. Step one, your database security is irrelevant if your cache layer completely bypasses it. So you might have perfect rowle security on your databases. A lot of people do, but your cache sits in front of your database. So when your AI cached that query result, it cached the output after your security rules ran for customer A. So So customer B never hit the database. They get customer A's cache result served directly to them. So you need to direct your AI to scope every single cache key to the tenant ID. No exceptions. Every cache query, every cache page fragment, every cache API response must include a tenant context in that key. That's a win. Step two, caching is not the only shared layer leaking. Search indexes, background job cues, file storage pads and logging pipelines, right? Every shared service in your stack is a potential cross-tenant leak if your AI never scoped it appropriately. So, direct your AI to audit every shared layer and verify tenant isolation on every single one. If the layer does not know which tenant is serving, it should not be serving anything at all. And step three, test this before your customer figures it out. Direct your AI to build a cross-tenant access test. Log in as customer A. Load a page. Log out. Log in as customer B. Load that same page. If any data from customer A appears, your cash is leaking. This takes 10 minutes to test. The lawsuit from not testing it will take you years and a couple bucks promised. So, one cash query, two customers, and zero trust is left in your product. Direct your AI to scope every shared layer to every tenant today. And that's the win.


</div>
