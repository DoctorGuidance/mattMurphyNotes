# درس 234: درس 234: Your frontend is a display layer, not a trust layer

> **عنوان انگلیسی:** Your frontend is a display layer, not a trust layer  
> **حوزه معماری:** معماری فرانت‌اند، طراحی واسط و بهداشت API (Frontend Architecture & API Hygiene)  
> **لایه پروداکشن:** لایه 1 (UI & Accessibility)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZhxVg2xu-u/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث معماری فرانت‌اند، طراحی واسط و بهداشت API است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Frontend Architecture & API Hygiene و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Frontend Architecture & API Hygiene در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 234
// Domain: Frontend Architecture & API Hygiene
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 234 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your front end, it's making decisions it should not be making. Pricing logic and JavaScript, roll checks and React components, API keys and environment variables that ship to the browser. Just one user opens any basic dev tool and they can see anything. Here are the three things you can do right now to fix it. Step one, move every business rule to the back end. Discount calculations, feature gating, permission checks. If it decides what a user concede, do or pay, it does not belong in the client side code. The front end asks, the back end answers. That is the boundary and that is a win. Step two, stop trusting client side validation. Validate inputs on the front end for user experience. Validate them again on the back end for security. A disabled button is not access control. Anyone with a fetch request can skip your UI entirely. That's not a win. Step three. Audit what your bundle actually exposes. Run your production build. Open it up. Search for API routes, keys, internal endpoints, and config objects. If you can find any of those, so can anyone else. Environment variables prefixed with next_public or vite shipped to the browser. Know which ones. Your front end is a display layer, not a trust layer. The moment you treat it like a security boundary, you've already lost the battle.


</div>
