# درس 047: درس 047: Your app just showed a user your database name, your server

> **عنوان انگلیسی:** Your app just showed a user your database name, your server  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcybEeAEhP8/)  

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
// Standard Hardening Snippet for Episode 047
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 047 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI built app just showed a user your database name, your server file path, and their query that failed. And they were not trying to hack you. They accidentally clicked on a broken link. Your AI built error handling. Great. Detailed stack traces, full database queries, and internal file paths. However, you shipped it to production, and now your users are seeing the same data. So, an attacker does not need to probe your system. Your error pages are doing the reconnaissance for them. So, let's get it cleaned up. Step one, separate your error responses by environment. Development shows the full stack trace. Production shows a generic message. Your users should never see an error that contains a file path, a query string, or a database name, or even a package version. So, direct your AI to implement environmentaware error handling so that it returns detailed errors only in development and returns generic userfriendly responses in production. That's definitely a win. Step two, route every error to centralized logging, not to the user screen. Every error your app throws should be captured, timestamped, and searchable in your monitoring system. No doubt about it. The user sees a clean error page. You see the full detail in your logs. So, direct your AI to implement structured error logging that captures the full stack trace request context and the user session data in your monitoring tool without exposing any of it to the client. That's also a win. And step three, build custom error pages that reveal nothing. So your 404 or your 500 or your timeout page, every one of them should be branded, helpful, and architecturally silent. So direct your AI to build custom error pages for every common error code. so that it gives the user a clear next step without revealing any server side details. Those users who found a bug, do not let the bug write itself or the report. That's not a win.


</div>
