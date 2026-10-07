# درس 175: درس 175: GitHub Copilot had a CVSS 9.6 remote code execution

> **عنوان انگلیسی:** GitHub Copilot had a CVSS 9.6 remote code execution  
> **حوزه معماری:** تست، محیط‌های کاری، CI/CD و خط لوله استقرار (Testing, Staging & CI/CD)  
> **لایه پروداکشن:** لایه 7 (CI/CD & Pipelines)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DaYKQ7-E6KB/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث تست، محیط‌های کاری، CI/CD و خط لوله استقرار است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Testing, Staging & CI/CD و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Testing, Staging & CI/CD در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 175
// Domain: Testing, Staging & CI/CD
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 175 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

If you haven't heard, GitHub Copilot just had a remote code execution vulnerability. CVSS score 9.6 out of 10. That's critical, folks. So, here's what happened. Someone put a hidden prompt injection in a PRD. Not in the code, in the description of the code. Copilot read the description as context. The injection triggered code execution on the developer's machine without them even knowing it. Remote code execution from a normal pull. request through an AI coding assistant. Let that sink in, vibe coders. That's a death spiral. The tool you trust the most to help you write code just became the attack vector. Not the code it generated. The AI itself. This has been patched, but the pattern has not. We're going to see a lot more of it. Every AI tool that reads context from external sources is a potential injection surface. Your AI assistant reads your repo, your comments, your issues. your PRs. If any of those inputs can be poisoned, your AI can be weaponized against your app. This is why we teach security as the entire layer in the AIdirected engineering stack because the threat model has changed and it will keep changing and most builders do not know it yet, especially vibe coders using AI assistance this exact same way.


</div>
