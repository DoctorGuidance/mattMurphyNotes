# درس 048: درس 048: You added Sign in with Google. Your AI left the redirect

> **عنوان انگلیسی:** You added Sign in with Google. Your AI left the redirect  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcwZzLckxZ4/)  

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
// Standard Hardening Snippet for Episode 048
// Domain: Authentication & Identity
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 048 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

So, your AI, it added signin with Google to your product, but your AI also left the redirect wide open. So, someone just sent your users a login link that delivers their token to a server you've never even seen. So, your AI, it built ooth flow, right? Log in with Google, get a token, redirect back to your app. But the redirect, that URL is not locked to your domain. And an attacker crafted a login link that looks exactly like you. So, the token gets redirected to their server instead of yours and your authentication worked perfectly, but it just worked for the wrong person. Let's get that tightened up. Step one, lock your redirect URL to exact registered URLs. No wild cards, no pattern matching, no open redirects. Every OOTH provider gives you a whitelist. If you redirect can point anywhere, your login can be hijacked from anywhere. So, direct your AI to audit every OOTH integration and restrict redirect URLs to exact hard-coded callback URLs registered with each provider. That's a win. Step two, enforce a state parameter on every OOTH request. The state parameter ties the login request to the user session. That's so the callback can verify the flow was initiated by your app and not by an attacker. Without it, anyone can forge an OOTH call call back. So direct your AI to generate a unique cryptographically random state value on every login request and reject any call back where that state does not match. That's also a win. And step three, scope your token request to the minimum permissions your app actually needs. So if you requested full profile access and your app only needs an email address, every stolen token gives the attacker more than it should. So direct your AI to audit every OOTH scope and reduce each to the minimum required for the feature it supports. Your users, they trust that login button, so make sure it only works for them.


</div>
