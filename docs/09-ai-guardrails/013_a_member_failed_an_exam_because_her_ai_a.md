# درس 013: درس 013: A member failed an exam because her AI argued with the

> **عنوان انگلیسی:** A member failed an exam because her AI argued with the  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/Ddl66hIAIkY/)  

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
// Standard Hardening Snippet for Episode 013
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 013 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

So, a member in our faction builders community failed an exam because her AI argued with the curriculum. Her entire application is one400 line file. Claude told her not to split it. The exam said, "Split it." She asked who to listen to. Her AI looked at the file and decided it worked fine as one piece. The code ran, the features loaded. The AI saw no reason to change it. The exam failed her. because the file was not organized for a team, for an audit or for the next version of herself. So your AI optimizes for the session. Got it? But the curriculum optimizes for your whole career. So let's talk about it. Number one, the model sees the code in front of it. It does not see the developer who inherits it in 6 months. It does not see the auditor who reviews it the next quarter. And it does not see the version of you who needs to find one function in a 1,400 line file at 2:00 a.m. when production goes down. So when the model says this works fine, it means this works fine right now for me. That is not the same as this is built correctly to support your users. Your AI is optimizing for its context window, not your future. Remember that. Number two, standards exist because someone already made the mistake. file organization, naming conventions, separation of concerns. These are not preferences. They are lessons. The model has never maintained a codebase for two plus years. It's never onboarded a new developer. It's never sat across from an enterprise buyer who asked to see the architecture. You see, the faction curriculum was written by someone who's done all that stuff. And step three, when your AI argues with the standard, that is the moment you are being tested not by the exam, by the work itself. The builders who override the model when it conflicts with the principle are the ones who ship products that survive. The ones who listen to the model ship products that work today and break tomorrow. The exam was right. Sorry. Your AI will argue with every standard that costs it efficiency. This time that efficiency was me. And that is exactly why the standard exists. You are welcome.


</div>
