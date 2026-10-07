# درس 026: درس 026: An attacker sent a phishing email from your domain

> **عنوان انگلیسی:** An attacker sent a phishing email from your domain  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdPTYpBAiuY/)  

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
// Standard Hardening Snippet for Episode 026
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 026 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

An attacker just sent a fishing email from your domain. SPF passed, DKIM passed, Demar passed. It was your own email system, but your AI let them in through a name field. So, your AI integrated resend for transactional emails and drops user input into the template. No sanitization. So, an attacker types HTML into a form field and resend delivers it from your verified domain. Well, the attacker did not comp compromise your email. Your template just invited them right in. So, let's get this locked down. Step one, a name field should contain a name, not a login button that links to an attacker's fishing page. The fishing email that results is indistinguishable from your legitimate ones because your infrastructure sent it to them. It's your domain. It's your sender reputation. It's your SPF record all confirming that it was real. So, one form field that accepts markup turns your entire email system into a fishing platform for attackers. So, direct your AI to sanitize every user input before it enters any template at all. Strip the HTML, escape special characters. That's a win. Step two, your template engine allows raw HTML insertion. User content should never use that path. Data gets displayed, markup gets executed. So, a password reset email that renders user input as HTML is an email and a attacker can turn into anything they want. So, you need to direct your AI to render user content as plain text, never as raw HTML. That's a win. And step three, send an email with angle brackets, link tags, and script tags in every input field. If any of them render as a clickable link instead of a plain text, your template is fully injectable. This test will take you 30 seconds. And the alternative is finding out when a customer clicks a fishing link that contain a domain that you sent them. So, direct your AI to test every single template. Your domain reputation is your business reputation, and one injectable template burns both to the ground. That's not a win. Get it fixed.


</div>
