# درس 191: درس 191: You deleted the API key from the file

> **عنوان انگلیسی:** You deleted the API key from the file  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DaJQlPhFeqw/)  

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
// Standard Hardening Snippet for Episode 191
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 191 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

So your API key is sitting in your repository again. You committed it 3 months ago, rotated it maybe last week. However, the old key is still in your git history, and git history never goes away. Here are the three things you can check right now to see if you're safe. Step one, scan your history. Every commit you have ever made is totally searchable. A secret you committed and deleted in the next commit still exists in the diff. Tools scan your entire git history for patterns that look like keys, tokens, and credentials all day long. Run one today. The results will absolutely surprise you. Step two, environment variables are not secrets management. AMV file works locally. In production, it becomes a total liability. Environment variables live in plain text. Anyone with server access can read them. So, a secrets manager encrypts at rest, controls access by role, and logs every read. The difference between a variable and a managed secret is an audit trail. That's the win. Step three, rotate on schedule. Not after a breach, but before one. If your key is not changed in 6 months, you're betting that nobody found it. Rotation is not paranoia, it's policy. And trust me, somebody found it. Your secrets are only secret if you treat them that way. So, you got to get in front of them.


</div>
