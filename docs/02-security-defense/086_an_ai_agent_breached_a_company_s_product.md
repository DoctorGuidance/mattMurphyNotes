# درس 086: درس 086: An AI agent breached a company's production database this

> **عنوان انگلیسی:** An AI agent breached a company's production database this  
> **حوزه معماری:** امنیت نرم‌افزار، حملات و دفاع لایه‌ای (Application Security & Defense)  
> **لایه پروداکشن:** لایه 8 (Security & RLS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/Db8WTQLke0j/)  

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
// Standard Hardening Snippet for Episode 086
// Domain: Application Security & Defense
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 086 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

An AI agent breached a company's production database this last week and the human supervising it clicked approve. This happened during a government evaluation of AI tools. This is not a hypothetical. This was not a lab exercise. This was production AI agent accessing government systems it was never authorized to touch. And the human reviewer, the human in the loop that's responsible for catching it, waved it right on through. So, here's what that means for how You're going to direct AI agents as you move forward. Step one, a human without the right tools is not a guardrail at all. They're just a bottleneck with no teeth. You cannot review hundreds of agent outputs every day and catch every single dangerous action by trying to read them. You're going to miss things. Everyone would. The skill set is not watch everything, read everything. The skill set is knowing what tools you put in front of that agent so the dangerous commands never reach it in in the first place. Scoped credentials, network egress controls, automated gates that reject operations that are outside the defined boundaries of the agent. Those tools catch what your eyes never will. Step two, logged tools. Calls are non-negotiable. Every action your agent takes needs to be fully recorded. What it accessed, what it changed, what it called, and when. If you cannot produce that log, you have no way to know what your agent did when you weren't looking. So, direct your AI to instrument every tool call with an appendon audit trail. When something goes wrong, and I last name's Murphy, I know it will. That log is the difference between a diagnosis and a guess. And you want to know. So, step three, run a structured audit against every build before it ships. Not a personal review, a full system audit. Same one we offer. Entry audits on the way in, exit audits on the way out. It's consistent. It's repeatable. It's not dependent on your attention span at 2 a.m. when something's failing. The human in the loop is only as good as the tools that they are using. So, direct your AI to build those tools, then direct the agents how to operate them safely.


</div>
