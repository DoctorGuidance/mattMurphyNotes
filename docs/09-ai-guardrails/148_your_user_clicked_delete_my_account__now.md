# درس 148: درس 148: Your user clicked delete my account. Now what

> **عنوان انگلیسی:** Your user clicked delete my account. Now what  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DavJP42gfEJ/)  

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
// Standard Hardening Snippet for Episode 148
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 148 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

You have a user that just clicked delete my account. Now what? Your AI built a login system, but it did not build a deletion system. Here are the three things you're going to direct your AI to do right now to fix it. Step one, the cascade map. Direct your AI to map every table relationship that touches the user. Orders, messages, uploads, payment history, session data, and support tickets. When the user is deleted, what happens to each of those records. If you do not know, your AI does not know either. Map it before the first deletion request arrives in your system. That's a win. Step two, soft delete with a retention window. Direct your AI to deactivate the user immediately, but retain the data for 30 more days. The user is gone from the application. The data lives just long enough for a compliance review. After 30 days, hard delete automatically. No manual cleanup. And step three, the GDPR response. A user in Europe requests a deletion. You have 72 hours. So direct your AI to generate a data report of everything you hold on that user and then confirm complete removal within the compliance window of 72 hours. If your AI cannot produce that report on demand, you have a legal exposure you do not know about. Delete is not a button. It's a business process. Build it. Like you have it from day one.


</div>
