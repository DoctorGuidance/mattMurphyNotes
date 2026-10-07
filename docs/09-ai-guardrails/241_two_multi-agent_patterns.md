# درس 241: درس 241: Two multi-agent patterns

> **عنوان انگلیسی:** Two multi-agent patterns  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZaJ_faRdcV/)  

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
// Standard Hardening Snippet for Episode 241
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 241 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

You're about to build a multi- aent system. The first architecture decision you make is going to determine whether it scales or it fails. There's two patterns. It's one decision to make. And here are the three things you do to determine which one. Step one, start with orchestrator pattern by default. I say this to everyone. Don't change it. One central agent receives every request. It decides which sub aents to call. It collects all of their outputs. It then synthesizes is the final response. Typical hub and spoke situation. Simple to reason about, simple to debug. That is your default. That is a win. Step two, know when to switch to the conductor pattern. Conductor means agents are passing work to each other in a chain or a graph. There's no single controller. So each agent decides who gets the baton next. You use this for emergent workflows like research tasks or complex reasoning chains or deep creative generation anywhere. The next step depends on what the previous agent discovered. So step three, never start with the conductor ever. The mistakes most builders make that we see is choosing conductor because it sounds cool or it looks cool, right? They then spend weeks debugging circular agent calls. So you start with orchestrator, get your outputs validated, get your error handling solid, and only migrate specific sub workflows to conductor when your data proves that the orchestrator is your bottleneck. So orchestrator first, conductor when earned always, that's the best practice. So what are you building right now with multi- aents? Tell me about it in the comments.


</div>
