# درس 201: درس 201: System-to-system auth is not user auth

> **عنوان انگلیسی:** System-to-system auth is not user auth  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DaAwzEqFWpT/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث احراز هویت و مدیریت نشست‌ها است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Authentication & Identity و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Authentication & Identity در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 201
// Domain: Authentication & Identity
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 201 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your API talks to three other services. Each one requires authentication. None of them are users logging in though. Here are the three things you got to get right. Step one, service to service off is not user off. There is no login screen, no session cookies, no password reset flow. One service proves to another that it has permission to make that request. The mechanism is different, but the stakes are definitely higher. A compromised service token does not affect one account, it affects all accounts. Step two, shared secrets are just a starting point. An API key in an environment variable works until that variable leaks. An environment variable leaks, they leak in logs, in error messages, and stack traces. So, rotate your secrets on a schedule, not after an incident. The rotation plan you build before the breach is the one that will save you, and that's a win. Step three, mutual TLS verifies both sides. ides the client proves itself to the server. The server proves itself to the client. No token to steal, no secret to rotate. The identity lives in the certificate. For high trust internal communications, MTLS removes the API key from the equation altogether. Your services trust each other. Make them prove it though.


</div>
