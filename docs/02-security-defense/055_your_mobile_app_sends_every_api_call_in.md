# درس 055: درس 055: Your mobile app sends every API call in plain text

> **عنوان انگلیسی:** Your mobile app sends every API call in plain text  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcoH5avEj3J/)  

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
// Standard Hardening Snippet for Episode 055
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 055 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your mobile app sends every API call in plain text. So someone on the same coffee shop Wi-Fi just watched all of your users log in. So your user opens your app at a coffee shop. Every request between the app and your server crosses the network where anyone on that Wi-Fi can read it. Login credentials, session tokens, personal data. An attacker running a free tool on the same network captures all of it without touching your server or your app at all. So let's get this thing locked down. Step one, your app is not verifying the server it's talking to. So, your AI set up the API connection but never pinned the certificate. An attacker on the same network can sit between your app and your server, intercept every single request, and your app will never know the difference at all. So, direct your AI to implement certificate pinning so your app only communicates with your verified server. That and it rejects any connection where the certificate kit does not match. That's a win. Step two, sensitive data is traveling in the request body with no additional protection. Even with a secure connection, tokens and credentials sitting in plain text in the request body are one misconfiguration away from full exposure. So, directory AI to encrypt sensitive fields in your API payloads independently of the transport layer that so the data is protected even if the connection is compromised. In step three, your app stores credentials on the device in plain text. So your AI saved the authentication token in local storage where any other app or anyone with physical access to the device can read it. So direct your AI to move all tokens and credentials into the platform secure storage. So they are encrypted at rest and inaccessible to other applications. And well, your app works, your connection is not secure. That's the problem. So fix that transport. layer before your users end up paying for it.


</div>
