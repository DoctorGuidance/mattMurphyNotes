# Episode 105: 7 Out of 10 Audits Had API Keys Committed to Client Bundles

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `CRITICAL` |
| **Architectural Domain** | Application Security & Defense (`امنیت نرم‌افزار، حملات و دفاع لایه‌ای`) |
| **Target Production Layer** | Layer 8 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DbgDhezjelJ/) |

---

## 🚨 1. The Incident & Attack Vector
Developers prefix Supabase Service Role keys or OpenAI secrets with `NEXT_PUBLIC_` or `VITE_`. The secret gets compiled directly into the client-side JavaScript bundle, allowing any visitor to open DevTools and obtain full administrative database access.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Prefixes database service-role secrets or private API keys with `NEXT_PUBLIC_` or `VITE_`, leaking admin credentials into client bundles. | Keeps secret API keys strictly on server runtimes, accessing backend services through authenticated server API proxies. |

---

## 💡 3. Root Cause & Architectural Principle
Anything sent to the browser is public knowledge. Never provide client bundles with administrative credentials; keep sensitive operations strictly server-side.

---

## ⚡ 4. Hardening Action Checklist
- [ ] Audit all environment variables: remove `NEXT_PUBLIC_` / `VITE_` prefixes from all administrative keys.
- [ ] Install Trufflehog or git-secrets pre-commit hooks to block secrets from ever entering git history.
- [ ] Immediately rotate any credential that was ever pushed to a public or private repository.

---

## 💻 5. Hardened Production Implementation
```typescript
// .pre-commit-config.yaml
repos:
  - repo: https://github.com/trufflesecurity/trufflehog
    rev: v3.63.7
    hooks:
      - id: trufflehog
        entry: trufflehog git file://. --since-commit HEAD --fail
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** If a secret is in your frontend bundle, it is not a secret—it is a public invitation to your database.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Seven of my last 10 audits had API keys committed to GitHub, database credentials, secret stripe keys, thirdparty service tokens, all of them sitting in a public repository where anyone with a browser can find them. This is not a hypothetical. I saw this in 70% of the apps that we reviewed just last week. Your AI does not know the difference between a config file and an environmental variable. Period. So, puts everything in the code and it pushes everything to that repo. Public, private, it's in there. And here are the three things you direct your AI to fix before someone finds your keys before you do. Number one, move every secret into environmental variables. And verify nothing's hard-coded. Simple as that. Your AI knows how to use files. It will never move your key on its own because it does not think about what happens when code goes public. So direct your AI to scan your entire codebase for hard-coded strings that match API key patterns and then move every one of them into environmental variables. Then verify your MV file is in your.getit ignore file because if it's not, you just moved your keys from one committed file to another committed file. That's not a win. Step two, rotate every key that has ever been committed. If your keys have been in a public repo for even more than an hour, assume they're compromised. cuz they are. It does not matter that you deleted the file. Get history is permanent and being crawled by bots non-stop. Anyone can pull a previous commit and see exactly what you removed. So, direct your AI to generate new keys for every single service. Revoke the old ones and update your environmental variables. The old keys, they're burned. Treat them exactly that way. And step three, install a pre-commit hook that blocks secrets from ever being pushed out again. Your AI can configure tools that scan every commit pattern and what it looks like and stop API keys, tokens, and credentials and reject pushing out before it reaches the repo. This is a 5minut setup that prevents the problem permanently. Without it, you're one careless commit away from doing this all over again. We find this in 70% of the apps we audit. So, do not let yours be the next one. Direct your AI to fix it today.

</div>
