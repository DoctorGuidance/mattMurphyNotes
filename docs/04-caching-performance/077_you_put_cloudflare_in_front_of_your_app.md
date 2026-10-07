# درس 077: درس 077: You put Cloudflare in front of your app

> **عنوان انگلیسی:** You put Cloudflare in front of your app  
> **حوزه معماری:** کشینگ، توزیع لبه و پرفورمنس سیستمی (Caching & Edge Performance)  
> **لایه پروداکشن:** لایه 10 (Caching & CDN)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DcHNH00EZ1T/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
چالش در این سناریو ناشی از عدم مدیریت صحیح معماری در مبحث کشینگ، توزیع لبه و پرفورمنس سیستمی است که باعث شکست سیستم زیر بار واقعی یا نفوذ مهاجم می‌شود.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
علت ریشه‌ای: عدم اعمال محدودیت‌ها و سیاست‌های سخت‌گیرانه در لایه Caching & Edge Performance و اتکا به تنظیمات پیش‌فرض یا خوش‌بینانه.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] بازبینی تنظیمات و کدهای مربوط به Caching & Edge Performance در سراسر پروژه
- [ ] اعمال محدودیت‌های اعتبارسنجی در لایه سرور به جای اعتماد به کلاینت
- [ ] تست حالات لبه (Edge Cases) و تزریق خطای شبیه‌سازی‌شده پیش از انتشار

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```bash
// Standard Hardening Snippet for Episode 077
// Domain: Caching & Edge Performance
export function verifyProductionHardening(config: Record<string, unknown>): boolean {
  if (!config.isHardened) {
    throw new Error('Production guardrail triggered: Review Episode 077 guidelines.');
  }
  return true;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

You put Cloudflare in front of your app, but an attacker found your server's real IP and went right around it. All your W rules, all your DDoS protection, your bot filtering, your rate limiting, all of it bypassed completely because your origin server's IP address is discoverable and your attacker just hit it directly. Cloudflare only protects you if all traffic is flowing through it. The moment someone finds your real IP, they skip everything. that you set up. Here is what your AI missed when it configured your Cloudflare. Step one, your origin IP is leaking. DNS history tools store every IP your domain has ever pointed to. If you added Cloudflare after your site was already live, your precloudflare IP is a public record. Your email headers are exposing it. Misconfigured subdomains will point straight to it. So, direct your AI to check every subdomain, every MX record. every outbound email header and every DNS history service for your origin IP. If it's discoverable anywhere, your Cloudflare setup is a locked front door with a wide openen garage door. That's not a win. Step two, your origin server still accepts connections from the entire internet. It should only accept connections from Cloudflare's IP range. So, direct your AI to configure your firewall to whitelist Cloudflare's published IP ranges and block everything else. If a request does not come through Cloudflare, it does not reach your server. Period. And number three, your SSL is probably set to flexible. That means traffic between your user and Cloudflare is encrypted, but traffic between Cloudflare and your server is not encrypted. So an attacker on the network between Cloudflare and your origin sees everything in plain text. So direct your AI to set SSL to full strict mode and install a Cloudflare origin certificate on your server. Encrypted end to end, no gaps. Cloudflare is not a switch that you flip. It is an architecture that you must configure. So, direct your AI to configure it correctly before somebody walks right around it.


</div>
