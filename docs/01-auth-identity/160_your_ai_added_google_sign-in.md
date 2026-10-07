# درس 160: درس 160: Your AI added Google Sign-In

> **عنوان انگلیسی:** Your AI added Google Sign-In  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DallI-2D9Q7/)  

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
// Standard Hardening Snippet for Episode 160
// Domain: Authentication & Identity
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 160 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your users get logged out every hour right in the middle of their important work and your app keeps dumping them to a login screen. So your AI did add Google Signin, but it did not handle the token life cycle. Here are the three things you're going to direct your AI to do right now to fix it. Step one, silent token refresh. Your access token expires every 60 minutes. Direct your AI to refresh it in the background before it expires. This way, the user never sees a login screen and the refresh happens invisibly. If your AI is only handling the initial login and ignores the refresh, every session has a 1 hour ceiling and that's not a win for your users. Step two, graceful refresh failure. The refresh token, it expires. The session, it's totally over. And so you need to direct your AI to redirect the login to the user's state preserved. Not a blank page, not a lost draft. not a cleared cart. Return them right where they were after reauthentication. That's a win. And step three, token rotations. Direct your AI to rotate refresh tokens on every use. A stolen refresh token that works forever is a permanent backdoor. A rotated token, it works once. Reuse flags a compromise. Login is always easy. So, keeping users safely logged in is the AIdirected orchestration that nobody else is teaching but the fact


</div>
