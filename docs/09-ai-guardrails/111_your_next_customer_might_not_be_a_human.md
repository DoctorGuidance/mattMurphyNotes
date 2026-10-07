# درس 111: درس 111: Your next customer might not be a human

> **عنوان انگلیسی:** Your next customer might not be a human  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DbYgfWbDWW2/)  

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
// Standard Hardening Snippet for Episode 111
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 111 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your next customer might not even be a human and your product is completely invisible. So right now, right now, AI agents are shopping for people all day long. Not researching, shopping for people, comparing products, reading pricing pages, evaluating reviews, making buying decisions, and in some cases, completing the purchase altogether. And this is without a human ever visiting your website. So here's what that means for you and what you're building right now. One, your product has two customers now, and you are only building for one of them. Everybody is. We get it. These agent things, they're new, right? But a human browses your site, reads your copy, and looks at your screenshot, and then makes an emotional decision. An AI agent reads your structured data, your pricing schema, and your API documentation, and then it makes a logical decision. If your product page is a beautiful design with no structured data underneath it, Yeah, a human might buy, but an AI agent will never find you. Cruises right on by. So, you need to direct your AI to audit every product page for machine readable structured data, schema markup, clean pricing tables, and product specs and formats, and AI can parse. The AI shopper does not care about your hero image at all. It cares about your metadata. Get it in line. Number two, AI agents are making decisions about criteria you never even specified. When a shopper tells their AI agent, "Find me a project management tool under $50 a month." That agent is filtering on things you never thought to even publish. Uptime guarantees, integration list, security, certifications, data export capabilities. If that information is not on your site in a structured format, the agent fills in the blanks with assumptions or skips you entirely. So, direct your AI to build a machine readable product specification page. That covers every criteria an AI agent might filter on. That's a win. Number three, the discovery game just changed permanently. SEO was about ranking for humans. The next era is ranking for AI. LLMs recommend products based on what they have been trained on. That what they can find in real time and how confidently they can describe your product to their shopper. So, direct your AI to audit how the major LLMs describe your product right now. Ask ChatGpt, Claude, Gemini to recommend a product in your category. If you're not in the response, you do not exist to the fastest growing shopping channel on the entire planet. So, your AI built a product for human customers. The next wave of customers is not human at all. So, direct your AI to make sure they can find you, and that is a win.


</div>
