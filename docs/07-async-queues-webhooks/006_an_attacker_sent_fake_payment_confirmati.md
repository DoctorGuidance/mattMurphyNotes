# درس 006: ارسال تاییدیه‌های پرداخت جعلی به وب‌هوک Stripe و مهار تقلب مالی

> **عنوان انگلیسی:** An attacker sent fake payment confirmations to your Stripe  
> **حوزه معماری:** صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی (Async Queues & Webhooks)  
> **لایه پروداکشن:** لایه 6 (Cloud & Compute)  
> **منبع ریلز اینستاگرام:** [مشاهده ویدیو در Instagram](https://www.instagram.com/reel/DduM5W5k4HF/)  

---

## 🚨 ۱. طرح مسئله و سناریوی آسیب‌پذیری (Problem & Attack Vector)
مهاجمان با ارسال پی‌لودهای جعلی HTTP POST به اندپوینت وب‌هوک پرداخت، اشتراک یا کیف پول خود را بدون پرداخت واقعی شارژ می‌کنند.

---

## 💡 ۲. تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)
اتکا به متغیرهای بدنه جیسون بدون احراز امضای رمزنگاری‌شده استرایپ (Stripe Signature) بر روی بافر خام درخواست (Raw Request Buffer).

---

## ⚡ ۳. برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)
- [ ] غیرفعال کردن پارسر JSON خودکار روی روت وب‌هوک و دریافت بافر خام (Raw Buffer)
- [ ] اعتبارسنجی امضا با استفاده از `stripe.webhooks.constructEvent` و کلید وب‌هوک
- [ ] بررسی شناسه رویداد (Event ID) در ردیس جهت مهار حملات تکرار (Replay Attacks)

---

## 💻 ۴. الگوی کد / کانفیگ استاندارد و سخت‌سازی‌شده (Hardened Implementation)
```typescript
// routes/stripeWebhook.ts
import Stripe from 'stripe';
import express from 'express';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

export const stripeWebhookHandler = express.raw({ type: 'application/json' });

export async function handleWebhook(req: express.Request, res: express.Response) {
  const sig = req.headers['stripe-signature'] as string;
  try {
    const event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET!);
    // Idempotency check:
    const alreadyProcessed = await redis.set(`evt:${event.id}`, '1', 'NX', 'EX', 86400);
    if (!alreadyProcessed) return res.status(200).json({ received: true });
    
    // Process event...
    res.json({ received: true });
  } catch (err: any) {
    res.status(400).send(`Webhook Error: ${err.message}`);
  }
}
```

---

## 🎧 ۵. متن کامل ترنسکریپت زبان اصلی (Original Audio Transcript)
<div dir="ltr">

Your AI integrated those Stripe web hooks, but an attacker just sent fake payment confirmation to your Stripe web hook endpoint and your application processed every single one of them. Stripe signs every event it sends. Your AI never checked the signature. So when a payment succeeds, Stripe sends a post to your endpoint. Your application reads the event body and provisions the service. So the endpoint accepts any post request with the right JSON structure. A web hook without signature verification is a command line anyone can type. It's time to tighten it up. Step one, Stripe includes a signature header with every web hook event. The signature is a hash of the payload using a secret only you and Stripe share. So your AI skipped verification because the integration worked without it. An attacker sends a post with a crafted event body, whether it's payment succeeded, subscription upgraded, or access granted. And so your application processes it because it never checked who sent it. So direct your AI to verify the Stripe web hook signature using your endpoint secret before processing any event at all. That's a win. Step two, this is not limited to Stripe at all. Clerk signs user events. GitHub signs repository web hooks. So every major service signs their payload. your AI integrated three services and verified none of them. So each unverified endpoint is a separate door without a lock. So direct your AI to audit every web hook endpoint in your application and implement signature verification for each one of those providers. That's a win. And step three, an attacker who captures a legitimate web hook payload can absolutely replay it. Same event, same signature, different timing, right? So a payment event replayed three times provisions three separate accounts. So direct your AI to store processed event ids and reject all duplicates. Stripe event ids are unique. Use them everywhere. Your web hook endpoint is not a notification. It's a command. Always verify who sent it before you execute it. That's the way it rolls.


</div>
