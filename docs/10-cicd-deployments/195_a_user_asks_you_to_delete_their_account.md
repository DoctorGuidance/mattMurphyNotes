# درس 195: درس 195: A user asks you to delete their account

> **عنوان انگلیسی:** A user asks you to delete their account  
> **حوزه معماری:** تست، محیط‌های کاری، CI/CD و خط لوله استقرار (Testing, Staging & CI/CD)  
> **لایه پروداکشن:** لایه 7 (CI/CD & Pipelines)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DaGFCCNFf7m/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث تست، محیط‌های کاری، CI/CD و خط لوله استقرار است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Testing, Staging & CI/CD و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Testing, Staging & CI/CD در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 195
// Domain: Testing, Staging & CI/CD
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 195 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your privacy policy says you do not sell user data, but your analytics send it to four different thirdparty services that do. A regulator will know the difference. Here are the three things you reconcile right now to protect yourself. Step one, know exactly what you collect. Most applications collect more than the team ever realizes. IP addresses and logs, device fingerprints and analytics, location data from API calls. If you cannot list every piece of personal data in your application touches your privacy policy is fiction. Audit the data map where it goes. That's the win. Step two, consent is not a checkbox. A banner that says we use cookies and a button that says accept is not informed consent. Users should understand what they're agreeing to in plain language before the data moves anywhere. The regulation is not about the checkbox. It is about whether the user undersod the deal altogether. Step three, data retention. Your user deleted their account. Their data still lives in your database, in all of your backups, in your analytics, and in your logs. Deletion is not a button click. It is an architectural decision. Know where user data lives. Build the deletion pipeline before someone asks about it. Privacy is not a legal page. It is a system. Build it to keep yourself from getting sued.


</div>
