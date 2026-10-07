# درس 057: درس 057: You moved to a VPS for more control

> **عنوان انگلیسی:** You moved to a VPS for more control  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/Dci-Qq_j9EL/)  

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
// Standard Hardening Snippet for Episode 057
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 057 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

You moved to a VPS for more control, and I can't blame you, but you accidentally left the front door wide open when you did it. Your managed platform is handling security invisibly. So, firewall rules, SSH hardening, automatic patching. You never thought about any of it because someone else's platform was doing it for you. Now, you own that server and every vulnerability that lives on it. So, here's what your AI never configured when you set up your VPS. No. Number one, SSH hardening. Right now, your server is accepting password authentication on a default port. Every bot on the internet is trying root passwords against port 22 around the clock. So, your server is being attacked right now. You don't even know it. So, disable password authentication entirely. Switch to keybased access only and change the default SSH port. Disable root login while you're there. These are four commands that take 5 minutes and stop 9 99% of automated attacks before they start. So direct your AI to harden your SSH configuration before you do anything else on that server. That's a win. Step two, a firewall that blocks everything you did not explicitly allow. Your managed platform had invisible firewall rules. Your VPS has none. So every port wide open, every service fully reachable, and your database port is exposed to the public internet. So direct your AI to configure UFW or IP tables to deny all inbound traffic by default and allow only specific ports your application needs like SSH, HTTP or HTTPS. Nothing else gets through. And step three, automatic security updates. Your managed platform patched itself. Your VPS does not. So every unpatched vulnerability is a door someone will eventually walk through and you don't know about it. The longer you wait, the more do doors that are open. So direct your AI to configure unattended security updates so critical patches apply automatically without you having to remember to check. More control means more responsibility. No doubt about it. Your managed platform protected you from yourself. Your VPS is not going to. You got to handle it.


</div>
