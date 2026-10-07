# درس 243: درس 243: Static credentials are permanent doors for attackers

> **عنوان انگلیسی:** Static credentials are permanent doors for attackers  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZXhEL2RVRu/)  

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
// Standard Hardening Snippet for Episode 243
// Domain: Authentication & Identity
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 243 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your database credentials are completely static. Same username and password for the last 6 months. If they leak, every query in your system is compromised until you change them manually. Here are three things you can do right now to fix it. Step one, deploy a secrets engine that generates credentials on demand. Hashy Corpse Vault or Infysical or your cloud provider's native manager. Whatever it is, the difference from basic secrets management Dynamic secrets are created per session and auto expire. That's a win. Your app requests those credentials. Vault generates a unique set. They live for 1 hour, then they die. No permanent credentials to steal. Like I said, that's a win. Step two, configure per service credential scoping. Your API server gets readr access to the tables it needs. Your analytics service gets read only rights. And your background worker gets access to job Q and nothing else. Least privilege enforced by the secrets engine, not by trust. That's a win. Step three, enable audit logging on every secret access. Who requested credentials? When from which IP address for which service, right? When something goes wrong, you have the full trail to audit, not a guess, a complete log. Dynamic secrets, scoped assets, audit trail, so your blast radius shrinks from infinite to just that one session. So, Oh, how are you managing database credentials right now? Be honest in the comments.


</div>
