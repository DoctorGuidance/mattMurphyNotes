# درس 017: درس 017: An attacker just used your login page to send your users to

> **عنوان انگلیسی:** An attacker just used your login page to send your users to  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdewD5fFOjE/)  

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
// Standard Hardening Snippet for Episode 017
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 017 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI built a return to feature. After login, the user redirects to the page they came from. The destination comes from a URL parameter your server never validates. A redirect after login is most trusted moment in your application. So an attacker knows how to exploit that trust completely. Here's the three steps you're going to take to fix it. Step one, your login URL includes a parameter. liked return to or redirect. An attacker crafts a link pointing to your real login page with the redirect set to their fishing site. That's not a win. The user sees your real form, types their real password, and after authentication, your server sends them to the attacker's page. No reason to suspect anything because they just logged in for real from their perspective. So, Directory AI to validate every redirect URL. against an allow list of your domains. Step two, an attacker who cannot use an external URL tries a relative path that resolves unexpectedly, like a double slash at the start, a backslash, an encoded character. URL parsing treats these differently than your validation does. The redirect passes the check and sends the user off of your site. So, direct your AI to parse the redirect URL and reject anything that resolves outside your application, including protocol relative and encoded variance. Right, that's a win. And step three, your logout flow has the same vulnerability. A redirect after logout sends the user to a fishing login page that looks just like yours. So, the user thinks they were logged out and logs back in on the attacker's page. It's time to direct your AI to audit every every redirect in your authentication flow, not just login. That is definitely a win because your login page is your users's front door, right? And an attacker just put a fake hallway behind it and they're trying to get all your users. Don't let it happen. Get it locked up.


</div>
