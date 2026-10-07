# درس 030: درس 030: Thousands of people scraped your prompt this week and you

> **عنوان انگلیسی:** Thousands of people scraped your prompt this week and you  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DdKJvRxjm6M/)  

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
// Standard Hardening Snippet for Episode 030
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 030 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Thousands of people scraped your prompts this week, ran them in their builds, and you have no idea that it even happened. So, let's say you publish a prompt, right? Someone copies it, runs it, uses your work without credit or payment to you. So, there's no watermark on a text prompt. There is a callback. And so, OAST gives you a trip wire for your intellectual property if you know how to set it up. So, let's talk about it. Number one, embed an outofband call back URL in every prompt. A unique URL that only resolves when an AI processes that prompt. So it sits in an instruction the AI reads but the user does not see it. If it does not affect the prompt's output, then no one notices it. When someone copies your prompt and runs it, the AI hits that URL every time you get a ping with a timestamp and the origin. I can tell you from experience that the first time you see a call back fire from a prompt you posted two days ago it changes how you think about what you share and what you're going to charge for it right and this is not theoretical I deal with it every single week you guys copy thousands of prompts so entire direc directories exist for scraping prompts number two one call back URL per prompt when it fires you know exactly which prompt was copied when it was used and roughly where from right so You are not guessing who is using your work. You have a full log of it over time. You see all the patterns, which prompts travel, which audiences are copying them, which ones generate the most scraping activity. That data informs you publicly what you need to keep behind your gate, right? And three, the callback is detection, not prevention. You cannot stop someone from copying a text prompt. And by the way, you shouldn't. If you're putting it out there, you want people to use it, but you can know when they did and where they went. Whether you use that for attribution enforcement or just awareness, the data is yours. You can do what you want with it. A prompt without a canary is invisible the moment someone copies it. A prompt with a canary calls home every time and tells you what happened. So, your prompts, they're your product. Treat them like they are.


</div>
