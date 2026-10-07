# Episode 238: Raw AI output should never touch your users

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance (`مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی`) |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZdbRXmv_lb/) |

---

## 🚨 1. The Incident & Attack Vector
Raw AI output should never touch your users.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Streams raw, unvalidated LLM generation directly to frontend users, exposing users to prompt injection leaks and broken formatting. | Validates and parses LLM outputs against strict JSON schemas (Zod) with regex sanitization before rendering in the UI. |

---

## 💡 3. Root Cause & Architectural Principle
Here are the three things you can do right now to fix it. Step one, validate every AI response before it reaches the users. Does it match your expected schema?

---

## ⚡ 4. Hardening Action Checklist
- [ ] validate every AI response before it reaches the users.
- [ ] retry feedback when validation fails.
- [ ] degrade gracefully when retries fail.

---

## 💻 5. Hardened Production Implementation
```typescript
// guardrails/aiAuditTrail.ts
import crypto from 'crypto';
import { db } from '../lib/db';

export async function recordAIGeneration(userId: string, model: string, prompt: string, output: string) {
  const promptHash = crypto.createHash('sha256').update(prompt).digest('hex');
  await db.aiAuditLogs.create({
    data: {
      userId,
      modelName: model,
      promptSha256: promptHash,
      isSyntheticallyGenerated: true,
      timestamp: new Date()
    }
  });
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** در نهایت، اگر اصلاح خودکار نتیجه ندهد، سیستم باید تنزل تدریجی و امن را اجرا کند و با استفاده از روش‌هایی مثل پاسخ‌های از پیش‌ذخیره‌شده یا کمک گرفتن از انسان، از ارائه صفحه خالی یا خطای خام به کاربر جلوگیری کند

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Oh no, your AI model is returning garbage to the users and it will. But your users, they should never have to see it. Here are the three things you can do right now to fix it. Step one, validate every AI response before it reaches the users. Does it match your expected schema? Is it within your length and boundaries? Does it contain prohibited content of some sort? If it fails any of these checks, it does not get through to the users. Most builders are piping raw model output directly to the front end. That works till your model hallucinates a credit card number or returns a 10,000word response to a yes or no question. That's not a win. Step two, retry feedback when validation fails. Do not just error out. Add the failure reason to your retry prompt. Your previous responses have exceeded 200 words, so respond in under 200 words. Give your model a chance to self-correct itself. They usually do. Two or three attempts max, though. That's to win for everyone. Now, step three, degrade gracefully when retries fail. Fall back to a simpler model, a cached response, or a human handoff. The user should get a usable experience when the AI fails. Never show a raw error, never show a blank screen of death. So, validate, retry, degrade. Build it once, use it everywhere. That's a best practice. So, what happens now when your app when the AI response is bad? What do you do? Drop it in the comments.

--------------------------------------------------
[NOTEBOOKLM GUIDE & TOPICS]
متن ارائه‌شده بر ضرورت محافظت از کاربران در برابر خروجی‌های نامشخص و آشفته هوش مصنوعی تأکید می‌کند و سه گام عملی برای این منظور پیشنهاد می‌دهد. نخستین گام، اعتبارسنجی دقیق پاسخ‌ها پیش از نمایش به کاربر است تا اطمینان حاصل شود که محتوا با ساختار و محدودیت‌های مورد انتظار مطابقت دارد. در صورت بروز خطا، دومین گام یعنی تلاش مجدد هوشمند به کار گرفته می‌شود که با بازگرداندن دلیل خطا به مدل، فرصتی برای اصلاح اشتباه به آن می‌دهد. در نهایت، اگر اصلاح خودکار نتیجه ندهد، سیستم باید تنزل تدریجی و امن را اجرا کند و با استفاده از روش‌هایی مثل پاسخ‌های از پیش‌ذخیره‌شده یا کمک گرفتن از انسان، از ارائه صفحه خالی یا خطای خام به کاربر جلوگیری کند.

</div>
