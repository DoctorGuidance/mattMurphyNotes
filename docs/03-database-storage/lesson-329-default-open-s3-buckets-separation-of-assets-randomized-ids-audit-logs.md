# Masterclass #329: Default Open S3 Buckets: Separation of Assets, Randomized IDs & Audit Logs

**Module**: `Database & Storage Engineering` | **Layer**: `Layer 03` | **Severity**: `CRITICAL`

---

## 🚨 Problem Statement
AI tools configure single cloud storage buckets with public-read permissions to bypass upload errors, unintentionally exposing database backups, private user exports, and system configs to automated internet crawlers.

### تشریح به زبان فارسی
هوش مصنوعی برای حل خطاهای آپلود، پرمیشن باکت S3 را روی عمومی (Public Read) می‌گذارد و بک‌آپ‌های دیتابیس و داده‌های کاربران را در کنار تصاویر عمومی ذخیره می‌کند که باعث افشای کل اطلاعات می‌شود.

---

## 🔍 Root Cause Analysis
Mixing public media and confidential backups in the same storage container, using predictable bucket names (company-backups), and omitting server access logging.

### ریشه خطا به فارسی
ترکیب فایل‌های عمومی و بک‌آپ‌های حساس در یک باکت، استفاده از نام‌های قابل پیش‌بینی برای باکت و عدم فعال‌سازی لاگینگ دسترسی سرور.

---

## ⚖️ Production Comparison Matrix
| Architectural Dimension | Vibe Coding Anti-Pattern (Trap) | Production Engineering Standard (Verified) |
| :--- | :--- | :--- |
| **Operational Standard** | Creating a single public bucket for both user images and DB backups with predictable names like company-backups. | Dual-bucket topology: public CDN bucket for static media + private bucket with expiring pre-signed URLs (TTL < 15m) and access logging. |
| **تحلیل استاندارد فارسی** | استفاده از یک باکت پابلیک واحد برای تصاویر و بک‌آپ‌های دیتابیس با نام‌های قابل حدس مانند company-backups. | توپولوژی دوباکتی: باکت استاتیک عمومی CDN برای تصاویر + باکت کاملاً خصوصی با لینک موقت انقضادار (زیر ۱۵ دقیقه) و ثبت تمام لاگ‌ها. |

---

## 🛠️ Step-by-Step Action Plan
1. Segregate storage into strictly separated buckets: public CDN assets vs. private air-gapped data served exclusively via expiring pre-signed URLs.
1. Apply high-entropy randomized suffixes to all bucket identifiers (e.g. `data-7f9a2b8e4c1d`) to prevent dictionary enumeration attacks.
1. Enable S3/GCS Server Access Logging and real-time CloudWatch/Alertmanager triggers on suspicious egress volumes and anomalous IP ranges.

### گام‌های عملیاتی فارسی
- تفکیک کامل باکت‌ها: نگهداری تصاویر در باکت عمومی و انتقال بک‌آپ‌ها به باکت خصوصی با دسترسی منحصراً از طریق لینک‌های امضاشده موقت (Pre-signed URLs).
- استفاده از شناسه‌های تصادفی با آنتروپی بالا برای نام باکت‌ها جهت مهار حملات پویش خودکار و کشف نام.
- فعال‌سازی لاگ دسترسی سرور (Server Access Logging) و هشدارهای بلادرنگ برای حجم دانلود غیرعادی یا دسترسی از آی‌پی‌های مشکوک.

---

## 💻 Hardened Production Code Pattern
```typescript
// PRODUCTION STANDARD: Secure Pre-Signed URL Generator for Private Assets
import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';
import { getSignedUrl } from '@aws-sdk/s3-request-presigner';

const s3 = new S3Client({ region: process.env.AWS_REGION });
const PRIVATE_BUCKET = process.env.RANDOMIZED_PRIVATE_BUCKET_ID!; // e.g. 'vault-8f3a9e2c'

export async function generateSecureDownloadUrl(fileKey: string, tenantId: string): Promise<string> {
  // Enforce tenant isolation in the key prefix
  const fullKey = `tenants/${tenantId}/${fileKey}`;
  const command = new GetObjectCommand({ Bucket: PRIVATE_BUCKET, Key: fullKey });
  // Short-lived pre-signed URL: strictly 15 minutes TTL
  return await getSignedUrl(s3, command, { expiresIn: 900 });
}
```

---

## 🎙️ Word-for-Word Audio Transcript
> "Your AI needed a place to store file uploads. So, it created an S3 bucket, a Google Cloud Storage bucket, or an Azure blob container, right? It set the permissions to public so the application could serve files without authentication errors. The uploads work, so does every unauthorized download. You don't want me to tell you what an attacker did, but they just downloaded your entire user database from a cloud storage bucket you forgot was public. So, your AI created the bucket with default permissions like they all do. Default means wide open and open means everyone gets in. So let's lock it down. Step one, your AI created a storage bucket and set the access control to public read because the application needed to serve images. But the same bucket also stores database backups, user exports, and configuration files. So any attacker who finds the bucket URL downloads everything in it. So, direct your AI to separate public assets from private data into different buckets. Public assets get public read. Everything else gets private with pre-signed URLs that expire. That is a win. Step two, your bucket name is predictable. Company name-uploads, company name-backups. So, attackers, they enumerate common naming patterns and scan for open buckets at scale all day long. So direct your AI to use randomized bucket names that do not contain your company name, an environment name, or a data purpose. And step three, your AI never enabled access logging on your bucket. So an attacker has been downloading files for weeks and you have no record of it at all. No IP addresses, no timestamps, no file access history. So direct your AI to enable server access logging and configure alerts for unusual download code patterns or access from unexpected IP ranges. Your cloud storage should store your data and not serve it to anyone who asks for it. Get it tied up."

---

## 💡 Golden Takeaway
> **"Your cloud storage should store data, not serve it to anyone who asks: isolate public assets from private records, randomize bucket identifiers, and enforce expiring pre-signed URLs."**
>
> *فضای ذخیره‌سازی ابری باید حافظ داده باشد نه توزیع‌کننده آن به عموم؛ داده‌های حساس را با لینک‌های موقت محافظت کنید، نام باکت‌ها را غیرقابل حدس بسازید و لاگ‌ها را پایش نمایید.*
