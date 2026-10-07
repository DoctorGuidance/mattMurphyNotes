# 🤖 Rule 05: AI Guardrails, EU AI Act & Generation Logs

> **Based on Matt Murphy Masterclasses:** Episodes 001, 008, 012, 013, 106, 108, 110, 111, 114, 115

---

## 1. Synthetic Generated Information (SGI) Disclosure (Lesson 001)
Under the EU AI Act:
- Any content generated or modified by AI models must be disclosed to users.
- Add visible UI badges ("تولیدشده توسط هوش مصنوعی" / "AI-Generated") and embed metadata tags in images and documents.

---

## 2. Immutable Generation Audit Trail
All LLM generation endpoints must persist an immutable audit log:

```typescript
interface AIGenerationAuditRecord {
  id: string;
  timestamp: string;
  userId: string;
  modelIdentifier: string; // e.g. "gemini-2.5-pro", "gpt-4o"
  promptTokens: number;
  completionTokens: number;
  promptHash: string;      // SHA-256 of the prompt (for privacy + reproducibility)
  isSyntheticallyGenerated: true;
}
```

---

## 3. Strict Token Budget Ceilings (FinOps)
- Never allow open-ended generation streams without setting explicit `max_tokens` / `maxOutputTokens`.
- Enforce daily cost limits per user or API key to prevent runaway cloud bills.
