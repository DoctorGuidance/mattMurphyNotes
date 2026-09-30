<p align="center">
  <img src="banner.svg" alt="Matt Murphy AI - Coming Soon" width="100%">
</p>

# 🧠 Matt Murphy AI Notes & Agent Skills `[COMING SOON ⏳]`

> **Bridging the chasm between "Vibe Coding" and hardened, scalable, enterprise-grade production engineering.**

[![Status: Coming Soon](https://img.shields.io/badge/Status-COMING%20SOON-f59e0b?style=for-the-badge&logo=git&logoColor=white)](#)
[![Stack: 13 Production Layers](https://img.shields.io/badge/Architecture-13%20Production%20Layers-2ed573?style=for-the-badge)](#)
[![Target: AI Agents](https://img.shields.io/badge/Platform-Antigravity%20%7C%20Cursor%20%7C%20Claude-ff4757?style=for-the-badge&logo=openai&logoColor=white)](#)
[![Archive: 320+ Reels](https://img.shields.io/badge/Catalog-320%2B%20Masterclasses-00d2ff?style=for-the-badge)](#)

> [!IMPORTANT]
> 🚧 **PRE-RELEASE NOTICE (COMING SOON):**  
> This repository is currently in active staging. The complete library of modular **Agent Skills (`SKILL.md`)**, system architecture checklists, and production playbooks synthesized from **320+ Matt Murphy masterclasses** will be published here in the coming days. **Star or watch this repository** to get notified on release day!

---

## 🧭 Overview

In the era of generative AI, shipping an MVP is instantaneous—but scaling it to hundreds of thousands of users without security breaches, runaway cloud bills, or database lockups is an entirely different discipline.

This repository codifies the battle-tested architectural principles, hardening checklists, and systems engineering frameworks shared by **Matt Murphy** ([@mattmurphyai](https://www.instagram.com/mattmurphyai) / [mattmurphy.ai](https://mattmurphy.ai)).

Rather than passive notes, this project translates **320+ technical breakdowns** into modular, executable **Agent Skills**—designed to be directly ingested by modern AI programming environments (**Google Antigravity**, **Cursor**, **Claude Code**, **Windsurf**, and autonomous multi-agent swarms).

```
   ┌─────────────────────────────────────────────────────────────┐
   │                     "VIBE CODING" (Day 1)                   │
   │           Fast Prototypes • AI Scaffolding • Fast Demos      │
   └──────────────────────────────┬──────────────────────────────┘
                                  │
                                  ▼
                 [ 🧠 Matt Murphy Production Guardrails ]
                                  │
   ┌──────────────────────────────┴──────────────────────────────┐
   │                HARDENED PRODUCTION (Day 30+)                │
   │   13-Layer Stack • RLS • Connection Pooling • Zero Leaks    │
   └─────────────────────────────────────────────────────────────┘
```

---

## 🏛️ The 13 Production Layers Architecture

A core pillar of Matt Murphy’s methodology is treating modern software as an interdependent **13-layer platform**:

| Layer | Domain | Critical Production Focus |
|:---:|:---|:---|
| **01** | **UI & Accessibility** | Layout thrashing prevention, keyboard navigation, contrast, WCAG. |
| **02** | **APIs & Logic** | Display layer $\ne$ trust layer; strict server-side business validation. |
| **03** | **Database & Storage** | Normalization, indexing strategies, zero blobs in DB tables. |
| **04** | **Auth & Permissions** | Secure HttpOnly cookies (never `localStorage`), short-lived tokens, PKCE. |
| **05** | **Staging & Deployments** | Canary releases, zero direct-to-main pushes, feature flags. |
| **06** | **Cloud & Compute** | Serverless timeouts, async worker queues, cloud cost guardrails. |
| **07** | **CI/CD & Pipelines** | Automated regression gates, one-click rollbacks, sealed builds. |
| **08** | **Security & RLS** | Database-level Row-Level Security, zero service-role keys in clients. |
| **09** | **Rate Limiting** | Three-tier protection (DoS hard limits, adaptive load, tier quotas). |
| **10** | **Caching & CDN** | Multi-tenant scope keys, deterministic invalidation, edge distribution. |
| **11** | **Connection Pooling** | PgBouncer/Supavisor, handling high-concurrency connection spikes. |
| **12** | **Observability & Logs** | Structured JSON tracing, correlation IDs, proactive alerting. |
| **13** | **Disaster Recovery** | Point-in-time recovery (PITR), tested restore runbooks, failovers. |

---

## 📂 Repository Blueprint

```text
mattMurphyNotes/
├── skills/                     # Executable AI Agent Skills (SKILL.md)
│   ├── production-stack/       # 13-layer rules & architectural constraints
│   ├── auth-and-security/      # RLS, token protection, and anti-leak rules
│   ├── database-scaling/       # Query optimization, indexes & connection pools
│   └── agent-orchestration/    # Task routing, prompt defenses & memory hygiene
├── playbooks/                  # Human-readable engineering checklists
│   ├── pre-launch-checklist.md # 47-point pre-deploy verification
│   └── cost-optimization.md    # API batching, caching & model tiering
└── archive/                    # Extracted transcripts, hooks & metadata
    └── index.json              # 320+ categorized episodes with source links
```

---

## 🚀 How to Use These Skills with AI Coding Assistants

### 1. In Google Antigravity
Copy any skill folder into your project's `.gemini/skills/` directory:
```bash
cp -r skills/production-stack/ .gemini/skills/
```

### 2. In Cursor IDE
Add relevant skills to your `.cursorrules` or `.cursor/rules/`:
```bash
cat skills/auth-and-security/SKILL.md >> .cursorrules
```

### 3. In Claude Code / Windsurf
Reference the guidelines directly in your project prompt or workspace context file.

---

## 🗺️ Roadmap & Milestones

- [x] **Phase 1: Knowledge Extraction** — 322 episodes cataloged, metadata extracted, and high-fidelity audio archived.
- [ ] **Phase 2: Taxonomy & Topic Clustering** — Grouping episodes into the 13 architectural layers and core operational domains.
- [ ] **Phase 3: Skill Codification** — Authoring production-ready `SKILL.md` documents with clear input/output contracts.
- [ ] **Phase 4: Multi-Agent Evaluation Suite** — Autonomous testing to verify that AI agents adhere to Matt Murphy’s guardrails.

---

## 🤝 Attribution & Disclaimer

* All architectural concepts and insights are synthesized from educational materials published by **Matt Murphy** (Founder & CEO of Faction Group, author of *Not Murphy's Law*).
* Visit his official platform for masterclasses and deep dives: **[mattmurphy.ai](https://mattmurphy.ai)**.
* This repository is an independent open-source synthesis maintained by the community for AI builders and operators.

---

<div align="center">
  <sub>Maintained with precision by <a href="https://github.com/DoctorGuidance">@DoctorGuidance</a> • Built for builders who ship to production.</sub>
</div>
