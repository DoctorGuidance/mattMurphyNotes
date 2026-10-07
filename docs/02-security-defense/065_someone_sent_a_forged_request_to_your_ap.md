# درس 065: درس 065: Someone sent a forged request to your API last Tuesday

> **عنوان انگلیسی:** Someone sent a forged request to your API last Tuesday  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcYrFHSAOhJ/)  

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
// Standard Hardening Snippet for Episode 065
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 065 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Someone sent a forged request to your API last Tuesday. Your server processed it. No questions asked. No request signing, no verification that the request came from a legitimate client. No check on whether the payload was tampered with in transit. So your server accepted the request, ran the mutation, and returned a 200. The attacker now knows your API better than your documentation does cuz your API is a front door with no lock, no doorbell. and no one watching. So, here is how we're going to fix it. Step one, request signing on every mutating endpoint. Every post, put, patch, and delete should carry a signature. An HMAC hash of the request body signed with a shared secret. So, your server verifies the signature before processing. So, unassigned requests, they get rejected. So, direct your AI to implement request signing middleware that validates HMAC signatures on all mutating API calls. That's a win. Step two, API versioning. From day one, your API path includes a version. V1 stays stable. V2 introduces breaking changes. Consumers migrate on their schedule. Without versioning, though, every schema change is a production incident for every consumer. So, direct your AI to implement path-based API versioning and a version negotiation strategy. That is definitely a win. And step three, Deprecation policy with sunset headers. When an endpoint is scheduled for removal, the response includes a sunset header with retirement date. Consumers get warnings. Monitoring tracks usage of deprecating endpoints. And when usage hits zero, the endpoint, it's removed. So, direct your AI to implement sunset headers and deprecating monitoring on every endpoint scheduled for retirement. Your API is your contract with every consumer. It's time to harden it.


</div>
