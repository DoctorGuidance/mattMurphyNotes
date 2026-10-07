# درس 205: کرش خاموش سرور در ساعت ۲ بامداد به دلیل خطاهای هندل‌نشده Async

> **عنوان انگلیسی:** Your app crashed at 2 AM  
> **حوزه معماری:** مشاهده‌پذیری، لاگ ساختاریافته و رهگیری خطا (Observability & Error Tracking)  
> **لایه پروداکشن:** لایه 12 (Observability & Logs)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DZ8HOqlgZy5/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
سرویس سرور در نیمه‌شب کرش می‌کند و هیچ لاگ یا اثری در کنسول باقی نمی‌ماند، کاربران ساعت‌ها با خطای 502 Bad Gateway مواجه می‌شوند.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
پرتاب Unhandled Promise Rejection در توابع Async که در نودجی‌اس باعث توقف کامل Event Loop و خروج پروسس می‌شود.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] ثبت هندلرهای سراسری پروسس برای `uncaughtException` و `unhandledRejection`
- [ ] ارسال لاگ خطای ساختاریافته JSON به سیستم Sentry با Correlation ID
- [ ] مدیریت چرخه حیات پروسس با PM2 یا Docker Restart Policy

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```typescript
// server.ts
process.on('unhandledRejection', (reason: Error, promise: Promise<any>) => {
  logger.error('Unhandled Rejection at:', { promise, reason: reason?.stack || reason });
  // Graceful shutdown & Sentry capture:
  Sentry.captureException(reason);
});

process.on('uncaughtException', (error: Error) => {
  logger.error('Uncaught Exception thrown:', { error: error.stack });
  Sentry.captureException(error);
  process.exit(1); // Exit to let orchestrator restart
});
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your app just crashed at 2:00 in the morning and you found out at 9 in the morning when a customer emailed support. 7 hours of downtime, zero alerts. Here are the three things you set up right now to make sure that never happens again. Step one, health checks. A process that pings your application every 60 seconds and asks it one question. Are you alive? Not are you fast, not are you correct, not are you connected, but are you alive? When the answer is no, your phone instantly rings, not your customer's patience. This takes 10 minutes to configure and saves you every single time it happens. That's a win. Step two, error tracking. Your application throws errors every single day. Most of them you never ever see. An error tracker captures every single exception, groups them by frequency, and shows you which ones affect real users. The error that crashes one user's workflow 300 times a week has been happening for months, and you didn't even know it. you just never looked and that's the reason that you set these systems up. Step three, uptime monitoring from your outside infrastructure. Your server says it is healthy all the time, but your users in Singapore can't reach it. External monitoring checks from multiple regions of the world. Your internal dashboard is not your customer's experience. So, stop finding out about downtime from people who are paying to use your system.


</div>
