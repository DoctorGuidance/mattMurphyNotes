# درس 009: درس 009: An attacker intercepted your magic link and landed inside

> **عنوان انگلیسی:** An attacker intercepted your magic link and landed inside  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdrEewmD01_/)  

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
// Standard Hardening Snippet for Episode 009
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 009 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI implemented magic link authentication, but an attacker just intercepted your magic link and landed inside your users's dashboard. So, your passwordless login just became a passwordless breakin and your AI built the flow without validating where the link resolves. So, the user enters their email, your server, generates a signed token, embeds it in a URL, and emails it out. The user clicks and authenticates the URL includes a redirect parameter your AI never locked down. So let's get it locked down. Step one, your magic link URL includes a redirect parameter that tells the application where to send the user after authentication. An attacker crafts a link with the redirect set to their server. The user clicks that magic link from their real email, authenticates against your real application, and your server sends their authentic ated session to the attacker's domain. So now the attacker has the session token. So you need to direct your AI to validate the redirect parameter against all allow list of your own domains before issuing a redirect at all. That is a win. Step two, magic link tokens that do not expire remain valid indefinitely in users email. So an attacker who gains access to a mailbox 6 months later finds every magic link still fully active. Each one is a valid authentication bypass. So, direct your AI to set Magic Link tokens to expire within 10 minutes and invalidate them immediately after first use. And step three, an attacker who discovers the Magic Link endpoint can request thousands of links per minute for any email address. So, each request sends a real email from your domain. This floods the targets inbox and damages your sender reputation. That's important. So direct your AI to rate limit magic link request to three per email address per hour and throttle total request per IP. Your magic link removes that password, but it should not remove all of your security. Get it fixed.


</div>
