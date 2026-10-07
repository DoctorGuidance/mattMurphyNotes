# Episode 147: Six documents before your first paying user

> **Category:** Cloud Infrastructure & FinOps (معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه)  
> **Production Layer:** Layer 6  
> **Official Instagram Reel:** [https://www.instagram.com/reel/Davh5IQjRBY/](https://www.instagram.com/reel/Davh5IQjRBY/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Your product's ready, your first customers are ready to pay, but before you accept a single payment, you want these six documents in place in your business or you're going to end up exposed. Doc number one, terms of service. You know that one that no one reads.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
You know that one that no one reads. Well, that's the one that defines what your users can and cannot do, what you are liable and not liable for, and what happens when things go wrong. Your AI can draft it, but you need to direct it with your specific use.

---

## ⚡ 3. Hardening Action Checklist
- [ ] terms of service. You know that one that no one reads.
- [ ] privacy policy. This tells users what data you collect and how you use it and how they request deletion from it.
- [ ] data processing agreement, a DPA. If you process data on behalf of another business, a DPA defines who is responsible for what.
- [ ] is a refund policy. What happens when a customer wants their money back?
- [ ] this one's big. Master service agreement.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Hardened Production Configuration - Episode #147
// Domain: 11-cloud-finops
export function enforceProductionGuardrail(context: Record<string, unknown>) {
  // Enforce Matt Murphy #147 invariants:
  if (!context.validated) {
    throw new Error('Production guardrail triggered: Review Masterclass #147');
  }
  return true;
}
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Your product's ready, your first customers are ready to pay, but before you accept a single payment, you want these six documents in place in your business or you're going to end up exposed. Doc number one, terms of service. You know that one that no one reads. Well, that's the one that defines what your users can and cannot do, what you are liable and not liable for, and what happens when things go wrong. Your AI can draft it, but you need to direct it with your specific use. case for your product, all of your data practices and your liability boundaries. A template you download from the internet protects nobody at all. Doc number two, privacy policy. This tells users what data you collect and how you use it and how they request deletion from it. If your policy says one thing and your app does another, you have a compliance violation. Not a technicality, but a sizable fine if you don't get it right. Doc number three, data processing agreement, a DPA. If you process data on behalf of another business, a DPA defines who is responsible for what. GDPR absolutely requires it. Enterprise customers will ask for it every single time. Doc number four is a refund policy. What happens when a customer wants their money back? Payment processors, they require it. Customer trust absolutely depends on it. Doc number five, this one's big. Master service agreement. If you were selling your system to a company that's going to use it. The MSA defines how you support it. SLAs's, uptime guarantees, response times, and what happens when something breaks. The MSA governs the relationship between your product and their business. It's a big deal. And doc six, it's optional, but it's important. Cyber liability insurance. When you handle someone else's data and something goes wrong, you will end up personally liable, not your LLC. I've corrected it in plenty of comments. Most Policies cost $200 to $600 a year and $200 to protect what could be a $50,000 problem. That's a big deal. Not everyone needs it on day one. I get it. But the moment you handle customer data at scale, the coverage protects what the documents alone cannot. So those six documents, none of them are code. All of them protect the business and the product underneath the code. Your AI can draft every single one of them for you, but only if you know what to ask for. Now you do.

</div>
