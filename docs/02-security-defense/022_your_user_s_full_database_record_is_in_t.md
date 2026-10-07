# درس 022: درس 022: Your user's full database record is in their browser right

> **عنوان انگلیسی:** Your user's full database record is in their browser right  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdZDAYDkr3A/)  

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
// Standard Hardening Snippet for Episode 022
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 022 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI put your user's full database record in the browser right now. Your React server component displays three fields. The payload contains all 20. Your AI fetched an entire row and let next.js serialize it. So your AI queried the database inside a server component and pass the result as props. Well, the component renders a name, an email, and a profile photo. So the browser received the password hash, the internal RO flag and the billing token alongside it. So the server components render on the server, right? But the data they use still travels to the browser. So let's get it fixed. Number one, React server components serialize every prop into a wire format the browser parses to build the page. So your AI passed the full database row because the query was simpler. The component only displays three fields, but the payload will contain all of them that you send. So, an attacker opens the network tab and reads what your UI chose not to show. So, direct your AI to select only the fields the component renders, never a full row. That's a win. Number two, nested components inherit the same props. So, your AI passes the full user object to a parent and three child components each take what they need. So the full object serializes once every field is in the payload. But a leak at the parent level exposes data to every child. So direct your AI to create a data transfer object at each component boundary with only the required fields there. And number three, the RSC payload. It's not HTML. It is a structured format any attacker can parse and extract at scale. 20 users loading the page means 20 full records are being exposed. So direct your AI to audit every server component that receives database results and verify no sensitive field reaches the wire format. Your UI is a window, folks. The payload, it's the wall behind it. If sensitive data is in the wall, someone is definitely going to look. So you got to get it locked down.


</div>
