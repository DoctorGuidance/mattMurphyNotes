# Episode 048: You added Sign in with Google. Your AI left the redirect

> **Category:** Authentication & Identity (احراز هویت و مدیریت نشست‌ها)  
> **Production Layer:** Layer 4  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DcwZzLckxZ4/](https://www.instagram.com/reel/DcwZzLckxZ4/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
So, your AI, it added signin with Google to your product, but your AI also left the redirect wide open. So, someone just sent your users a login link that delivers their token to a server you've never even seen. So, your AI, it built ooth flow, right?

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
So, your AI, it built ooth flow, right? Log in with Google, get a token, redirect back to your app. But the redirect, that URL is not locked to your domain.

---

## ⚡ 3. Hardening Action Checklist
- [ ] lock your redirect URL to exact registered URLs. No wild cards, no pattern matching, no open redirects.
- [ ] enforce a state parameter on every OOTH request. The state parameter ties the login request to the user session.
- [ ] scope your token request to the minimum permissions your app actually needs. So if you requested full profile access and your app only needs an email address, every stolen token gives the attacker more than it should.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
// Strict Tenant & User-Scoped Query
const record = await prisma.document.findFirst({
  where: {
    id: req.params.id,
    tenantId: req.user.tenantId // Mandatory tenant isolation
  }
});
if (!record) throw new NotFoundError('Access denied or record not found');
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

So, your AI, it added signin with Google to your product, but your AI also left the redirect wide open. So, someone just sent your users a login link that delivers their token to a server you've never even seen. So, your AI, it built ooth flow, right? Log in with Google, get a token, redirect back to your app. But the redirect, that URL is not locked to your domain. And an attacker crafted a login link that looks exactly like you. So, the token gets redirected to their server instead of yours and your authentication worked perfectly, but it just worked for the wrong person. Let's get that tightened up. Step one, lock your redirect URL to exact registered URLs. No wild cards, no pattern matching, no open redirects. Every OOTH provider gives you a whitelist. If you redirect can point anywhere, your login can be hijacked from anywhere. So, direct your AI to audit every OOTH integration and restrict redirect URLs to exact hard-coded callback URLs registered with each provider. That's a win. Step two, enforce a state parameter on every OOTH request. The state parameter ties the login request to the user session. That's so the callback can verify the flow was initiated by your app and not by an attacker. Without it, anyone can forge an OOTH call call back. So direct your AI to generate a unique cryptographically random state value on every login request and reject any call back where that state does not match. That's also a win. And step three, scope your token request to the minimum permissions your app actually needs. So if you requested full profile access and your app only needs an email address, every stolen token gives the attacker more than it should. So direct your AI to audit every OOTH scope and reduce each to the minimum required for the feature it supports. Your users, they trust that login button, so make sure it only works for them.

</div>
