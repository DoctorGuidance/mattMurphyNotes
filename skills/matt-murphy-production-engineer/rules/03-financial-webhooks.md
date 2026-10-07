# 💳 Rule 03: Financial Webhooks, Payments & Idempotency

> **Based on Matt Murphy Masterclasses:** Episodes 006, 022, 103

---

## 1. Raw Buffer Webhook Signature Verification (Lesson 006)
- Stripe signatures cannot be validated on parsed JSON objects because body-parsers reformat whitespace and keys.
- Always mount raw body buffer parser on webhook routes:

```typescript
// server.ts (Express example)
app.post(
  '/api/webhooks/stripe',
  express.raw({ type: 'application/json' }),
  async (req, res) => {
    const sig = req.headers['stripe-signature'] as string;
    let event: Stripe.Event;

    try {
      event = stripe.webhooks.constructEvent(
        req.body, // Must be Buffer!
        sig,
        process.env.STRIPE_WEBHOOK_SECRET!
      );
    } catch (err: any) {
      return res.status(400).send(`Webhook Signature Verification Failed: ${err.message}`);
    }

    // Process event idempotently...
  }
);
```

---

## 2. Idempotency Key Guardrail
- Webhooks can be retried up to 72 hours by payment gateways on network timeout.
- Every state change (credits grant, subscription activation) must check and lock an idempotency key:

```typescript
const isNew = await redis.set(`webhook:event:${event.id}`, 'processed', 'NX', 'EX', 86400 * 3);
if (!isNew) {
  // Event was already processed; safely acknowledge with HTTP 200 without duplicate action
  return res.status(200).json({ received: true, duplicate: true });
}
```
