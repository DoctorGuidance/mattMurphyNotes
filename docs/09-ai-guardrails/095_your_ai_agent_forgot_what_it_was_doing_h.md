# درس 095: درس 095: Your AI agent forgot what it was doing halfway through the

> **عنوان انگلیسی:** Your AI agent forgot what it was doing halfway through the  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DbwB5V_EvJS/)  

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
// Standard Hardening Snippet for Episode 095
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 095 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Did your AI agent forget what it was doing halfway through the job? It started strong. Step one was great. Step five was pretty solid. By step 15, it was contradicting step three. And by step 30, it had forgotten the project altogether. Well, that's not a bug, folks. That is a context window limit. And every single builder using AI agents for complex work hits it every day. So, here are three things you direct your AI to build so your agent stays coherent. across long operations. Step one, a structured context document that travels with every task. Your AI agent does not remember what it did 10 steps ago unless you tell it. So direct your AI to create a running project state file that updates after every step, what has been completed, what is in progress, what the constraints might be, and what decisions have been made. So when the agent starts a new step, it reads that state file first. And that file is the memory your agent does not not have natively. So that's a win. Step two, task decomposition before execution. A 30-step job should never run as one continuous conversation. So direct your AI to break complex work into discrete chunks of five to seven steps each. Each chunk gets its own session with the state file that passed in the start. So smaller scopes mean the agent never drifts far enough to contradict itself. The architecture of how you feed your work work to your agent matters more than which model you're using. So figure it out. Step three, a validation checkpoint between every chunk. Before the agent moves from chunk one to chunk two, something has to verify that output. And that something, that's you. So direct your AI to pause after each chunk and present a summary for you to review before proceeding. The builders who let agents run unsupervised for 30 steps, they know they're getting hallucinated garbage. The builders who check every live step before it goes to production get quality output. So your AI agent is powerful but it's not persistent. Directed in pieces verify in between that is orchestration and that is the win.


</div>
