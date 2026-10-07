# درس 118: درس 118: You picked your auth provider because it was free

> **عنوان انگلیسی:** You picked your auth provider because it was free  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DbOpQ2mDrD1/)  

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
// Standard Hardening Snippet for Episode 118
// Domain: Authentication & Identity
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 118 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Remember when you picked your off provider because it was free? Well, an enterprise deal just walked through the door and it's time for a reckoning. They're going to ask you these four questions. Do you support SAML? Do you support SSO into their identity provider? Can you show them your SOCK 2 at astation? And where is your security documentation to review? If you can't answer any of those questions, the deal will die before your demo begins. So, here are three things you're going to direct your AI to evaluate right now before your off choice kills your biggest deal. Step one, SAML and SSO support. Enterprise buyers do not create accounts on your platform ever. They authenticate through their own identity provider. If your O system does not support SAML or SSO, you're asking a company with 10,000 plus employees to manage separate credentials just for your app. Guess what? They aren't going to do it. They will buy from someone who supports their identity provider. Step two, sock 2 and compliance documentation from your provider. Your enterprise buyer security team will audit your entire vendor stack. If your off provider cannot produce compliance documentation specific to them, procurement will flag it as a risk and kill that deal. So, your AI picked the provider with the best developer docs, right? Well, your buyer security team is not asking you for developer docs. Step three, a migration path for when you outgrew your current provider. The free tier got you through launch. But if your off provider cannot scale to enterprise requirements, you probably need to know that and what a migration looks like before you have thousands of users locked into a system that you have to tear out. So, your AI can evaluate migration complexity right now, but doing it after you pay customers are on board is exponentially harder. So your AI picked the off provider that was easiest to set up and cheapest, right? But your buyer picked the competitor whose off provider was easiest to trust with the biggest investment. So direct your AI to evaluate that gap before your next enterprise conversation or don't sell any enterprise deals. It is what it is.


</div>
