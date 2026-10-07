# Episode 125: Do you have a social proof page on your website

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Frontend Architecture & API Hygiene (`معماری فرانت‌اند، طراحی واسط و بهداشت API`) |
| **Target Production Layer** | Layer 1 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbGGiOKjxe2/) |

---

## 🚨 1. The Incident & Attack Vector
Do you have a social proof page on your website?

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Displays fabricated, static social proof testimonials on marketing pages, destroying customer trust upon inspection. | Renders authentic, verifiable customer metrics and dynamic social proof backed by real customer case studies. |

---

## 💡 3. Root Cause & Architectural Principle
Well, we do. And your name is probably on it. So, here's what we did, why it matters, and how you can build one for your own product.

---

## ⚡ 4. Hardening Action Checklist
- [ ] we collect everything.
- [ ] in the world of AI, social proof might be the number one thing you need because without it, everybody thinks you're full of it.
- [ ] social media comments, product reviews, client feedback, third-party assessments, testimonials from people you've worked with.

---

## 💻 5. Hardened Production Implementation
```typescript
// middleware/rateLimiter.ts
import { RateLimiterRedis } from 'rate-limiter-flexible';
import { redisClient } from '../lib/redis';
import { Request, Response, NextFunction } from 'express';

const limiter = new RateLimiterRedis({
  storeClient: redisClient,
  keyPrefix: 'rl_global',
  points: 10,       // Max 10 requests
  duration: 60,     // Per 60 seconds
  blockDuration: 60 // Block for 60s if exceeded
});

export async function rateLimitMiddleware(req: Request, res: Response, next: NextFunction) {
  try {
    await limiter.consume(req.ip);
    next();
  } catch (err) {
    res.status(429).json({ error: 'Rate limit exceeded. Try again in 60s.' });
  }
}
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Then direct your AI to build one for your product.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Do you have a social proof page running on your website? I know that you don't. Well, we do. And your name is probably on it. So, here's what we did, why it matters, and how you can build one for your own product. Step one, we collect everything. Every comment from every platform constantly. And there are thousands of them. Trust me, there's no way to show thousands of comments to anyone in a very reasonable way, right? So, we curate them down. We take the ones that matter the most for the products that we sell and we align them with those products embedded completely across our entire website. A couple hundred of the strongest statements from real people about what we do and how we do it. And I'm not talking about testimonials in a slider buried at the bottom of a landing page. A full standalone page. That's the process. So collect constantly, curate ruthlessly, and align everything with your products. That's a win. Step two, in the world of AI, social proof might be the number one thing you need because without it, everybody thinks you're full of it. And everybody has an idea. Everybody has a product. And your customer has no way to tell the difference between you and the next person in their feed. If you were a welder last month and today you're trying to sell me advanced AI for voice recognition, how do I connect those two dots? The only way I bridge that gap is if other people are telling me you're the real deal, that you do the work, and that they bought it from you and it was worth it. That's how you figure out if they're the real deal. Proof is the only thing that closes that gap. And step three, social media comments, product reviews, client feedback, third-party assessments, testimonials from people you've worked with. All of it counts. Your AI will build you a product page, a pricing page, and a security page, but it'll never tell you to build the page that makes a stranger trust you enough to buy it. But that page might be the most valuable one on your entire website in the days we're in right now. You can go to the matte.ai website/proof. You can see what we built. Then you can direct your AI to build one for your product. And that is a win.

</div>
