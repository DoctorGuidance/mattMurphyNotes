# درس 281: درس 281: No privacy policy

> **عنوان انگلیسی:** No privacy policy  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DYrvI-fAPC2/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه AI Guardrails, LLM Security & Compliance و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به AI Guardrails, LLM Security & Compliance در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 281
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 281 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

So, you just shipped the vibecoded app that collects user data. No privacy policy, no terms of service, no CCPA compliance. Uh-oh. Congratulations. You're one complaint away from a lawsuit. But here's how you fix it. Step one, privacy policy generator. You can use termly privacypolicies.com. Both free, less than 10 minutes. Cover what data you collect, how you store it, how users can delete it. This isn't optional, folks. This is table stakes. You got to have it. Step two, terms of service, liability limitation, user conduct rules, dispute resolution. Use a template. There's a million of them. Customize it for your app. This is your legal shield. You need it. Without it, every user interaction is an unlimited liability exposure. You don't want that. Step three, CCPA and GDPR basics. If you're collecting any data from California or EU residents, which you probably are, you need an opt- out mechanis. ISM and a data deletion on request. Add a delete my data button to the app. It's not optional. It's not a nice to have. It's the law. And so with those three steps, one afternoon, you can go from one complaint away from a lawsuit to completely and totally legally covered. We've got you handled. Talk to you soon.


</div>
