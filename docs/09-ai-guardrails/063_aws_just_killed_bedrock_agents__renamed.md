# درس 063: درس 063: AWS just killed Bedrock Agents. Renamed it to Classic.

> **عنوان انگلیسی:** AWS just killed Bedrock Agents. Renamed it to Classic.  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcbP4U7G6QK/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه AI Guardrails, LLM Security & Compliance و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به AI Guardrails, LLM Security & Compliance در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 063
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 063 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

AWS just killed Bedrock Agents. Now everyone who built on it for the healthcare baa has a migration path they did not plan for. And if you built your healthcare app on bedrock agents, your compliance path just got rerouted. So agent core is the replacement, but it's a different architecture, a different runtime and different integration surface altogether. So your existing deployment does not migrate itself. Here's how you're going to handle it. Step one, an abstraction layer between your application and any cloud provider's agent framework. Your business logic should never be hardwired to a vendor's SDK. If your agent orchestration is built directly on Bedrock's API surface, every line of that code is now migration liability. So, direct your AI to refactor your agent orchestration behind an internal interface. That way, the underlying framework can be swapped without rewriting your application. That's That's a win. Step two, a BAA audit on every service in your stack after any provider migration. So your BAA covers specific services by name. When the service changes, the BAA coverage may not follow it automatically. So moving from bedrock agents classic to agent core means you need to reverify that every service in your healthcare data path is covered under the current agreement. Direct your AI to map every service that touches PHI. and verify the BAA coverage against the current AWS service list. That's a win. And step three, a migration runway, not a migration emergency. Classic is not shutting down tomorrow. So, it's also no longer receiving any of the new features, which means every month you stay on it, you fall a little further behind the platform providers actually investing in. So, direct your AI to build a migration timeline that moves your agent orchestration to the supported framework. That way, Before classic becomes a liability, instead of a convenience, you're already ahead of it. This way, your cloud provider will always build the next thing. We hear it. But architect your system so the next thing doesn't break what you built.


</div>
