# درس 027: درس 027: An attacker just skipped your entire form and sent raw data

> **عنوان انگلیسی:** An attacker just skipped your entire form and sent raw data  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdOvuLgiUiv/)  

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
// Standard Hardening Snippet for Episode 027
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 027 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI just let an attacker skip your entire form and send raw data straight to your API. Empty strings, negative prices, garbage in every single field. So your AI validated everything in the browser, but none of it runs on the server. So your AI added ZOD validation to your forms, required fields, email format, password length, right? Well, it catches everything in the browser, but the server accepts the raw request body without checking it at all. So, client validation is a user experience feature. Server validation is a security control. Your AI built one and skipped the other. Let's get it fixed. Number one, your form validates on the client. Your server does not. An attacker sends a request directly to your endpoint. Your form never sees it. Your server processes it without a question. And your database stores whatever arrived. So, Zod runs anywhere JavaScript runs. So your AI treated it as a front-end tool. You need to direct your AI to run the same schema on the server. That's the win. Step two, an attacker adds fields your form does not have an is admin flag or a roll override or a price override. Your server passes the full request body to your database without stripping anything unexpected. So if your schema defines 10 fields and the request contains 11, the 11th should not exist. in your system at all. So direct your AI to reject unknown fields from every single request. And number three, every API endpoint is accessible without your front end. Invalid values, extra fields. If the server accepts them, the validation is cosmetic. Your server must enforce the same rules your form does independently. So direct your AI to test every route by sending a request without the form. The form catches the mistakes. The server catches attacks. That's something you want to get your hands around for the win.


</div>
