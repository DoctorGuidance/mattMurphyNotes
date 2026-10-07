# درس 069: درس 069: Your login endpoint received 14,000 requests last night.

> **عنوان انگلیسی:** Your login endpoint received 14,000 requests last night.  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcRgRM2jjuv/)  

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
// Standard Hardening Snippet for Episode 069
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 069 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your login endpoint received 14,000 requests last night and none of them were your users. Credential stuffing bots hitting your login 200 requests per minute. Scrapers on your pricing page every 3 seconds and automated scanners probing every route for potential vulnerabilities. All of it sailing right through Cloudflare, hitting your origin, consuming your compute, and spiking your bill. You have a security layer in front of your application and it's doing nothing because your AI never configured it correctly. Happens to the best of us. Step one, rate limiting rules on authentication endpoints. Your login, registration, and password reset endpoints should never accept more than a defined number of requests per IP per minute. Not at your application level, at the edge before the request ever reaches your server. So, direct your AI to configure Cloudflare rate limiting rules that block or challenge any IP exceeding thresholds on authentication routes. That is definitely a win. Step two, bot management rules on high-v value pages. Your pricing page, your checkout flow, your API documentation. Bots hit these pages thousands of times every day. Cloudflare can identify automated traffic by behavior fingerprint and challenge or block it before it touches your origin. So, direct your AI to configure bot management rules. that protect high-V value routes from automated scraping and reconnaissance. And number three, custom WFT rules, known attack patterns, SQL injection attempts and query strings, XSS payloads and form fields, path traversal and URLs. Cloudflare's WFT can catch these at the edge and drop the request before your application ever sees it. So direct your AI to deploy custom WFT rules that block the OASP top 10 attack patterns at the Cloudflare edge. You're paying for a wall. Configure it as a wall.


</div>
