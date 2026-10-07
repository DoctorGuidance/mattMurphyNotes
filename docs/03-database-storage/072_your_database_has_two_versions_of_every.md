# درس 072: درس 072: Your database has two versions of every record right now

> **عنوان انگلیسی:** Your database has two versions of every record right now  
> **حوزه معماری:** پایگاه‌داده، روابط، ایندکس و پایداری داده (Database & Storage Engineering)  
> **لایه پروداکشن:** لایه 3 (Database & Storage)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcOX9AdERD2/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث پایگاه‌داده، روابط، ایندکس و پایداری داده است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Database & Storage Engineering و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Database & Storage Engineering در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 072
// Domain: Database & Storage Engineering
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 072 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your database has two versions of every record right now. And your app is showing users the wrong one. So your right went to primary, but your read came back from a replica that's 3 seconds behind it. Two databases, two versions of the truth, and your user is staring at the wrong one. They submitted a support ticket saying your app is broken. It is not broken. It is lying to them. Here's what happens when your app scales past one database and Your AI never accounted for replication lag. Step one, read after write consistency routing. When a user writes data, the next read from that same user must come from a primary, not a replica. A short consistency window routes that user's reads to the primary for a defined period after any write. Everyone else continues reading from replicas. So, direct your AI to implement sessionaware read routing that pins the user to the primary for a configurable window after any write. That's a win. Step two, replica lag monitoring with automatic failover thresholds. So, replication lag spikes under load, during large transactions, and during schema changes. If your replica falls 10 seconds behind, every read from it returns data your users changed 10 seconds ago. So, direct your AI to instrument replica lag monitoring and define a threshold. that reads automatically reroute to all primary until the replica catches up. And step three, conflict resolution on concurrent rights across regions. Two users editing the same record in two regions. Both rights succeed on their local primary. Replication carries both changes. One overwrites the other with no warning at all. So direct your AI to implement last right wins with timestamp resolution or operational transforms that merge concurrent changes instead of silently dropping one. Your database scaled. Your consistency, well, it didn't. So, direct your AI to fix the gap before your users find it for you. And that's the win.


</div>
