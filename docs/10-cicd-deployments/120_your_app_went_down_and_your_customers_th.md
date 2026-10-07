# درس 120: درس 120: Your app went down and your customers think you stole their

> **عنوان انگلیسی:** Your app went down and your customers think you stole their  
> **حوزه معماری:** تست، محیط‌های کاری، CI/CD و خط لوله استقرار (Testing, Staging & CI/CD)  
> **لایه پروداکشن:** لایه 7 (CI/CD & Pipelines)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DbL-9-3kT8H/)  

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
// Standard Hardening Snippet for Episode 120
// Domain: Testing, Staging & CI/CD
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 120 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your app went down when you were asleep and now your customers think you stole their money. 6 hours of downtime, no status page, no status updates, no maintenance announcement, no communication to the users of any kind. And this is all because your AI never built you a status system. Here are three things you direct your AI to build before your next outage becomes a trust crisis. Step one, a public status page on a separate domain altogether, not hosted on your main infrastructure. Because when your app goes down, your status page goes down with it. So your AI can deploy a standalone status page in 20 minutes on a completely separate host. The difference between the site is down and I have no idea why. And we know and we are trying to fix it is the difference between a chargeback and patience. Right? And that's a win if you get it right. Step two, a scheduled maintenance announcement system. Every application needs downtime. The Builders who announce maintenance windows in advance, they look professional. The builders who take their app down at 2 p.m. on a Tuesday afternoon with no warning look pretty amateur. So, your AI can build an automated notification system that emails active users before scheduled downtime and posts it to your status page so your customers do not mind downtime. They don't mind it at all. They mind surprises and time that they had set aside that you didn't notify them. And step three, an incident communication workflow. When an outage hits, you need a status page update with defined intervals, email notifications to active subscribers, and an estimated restoration time, even if it's just a guess. Silence during an outage is what turns technical problems into a reputation and revenue problem. Your AI can build the entire workflow with templates preloaded and triggers fully automated, but it'll never build it on its own because it does not know that silence is the fastest way to lose every customer you earned. So your AI built a product and never built the system. It tells your customers the product is still alive even when it isn't. So direct your AI to build it before your next outage cost you more than just a little bit of downtime.


</div>
