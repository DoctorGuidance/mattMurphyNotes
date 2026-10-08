# Masterclass #327: The Wildcard CORS Breach: Explicit Allowlists & Safe Credential Handling

**Module**: `Application Security & Defense` | **Layer**: `Layer 08` | **Severity**: `CRITICAL`

---

## 🚨 Problem Statement
AI assistants configure wildcard CORS headers (Access-Control-Allow-Origin: *), combine them with credentials, or echo arbitrary Origin headers, allowing malicious websites to harvest private user data via CSRF/cross-origin requests.

### تشریح به زبان فارسی
هوش مصنوعی هدرهای CORS را با ستاره (*) تنظیم می‌کند یا اوریجین مهاجم را عینا بازتاب می‌دهد؛ در نتیجه وب‌سایت مهاجم کوکی‌های کاربر را ارسال کرده و پاسخ‌های محرمانه API را می‌خواند.

---

## 🔍 Root Cause Analysis
Defaulting to permissive CORS settings to bypass local development browser errors, combined with naive origin reflection that bypasses simplistic static scanners.

### ریشه خطا به فارسی
تنظیم CORS روی مقادیر باز برای حل سریع خطاهای مرورگر در محیط لوکال و اکو کردن خودکار اوریجین ورودی جهت دور زدن اسکنرهای امنیتی.

---

## ⚖️ Production Comparison Matrix
| Architectural Dimension | Vibe Coding Anti-Pattern (Trap) | Production Engineering Standard (Verified) |
| :--- | :--- | :--- |
| **Operational Standard** | Setting Access-Control-Allow-Origin: * or echoing req.headers.origin blindly with allowCredentials: true. | Explicit domain allowlist, strict regex matching for trusted origins, and credentials set exclusively for verified peers. |
| **تحلیل استاندارد فارسی** | قرار دادن * در Access-Control-Allow-Origin یا اکو کردن هر Origin ورودی همراه با فعال‌سازی کوکی‌ها. | تعریف لیست سفید سخت‌گیرانه دامنه‌ها، اعتبارسنجی مبدا با Regex دقیق و فعال‌سازی کوکی تنها برای کلاینت‌های مجاز. |

---

## 🛠️ Step-by-Step Action Plan
1. Replace wildcard origins with an immutable, strict allowlist of validated production domains.
1. Reject Access-Control-Allow-Credentials when incoming requests do not strictly match the domain allowlist.
1. Sanitize and validate Origin headers against exact regex/whitelist rules before dynamic reflection, returning null for unverified domains.

### گام‌های عملیاتی فارسی
- جایگزینی هدر ستاره با لیست سفید قطعی و صریح دامنه‌های مجاز پروداکشن.
- غیرفعال‌سازی Access-Control-Allow-Credentials در صورت عدم تطابق دقیق درخواست با لیست مجاز دامنه‌ها.
- اعتبارسنجی دقیق هدر Origin قبل از بازتاب در پاسخ و بازگرداندن هدر خالی یا خطای 403 برای مبداهای ناشناس.

---

## 💻 Hardened Production Code Pattern
```typescript
// PRODUCTION STANDARD: Hardened Express CORS Middleware
import cors from 'cors';

const ALLOWED_ORIGINS = new Set([
  'https://app.productiondomain.com',
  'https://admin.productiondomain.com'
]);

export const secureCors = cors({
  origin: (origin, callback) => {
    // Allow non-browser server-to-server or strictly allowed web origins
    if (!origin || ALLOWED_ORIGINS.has(origin)) {
      callback(null, true);
    } else {
      callback(new Error('CORS Policy: Origin strictly blocked by security rule.'));
    }
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
  allowedHeaders: ['Content-Type', 'Authorization', 'X-Requested-With']
});
```

---

## 🎙️ Word-for-Word Audio Transcript
> "Your AI configured CORS on your API. The browser asked which origins are allowed and your server said all of them. So an attacker just read your user's private data from a completely different website. Your CORS policy allowed it. So your API trusts every origin on the internet because your AI set access control allow origin to the wild card. An API that trusts every origin trusts the attacker's origin too. So here are three steps to get it fixed. Step one, the wildcard header tells every browser that any website can read responses from your API. So an attacker hosts a page that makes requests to your API using your user's cookies. The browser sends the credentials. Your API returns the data and the attacker's page reads it. So your user never leaves the attacker's website. You need to direct your AI to replace the wild card with an explicit allow list of your own domains. That is the win. Step two, your AI may have added access control allow credentials alongside the wild card. This tells the browser to include cookies with cross origin requests. The wild card with credentials is the most dangerous CORS configuration possible. Don't do it. Every website on the internet can make authenticated requests to your API and read the full response. So, direct your AI to set credentials to true only when the origin header matches your allow list. That's a win. And step three, your API reflects the origin header back as the access control allow origin value without checking it. This is functionally identical to a wild card, but passes automated scans that flag wild cards. So, an attacker sets their origin, your API echoes it back and the browser fully trusts it. So direct your AI to validate the origin header against a hard-coded allow list before reflecting it. Your API has a guest list. Right now, everyone is on it, and that is not a win."

---

## 💡 Golden Takeaway
> **"Your API must have a strict guest list: wildcard CORS or unvalidated origin reflection hands your authenticated user data directly to any malicious site on the web."**
>
> *اندپوینت‌های شما باید لیست مهمانان اختصاصی داشته باشند؛ تنظیم ستاره در CORS یا بازتاب کورکورانه هدر Origin، اطلاعات محرمانه کاربران را تقدیم سایت‌های مخرب می‌کند.*
