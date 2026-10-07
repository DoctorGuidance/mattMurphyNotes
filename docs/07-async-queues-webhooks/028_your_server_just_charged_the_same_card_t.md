# درس 028: درس 028: Your server just charged the same card twice, provisioned

> **عنوان انگلیسی:** Your server just charged the same card twice, provisioned  
> **حوزه معماری:** صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی (Async Queues & Webhooks)  
> **لایه پروداکشن:** لایه 6 (Cloud & Compute)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdMufvsE6Z3/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Async Queues & Webhooks و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Async Queues & Webhooks در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 028
// Domain: Async Queues & Webhooks
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 028 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Uh-oh. Your server just charged the same credit card twice, provisioned the same user twice, and sent the exact same email to them twice, but every web hook signature was totally valid. And that quite frankly is the problem. So your AI verified the web hook signature, clerk, resend, and GitHub all retry failed web hooks, right? But your server processes the same valid event two times. So signature ver ification is step one. Item potency is step two, but your AI stopped at step one. So, let's get it fixed. Number one, direct your AI to store every event ID before it processes the handler logic. Check the ID against your database. If it already exists, return a success response and do nothing at all. If it does not, store it, then process it. The order definitely matters. Store first, process second. If the handler crashes mid process, process. The retry sees the stored ID and skips the duplicate process. Without this, every network timeout, every slow response, every infrastructure hiccup triggers a retry with a valid signature that your server treats as a brand new event. So, a user provisioned twice, a payment recorded twice, and an email sent twice. That web hook wasn't forged, folks. It was just delivered more than once. And that is not a win. Number two, set a replay window. Reject event IDs older than 24 hours. Without a window, your storage grows indefinitely, and an attacker can replay a captured web hook from 3 months ago with a valid signature. So, a timestamp checks close that gap permanently. Direct your AI to compare the events creation time against a 24-hour threshold and reject anything. side of it. That's a win. And number three, return a success response for all duplicates. Right? If your server returns an error on a duplicate event, the provider will retry it again. So more duplicates equals more duplicate processing, which equals more duplicate emails. That's not a win. So a success response tells the provider the event was received even if your server already handled it. Especially if your server already handled it, right? So the sign proves the sender. Item potency proves you only acted once. And that that's the double check system that works.


</div>
