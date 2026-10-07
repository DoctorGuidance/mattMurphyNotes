# درس 238: درس 238: Raw AI output should never touch your users

> **عنوان انگلیسی:** Raw AI output should never touch your users  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZdbRXmv_lb/)  

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
// Standard Hardening Snippet for Episode 238
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 238 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Oh no, your AI model is returning garbage to the users and it will. But your users, they should never have to see it. Here are the three things you can do right now to fix it. Step one, validate every AI response before it reaches the users. Does it match your expected schema? Is it within your length and boundaries? Does it contain prohibited content of some sort? If it fails any of these checks, it does not get through to the users. Most builders are piping raw model output directly to the front end. That works till your model hallucinates a credit card number or returns a 10,000word response to a yes or no question. That's not a win. Step two, retry feedback when validation fails. Do not just error out. Add the failure reason to your retry prompt. Your previous responses have exceeded 200 words, so respond in under 200 words. Give your model a chance to self-correct itself. They usually do. Two or three attempts max, though. That's to win for everyone. Now, step three, degrade gracefully when retries fail. Fall back to a simpler model, a cached response, or a human handoff. The user should get a usable experience when the AI fails. Never show a raw error, never show a blank screen of death. So, validate, retry, degrade. Build it once, use it everywhere. That's a best practice. So, what happens now when your app when the AI response is bad? What do you do? Drop it in the comments.

--------------------------------------------------
[NOTEBOOKLM GUIDE & TOPICS]
متن ارائه‌شده بر ضرورت محافظت از کاربران در برابر خروجی‌های نامشخص و آشفته هوش مصنوعی تأکید می‌کند و سه گام عملی برای این منظور پیشنهاد می‌دهد. نخستین گام، اعتبارسنجی دقیق پاسخ‌ها پیش از نمایش به کاربر است تا اطمینان حاصل شود که محتوا با ساختار و محدودیت‌های مورد انتظار مطابقت دارد. در صورت بروز خطا، دومین گام یعنی تلاش مجدد هوشمند به کار گرفته می‌شود که با بازگرداندن دلیل خطا به مدل، فرصتی برای اصلاح اشتباه به آن می‌دهد. در نهایت، اگر اصلاح خودکار نتیجه ندهد، سیستم باید تنزل تدریجی و امن را اجرا کند و با استفاده از روش‌هایی مثل پاسخ‌های از پیش‌ذخیره‌شده یا کمک گرفتن از انسان، از ارائه صفحه خالی یا خطای خام به کاربر جلوگیری کند.


</div>
