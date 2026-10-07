# درس 297: درس 297: Your app works in the demo. It works when you show your

> **عنوان انگلیسی:** Your app works in the demo. It works when you show your  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DYZ1EeNgGIu/)  

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
// Standard Hardening Snippet for Episode 297
// Domain: Authentication & Identity
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 297 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Sure, that cool app you've been telling everybody about works on your computer. Works in a cool little demo. It works when you show your family and your friends on your laptop, right? But it's not actually a product. It's a demo pretending to be a product. So, let's turn it into a product. Here's how you make that change. Number one, give it to five people that you didn't build it for. Not your friends, not your co-founder, not even your mom. Five strangers who fit your target user. Just watch them use it. Don't explain anything to them. Don't help out. If they can't figure it out in 30 seconds, it's not ready for production. Trust me. A demo needs context. A product never does. Number two, break it on purpose a bunch. Enter a blank form. Type a,000 characters. Type 10,000 characters. Hit submit 47 times. Open it on a phone. Whatever you didn't think it would do, your users will do in the first hour anyway. So, if your app crashes when someone does something, totally unexpected. You shipped a prototype, not a product. Find the brakes before they do. Number three, add all the boring stuff. Error messages, loading states, empty states, password resets, terms of service pages. None of this is exciting. Not even a little bit. But all of it is required. The gap between a demo and a product is 100 boring things done, right? That's what separates builders from your friend with a little hobby on his phone, right? A demo impresses people. A product services people. You have to serve people with a product you can ship.


</div>
