# Episode 030: Thousands of people scraped your prompt this week and you

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | AI Guardrails, LLM Security & Compliance |
| **Target Production Layer** | Layer 2 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DdKJvRxjm6M/) |

---

## 🚨 1. The Incident & Attack Vector
Thousands of people scraped your prompt this week and you have no idea it happened.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Exposes proprietary system prompts and confidential business logic in client-side code, allowing trivial prompt reverse-engineering. | Encapsulates system prompts behind authenticated backend API proxies, returning only sanitized domain responses to clients. |

---

## 💡 3. Root Cause & Architectural Principle
Someone copies it, runs it, uses your work without credit or payment to you. So, there's no watermark on a text prompt. There is a callback.

---

## ⚡ 4. Hardening Action Checklist
- [ ] embed an outofband call back URL in every prompt.
- [ ] one call back URL per prompt when it fires you know exactly which prompt was copied when it was used and roughly where from right so You are not guessing who is using your work.

---

## 💻 5. Hardened Production Implementation
```typescript
// middleware/cors.ts
import cors from 'cors';

const ALLOWED_ORIGINS = ['https://app.company.com', 'https://portal.company.com'];

export const secureCors = cors({
  origin: (origin, callback) => {
    if (!origin || ALLOWED_ORIGINS.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Blocked by CORS policy: unauthorized origin'));
    }
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
});
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Your prompts are your product. Treat them like it.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Thousands of people scraped your prompts this week, ran them in their builds, and you have no idea that it even happened. So, let's say you publish a prompt, right? Someone copies it, runs it, uses your work without credit or payment to you. So, there's no watermark on a text prompt. There is a callback. And so, OAST gives you a trip wire for your intellectual property if you know how to set it up. So, let's talk about it. Number one, embed an outofband call back URL in every prompt. A unique URL that only resolves when an AI processes that prompt. So it sits in an instruction the AI reads but the user does not see it. If it does not affect the prompt's output, then no one notices it. When someone copies your prompt and runs it, the AI hits that URL every time you get a ping with a timestamp and the origin. I can tell you from experience that the first time you see a call back fire from a prompt you posted two days ago it changes how you think about what you share and what you're going to charge for it right and this is not theoretical I deal with it every single week you guys copy thousands of prompts so entire direc directories exist for scraping prompts number two one call back URL per prompt when it fires you know exactly which prompt was copied when it was used and roughly where from right so You are not guessing who is using your work. You have a full log of it over time. You see all the patterns, which prompts travel, which audiences are copying them, which ones generate the most scraping activity. That data informs you publicly what you need to keep behind your gate, right? And three, the callback is detection, not prevention. You cannot stop someone from copying a text prompt. And by the way, you shouldn't. If you're putting it out there, you want people to use it, but you can know when they did and where they went. Whether you use that for attribution enforcement or just awareness, the data is yours. You can do what you want with it. A prompt without a canary is invisible the moment someone copies it. A prompt with a canary calls home every time and tells you what happened. So, your prompts, they're your product. Treat them like they are.

</div>
