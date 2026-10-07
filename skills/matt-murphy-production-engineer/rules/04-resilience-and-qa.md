# 🧪 Rule 04: The 4 UI States, Error Budgets & Parity

> **Based on Matt Murphy Masterclasses:** Episodes 205, 289, 291, 294, 295, 300

---

## 1. The 4 Essential UI States (Lesson 289, 291)
Never render components that assume API calls always succeed instantly. Every async view must handle:
1. **Loading State:** Skeleton screen or indicator without freezing the main thread.
2. **Error State:** Human-friendly explanation with a retry button (`onRetry()`).
3. **Empty State:** Actionable prompt when zero records exist (no blank void).
4. **Success State:** Properly typed, responsive view.

```tsx
// React Example:
export function DashboardMetrics({ data, isLoading, error, refetch }: Props) {
  if (isLoading) return <MetricsSkeleton />;
  if (error) return <ErrorState message="خطا در دریافت داده‌ها" onRetry={refetch} />;
  if (!data || data.length === 0) return <EmptyState message="هنوز تراکنشی ثبت نشده است" actionText="ثبت اولین تراکنش" />;
  return <MetricsGrid data={data} />;
}
```

---

## 2. Dev / Staging / Prod Parity (Lesson 294)
- Never use SQLite in development if PostgreSQL is used in production.
- Keep environment secrets isolated across `.env.development`, `.env.staging`, and secure cloud secret managers.
- No direct commits to `main` branch. Require Pull Request reviews and passing CI checks.
