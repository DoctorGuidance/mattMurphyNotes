# درس 169: درس 169: A $20 self-hosted runner runs unlimited minutes

> **عنوان انگلیسی:** A $20 self-hosted runner runs unlimited minutes  
> **حوزه معماری:** تست، محیط‌های کاری، CI/CD و خط لوله استقرار (Testing, Staging & CI/CD)  
> **لایه پروداکشن:** لایه 7 (CI/CD & Pipelines)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DabfLrfF-OA/)  

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
// Standard Hardening Snippet for Episode 169
// Domain: Testing, Staging & CI/CD
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 169 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your CI/CD pipeline just exceeded the free tier midsprint. Here are three things you're going to change right now to fix it. Step one, self-hosted runners. GitHub actions let you bring your own compute. It's a $20 per month server and it runs unlimited minutes. So that same pipeline that cost $1,200 in overrun charges now runs for $20 on your own machine. Yeah, you manage the server and you manage the runner software. and you manage the updates. But for teams that are burning through CI minutes, the math takes 5 seconds to figure out. It's a win. Step two, conditional pipelines. Not every commit needs every single test. A change to your readme does not need integration tests. A change to your marketing page does not need your back-end build. Pathbased triggers run only the stages that match the change files. Fewer stages, fewer minutes, same safety. Most Teams run the full suite on every push. That's not thorough, that's wasteful. Step three, monitor your usage before it surprises you. GitHub shows you your minute consumption and settings. Check it weekly. Set a team alert at 75% of your monthly allocation. When the alert fires, you have time to optimize and fix. When the pipeline stops, you have no time for anything. So, the CI that scales is not the one with the most features. It's the one that does not surprise you on day 19. in the middle of that sprint.


</div>
