# درس 203: درس 203: Your cloud bill doubled

> **عنوان انگلیسی:** Your cloud bill doubled  
> **حوزه معماری:** معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه (Cloud Infrastructure & FinOps)  
> **لایه پروداکشن:** لایه 6 (Cloud & Compute)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZ-KjLZEcwV/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Cloud Infrastructure & FinOps و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Cloud Infrastructure & FinOps در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 203
// Domain: Cloud Infrastructure & FinOps
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 203 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your cloud bill doubled last month. You're not exactly sure which service is causing it. And you're not alone. So, here are the three things you're going to check right now to figure it out. Step one, check your idle resources. That staging environment you spun up 3 months ago, it's still running. Or the database replica you created for a load test that's still accepting connections. Uh-oh. What about the storage bucket from a feature you never shipped still acrewing charges daily? I'm telling you, cloud providers, they do not remind you, they bill you forever. So, audit what is running, kill what is not. That's the win. Step two, rightize it. Your production server runs on an instance built for traffic you don't have yet. Overprovisioning, yeah, it feels safe, but it's also really expensive. Most applications run at about 15% utilization on hardware sized for the full 100%. So, make sure you match the resources to the actual load, not the load you hope to have. Step three, data going into the cloud is free, but data coming out is not egress fees. So every API response, every image served, every web hook payload. If your architecture moves data between regions or between providers, the bill is growing quietly. So you have to know where your data travels, folks. Your cloud bill is not a mystery. It is a mirror of your architecture decisions.


</div>
