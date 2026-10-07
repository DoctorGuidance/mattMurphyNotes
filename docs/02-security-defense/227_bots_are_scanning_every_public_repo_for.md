# درس 227: درس 227: Bots are scanning every public repo for API keys right now

> **عنوان انگلیسی:** Bots are scanning every public repo for API keys right now  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZnYDewRV_h/)  

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
// Standard Hardening Snippet for Episode 227
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 227 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Right now, like right now, there are bots scanning every single public GitHub repository for API keys, every commit, every pull request, every accidentally pushv file. Here are the three things you're going to do right now to prevent it. Step one, check your git history. Not your current code, your history. You might have removed the key from your file, but git remembers everything. That API key you accidentally committed 6 months ago and then deleted in the next commit. Guess what? It's still in the repository. Anyone who clones your repo can find it. If that repo was ever public, even for 5 minutes, assume that key was harvested by bots. Rotate it today. That's the win. Step two, use Git Secret scanning. GitHub has push protection. It scans every commit before it is pushed and blocks every known secret pattern. GitG Guardian does the same thing. Get leaks runs locally. Truffle hog digs through your entire history. These are the tools that catch the mistakes before it becomes a breach. And don't forget, turn on push protection. It takes 2 minutes. It prevents the kind of incident that takes two weeks to recover from. And that's a win. Step three, scope your keys. Most API providers let you restrict what a key can do. So, only specific endpoints, specific IP addresses, specific domains. If your Stripe key can do everything and it leaks, everything's at risk. If your Stripe key can only create checkout sessions from one domain, that blast radius nice and small. So scoping a key is free. Recovering from an unscoped key is not free. So the lesson is assume every key will leak and plan accordingly every day.


</div>
