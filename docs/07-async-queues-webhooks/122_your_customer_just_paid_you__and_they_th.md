# Episode 122: Your customer just paid you. And they think you are a scam

> **Category:** Async Queues & Webhooks (صف‌های پردازش غیرهمزمان و وب‌هوک‌های مالی)  
> **Production Layer:** Layer 6  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DbJSeKTFKW0/](https://www.instagram.com/reel/DbJSeKTFKW0/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your customer just sent you a payment. And now they think you're a scam. The charge hit their bank account, but the confirmation email never showed up behind it.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
The charge hit their bank account, but the confirmation email never showed up behind it. Not in their inbox, not in promotions, not in spam, nowhere. And so now they're staring at a bank charge from a company they found on Instagram with no receipt, no way to know if they just got scammed.

---

## ⚡ 3. Hardening Action Checklist
- [ ] SPF and DKIM records in your sending domain. These are the authentication protocols that tell Gmail and Outlook your app is allowed to send email from your domain.
- [ ] a dedicated sending domain for transactional emails separate from your marketing. When your newsletter gets spam complaints, that reputation bleeds into your receipts.
- [ ] delivery monitoring. That tells you where your emails actually land.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #122
// Domain: 07-async-queues-webhooks
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #122 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #122');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your customer just sent you a payment. And now they think you're a scam. The charge hit their bank account, but the confirmation email never showed up behind it. Not in their inbox, not in promotions, not in spam, nowhere. And so now they're staring at a bank charge from a company they found on Instagram with no receipt, no way to know if they just got scammed. This is not a code problem. This is actually a deliverability problem your AI never set up. So here are the three things things you're going to direct your AI to configure before your payment emails start destroying customer trust. Step one, SPF and DKIM records in your sending domain. These are the authentication protocols that tell Gmail and Outlook your app is allowed to send email from your domain. Without them, email providers treat your receipts with the same way they treat a fishing attempt. Your emails work in development because your test inbox doesn't care. But Gmail, it cares. and your paying customer checking their bank statement at midnight cares even more. So, got to get it fixed. Step two, a dedicated sending domain for transactional emails separate from your marketing. When your newsletter gets spam complaints, that reputation bleeds into your receipts. Your password resets start bouncing. Your customer file chargebacks because they never got proof of purchase because your marketing program marked it as spam. One domain for receipts, one domain for marketing. The separation takes an afternoon and will save you everything. Trust me. And step three, delivery monitoring. That tells you where your emails actually land. Your logs say delivered, right? But delivered means it reached the mail server, not a human inbox. You need to know your inbox placement rate and your spam complaint rate before your customers tell you about it. Because they will not tell you politely. Trust me, they'll not be nice. They'll tell you with a chargeback. They'll cancel and then they'll go report it. So, your AI built the payment flow, but it never built proof that the payment has happened. Direct your AI to fix that before your next customer thinks they got scammed by you.

</div>
