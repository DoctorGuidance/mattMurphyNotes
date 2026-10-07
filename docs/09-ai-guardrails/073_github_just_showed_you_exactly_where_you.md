# درس 073: درس 073: GitHub just showed you exactly where your AI money goes

> **عنوان انگلیسی:** GitHub just showed you exactly where your AI money goes  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcMWtOgEgaE/)  

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
// Standard Hardening Snippet for Episode 073
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 073 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

GitHub has just showed you exactly where your AI money goes, and most of you might not ever look, but GitHub's new usage report now breaks down your AI credits by model. Input tokens, output tokens, cash reads, and cash rights. For the first time, you can see exactly which model consumed the credits and what kind of tokens created the costs. So, your AI bill used to be a black box. Not anymore. And here's what you're going to do with that vis. ibility. Step one, model routing by task complexity. When an agent picks a model, it picks the best model available for every single call. Formatting, parsing, boilerplate, routine lookups, all of it running through the most capable model because nobody told the agent to go match a model to the job. That one routing decision can cut a bill in half without changing a single output. So, direct your AI to build a routing layer that sends complex tasks to the best model and routes routine work to the cheapest model that produces the equivalent output. That's a win. Step two, input caching on repeating workflows. If your agent sends the same project context, the same system prompt, the same instructions on every single call, you're paying full token price for identical outputs on every cycle. So, low cache reads on the report, meaning nothing is being reused. The same input sent 10 times cost 10 times what it should. That's not a win. That is not a cost problem and it's actually an architecture problem that you're going to solve. So, direct your AI to restructure repeated inputs into cacheed context that carries across all calls. That's a win. And step three, a weekly cost breakdown by model, by workflow, and by token type. A monthly invoice tells you what you spent, sure, but a weekly breakdown tells you where to cut. Set a budget per workflow and flag anything that spikes. above that baseline. The difference between paying a bill and engineering cost structure is the difference between reacting and operating a business. So, direct your ad to build a weekly cost report you can actually review. Your AI bill just became fully readable. So, it's time to start reading it and that is definitely a win.


</div>
