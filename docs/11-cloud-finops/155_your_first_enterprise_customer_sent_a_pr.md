# درس 155: درس 155: Your first enterprise customer sent a procurement checklist

> **عنوان انگلیسی:** Your first enterprise customer sent a procurement checklist  
> **حوزه معماری:** معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه (Cloud Infrastructure & FinOps)  
> **لایه پروداکشن:** لایه 6 (Cloud & Compute)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DaqKoflEgzB/)  

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
// Standard Hardening Snippet for Episode 155
// Domain: Cloud Infrastructure & FinOps
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 155 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your first enterprise customer wants to buy your product. That's a win. Their IT team just sent over a procurement checklist. Line one, do you support single sign on via SAML and OIDC? You have Google signin and an email password, but I don't think that's SSO. Here are the three things you need to understand right now to fix it. Step one, SSO is not optional for the enterprise. Their employees log in through one corporate identity provider every day. Octa, Azure AD, Google Workspace. If your app cannot authenticate through their provider, their IT team will not approve the purchase at all. You're out of there. This is not a feature request. It is a gate and a bare minimum to get in the door. Step two, SAML is a protocol your AI needs to learn fast. Direct your AI to implement SAML 2.0 or OIDC integration. The handshake, the assertion, the attribute mapping, the session management, your AI can build it all, but you have to know to ask for it before the checklist arrives from the client. And step three, plan for multi-tenant SSO. Each customer uses a different identity provider. Customer A uses Octa, customer B uses Azure AD. Direct your AI to build tenants specific SSO configurations. One integration pattern per tenant credentials. The potential enterprise deals that can change your business. Start with three letters every single time. S O That's the win.


</div>
