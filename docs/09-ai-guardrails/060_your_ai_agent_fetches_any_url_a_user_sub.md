# درس 060: درس 060: Your AI agent fetches any URL a user submits

> **عنوان انگلیسی:** Your AI agent fetches any URL a user submits  
> **حوزه معماری:** مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی (AI Guardrails, LLM Security & Compliance)  
> **لایه پروداکشن:** لایه 2 (APIs & Business Logic)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DceYRVpCFKG/)  

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
// Standard Hardening Snippet for Episode 060
// Domain: AI Guardrails, LLM Security & Compliance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 060 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI agent fetches URLs from user inputs. So, a hacker just used it to map every service running inside your network. Your AI agent has the same network access that your server has. It can see internal databases, admin panels, and cloud credentials. So, when a user gives it a URL to fetch, your agent does not ask whether that URL belongs to you or to someone trying to rob you. It fetches it from inside your perimeter and it hands the response back. So, an attacker just used your own infrastructure to bypass your own firewall. Let's get ahead of it. Step one, your agent needs a boundary. Right now, it'll fetch anything from anywhere. Internal services, cloud credential endpoints, admin dashboards. It does not know the difference between a legitimate request and an attack. So, direct your AI to restrict all outbound fetches to an approved list of external domains. and block any requests targeting your internal network altogether. That's a win. Step two, a single validation check. That is not enough. Attackers use techniques that pass your domain check on the first look and redirect to an internal target on the actual fetch. So, your agent validates the front door and walks right through the back. So, direct your AI to pin every URL to a single resolved address and revalidate on every redirect. This is so the destination cannot change between the check and the fetch. That's a win. And step three, your error messages are giving away the map. Every failed fetch returns a different error. Connection refused means a host exists. Timeout means a service is listening. So an attacker reads those differences and builds a blueprint of your internal network without ever touching it directly. So direct your AI to return one generic error for all failed fetches and log the details where Only your team can see them. So, your AI AI agent has the keys to every room in your building, right? Make sure strangers cannot tell which doors they open. That's the win.


</div>
