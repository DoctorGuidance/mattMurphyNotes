# Episode 010: Last week I showed you the software

> **Category:** Cloud Infrastructure & FinOps (معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه)  
> **Production Layer:** Layer 6  
> **Official Instagram Reel:** [https://www.instagram.com/reel/DdpDWXlD-Nn/](https://www.instagram.com/reel/DdpDWXlD-Nn/)  

---

## 🚨 1. Problem Statement & Failure Vector (From Voice Transcript)
Last week, I showed you my default VPS stack software, nine components, most of them totally free. This week, I'm showing you what it runs on, as well as a few builder stacks from my comments. For example, one commenter is running a Mac Studio with two 3090s as a secondary node, running Quen locally, handling enterprise workloads without a single cloud API call.

---

## 💡 2. Root Cause & Architectural Solution (Matt Murphy Analysis)
For example, one commenter is running a Mac Studio with two 3090s as a secondary node, running Quen locally, handling enterprise workloads without a single cloud API call. No subscription, no usage fees, no data data leaving his building at All that's totally a win. Another member is running 4090s.

---

## ⚡ 3. Hardening Action Checklist
- [ ] Apple Silicon runs inference efficiently because memory is unified.
- [ ] And the used market for 3090s has totally collapsed.

---

## 💻 4. Hardened Implementation Code / Config
```typescript
# Docker Compose Network Segmentation
networks:
  frontend_net:
  backend_net:
    internal: true # No direct internet access
services:
  marketing:
    networks: [frontend_net]
  database:
    networks: [backend_net] # Isolated from marketing container
```

---

## 🎧 5. Exact Spoken Audio Transcript (Word-for-Word)
<div dir="ltr">

Last week, I showed you my default VPS stack software, nine components, most of them totally free. This week, I'm showing you what it runs on, as well as a few builder stacks from my comments. For example, one commenter is running a Mac Studio with two 3090s as a secondary node, running Quen locally, handling enterprise workloads without a single cloud API call. No subscription, no usage fees, no data data leaving his building at All that's totally a win. Another member is running 4090s. Another's pricing B300's right now. So VPS is clearly here to stay and you guys want to talk about it. Here's what the local inference setup actually looks like. A Mac Studio with an M series chip handles small to mid-range models natively. Apple Silicon runs inference efficiently because memory is unified. So a model that fits in 64 128 gigs of unified memory runs without the complexity of GPU clusters. That's a tidy setup for sure. For heavier workloads, add Nvidia, right? A 3090 with 24 GB of VRAM handles 13 billion parameter models. Two of them, 30 billion. A 4090 runs those same models, but faster. And the used market for 3090s has totally collapsed. Enterprisegrade inference hardware for the price of a business class flight. Go check it out. It's totally a win. The VPS I shared from last last week still works for teams that do not want to rack hardware, but many of the people in my comments are totally past that. They want the model on their desk, in their office, on their network, and nowhere else. I get it. And the cost comparison has totally flipped. A year of API calls to a Frontier provider costs more than the hardware that replaces it permanently. And the hardware does not raise its price every quarter. So, your prompts, those are your IP. Last week, I told you to keep them off of someone else's server. This week, I'm telling you what to run them on. So, get out there and build something.

</div>
