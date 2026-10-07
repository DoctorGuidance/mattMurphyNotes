# درس 024: درس 024: An attacker just accessed every protected page in your app

> **عنوان انگلیسی:** An attacker just accessed every protected page in your app  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdWeKvGDz5k/)  

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
// Standard Hardening Snippet for Episode 024
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 024 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI set up next.js middleware to check authentication, right? But an attacker just accessed every protected page in your app without logging in at all because the attacker's request never hit next.js. So your AI added authentication in middleware, one file, every route protected, right? But middleware does not run on every single request type. So some pass can bypass it entirely. One off layer with gaps is no off layer. at all. So, let's get it locked down. Number one, next.js middleware matches routes using your matcher config. If API routes are excluded from the matcher, every API endpoint is unprotected. So, your AI built to check for your page navigation, but an attacker calls the API endpoint directly. The middleware never fires and so the response comes back with all the data. So, directory AI to verify the middleware matcher includes every route that requires authentication. That's a win. Number two, a trailing slash a double encoded character or a path prefix changes how the matcher evaluates in a request. Right? So when your middleware does not recognize the variation it's seeing, the request passes right on through. So the route resolves and returns protected data on that request. So you need to direct your AI to test every protected route with path variations and confirm Confirm the middleware intercepts each one. That's a win. And step three, middleware runs at the edge before your server. Your AI may check that a cookie exists without validating it against your session store. So where an AI expired or forged cookie passes through, the real validation must happen server side. So direct your AI to add server side authorization checks on every API route and server component independent of the middleware. middleware. It's a convenience layer. And if it's your only authorization check, it's your weakest one. So, let's get it fixed.


</div>
