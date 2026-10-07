# درس 135: درس 135: Every push goes straight to production

> **عنوان انگلیسی:** Every push goes straight to production  
> **حوزه معماری:** تست، محیط‌های کاری، CI/CD و خط لوله استقرار (Testing, Staging & CI/CD)  
> **لایه پروداکشن:** لایه 7 (CI/CD & Pipelines)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/Da51JT3DSQi/)  

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
// Standard Hardening Snippet for Episode 135
// Domain: Testing, Staging & CI/CD
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 135 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

So every push goes directly to production. One bad merge and your customers see the bug before you do. Your AI builds on main and ships it live. Here are the three things you direct your AI to set up right now to fix it. Step one, build a staging environment. So direct your AI to create an environment that mirrors your production environment. Same database schema, same services, same environmental variables. Versel preview deployments give you this almost for free. But if it doesn't, you got to build it. Every pull request gets its own preview. Test there, not in production. That's the win. Step two, nothing ships without passing staging. Direct your AI to build a CI pipeline that runs tests against staging. Tests pass, the pipeline promotes to production automatically. Tests fail, production never sees it. Your customers never see a broken feature, your team catches it for first. That's also a win. And step three, one-click roll back. Something got through. A bug made it past staging. These things happen to the best of us. Direct your AI to implement roll back to the last known good deploy. Not SSH into the server. Just one button previous version immediately. Every deployment is either a confident push or a quick roll back. It's time to stop shipping to production on a prayer. Start shipping to staging with a full plan. That's the win.


</div>
