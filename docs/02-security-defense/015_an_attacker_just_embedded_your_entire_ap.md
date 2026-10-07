# درس 015: درس 015: An attacker just embedded your entire app inside their

> **عنوان انگلیسی:** An attacker just embedded your entire app inside their  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdjWI7CDKC3/)  

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
// Standard Hardening Snippet for Episode 015
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 015 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your users are clicking buttons on your app while looking at an attacker's website. All because an attacker embedded an entire application inside of your website. Purchases, transfers, permission changes, all triggered by invisible clicks. So, your AI deployed your application without the one thing that prevents framing. So, any website can load your app inside of an invisible iframe and overlay their own buttons on top of yours. So users can't attack what they can't see, but an attacker makes them click what they cannot see. And that's the trick. We need to get it shut down. Step one, the attacker builds a page with a prize, a game, or a form. Behind it, your application loads in a transparent iframe. So the user clicks what they think is an attacker's button in a game, but they're actually clicking your app, a purchase confirmation, a permission grant, or a password change. They never see your application at all. Their browser executed the action because they are already logged into your system. So, direct your AI to add the X-Frame options header and set deny on every single response. That's a win. Step two, X-Frame options is the legacy protection content security policy frame. Ancestors is the modern replacement and gives you more control. Try it out. You can allow your own domain to frame itself while blocking everyone else. Both headers should be present because older browsers only support X-frame options. So direct your AI to set both headers. X-frame options deny and content security policy frame ancestors to self. That's the win. And three, your application may intentionally use Iframes for embedded widgets, payment forms or third party integrations. Those iframes, they need framing. Your main application doesn't. So your AI may have skipped the header because one feature requires framing and the blanket restriction would have broken it. So direct your AI to set frame ancestors on a per route basis. This allows framing only on the specific endpoints that require it. One header, two versions, every resp. response. That's all it takes for a win.


</div>
