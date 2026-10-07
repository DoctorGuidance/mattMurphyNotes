# درس 260: درس 260: Same API key for six months

> **عنوان انگلیسی:** Same API key for six months  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZGYLpLPDR-/)  

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
// Standard Hardening Snippet for Episode 260
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 260 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your API key is hardcoded in yourv file. It has been the same key for the last 6 months. And if it leaks and keys leak, every system that touches it is compromised until you rotate it manually, right? While your app is down. So here are the three things you do right now to fix it. Step one, move your secrets to a dedicated manager. Doppler, infysical or AWS secrets manager, not yourv file. Not your Versell dashboard, but a real secrets manager that gives you versioning, audit logs, and rotation APIs, your app. It fetches secrets at runtime instead of bundling them at deploy time. One command swaps a key across every environment simultaneously. Step two, implement dual key rotation. Generate a key while the old one still works. Deploy the new key to your application. Verify traffic flows on the new key, then revoke the old key. Two keys active simultaneously during the transition window. Zero downtime, zero failed request. That one's a win. Step three, automate the rotation schedule. Set a cron job or a scheduled function. Every 30 days, generate a new key, update your secrets manager, trigger redeployment, verify a health check, and revoke the old key. Clean automation. No human in the loop. No calendar reminder that you're going to forget. Manual rotation means you're only one rotation away from a breach. Automated rotation means a breach has 30-day blast radius instead of an infinite blast radius. So, when did the last time you changed your API keys? If you can't remember, it's probably time.


</div>
