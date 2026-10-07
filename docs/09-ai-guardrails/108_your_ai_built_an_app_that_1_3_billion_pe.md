# درس 108: درس 108: Your AI built an app that 1.3 billion people cannot use

> **عنوان انگلیسی:** Your AI built an app that 1.3 billion people cannot use  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DbaxXyTgbRR/)  

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
// Standard Hardening Snippet for Episode 108
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 108 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI built an entire app that 1.3 billion people cannot use and some of them are going to sue you for it. So 1.3 billion people worldwide live with a disability. They use screen readers and keyboard only navigation because of color blindness and motor impairments. Right? So your AI built your entire product assuming every user has a mouse, perfect vision, and two working hands. That's not just exclusion, folks. That is a legal liability and ADA lawsuits for inaccessible AI products and websites are just exploding and your AI has never heard of WCAG. So, here's what you direct your AI to fix before you end up in one of these lawsuits. Step one, keyboard navigation across your entire application. Right now, if a user cannot use a mouse, they cannot use your product. Every button, every form, every dropdown, and every mode needs to be reachable and operable with a keyboard by itself. So direct your AI to audit every interactive element and ensure full keyboard accessibility. If a user cannot tab through your entire app and complete every core action without touching a mouse at all, you are excluding millions of people and exposing yourself and your business legally. So step two, screen reader compatibility. Your AI built visual interfaces by default and they're beautiful. A screen reader though sees code not design. So if your images have no alt text and your buttons have no labels and your forms have no Arya attributes, a screen reader, those users, they hear nothing useful at all. So you need to direct your AI to audit every image, every button, every input, every navigation element for proper labeling. This is not optional polish and it's not something the AI will do without prompting. So, this is how 285 million visually impaired people experience your product every day. It's important. Step three, color contrast ratios that meet WC AAA standards. Your AI picked colors that look great. It never checked whether a colorblind user can read your text against your background. So, direct your AI to run a contrast audit on every text element and fix anything below 4.5 to1 ratio. ratio. Your AI built for users who look and like you and act like you, right? But your customers do not look like you and act like you. So direct your AI to build for everyone. Guess why? Because it's the law.


</div>
