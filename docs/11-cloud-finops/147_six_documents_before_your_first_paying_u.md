# درس 147: درس 147: Six documents before your first paying user

> **عنوان انگلیسی:** Six documents before your first paying user  
> **حوزه معماری:** معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه (Cloud Infrastructure & FinOps)  
> **لایه پروداکشن:** لایه 6 (Cloud & Compute)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/Davh5IQjRBY/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Cloud Infrastructure & FinOps و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Cloud Infrastructure & FinOps در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 147
// Domain: Cloud Infrastructure & FinOps
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 147 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your product's ready, your first customers are ready to pay, but before you accept a single payment, you want these six documents in place in your business or you're going to end up exposed. Doc number one, terms of service. You know that one that no one reads. Well, that's the one that defines what your users can and cannot do, what you are liable and not liable for, and what happens when things go wrong. Your AI can draft it, but you need to direct it with your specific use. case for your product, all of your data practices and your liability boundaries. A template you download from the internet protects nobody at all. Doc number two, privacy policy. This tells users what data you collect and how you use it and how they request deletion from it. If your policy says one thing and your app does another, you have a compliance violation. Not a technicality, but a sizable fine if you don't get it right. Doc number three, data processing agreement, a DPA. If you process data on behalf of another business, a DPA defines who is responsible for what. GDPR absolutely requires it. Enterprise customers will ask for it every single time. Doc number four is a refund policy. What happens when a customer wants their money back? Payment processors, they require it. Customer trust absolutely depends on it. Doc number five, this one's big. Master service agreement. If you were selling your system to a company that's going to use it. The MSA defines how you support it. SLAs's, uptime guarantees, response times, and what happens when something breaks. The MSA governs the relationship between your product and their business. It's a big deal. And doc six, it's optional, but it's important. Cyber liability insurance. When you handle someone else's data and something goes wrong, you will end up personally liable, not your LLC. I've corrected it in plenty of comments. Most Policies cost $200 to $600 a year and $200 to protect what could be a $50,000 problem. That's a big deal. Not everyone needs it on day one. I get it. But the moment you handle customer data at scale, the coverage protects what the documents alone cannot. So those six documents, none of them are code. All of them protect the business and the product underneath the code. Your AI can draft every single one of them for you, but only if you know what to ask for. Now you do.


</div>
