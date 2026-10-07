# درس 004: درس 004: An attacker moved from a compromised marketing tool to your

> **عنوان انگلیسی:** An attacker moved from a compromised marketing tool to your  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/Dd1Xt-zETRJ/)  

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
// Standard Hardening Snippet for Episode 004
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 004 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI deployed multiple services on the same network. The marketing dashboard, the admin API, and the production database all communicate freely. A vulnerability in one gives access to them all. So, a network where everything trusts everything is one breach away from losing everything. It's time to do something about it. Step one, your marketing tool has a known vulnerability. An attacker exploits it and gains a shell on that container. From there, they can reach the admin API because both services share a network with no segmentation. So the admin API connects to the production database with credentials that are stored in environment variables that an attacker can now read. So one compromised marketing widget escalated to full database access. So direct your AI to segment your network so each service can only reach the specific services that it needs. Marketing can't reach the database. The admin API cannot reach marketing and that that's a win. Step two, service to service communication inside your network happens without authentication. So any process on the network can call any internal endpoint. An attacker who compromises one service makes unauthenticated requests to every other service. So direct your AI to require mutual TLS or service tokens for every internal API call. No internal request should be trusted because of its network location alone. Never. And number three, your AI deployed every service with the same permissions. The marketing container has the same network access as the database container. If a service does not need to reach the internet, should not be able to. If it does not need to write of the database, its credentials should be read only. So direct your AI to apply the principle of least privilege to every container, service account, and network rule. One breach should give an attacker one service, not your entire operation. And that is a win.


</div>
