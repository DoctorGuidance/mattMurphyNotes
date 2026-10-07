# درس 197: درس 197: Not Everything Should Be Cached

> **عنوان انگلیسی:** Not Everything Should Be Cached  
> **حوزه معماری:** کشینگ، توزیع لبه و پرفورمنس سیستمی (Caching & Edge Performance)  
> **لایه پروداکشن:** لایه 10 (Caching & CDN)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DaDuf2DFSP-/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث کشینگ، توزیع لبه و پرفورمنس سیستمی است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Caching & Edge Performance و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Caching & Edge Performance در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 197
// Domain: Caching & Edge Performance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 197 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

There are two hard problems in computer science. Cash invalidation and naming things. The naming part, that's a joke. The cash part, not a joke. Here are three things you can do about it right now. Step one, stale data. Your user updates their profile. The cache still holds the old version. For 30 seconds or 30 minutes, every request returns yesterday's data. The user sees the old name, the old photo, the old permissions. C. ing is not a performance feature. It's a consistency decision. Know what you are willing to show stale and for how long. That's the win. Step two, invalidation strategy. Timebased expiration is simple. Set a lifetime. When it expires, fetch fresh every time. Event-based invalidation is precise. Data changes. Cache clears immediately. Most applications need both. Static content gets timebased. User data gets event-based. The mistake is treating all cache data the exact same way. Step three, cash stampede. Your cash expires. 1,000 requests hit the database at the same instant. That one request should refresh the cache, but the other 999, they're going to wait. Without protection, your database sees a spike every time a popular key expires. Caching solves one problem, but it creates three. Solve all four.


</div>
