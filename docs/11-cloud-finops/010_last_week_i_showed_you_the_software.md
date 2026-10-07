# درس 010: درس 010: Last week I showed you the software

> **عنوان انگلیسی:** Last week I showed you the software  
> **حوزه معماری:** معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه (Cloud Infrastructure & FinOps)  
> **لایه پروداکشن:** لایه 6 (Cloud & Compute)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdpDWXlD-Nn/)  

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
// Standard Hardening Snippet for Episode 010
// Domain: Cloud Infrastructure & FinOps
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 010 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Last week, I showed you my default VPS stack software, nine components, most of them totally free. This week, I'm showing you what it runs on, as well as a few builder stacks from my comments. For example, one commenter is running a Mac Studio with two 3090s as a secondary node, running Quen locally, handling enterprise workloads without a single cloud API call. No subscription, no usage fees, no data data leaving his building at All that's totally a win. Another member is running 4090s. Another's pricing B300's right now. So VPS is clearly here to stay and you guys want to talk about it. Here's what the local inference setup actually looks like. A Mac Studio with an M series chip handles small to mid-range models natively. Apple Silicon runs inference efficiently because memory is unified. So a model that fits in 64 128 gigs of unified memory runs without the complexity of GPU clusters. That's a tidy setup for sure. For heavier workloads, add Nvidia, right? A 3090 with 24 GB of VRAM handles 13 billion parameter models. Two of them, 30 billion. A 4090 runs those same models, but faster. And the used market for 3090s has totally collapsed. Enterprisegrade inference hardware for the price of a business class flight. Go check it out. It's totally a win. The VPS I shared from last last week still works for teams that do not want to rack hardware, but many of the people in my comments are totally past that. They want the model on their desk, in their office, on their network, and nowhere else. I get it. And the cost comparison has totally flipped. A year of API calls to a Frontier provider costs more than the hardware that replaces it permanently. And the hardware does not raise its price every quarter. So, your prompts, those are your IP. Last week, I told you to keep them off of someone else's server. This week, I'm telling you what to run them on. So, get out there and build something.


</div>
