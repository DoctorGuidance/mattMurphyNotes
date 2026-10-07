# درس 018: درس 018: An attacker just used a password reset link from four

> **عنوان انگلیسی:** An attacker just used a password reset link from four  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdeMk-bFdui/)  

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
// Standard Hardening Snippet for Episode 018
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 018 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Did an attacker just use a password reset link from four months ago to hack your app? That token still works. Uh-oh. Your user change their password twice since then, but the old link still logs them in. So, your AI built a password reset flow. It generates a token, sends an email, and lets the user set a new password, but the token never expires, and the token is never invalidated after use. So, a reset token without an expiration is a permanent key to your account. Let's get it locked down. Step one, an attacker who accesses an old email, a forwarded message, a breached inbox finds every reset link ever sent. Each one still works because your AI never set a time limit. Four months later, a token is still valid. The user has changed their password, updated their security settings, enabled two-factor authentication, but none of it matters because the old link bypasses all of that. So, direct your AI to set every password reset token to expire within 15 minutes. That's a win. Step two, a reset token that works more than once lets an attacker use it after the legitimate user already has. So, the user clicks the link, resets the password, and moves on, right? Well, the attacker clicks the same link an hour later and resets it again. The user has no idea what just happened. So, directory AI to invalidate every reset token immediately after the first use. In step three, an attacker who finds the reset endpoint can request thousands of tokens per minute. Each one is a valid entry point. Each one lands in the inbox the attacker may have access to. Without rate limiting, your reset flow is a token factory. So, direct your AI to Limit reset requests to three per email address per hour. That's a win. Your your password reset has a door, folks. Your AI built it without a lock, without a timer, and without a limit. Time to lock it down for good.


</div>
