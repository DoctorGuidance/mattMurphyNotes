# درس 036: درس 036: NIST says most agents run on borrowed credentials

> **عنوان انگلیسی:** NIST says most agents run on borrowed credentials  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdCbUuPFMA9/)  

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
// Standard Hardening Snippet for Episode 036
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 036 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Most AI agents in production environments are running on borrowed human credentials with no clear audit trail. And that that's really dangerous. And it's not an argument against AI agents. I think they're awesome. It's an argument for directing them to operate safely. So here are some safety tips. Number one, every AI agent you deploy needs its own identity, not your API key and not your login credentials. A unique credential scoped for that agent and to that task. When one of your agent takes an action you did not expect, and it will. Trust me, Murphy's law. You need to know which agent did what and when. If all your agents share your credentials, a compromised agent is a compromised you with a really bad audit trail, your code, your data, your access. It was your fault. So, direct your AI to create scoped identities for every agent before you deploy any of them. That is a win. Step two, short-lived keys and approval gates before production. An agent's credentials should expire. An agent that needs to touch live data, customer records, or production systems should always require your approval before it does. Anthropic literally just froze reinforcement learning for a month this quarter after those agents escaped their sandboxes. So, these are not theoretical controls. They are the difference between an a agent that serves your business and an agent that operates without a leash on your infrastructure. And that's dangerous, right? Step three, separate logs for every agent session. Your agents are making decisions you're not watching in real time. Jetream, Orchestra, and Crowd Strike all launched agent control planes this last quarter for this exact reason. So, a director using their system decides what agents are allowed to do before they start it all. And Per agent log lets you reconstruct what just happened. Without it, you are trusting and never verifying. So direct your AI agents or they will direct themselves and get you in trouble.


</div>
