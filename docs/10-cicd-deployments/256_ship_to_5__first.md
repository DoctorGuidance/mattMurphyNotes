# درس 256: درس 256: Ship to 5% first

> **عنوان انگلیسی:** Ship to 5% first  
> **حوزه معماری:** تست، محیط‌های کاری، CI/CD و خط لوله استقرار (Testing, Staging & CI/CD)  
> **لایه پروداکشن:** لایه 7 (CI/CD & Pipelines)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZKp4rPAasV/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث تست، محیط‌های کاری، CI/CD و خط لوله استقرار است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Testing, Staging & CI/CD و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Testing, Staging & CI/CD در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 256
// Domain: Testing, Staging & CI/CD
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 256 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

You push to main, the deploy runs. Every user gets a new code simultaneously. If it is broken, every user is broken simultaneously. That's not a deployment. That's a dice roll. Here are the three things you do right now to fix it. Step one, deploy to 5% of the traffic first. Verscell supports gradual rollouts natively. So does Cloudflare. Push your new version, route 5% of requests to it, make sure everything's working. working. The other 95% stay on the current stable version until you're ready to move them. Monitor error rates for 15 minutes. If errors spike, roll back instantly. Nobody even noticed. Step two, gate rollouts with feature flags. Launch Darkly, Flag Smmith, or even a simple JSON config in your database. New feature ships to production behind a flag. You enable it for internal users first, then beta users, then 10% Then everybody, if something breaks, kill the flag. The code stays deployed but the feature disappears. No roll back needed. Step three, automate the promotion. Your CI pipeline should watch error rates after Canary deployments. If error rate stays below your threshold for, let's say, 30 minutes, automatically promote to 100%. If it exceeds the threshold, automatically roll it back. No human watching a dashboard at midnight. That's old stuff. Just GitHub action plus your error monitoring API. 20 lines of code between you and a fully automated safe deployment. 5% canary feature flags and automated promotion. You never ship broken code to all your users again. So tell me, what's your scariest deploy story? Share it in the comments.


</div>
