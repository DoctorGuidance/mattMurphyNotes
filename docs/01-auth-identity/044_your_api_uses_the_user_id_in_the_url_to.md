# درس 044: آسیب‌پذیری ارجاع مستقیم و ناامن به اشیاء (IDOR) از طریق شناسه در URL

> **عنوان انگلیسی:** Your API uses the user ID in the URL to load their data  
> **حوزه معماری:** احراز هویت و مدیریت نشست‌ها (Authentication & Identity)  
> **لایه پروداکشن:** لایه 4 (Auth & Permissions)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/Dc1jZHyiWz0/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
تغییر ساده شناسه در آدرس (`/api/invoices/1042` به `1043`) به هر کاربری اجازه می‌دهد فاکتورها و اطلاعات حساس سایر مشتریان را مشاهده یا دانلود کند.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
اعتماد کورکورانه به شناسه ورودی URL و عدم اسکوپ کردن کوئری دیتابیس به شناسه کاربری و شناسه سازمان (Tenant ID).

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] الزام شرط `tenant_id` و `user_id` در تمامی کوئری‌های واکشی داده در دیتابیس
- [ ] استفاده از Row-Level Security (RLS) در لایه پایگاه‌داده به عنوان خط دفاع نهایی
- [ ] استفاده از شناسه‌های تصادفی غیرقابل حدس (UUIDv7 یا NanoID) به جای ID عددی متوالی

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```typescript
// services/invoiceService.ts
export async function getInvoice(invoiceId: string, currentTenantId: string) {
  // ❌ BAD: const invoice = await db.invoices.findUnique({ where: { id: invoiceId } });
  // ✅ SECURE: Strict Tenant-scoped query
  const invoice = await db.invoices.findFirst({
    where: {
      id: invoiceId,
      tenantId: currentTenantId // شناسه مستاجر احراز هویت شده
    }
  });
  if (!invoice) throw new NotFoundError('Invoice not found or access denied');
  return invoice;
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your API is using the user ID and the URL to load the data. So you change the number and you see someone else's account algether. So your AI yeah built your API endpoints. Your front end sends the logged in user's ID and gets their data right back. But your API never checks whether the person making the request is actually the right user. So your authorization is in the URL and your URL is one guess away from every other user's data. Let's get this handled. Step one, verify ownership on every API request. Every endpoint that returns user specific data must check the authenticated user's identity against the resource they are requesting. So if user 12 requests user 15's data, the server returns a 403. So direct your AI to add ownership verification middleware so that it compares the authenticated session user against the resource owner on every protected endpoint. That's a win. Step two, stop using sequential IDs in your URLs. User 1, user 2, user 3, or order 1, 10,002, 10,003. Sequential IDs make enumeration trivial. An attacker writes a loop and downloads every user's data in minutes. So, direct your AI to replace sequential integer IDs with UYU IDs and all API endpoints and database references. That's a win. And step three, audit every endpoint that takes an ID as a parameter. Your AI built dozens of endpoints. Every one of them accepts an ID in the URL, query string, or a request body, a potential access control failure. So, direct your AI to list every endpoint so that it accepts a resource identifier, verify ownership checks exist on each one, and flag any endpoint where a user can access resources that do not belong to them. Your API should not trust the URL. It should Trust the user session. That's your win.


</div>
