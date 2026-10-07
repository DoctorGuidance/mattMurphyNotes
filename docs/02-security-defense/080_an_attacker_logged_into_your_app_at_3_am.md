# درس 080: درس 080: An attacker logged into your app at 3 AM from another

> **عنوان انگلیسی:** An attacker logged into your app at 3 AM from another  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcEEyocD8II/)  

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
// Standard Hardening Snippet for Episode 080
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 080 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

A hacker logged into your app at 3:00 a.m. from another country. Your app said, "Welcome back." Stolen credentials, foreign IP, middle of the night. So, your app cannot tell the difference between your real user and the person who has stolen their password. It's the same role, same permissions, same access to everything because your AI built static roles that never evaluate context in the moment. So, here's what tier 3 RBAC actually looks like for your app. Step one, attribute-based access control. Permissions that evaluate context, not just the role. What time of day it is, what location, where the device fingerprint is, what's the IP reputation, what's the data sensitivity level. So, direct your AI to build a policy engine that evaluates these attributes on every single request. A user accessing financial records at 3:00 a.m. from an unrecognized device gets stepped up authentication or denied entirely. Same role, different context. effects different decision. That's definitely a win. Step two, zero trust enforcement on every internal request, not just the login gate, every API call, every database query. So every service to service request that reverifies identity and authorization. Your AI trusts everything inside the network perimeter. Zero trust assumes there is no perimeter. Every request who proves it is or gets rejected. And step three, continue. continuous session risk scoring, not a one-time check at login, a running evaluation that monitors behavior throughout their session. If a user's behavior pattern shifts midsession, the system challenges or terminates automatically. So, direct your AI to build session anomaly detection that watches for impossible travel, unusual data access volume, or privilege escalation attempts in real time. Static roles tell you who someone else is. Context tells you whether to trust them right now or not. So, direct your eye to build for both.


</div>
