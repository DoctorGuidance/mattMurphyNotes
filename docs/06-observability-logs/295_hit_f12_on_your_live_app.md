# Episode 295: Hit F12 on your live app

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | ℹ️ `MEDIUM` |
| **Architectural Domain** | Observability & Error Tracking (`مشاهده‌پذیری، لاگ ساختاریافته و رهگیری خطا`) |
| **Target Production Layer** | Layer 12 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DYaNabIR0KG/) |

---

## 🚨 1. The Incident & Attack Vector
Open your browser. Go to your live app. Hit F12.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Assumes happy-path behavior without anticipating edge cases or malicious input. | Enforces defensive validation, isolated boundaries, and fail-safe recovery mechanisms. |

---

## 💡 3. Root Cause & Architectural Principle
Hit F12. Click on sources. Now search for the word key.

---

## ⚡ 4. Hardening Action Checklist
- [ ] The browser is the user's machine.

---

## 💻 5. Hardened Production Implementation
```typescript
// Raw Buffer Webhook Signature Verification
const sig = req.headers['stripe-signature'] as string;
const event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET!);
// Idempotency check:
const isNew = await redis.set(`evt:${event.id}`, '1', 'NX', 'EX', 86400 * 3);
if (!isNew) return res.status(200).json({ received: true });
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Never deploy unverified AI-generated code directly to production without testing failure modes.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Open your browser. Go to your live app. Hit F12. Click on sources. Now search for the word key. If you see your open API key, if you see your Stripe secret key, if you see your database connection screen sitting right there in JavaScript, congratulations. Every single person who visits your app can see it, too. The AI puts the key where the code needs it. It doesn't think about or the code runs. Front-end code ships to the browser, right? The browser is the user's machine. Your secrets are now their secrets. This is important to know cuz someone takes your Stripe key, they're making charges on your account. And my buddy last week, $2500. Someone takes your Open AI key, they're running your bill up to 10,000 bucks while you're sleeping. You didn't get hacked, you left the vault wide open. The fix is coming next week. Follow along so you don't Don't miss it. It's an important one.

</div>
