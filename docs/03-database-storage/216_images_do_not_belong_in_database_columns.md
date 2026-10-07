# Episode 216: Images do not belong in database columns

| Parameter | Specification |
|:---|:---|
| **Production Risk Severity** | 🚨 `MEDIUM` |
| **Architectural Domain** | Database & Storage Engineering (`پایگاه‌داده، روابط، ایندکس و پایداری داده`) |
| **Target Production Layer** | Layer 3 |
| **Official Video Source** | [Watch Reel on Instagram](https://www.instagram.com/reel/DZxfOW9xsFD/) |

---

## 🚨 1. The Incident & Attack Vector
Images do not belong in database columns.

---

## ❌ 2. Vibe-Coding Trap vs. Production Reality

| ❌ The Vibe-Coding Trap (Common Mistake) | ✅ Hardened Production Standard |
|:---|:---|
| Stores image binaries or large base64 blobs directly in database tables, bloating storage and exhausting buffer pool memory. | Offloads media assets to dedicated S3/Object Storage with CDN edge distribution, storing only normalized URLs/keys in the database. |

---

## 💡 3. Root Cause & Architectural Principle
Your database is now doing two jobs it was never designed to do at the exact same time. Here are the three things you're going to do to your database right now to fix it. Step one, move files out of the database.

---

## ⚡ 4. Hardening Action Checklist
- [ ] move files out of the database.
- [ ] serve files from a CDN.
- [ ] separate your data model completely.

---

## 💻 5. Hardened Production Implementation
```typescript
// middleware/cors.ts
import cors from 'cors';

const ALLOWED_ORIGINS = ['https://app.company.com', 'https://portal.company.com'];

export const secureCors = cors({
  origin: (origin, callback) => {
    if (!origin || ALLOWED_ORIGINS.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Blocked by CORS policy: unauthorized origin'));
    }
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
});
```

---

## 🌟 6. Golden Takeaway
> [!TIP]
> **Production Heuristic:** Object storage exists for a reason.

---

## 🎧 7. Exact Word-for-Word Audio Transcript
<div dir="ltr">

Your users are uploading images. You store them in the database. Your database is now doing two jobs it was never designed to do at the exact same time. Here are the three things you're going to do to your database right now to fix it. Step one, move files out of the database. Images, PDFs, videos. None of these belong in a database column. They belong in object storage. Object storage is built for these files specifically. Databases are built for rows. Mixing them is how a $200 a month database becomes an $800 a month database. No reason at all. Step two, serve files from a CDN. When someone loads a profile picture, that request should never hit your origin server. It should hit the CDN node closest to your end user. Faster delivery, lower bandwidth cost. The user gets the file in milliseconds instead of seconds. You know what? That's a win. Step three, separate your data model completely. Your database stores a URL that points to the file, not the file itself. A string column instead of a blob column holding 10 megabytes. This is not optimization. This is the standard and the way you should be building. Every production system separates storage from data. The ones that don't just haven't hit the wall yet. So, make sure you store smart for the win every time.

</div>
