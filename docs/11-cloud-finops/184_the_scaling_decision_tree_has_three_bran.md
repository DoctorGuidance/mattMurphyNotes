# درس 184: درس 184: The scaling decision tree has three branches

> **عنوان انگلیسی:** The scaling decision tree has three branches  
> **حوزه معماری:** معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه (Cloud Infrastructure & FinOps)  
> **لایه پروداکشن:** لایه 6 (Cloud & Compute)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DaQasDJDxqZ/)  

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
// Standard Hardening Snippet for Episode 184
// Domain: Cloud Infrastructure & FinOps
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 184 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your vibe coded app just hit that wall. Users are complaining. Pages are loading slow. The database is sweating like it's running a marathon. The instinct, throw more money and resources at it. Bigger servers, more replicas, higher tier plans, right? Well, here's what I actually tell clients before they spend a dollar solving this problem. The scaling decision tree has three branches, and you must check them in this order. Branch one, is it a connection problem or capacity problem, right? Most of the time it's a connection problem 90% of the time. Your database, it can handle all the queries you can throw at it, but it cannot handle 200 connections that are fighting for 50 slots. A connection pooler fixes this for $0. PG balancer supervisor built-in pooling on most managed platforms. So, that's a win. If you add a read replica before you add a pooler, you just doubled your infrastructure cost to solve a problem that costs nothing to fix. That's not the win. So, you got to check your connections first. Next is branch two. Is it a query problem or a volume problem? PG_stat_ statements tells you which queries consume the most time. Your slowest query might not be the problem. Your most frequent query running 10,000 times a day at 40 milliseconds each, well, that's 400 seconds of unnecessary database time. One index, one cache, one Query optimization. The database, it's not slow, but that query super expensive. Branch three, is it a read problem or a write problem? 80% of database operations are reads. A read replica handles reads. It does not though help with contention. So if your rights are the bottleneck, replicas do nothing but make it worse. You need Q processing, background jobs, right batching. So before you Scale horizontally. Know which access you're scaling on. The decision tree matters because every wrong branch costs money and solves nothing if you use it wrong. Connection pooling, query optimization, and read write separation. Go through it in that order. That's where you're going to find the win. And clients who follow this order spend thousands. The ones who skip the replicas spend tens of thousands. Same result, different bill. Help your clients find And the answer


</div>
