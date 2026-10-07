# درس 128: درس 128: Your user clicked delete my account

> **عنوان انگلیسی:** Your user clicked delete my account  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DbDv862jzKb/)  

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
// Standard Hardening Snippet for Episode 128
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 128 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your user clicked delete my account. So you deleted all their data. Well, you just broke a federal law. Certain industries require you to retain customer records for up to 7 years after your relationship ends. Financial services, health care, tax related transactions, and even some legal agreements. So your user might want their data gone, but the federal government says you have to keep it. Here are the three things you're going to direct your AI to build right now to handle this for you going forward. Step one, a data retention policy engine. This isn't a toggle that says active or deleted. It's a system that knows the difference between the data a user controls and the data the law requires you to keep. Those are two completely different categories and your AI will lump them together unless you tell it not to. So your customer-f facing data gets anonymized and your compliance data stays locked in a separate retention layer with an expiration date attached to it. That's a win. All right. Step two, a retention schedule mapped to your actual obligations. 7 years is not universal to all companies and all projects, right? It depends on your industry, your state, and the type of record you're collecting. Payment records, for example, have a different timeline than user communications. So, your AI can research the requirements for your specific business, but it'll never do it unprompted. because it does not know what industry you're in or what laws apply to you wherever you're at. And step three, an audit trail that proves you followed the policy. When a regulator asks, and in certain industries they absolutely will, you need to show exactly what was retained, what was anonymized, and when the clock started, and also when it expires. Your AI can build that logging system in an afternoon. Without it, your policy retention is a promise with no proof. So last week I told you to soft delete. This week I'm telling you that sometimes you cannot delete at all. The rules depend on what you are building. You have to do the research. So direct your AI to find out before your your first user asks you to leave.


</div>
