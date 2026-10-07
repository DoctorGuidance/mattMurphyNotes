# درس 043: سرقت توکن‌های احراز هویت به دلیل ذخیره‌سازی در localStorage

> **عنوان انگلیسی:** Your AI stored your authentication token in localStorage  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/Dc3kkckjyYV/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
کدهای تولیدشده توسط AI توکن‌های JWT نشست را در localStorage مرورگر ذخیره می‌کنند؛ هر اسکریپت ثالث، ویجت چت، یا باگ XSS در صفحه می‌تواند توکن را بدون نیاز به سرور به سرقت ببرد.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
اشتباه گرفتن حافظه ذخیره‌سازی عمومی کلاینت با مخزن امن هویت کاربر و نبود فلگ‌های محافظتی مرورگر.

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] انتقال کلیه توکن‌های دسترسی به کوکی‌های امن با فلگ HttpOnly
- [ ] تنظیم فلگ‌های `Secure` (انحصاری HTTPS) و `SameSite=Lax` جهت مهار CSRF
- [ ] کاهش طول عمر توکن دسترسی به ۱۰ تا ۱۵ دقیقه و چرخش توکن بازنشانی (Rotating Refresh Token)

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```typescript
// auth/cookieManager.ts
export function issueSessionCookie(res: Response, token: string) {
  res.cookie('auth_token', token, {
    httpOnly: true,                               // مسدودسازی دسترسی JS
    secure: process.env.NODE_ENV === 'production', // انحصاری HTTPS
    sameSite: 'lax',                              // مهار CSRF
    path: '/',
    maxAge: 15 * 60 * 1000                        // انقضای ۱۵ دقیقه‌ای
  });
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI stored your authentication token in local storage. Now any script on your page can steal it and log in as your user. So your AI built your login system. User authenticates. Server sends back to a jot file. Front end stores it in local storage. That token is your user's identity and it is sitting in a storage location that every script on your page can read. So that chat widget you added last week can read your users off tokens right now. Here's how we're going to fix it. Number one, move your tokens out of local storage and into HTTPON cookies. An HTTPon cookie cannot be read by JavaScript. It travels with every request automatically and is invisible to any script running on your page. So, direct your AI to refactor authentication flow. So, it stores the jot in a secure HTTPON same site cookie instead of local storage. That's a win. Number two, Set token expiration short and implement refresh tokens. A stolen jot that lasts 30 days is an open door for 30 days. A token that expires in 15 minutes limits that damage window. So direct your AI to implement short-lived access tokens with a secure refresh token rotation that issues a new pair on each refresh. That's a win. And number three, add token revocation. If a user changes their password or reports a compromised account, every active token for that user should die immediately. So, directory AI to implement a token revocation list or a per user user token version, right? So that it invalidates all existing tokens when the user's security state changes. Your off token is your user's key to the building. Stop leaving it on the counter where anyone can copy it. And that is a win.


</div>
