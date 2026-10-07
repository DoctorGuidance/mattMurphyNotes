# درس 071: درس 071: Your status page says operational. Your customers are

> **عنوان انگلیسی:** Your status page says operational. Your customers are  
> **حوزه معماری:** معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه (Cloud Infrastructure & FinOps)  
> **لایه پروداکشن:** لایه 6 (Cloud & Compute)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcO7fDEj9eg/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Cloud Infrastructure & FinOps و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Cloud Infrastructure & FinOps در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 071
// Domain: Cloud Infrastructure & FinOps
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 071 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your status page is saying fully operational, but your customers are screenshotting error messages in your support channel right now. So, you have no idea which endpoints are failing, which customers are affected, and how much revenue those failures are costing you because your monitoring is telling you the system is up when it's down. And it never tells you how much failure your business can actually afford. So, here's what tier three reliability engineering looks like for your platform. Step one, a defined error budget per critical endpoint. Not a global uptime number, a budget. Your payment endpoints get a 0.1% error budget per rolling 30-day window. Out of 100,000 requests, 100 can fail before you're in violation. When you're within budget, ship features. When you're burning budget, freeze deploys and fix your reliability. So, direct your AI to define error budgets for your three highest revenue endpoints based on business. business impact, not infrastructure default. That's a win. Step two, burn rate alerting that catches trends before they become outages. If your 30-day error budget is 50% consumed in 48 hours, something changed and you are on track for a breach. Burn rate alerts measure the speed at which your budget is being consumed and fire when the trajectory is unsustainable. So, direct your AI to calculate burn rate on each error budget. and alert when projected consumption will exhaust the budget before the window resets. That's a win. Step three, business cost attribution on every single incident. Not the API returned 500 for errors in 12 minutes, but how many users were affected, how many transactions failed, and what the revenue impact was. An incident on your documentation page and your incident on your checkout page are not the same severity levels. You have to prioritize them. So, directory AI to instrument business metric correlation so incidents are measured in dollars lost, not status codes logged. 99.9% uptime is not a badge, it's a budget. Direct your AI to start spending it like it is one.


</div>
