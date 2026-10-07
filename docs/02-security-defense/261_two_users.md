# Episode 261: Two users

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZFdS70R9Pv/) |

---

## 🚨 1. The Incident & Attack Vector
Two users edit the same document at the same time. One saves, then the other saves, and the first user's changes completely vanish. Congratulations, you built a data loss machine.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Relies on unverified AI code assumptions without failure handling or production boundaries in Application Security & Defense. | Applies hardened architectural patterns, strict input boundaries, and automated monitoring for Application Security & Defense. |

---

## 💡 3. Root Cause & Architectural Principle
Congratulations, you built a data loss machine. Here are the three things you can do right now to fix it. Step one, choose your conflict resolution strategy before you write a single line of code.

---

## ⚡ 4. Hardening Action Checklist
- [ ] choose your conflict resolution strategy before you write a single line of code.
- [ ] for collaborative features implement operational transforms or CRDTS.
- [ ] for structured data, use event sourcing.

---

## 💻 5. Hardened Production Implementation
```typescript
// lib/logger.ts
import winston from 'winston';

export const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  defaultMeta: { service: 'api-gateway', env: process.env.NODE_ENV },
  transports: [
    new winston.transports.Console()
  ]
});
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** The patterns that make it work.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Two users edit the same document at the same time. One saves, then the other saves, and the first user's changes completely vanish. Congratulations, you built a data loss machine. Here are the three things you can do right now to fix it. Step one, choose your conflict resolution strategy before you write a single line of code. Last right wins is always the simplest. Time stamp on mutation. Latest time AMP takes priority. It works for low collaboration apps, things like settings pages and user profiles. Unfortunately, for dynamic documents or shared state, last write wins destroys data silently. So, step two for collaborative features implement operational transforms or CRDTS. CRDTs are conflict-free replicated data types. They merge automatically without a central server. YJS is the library. It gives you the collaborative text editing, shared arrays, and maps. Plug it into Superbase Realtime or Websocket Server. Users see each other's changes instantly. Conflicts resolve mathematically. No human intervention needed. Step three, for structured data, use event sourcing. Do not store the current state. Store every change as an immutable event. User A changed field X to Y at time stamp t. Then user B. Change field X to Z at time stamp T + 1. Your application replays events in order. So conflicts become visible, resolvable, and auditable. Last right wins for simple data, CRDTS for collaborative editing, and event sourcing for business logic. So tell me, what are you building right now that needs real time sync? I want to hear about it in the comments.

</div>
