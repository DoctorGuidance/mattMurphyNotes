# درس 103: خواباندن کل سرویس توسط یک لپ‌تاپ به دلیل نبود محدودیت نرخ (Rate Limiting)

> **عنوان انگلیسی:** One kid with a laptop can take your entire product offline  
> **حوزه معماری:** محدودسازی نرخ، مقابله با DoS و بات‌ها (Rate Limiting & Abuse Prevention)  
> **لایه پروداکشن:** لایه 9 (Rate Limiting & DoS)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DbjN2IVCeEm/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
یک اسکریپت ساده با ایجاد حلقه‌ای از ۵۰۰ درخواست در ثانیه روی اندپوینت‌های سنگین سرچ یا لاگین، دیتابیس را اشباع کرده و سیستم را برای تمامی کاربران از دسترس خارج می‌کند.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
نبود لایه‌های تراتلینگ (Throttling) و محدودسازی درخواست بر اساس IP، شناسه کاربر و کلید API.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] پیاده‌سازی الگوریتم Token Bucket با استفاده از Redis در لایه Gateway / Middleware
- [ ] تفکیک سقف نرخ برای اندپوینت‌های عمومی (۱۰ در دقیقه) و اندپوینت‌های احراز شده (۱۰۰ در دقیقه)
- [ ] بازگرداندن هدرهای استاندارد `Retry-After` و کد وضعیتی `429 Too Many Requests`

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```typescript
// middleware/rateLimiter.ts
import { RateLimiterRedis } from 'rate-limiter-flexible';
import Redis from 'ioredis';

const redisClient = new Redis(process.env.REDIS_URL!);
const rateLimiter = new RateLimiterRedis({
  storeClient: redisClient,
  keyPrefix: 'middleware_rl',
  points: 10,       // حداکثر ۱۰ درخواست
  duration: 60,     // در هر ۶۰ ثانیه
});

export async function rateLimitMiddleware(req: Request, res: Response, next: NextFunction) {
  try {
    const key = req.ip || req.headers['x-forwarded-for'];
    await rateLimiter.consume(key as string);
    next();
  } catch (rejRes) {
    res.status(429).json({ error: 'Too Many Requests', retryAfter: 60 });
  }
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Do you know that one kid with a laptop can take your entire product offline right now? Not a nation state hacker and not a sophisticated criminal organization, but a teenager who watched a YouTube tutorial and wrote a loop that sends 10,000 requests per second to your API. Your app goes down. Every customer is dark. Every page, every transaction gone because your AI never built a proper firewall. So here's what you direct your AI to set up before someone decides to test you. Step one, a web application firewall that sits in front of your entire stack. Not rate limiting on individual endpoints, but a WFT that filters malicious traffic patterns before they ever reach your server. Your AI deployed your app directly to the internet with nothing between the user and your infrastructure. And unfortunately, that's the equivalent of opening a store with no front door and no security. camera. You don't want that. So, direct your AI to configure a WFT through your hosting provider or a service like Cloudflare. Takes an afternoon, you'll nail it. Without it, your uptime depends entirely whether anyone has decided to hack you today. Step two, adaptive rate limiting that recognizes attack patterns. Basic rate limiting caps requests per user per minute. Sure, not bad. But adaptive limiting detects when request volume, frequency, and origin patterns shift to a attack behavior and then it throttles it automatically. So direct your AI to implement IP based anomaly detection that escalates from throttle to temporary ban based on behavior, not just volume. That's a win. Step three, a DDoS response plan documented before the attack starts. When your app goes down under a flood of traffic, you need a predefined playbook. Who gets notified? What gets toggled? Where traffic gets redirected? So direct your AI to build a plan right now. Not during the outage when you are panicking and your customers are leaving because the front door is wide open. You need to direct your AI to put a wall in front of it today.


</div>
