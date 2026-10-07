#!/usr/bin/env python3
"""
Bespoke matrices for Part 1:
Modules:
- 01-auth-identity (30 episodes)
- 02-security-defense (47 episodes)
- 03-database-storage (33 episodes)
- 04-caching-performance (12 episodes)
- 05-rate-limiting-abuse (4 episodes)
- 06-observability-logs (16 episodes)
Total: 142 episodes
"""

PART1_DATA = {
    # ==========================================
    # 01-AUTH-IDENTITY (30 episodes)
    # ==========================================
    "040": (
        "Accepts unrestricted request body payloads in user update endpoints, enabling privilege escalation via `isAdmin: true` mass assignment.",
        "Enforces strict Zod schema whitelisting on update endpoints and strips sensitive role/permission fields at the controller layer.",
        "پذیرش کلیه فیلدهای ارسالی در بدنه درخواست که امکان ارتقای دسترسی کاربر به ادمین را با ارسال `isAdmin: true` فراهم می‌کند.",
        "اعمال اسکیماهای سخت‌گیرانه با Zod، حذف فیلدهای حساس دسترسی در کنترلر و تفکیک کامل اندپوینت‌های عادی از مدیریتی."
    ),
    "043": (
        "Stores JWT authentication tokens in browser LocalStorage, leaving sessions vulnerable to complete theft via Cross-Site Scripting (XSS).",
        "Stores authentication tokens exclusively in HttpOnly, Secure, SameSite=Lax cookies completely inaccessible to JavaScript.",
        "ذخیره توکن‌های احراز هویت در LocalStorage مرورگر که نشست کاربر را در معرض سرقت کامل از طریق حملات XSS قرار می‌دهد.",
        "انتقال توکن‌های احراز هویت به کوکی‌های امن با فلگ‌های HttpOnly، Secure و SameSite=Lax بدون امکان دسترسی توسط جاوااسکریپت."
    ),
    "044": (
        "Fetches user records directly by sequential URL parameters (`/api/users/:id`) without validating requesting user ownership (IDOR).",
        "Enforces ownership verification on every database query (`where: { id, tenantId, userId }`) and replaces sequential IDs with UUIDv4.",
        "واکشی رکوردهای کاربری مستقیماً بر اساس شناسه عددی موجود در آدرس URL بدون احراز مالکیت درخواست‌دهنده (آسیب‌پذیری IDOR).",
        "بررسی اجباری مالکیت در تمامی کوئری‌های پایگاه‌داده و جایگزینی شناسه‌های ترتیبی با شناسه‌های تصادفی UUIDv4."
    ),
    "048": (
        "Accepts unvalidated `returnTo` redirect destinations after Google OAuth login, enabling phishing redirection attacks.",
        "Validates post-authentication redirect URLs against a strict domain whitelist and enforces PKCE state parameters.",
        "پذیرش آدرس‌های ریدایرکت تاییدنشده پس از ورود با گوگل که کاربران را به صفحات فیشینگ هدایت می‌کند.",
        "اعتبارسنجی دقیق آدرس مقصد ریدایرکت با لیست سفید دامنه‌ها و استفاده از پارامترهای ضدجعل PKCE State."
    ),
    "050": (
        "Embeds third-party chat widgets directly in the main DOM, allowing unverified scripts to read authenticated session state.",
        "Isolates third-party widgets inside sandboxed iframes with restricted permissions and zero direct access to parent cookies.",
        "قراردادن ویجت‌های پشتیبانی شخص‌ثالث مستقیماً در صفحه اصلی که به اسکریپت‌ها اجازه دسترسی به نشست کاربر را می‌دهد.",
        "قراردادن ویجت‌های کمکی درون آی‌فریم‌های ایزوله (Sandboxed Iframe) بدون دسترسی مستقیم به کوکی‌ها و توکن‌های اصلی."
    ),
    "052": (
        "Deploys internal administrative dashboards without authentication, assuming security through obscure unguessable URLs.",
        "Enforces enterprise Single Sign-On (SSO), mandatory hardware MFA, and IP-restricted VPN gateways for all administrative tools.",
        "انتشار پنل‌های مدیریت داخلی بدون احراز هویت به امید اینکه کسی آدرس محرمانه صفحه را پیدا نخواهد کرد.",
        "اجبار احراز هویت چندعاملی (MFA)، سامانه ورود یکپارچه سازمانی و محدودسازی دسترسی بر اساس شبکه اختصاصی VPN."
    ),
    "067": (
        "Spawns direct database session queries for every user request during traffic surges, crashing under authentication connection saturation.",
        "Caches validated session tokens in distributed Redis clusters with 60-second TTLs to shield the database from connection spikes.",
        "اجرای کوئری مستقیم روی دیتابیس برای تایید هر نشست در زمان هجوم ترافیک که موجب قطعی کامل سرویس به دلیل پر شدن اتصالات می‌شود.",
        "کش کردن توکن‌های نشست تاییدشده در ردیس با مدت اعتبار ۶۰ ثانیه جهت محافظت از دیتابیس در برابر هجوم ترافیک."
    ),
    "090": (
        "Launches authentication flows without telemetry, remaining blind to user drop-offs and broken third-party OAuth providers.",
        "Instruments conversion funnels and automated alerts on authentication failure spikes across all social login providers.",
        "انتشار سیستم لاگین بدون ابزارهای تله‌متری که تیم را از ریزش کاربران و قطعی ارائه‌دهندگان OAuth بی‌خبر می‌گذارد.",
        "پایش نرخ تبدیل و ایجاد هشدارهای بلادرنگ در صورت افزایش ناگهانی خطاهای ورود در هر یک از ارائه‌دهندگان اجتماعی."
    ),
    "118": (
        "Selects identity providers solely on free-tier limits without evaluating data exportability or custom domain SSO capabilities.",
        "Selects auth providers based on tenant isolation, SAML/OIDC compliance, and zero-downtime user credential export policies.",
        "انتخاب ارائه‌دهنده هویت صرفاً به خاطر پلن رایگان بدون ارزیابی قابلیت خروجی گرفتن داده‌ها و امکان اتصال SSO سازمانی.",
        "ارزیابی ارائه‌دهندگان احراز هویت بر اساس ایزولاسیون سازمان‌ها، پشتیبانی از استانداردهای SAML/OIDC و خروجی کامل اطلاعات."
    ),
    "124": (
        "Issues long-lived session tokens that never expire, leaving accounts vulnerable if client devices are lost or stolen.",
        "Enforces rotating refresh tokens with 7-day idle timeouts, 30-day absolute expirations, and remote session revocation.",
        "صدور توکن‌های نشست دائمی و بدون انقضا که در صورت سرقت یا گم شدن دستگاه کاربر دسترسی را باز می‌گذارد.",
        "استفاده از رفرش‌توکن‌های چرخشی با انقضای ۷ روزه در صورت عدم فعالیت و قابلیت ابطال سراسری نشست‌ها از راه دور."
    ),
    "136": (
        "Forces lengthy multi-step registration forms upfront, causing 70% of prospective users to abandon the authentication funnel.",
        "Adopts progressive profiling with frictionless passwordless magic links, collecting extended metadata only after user activation.",
        "اجبار کاربران به پر کردن فرم‌های طولانی در همان ابتدای کار که موجب ترک ۷۰ درصدی فرآیند ثبت‌نام می‌شود.",
        "پیاده‌سازی ثبت‌نام سریع با لینک‌های جادویی بدون رمز و دریافت اطلاعات تکمیلی به مرور زمان پس از فعال‌سازی کاربر."
    ),
    "139": (
        "Allows user profile update endpoints to modify email and phone identifiers without sending verification challenges.",
        "Requires re-authentication and automated one-time confirmation challenges before altering primary identity attributes.",
        "امکان تغییر ایمیل یا شماره موبایل کاربر در اندپوینت پروفایل بدون ارسال کد تایید و احراز هویت مجدد.",
        "اجبار احراز هویت مجدد و ارسال کد تایید یکبارمصرف به آدرس جدید قبل از نهایی شدن تغییر اطلاعات اصلی حساب."
    ),
    "141": (
        "Permits automated AI support workflows to execute account actions based on unauthenticated user-supplied email claims.",
        "Verifies cryptographic session signatures and tenant scopes before allowing AI agents to trigger administrative or billing operations.",
        "اجازه به بات‌های پشتیبانی برای اعمال تغییرات در حساب‌ها صرفاً بر اساس ادعای متنی کاربر بدون بررسی توکن معتبر.",
        "اعتبارسنجی کریپتوگرافیک نشست و دامنه دسترسی کاربر قبل از اجرای هرگونه عملیات حساس مالی یا تغییر حساب توسط بات."
    ),
    "145": (
        "Forces abrupt user logouts every 15 minutes by failing to implement silent background token renewal flows.",
        "Implements seamless background token refresh using rotating refresh tokens without interrupting active user sessions.",
        "خروج اجباری و ناگهانی کاربران هر ۱۵ دقیقه به دلیل عدم پیاده‌سازی مکانیزم تمدید بی‌صدای توکن در پس‌زمینه.",
        "پیاده‌سازی تمدید نامحسوس توکن در پس‌زمینه با رفرش‌توکن‌های چرخشی بدون ایجاد وقفه در تجربه کاری کاربر."
    ),
    "157": (
        "Loads external JavaScript tracking scripts directly onto authentication pages, risking credential harvesting via script tampering.",
        "Enforces strict Content Security Policy (CSP) blocking third-party scripts on all login and password reset routes.",
        "بارگذاری اسکریپت‌های تحلیلی متفرقه در صفحات حساس لاگین که خطر سرقت رمزهای عبور را به شدت افزایش می‌دهد.",
        "اعمال سیاست امنیت محتوا (CSP) سخت‌گیرانه و مسدودسازی کامل هرگونه اسکریپت خارجی در صفحات ورود و بازیابی رمز."
    ),
    "160": (
        "Trusts Google Sign-In identity payloads without verifying the `email_verified: true` claim, risking account takeover.",
        "Validates issuer, audience, and the `email_verified` boolean claim on every external OAuth identity token before account linkage.",
        "اعتماد کورکورانه به خروجی ورود با گوگل بدون بررسی فلگ `email_verified: true` که امکان تصاحب حساب را ایجاد می‌کند.",
        "اعتبارسنجی دقیق صادرکننده، مخاطب و وضعیت تایید ایمیل در توکن‌های هویتی قبل از اتصال حساب کاربری."
    ),
    "161": (
        "Fails to detect credential stuffing attacks by logging failed logins as normal application events without threshold alarms.",
        "Monitors failed login ratios per IP and user account, triggering progressive delays, CAPTCHAs, and security alerts.",
        "نادیده گرفتن حملات حدس متوالی رمز عبور با ثبت لاگ‌های عادی بدون فعال‌سازی آستانه هشدار امنیتی.",
        "پایش نرخ تلاش‌های ناموفق ورود به ازای آی‌پی و حساب، و اعمال تاخیر تدریجی، کپچا و هشدارهای امنیتی."
    ),
    "165": (
        "Swallows authentication exceptions in frontend error boundaries, leaving users on unresponsive screens without error feedback.",
        "Catches authentication exceptions explicitly, clearing invalid tokens and redirecting to login with explanatory context.",
        "نادیده گرفتن خطاهای احراز هویت در رابط کاربری که موجب فریز شدن صفحه و سردرگمی کاربر بدون هیچ پیامی می‌شود.",
        "مدیریت صریح خطاهای ۴۰۱ و ۴۰۳، پاکسازی توکن‌های منقضی و انتقال کاربر به صفحه ورود همراه با پیام راهنما."
    ),
    "194": (
        "Restricts administrative actions solely by hiding UI buttons on the client while leaving underlying API endpoints unprotected.",
        "Decouples permissions from roles and enforces granular authorization checks on every backend controller and database query.",
        "مخفی کردن ظاهری دکمه‌های ادمین در رابط کاربری بدون اعتبارسنجی مجوزها در اندپوینت‌های بک‌اند.",
        "تفکیک نقش‌ها از دسترسی‌ها و اعتبارسنجی صریح مجوز در تک‌تک کنترلرهای بک‌اند و کوئری‌های دیتابیس."
    ),
    "201": (
        "Uses human user session cookies and interactive login flows for automated machine-to-machine microservice integrations.",
        "Enforces dedicated service-to-service authentication using mutual TLS (mTLS) or OAuth2 client credentials with scoped tokens.",
        "استفاده از کوکی‌های نشست کاربران عادی برای ارتباطات بین‌سرویسی خودکار در معماری میکروسرویس.",
        "پیاده‌سازی احراز هویت ماشین‌به‌ماشین با احراز هویت دوطرفه mTLS یا توکن‌های محدود OAuth2 Client Credentials."
    ),
    "206": (
        "Verifies JWT tokens using libraries that accept the insecure `none` algorithm or fails to enforce strict signing key verification.",
        "Enforces asymmetric algorithm validation (RS256/ES256), explicitly rejects tokens with `alg: none`, and validates audience/issuer claims.",
        "اعتبارسنجی JWT با کتابخانه‌هایی که الگوریتم ناامن `none` را می‌پذیرند و امکان جعل توکن را باز می‌گذارند.",
        "اجبار الگوریتم‌های نامتقارن، رد صریح الگوریتم `none` و اعتبارسنجی کامل هدرهای Issuer و Audience."
    ),
    "213": (
        "Deploys self-hosted authentication instances without dedicated security maintenance, falling behind critical vulnerability patches.",
        "Establishes automated vulnerability scanning and immediate patch deployment pipelines for all self-hosted identity engines.",
        "راه‌اندازی سرویس‌های احراز هویت محلی بدون فرآیند نگهداری که موجب غفلت از پچ‌های امنیتی بحرانی می‌شود.",
        "ایجاد پایپ‌لاین‌های اسکن خودکار آسیب‌پذیری و استقرار فوری پچ‌های امنیتی برای سرورهای احراز هویت محلی."
    ),
    "218": (
        "Migrates between auth vendors on impulsive whim without accounting for user credential migration friction and webhook divergence.",
        "Abstracts authentication interfaces behind internal adapter contracts to enable vendor transitions without rewriting business code.",
        "مهاجرت عجولانه بین ارائه‌دهندگان هویت بدون پیش‌بینی پیچیدگی‌های انتقال رمزهای عبور و تفاوت ساختار وب‌هوک‌ها.",
        "طراحی لایه واسط (Adapter) اختصاصی برای سیستم احراز هویت تا تغییر ارائه‌دهنده نیازی به بازنویسی کدها نداشته باشد."
    ),
    "228": (
        "Generates permanent personal access tokens that cannot be selectively revoked, creating permanent backdoors if leaked.",
        "Issues scoped personal access tokens with mandatory expiration dates and instant cryptographic revocation capabilities.",
        "تولید توکن‌های دسترسی دائمی بدون قابلیت ابطال گزینشی که در صورت افشا به در پشتی همیشگی تبدیل می‌شوند.",
        "صدور توکن‌های دسترسی با محدوده کاری مشخص، تاریخ انقضای اجباری و امکان ابطال آنی در پایگاه‌داده."
    ),
    "230": (
        "Builds proprietary cryptographic password hashing and session management algorithms from scratch, inviting subtle implementation flaws.",
        "Leverages hardened, audited open-source authentication frameworks and standard password hashing primitives (Argon2id).",
        "اختراع مجدد سیستم هش کردن رمزها و مدیریت نشست‌ها که منجر به خطاهای پنهان در پیاده‌سازی رمزنگاری می‌شود.",
        "استفاده از فریم‌ورک‌های تست‌شده و استاندارد با استفاده از الگوریتم‌های مدرن هشینگ مانند Argon2id."
    ),
    "243": (
        "Deploys static, hardcoded API secret keys that remain unchanged across environments for years, maximizing breach blast radiuses.",
        "Enforces automated secret rotation using cloud secret managers and issues short-lived ephemeral credentials to services.",
        "هاردکد کردن کلیدهای دسترسی ثابت که سال‌ها تغییر نمی‌کنند و دامنه خسارت را در زمان نشت به حداکثر می‌رسانند.",
        "چرخش خودکار کلیدها با ابزارهای مدیریت کلید ابری و صدور گواهی‌های موقت کوتاه‌مدت برای سرویس‌ها."
    ),
    "276": (
        "Treats Layer 8 Identity as an isolated feature rather than an architectural foundation integrated across all 13 production tiers.",
        "Propagates validated identity contexts through edge middleware, service meshes, and database row-level security boundaries.",
        "نگاه تک‌بعدی به لایه هویت به عنوان یک ویژگی مجزا به جای یکپارچه‌سازی آن در سرتاسر استک سیزده‌گانه تولید.",
        "انتشار هویت احرازشده از میان‌افزار لبه تا لایه مش سرویس‌ها و سیاست‌های امنیتی سطر دیتابیس (RLS)."
    ),
    "285": (
        "Skips formal session invalidation on user password changes, leaving previously authenticated devices active indefinitely.",
        "Revokes all active refresh tokens and invalidates existing session caches immediately upon successful password resets.",
        "عدم ابطال نشست‌های قبلی در زمان تغییر رمز عبور که دستگاه‌های قبلی را برای همیشه لاگین نگه می‌دارد.",
        "ابطال فوری کلیه رفرش‌توکن‌های فعال و پاکسازی کش نشست‌ها به محض تغییر موفقیت‌آمیز رمز عبور."
    ),
    "308": (
        "Accepts unverified client-supplied user identifiers in backend mutations, allowing users to alter peer account settings.",
        "Extracts authenticated user identities strictly from verified server-side session cookies, ignoring client body ID inputs.",
        "اعتماد به شناسه‌های ارسالی کاربر در بدنه درخواست که امکان دستکاری تنظیمات حساب دیگران را فراهم می‌کند.",
        "استخراج شناسه کاربر صرفاً از کوکی‌های تاییدشده نشست سمت سرور و نادیده گرفتن شناسه‌های ارسالی کلاینت."
    ),
    "314": (
        "Relies on in-memory session arrays in multi-instance deployments, causing random logouts when requests hit different server nodes.",
        "Backs user sessions with centralized Redis clusters or stateless encrypted JWT cookies to ensure seamless multi-node scaling.",
        "ذخیره نشست‌ها در حافظه موقت رم سرور که در محیط‌های چندسروره موجب خروج تصادفی کاربر در جابجایی سرورها می‌شود.",
        "اتصال نشست‌ها به کلاستر مرکزی ردیس یا استفاده از کوکی‌های امضاشده جهت تضمین مقیاس‌پذیری چندسروره."
    ),

    # ==========================================
    # 02-SECURITY-DEFENSE (47 episodes)
    # ==========================================
    "004": (
        "Allows public-facing marketing or CMS containers to communicate directly with internal production database subnets.",
        "Isolates container networks into private VPC subnets, requiring mutual TLS (mTLS) and read-only roles for peripheral tools.",
        "دسترسی مستقیم کانتینرهای عمومی وب و ابزارهای مارکتینگ به شبکه دیتابیس عملیاتی.",
        "تفکیک شبکه در ساب‌نت‌های خصوصی، اجبار mTLS برای ارتباطات داخلی و اعمال نقش‌های فقط-خواندنی."
    ),
    "005": (
        "Configures wildcard `Access-Control-Allow-Origin: *` with credentials enabled to silence development CORS errors in production.",
        "Restricts CORS headers to an explicit whitelist of trusted production domains and validates preflight request origins.",
        "تنظیم وایلدکارد CORS روی `*` همراه با کوکی‌ها جهت دور زدن خطاهای محیط محلی.",
        "تعریف لیست سفید سخت‌گیرانه از دامنه‌های معتبر و اعتبارسنجی دقیق هدرهای Preflight."
    ),
    "007": (
        "Relies purely on edge WAF rules while concatenating raw strings in application SQL queries, exposing data to injection bypasses.",
        "Enforces parameterized queries via ORM/prepared statements and validates all endpoint inputs using strict Zod schemas.",
        "اتکای صوری به فایروال WAF همراه با چسباندن رشته‌های متنی در کوئری‌های خام دیتابیس.",
        "استفاده ۱۰۰٪ از کوئری‌های پارامتری با ORM و اعتبارسنجی کامل ورودی‌ها با Zod قبل از رسیدن به دیتابیس."
    ),
    "009": (
        "Issues long-lived, un-throttled magic login links with open redirect parameters, enabling token theft and phishing redirection.",
        "Issues short-lived (5-10m) single-use magic tokens, locks redirect URLs to whitelisted domains, and rate limits email dispatch.",
        "ارسال لینک‌های لاگین جادویی بدون تاریخ انقضا و با پارامتر ریدایرکت باز بدون محدودیت نرخ.",
        "تولید توکن‌های یکبارمصرف کوتاه‌مدت (۵ دقیقه)، قفل کردن ریدایرکت به دامنه اصلی و محدودسازی ارسال ایمیل."
    ),
    "011": (
        "Hardcodes unpinned Redis dependency libraries without tracking critical security CVEs or upstream license forks.",
        "Pins exact dependency versions with hash integrity locks and automates Dependabot/Snyk security vulnerability scanning in CI.",
        "استفاده از کتابخانه‌های بدون نسخه مشخص ردیس بدون ردیابی آسیب‌پذیری‌های امنیتی بحرانی.",
        "پین کردن نسخه‌های دقیق پکیج‌ها با هش‌های اعتبارسنجی و فعال‌سازی اسکن خودکار در پایپ‌لاین CI."
    ),
    "015": (
        "Omits iframe clickjacking protection headers, allowing phishing sites to embed the authenticated UI inside transparent frames.",
        "Enforces `X-Frame-Options: DENY` and `Content-Security-Policy: frame-ancestors 'none'` on all authenticated HTTP responses.",
        "عدم تنظیم هدرهای مسدودسازی آی‌فریم که به سایت‌های مخرب اجازه بارگذاری نامرئی صفحه جهت دزدی کلیک را می‌دهد.",
        "اعمال اجباری هدرهای `X-Frame-Options: DENY` و `Content-Security-Policy: frame-ancestors 'none'` روی کلیه پاسخ‌ها."
    ),
    "016": (
        "Retains existing session identifiers across authentication transitions (Session Fixation), enabling session hijacking.",
        "Regenerates session IDs on every privilege change using `req.session.regenerate()` with Secure, HttpOnly, and SameSite flags.",
        "ثابت ماندن شناسه نشست قبل و بعد از لاگین که به مهاجم اجازه سرقت نشست را با فریب کاربر می‌دهد.",
        "تولید مجدد شناسه نشست در هر تغییر سطح دسترسی با `req.session.regenerate()` همراه با فلگ‌های امنیتی کوکی."
    ),
    "017": (
        "Accepts unvalidated redirect destinations in query parameters, enabling attackers to route users to external phishing portals.",
        "Validates post-action redirect paths against an explicit relative route allowlist, rejecting scheme-relative URLs (`//`).",
        "پذیرش مقاصد ریدایرکت فاقد اعتبارسنجی که مهاجمان را قادر می‌سازد کاربران را به صفحات فیشینگ خارجی بفرستند.",
        "اعتبارسنجی مسیر ریدایرکت با لیست سفید مسیرهای نسبی داخلی و مسدودسازی آدرس‌های با اسلش مضاعف."
    ),
    "018": (
        "Issues permanent, multi-use password reset tokens without expiration or post-consumption invalidation.",
        "Enforces 15-minute token TTLs, single-use invalidation, and throttles password reset dispatches to 3 requests per hour.",
        "صدور توکن‌های بازیابی رمز عبور دائمی و چندبارمصرف بدون تاریخ انقضا و بدون باطل شدن پس از استفاده.",
        "تنظیم انقضای ۱۵ دقیقه‌ای توکن، ابطال قطعی پس از اولین استفاده و محدودسازی درخواست‌ها به ۳ بار در ساعت."
    ),
    "020": (
        "Leaves GraphQL introspection endpoints enabled in production, giving attackers a complete structural blueprint of the API.",
        "Disables GraphQL schema introspection in production environments and enforces strict query depth/complexity limits.",
        "روشن گذاشتن قابلیت Introspection در گراف‌کیوال محیط عملیاتی که نقشه کامل دیتابیس را به مهاجمان لو می‌دهد.",
        "غیرفعال‌سازی ویژگی Introspection در پروداکشن و تعیین سقف عمق و پیچیدگی کوئری‌ها جهت پیشگیری از حملات DoS."
    ),
    "022": (
        "Passes raw database entity objects directly into React Server Components, serializing sensitive fields to the browser wire.",
        "Transforms database results into explicit Data Transfer Objects (DTOs), stripping internal fields before serializing props.",
        "پاس دادن آبجکت کامل دیتابیس به سرور کامپوننت‌های ریکت که موجب نشت فیلدهای حساس به مرورگر کلاینت می‌شود.",
        "تبدیل نتایج دیتابیس به DTOهای مشخص و حذف فیلدهای حساس قبل از سریالایز شدن در بستر شبکه."
    ),
    "024": (
        "Relies exclusively on edge middleware route matchers for authorization, leaving endpoints exposed to URL normalization bypasses.",
        "Enforces defense-in-depth authorization checks inside individual route handlers and database queries, not just at middleware boundaries.",
        "اتکای صرف به میان‌افزار لبه برای بررسی دسترسی‌ها که با ترفندهای نرمال‌سازی URL به راحتی دور زده می‌شود.",
        "پیاده‌سازی بررسی دسترسی درون تک‌تک هندلرها و کوئری‌ها در کنار میان‌افزار به عنوان دفاع چندلایه‌ای."
    ),
    "026": (
        "Sends transactional emails without SPF, DKIM, and DMARC DNS records, enabling attackers to spoof domain emails.",
        "Configures strict SPF, DKIM 2048-bit keys, and DMARC `p=reject` policies to ensure verifiable domain email authentication.",
        "ارسال ایمیل‌های سیستم بدون تنظیم رکوردهای SPF و DKIM که به کلاهبرداران امکان جعل آدرس ایمیل دامنه را می‌دهد.",
        "تنظیم رکوردهای استاندارد SPF، کلیدهای ۲۰۴۸ بیتی DKIM و سیاست DMARC روی حالت reject جهت مهار جعل ایمیل."
    ),
    "027": (
        "Relies solely on frontend HTML form validation attributes, trusting raw HTTP requests submitted directly to API handlers.",
        "Enforces identical server-side input schema validation using Zod/Valibot on all incoming API request payloads.",
        "اتکا به اعتبارسنجی فرم‌ها در فرانت‌اند و اعتماد کاذب به درخواست‌های خامی که مستقیماً به API ارسال می‌شوند.",
        "اعمال اعتبارسنجی ۱۰۰٪ داده‌ها در لایه سرور با Zod بر روی کلیه درخواست‌های ورودی پیش از پردازش."
    ),
    "033": (
        "Concatenates user search input directly into raw database query strings, opening critical SQL/NoSQL injection vulnerabilities.",
        "Uses parameterized queries and typed ORM builders exclusively, treating all user inputs as non-executable literal data.",
        "چسباندن مستقیم ورودی جستجوی کاربر به متن کوئری خام دیتابیس که منجر به نفوذ از طریق SQL Injection می‌شود.",
        "استفاده انحصاری از کوئری‌های پارامتری و ORMهای تایپ‌شده تا ورودی‌ها هرگز به عنوان کد اجرایی تفسیر نشوند."
    ),
    "035": (
        "Allows users to pass arbitrary role fields in signup or profile updates, allowing self-promotion to administrator status.",
        "Isolates role assignments to dedicated internal administrative workflows, stripping role fields from public mutation schemas.",
        "امکان ارسال فیلد نقش در ثبت‌نام یا آپدیت حساب که به کاربر اجازه می‌دهد خود را به ادمین تبدیل کند.",
        "تفکیک فیلدهای نقش به فرآیندهای مدیریتی داخلی و حذف کامل آن از اسکیماهای عمومی ورودی کاربران."
    ),
    "037": (
        "Implements OAuth authorization code exchanges without validating PKCE code verifiers or cross-site state parameters.",
        "Enforces PKCE (RFC 7636) code challenges and cryptographically signed state parameters on all third-party OAuth integrations.",
        "پیاده‌سازی لاگین OAuth بدون اعتبارسنجی PKCE یا پارامتر ضدجعل State که امکان سرقت کد دسترسی را می‌دهد.",
        "اجبار اعتبارسنجی چالش‌های PKCE و پارامترهای امضاشده State در تمام تبادلات کد احراز هویت با سرویس‌های خارجی."
    ),
    "047": (
        "Returns raw database error stack traces and internal file paths to users upon unhandled server exceptions.",
        "Sanitizes error responses into generic user messages while routing full diagnostic stack traces to centralized Sentry trackers.",
        "نمایش خطاهای خام دیتابیس و مسیرهای فایل سرور به کاربر در زمان رخداد خطاها در محیط عملیاتی.",
        "تبدیل خطاها به پیام‌های عمومی و امن برای کلاینت و هدایت لاگ کامل به سیستم مانیتورینگ متمرکز سنتری."
    ),
    "055": (
        "Communicates with mobile app backends over unencrypted HTTP or without TLS certificate pinning, exposing mobile traffic to interception.",
        "Enforces HTTPS with TLS 1.3 and implements certificate pinning in mobile apps to prevent man-in-the-middle proxy inspection.",
        "برقراری ارتباط اپلیکیشن موبایل از طریق HTTP ساده یا بدون پین کردن گواهی که امکان شنود ترافیک را می‌دهد.",
        "اجبار ارتباطات امن TLS 1.3 و پیاده‌سازی Certificate Pinning در اپ موبایل جهت مسدودسازی شنود بین‌راهی."
    ),
    "057": (
        "Leaves VPS root SSH access enabled with default passwords and open administrative ports on public IP addresses.",
        "Hardens Linux VPS hosts: disables root SSH, enforces key-based authentication, configures UFW firewalls, and enables Fail2ban.",
        "رها کردن سرور لینوکس با پورت SSH باز، رمز عبور پیش‌فرض و کاربر root بدون فایروال در معرض اینترنت.",
        "سخت‌سازی امنیتی سرور: غیرفعال‌سازی لاگین root، اجبار کلید SSH، تنظیم فایروال UFW و فعال‌سازی Fail2ban."
    ),
    "058": (
        "Installs unvetted npm packages that execute malicious postinstall scripts or exfiltrate `process.env` credentials at runtime.",
        "Audits dependencies using `npm audit`, runs untrusted packages in restricted sandboxes, and verifies lockfile integrity in CI.",
        "نصب پکیج‌های بررسی‌نشده npm که با اسکریپت‌های پنهان متغیرهای محیطی و کلیدهای سرور را به سرقت می‌برند.",
        "ممیزی پکیج‌ها با `npm audit`، قرنطینه کردن فرآیند اجرا و اعتبارسنجی یکپارچگی فایل lockfile در پایپ‌لاین CI."
    ),
    "059": (
        "Echoes back incoming request origins in `Access-Control-Allow-Origin` headers, rendering CORS protections completely useless.",
        "Validates incoming origins against an explicit static allowlist before setting access control response headers.",
        "بازتاب دادن مبدأ درخواست ورودی در هدر CORS که عملاً تمام لایه‌های دفاعی مرورگر را بی‌اثر می‌کند.",
        "بررسی دقیق آدرس مبدأ درخواست در برابر لیست سفید استاتیک دامنه‌های مجاز قبل از مقداردهی به هدر CORS."
    ),
    "065": (
        "Accepts state-modifying POST requests without Cross-Site Request Forgery (CSRF) tokens on cookie-authenticated sessions.",
        "Implements Double Submit Cookie patterns or SameSite=Strict cookie policies to neutralize cross-site request forgery.",
        "پذیرش درخواست‌های تغییر داده بدون توکن CSRF در نشست‌هایی که با کوکی احراز هویت می‌شوند.",
        "استفاده از الگوی Double Submit Cookie و فلگ SameSite=Strict برای پیشگیری از حملات جعل درخواست مرورگر."
    ),
    "069": (
        "Leaves authentication endpoints vulnerable to credential stuffing attacks by allowing 14,000 un-throttled login requests.",
        "Deploys IP-based and username-based Token Bucket rate limiters backed by Redis with progressive delays and CAPTCHA gates.",
        "عدم محدودسازی تعداد دفعات ورود که به بات‌ها اجازه می‌دهد ۱۴هزار رمز عبور را در یک شب تست کنند.",
        "پیاده‌سازی محدودسازی نرخ با سطل توکن در ردیس بر اساس آی‌پی و نام‌کاربری همراه با کپچای تطبیقی."
    ),
    "078": (
        "Feeds un-redacted multi-tenant databases into customer-facing LLMs, leaking peer customer data through prompt completions.",
        "Enforces strict data masking, tenant isolation filters, and prompt boundaries before feeding context into LLM generation.",
        "ارسال مستقیم داده‌های تفکیک‌نشده کاربران به مدل زبانی که موجب افشای اطلاعات سایر مشتریان در پاسخ‌ها می‌شود.",
        "ماسک کردن داده‌های حساس، اعمال فیلتر سفت‌وسخت سازمان و اعتبارسنجی خروجی قبل از نمایش پاسخ هوش مصنوعی."
    ),
    "080": (
        "Allows logins from unprecedented geolocations without requiring step-up verification or alerting account owners.",
        "Calculates risk scores based on IP reputation, device fingerprints, and impossible travel velocity, requiring step-up MFA challenges.",
        "اجازه ورود به حساب از کشورهای نامتعارف بدون درخواست اعتبارسنجی تکمیلی یا هشدار به مالک حساب.",
        "محاسبه امتیاز ریسک ورود بر اساس اثرانگشت دستگاه و موقعیت جغرافیایی، و اجبار تایید دومرحله‌ای در شرایط مشکوک."
    ),
    "082": (
        "Postpones founder-led video distribution until after product launch, launching to zero audience and zero distribution velocity.",
        "Builds distribution channels and founder video cadences simultaneously alongside product engineering before launch day.",
        "به تعویق انداختن تولید محتوا و ویدیو تا بعد از روز عرضه که موجب عرضه محصول به مخاطب صفر می‌شود.",
        "ایجاد همزمان کانال‌های توزیع و تعامل ویدیویی همگام با توسعه فنی محصول پیش از فرارسیدن روز رونمایی."
    ),
    "086": (
        "Grants autonomous AI agents unrestricted read/write database credentials, risking catastrophic hallucinated record destruction.",
        "Restricts AI agents to least-privilege read-only replicas and scopes mutation capabilities through hardened API contracts.",
        "اعطای دسترسی مستقیم نوشتن در دیتابیس اصلی به ایجنت‌های هوش مصنوعی که ریسک تخریب داده‌ها را به همراه دارد.",
        "محدود کردن ایجنت‌ها به رپلیکای فقط-خواندنی و اجرای تغییرات داده صرفاً از طریق توابع کنترل‌شده و اعتبارسنجی‌شده."
    ),
    "105": (
        "Exposes private database credentials, Stripe secret keys, and third-party tokens by committing them to public git repositories.",
        "Automates secret scanning in CI with Gitleaks/Trufflehog and stores production credentials exclusively in environment vaults.",
        "متعهد کردن کلیدهای خصوصی دیتابیس و استرایپ در گیت‌هاب که اطلاعات را در دسترس ربات‌های اسکنر قرار می‌دهد.",
        "اسکن خودکار تاریخچه گیت با Gitleaks قبل از کامیت و نگهداری امن کلیدها در محیط‌های مدیریت متغیر ابری."
    ),
    "132": (
        "Treats APIs solely as frontend data conduits without recognizing them as the primary attack surface requiring continuous defense.",
        "Architects APIs with defense-in-depth: edge rate limiting, schema validation, least-privilege scoping, and audit telemetry.",
        "نگاه ساده به API به عنوان پل ارتباطی فرانت‌اند بدون درک اینکه API مرز اصلی حمله برای نفوذگران است.",
        "معماری API با دفاع چندلایه‌ای: محدودسازی لبه، اعتبارسنجی اسکیما، حداقل دسترسی و ثبت لاگ‌های نظارتی."
    ),
    "167": (
        "Operates without community peer review or senior engineering oversight, shipping known security anti-patterns into production.",
        "Subject architectures to structured peer audits, threat modeling, and senior production engineering code reviews.",
        "توسعه نرم‌افزار بدون بازبینی توسط مهندسان ارشد که الگوهای ناامن شناخته‌شده را وارد محیط عملیاتی می‌کند.",
        "برگزاری جلسات مدل‌سازی تهدیدات، ممیزی معماری و بازبینی کد توسط مهندسان ارشد قبل از انتشار."
    ),
    "175": (
        "Allows AI coding assistants to execute unsanitized bash commands or file modifications directly on local developer machines.",
        "Runs untrusted AI-generated terminal scripts inside containerized developer sandboxes with constrained network access.",
        "اجازه به ابزارهای دستیار کدنویسی برای اجرای دستورات ناشناخته خط فرمان روی سیستم توسعه‌دهنده بدون قرنطینه.",
        "اجرای اسکریپت‌ها و پیشنهادات کدنویسی هوش مصنوعی درون محیط‌های کانتینری ایزوله با دسترسی محدود."
    ),
    "187": (
        "Installs unverified Model Context Protocol (MCP) servers with unrestricted file system and environment variable access.",
        "Audits MCP server source code, applies least-privilege operating system permissions, and restricts tool execution capabilities.",
        "نصب ابزارهای سرور پروتکل کانتکست (MCP) تاییدنشده با دسترسی باز به فایل‌های سیستمی و متغیرهای محرمانه.",
        "ممیزی سورس سرورهای MCP، اعمال کمترین سطح دسترسی سیستمی و مسدودسازی دسترسی به فایل‌های حیاتی."
    ),
    "191": (
        "Removes exposed secrets from source code via git commits without purging historical commits or revoking compromised keys.",
        "Revokes leaked credentials immediately at the provider, rotates secrets, and purges git commit history with BFG Repo-Cleaner.",
        "حذف کلیدهای لو رفته با کامیت جدید در گیت بدون باطل کردن کلید در ارائه‌دهنده یا پاکسازی تاریخچه گیت.",
        "ابطال فوری کلید در ارائه‌دهنده سرویس، چرخش کلیدها و پاکسازی کامل تاریخچه مخزن با ابزار BFG Repo-Cleaner."
    ),
    "215": (
        "Deploys web applications to production without running automated dynamic application security testing (DAST) tools.",
        "Integrates OWASP ZAP dynamic vulnerability scanning into CI/CD pipelines to detect injection and header flaws before release.",
        "انتشار برنامه‌ها در محیط عملیاتی بدون اجرای اسکنرهای پویای تست نفوذ و بررسی آسیب‌پذیری‌های امنیتی.",
        "یکپارچه‌سازی ابزار OWASP ZAP در خط استقرار CI/CD جهت شناسایی آسیب‌پذیری‌های امنیتی پیش از انتشار."
    ),
    "219": (
        "Builds ad-hoc security mechanisms in application code instead of leveraging battle-tested security framework primitives.",
        "Standardizes security defenses on proven industry frameworks, avoiding brittle custom security implementations.",
        "اختراع روش‌های من‌درآوردی برای امنیت در کد به جای استفاده از راهکارهای اثبات‌شده و استاندارد مهندسی.",
        "استانداردسازی معماری دفاعی با فریم‌ورک‌های معتبر و پرهیز از پیاده‌سازی‌های سلیقه‌ای و شکننده."
    ),
    "226": (
        "Relies on free unmaintained security plugins that introduce transitive vulnerabilities and silent security failures.",
        "Audits and minimizes third-party security plugins, adopting native framework defenses with active security maintenance.",
        "اتکا به پلاگین‌های امنیتی رایگان و رهاشده که خودشان منشأ آسیب‌پذیری‌های جدید و شکست‌های خاموش می‌شوند.",
        "حذف پلاگین‌های زائد، استفاده از قابلیت‌های بومی فریم‌ورک و نظارت مداوم بر به‌روزرسانی‌های امنیتی."
    ),
    "227": (
        "Leaves public repositories unmonitored for accidental secret commits, allowing automated crawler bots to steal keys in seconds.",
        "Installs pre-commit Git hooks (TruffleHog/git-secrets) that block commits containing API keys, private certificates, or tokens.",
        "عدم محافظت از مخازن عمومی که به بات‌های اینترنتی اجازه می‌دهد ظرف چند ثانیه کلیدهای کامیت‌شده را بربایند.",
        "نصب هوک‌های گیت pre-commit برای جلوگیری از کامیت شدن فایل‌های حاوی کلیدهای محرمانه و رمزها."
    ),
    "244": (
        "Stores AI provider API keys in raw `.env` files committed to repository roots and packaged into Docker build artifacts.",
        "Injects AI provider credentials at runtime via secure secret managers (AWS SSM/Doppler) without baking them into images.",
        "ذخیره کلیدهای API هوش مصنوعی در فایل‌های `.env` که در مخزن کامیت شده یا درون ایمیج‌های داکر جا می‌مانند.",
        "تزریق کلیدها در زمان اجرا از طریق سامانه‌های مدیریت کلید امن (Doppler/AWS Secrets) بدون هاردکد در ایمیج داکر."
    ),
    "249": (
        "Postpones vulnerability scanning until after security incidents occur, lacking continuous automated compliance verification.",
        "Runs automated container, dependency, and dynamic endpoint vulnerability scans on every merge to production branches.",
        "موکول کردن اسکن‌های امنیتی به بعد از رخداد نفوذ و فقدان فرآیند پیوسته جهت ارزیابی آسیب‌پذیری‌های سیستم.",
        "اجرای اسکن‌های خودکار کانتینرها، پکیج‌ها و اندپوینت‌ها در گیت‌هاب اکشنز به ازای هر ادغام در برنچ اصلی."
    ),
    "260": (
        "Maintains the identical static production API secret key for months without rotation schedules or breach contingency plans.",
        "Automates 90-day secret rotation pipelines supporting dual-key grace periods to prevent service disruption during rotation.",
        "استفاده از یک کلید دسترسی ثابت برای ماه‌های طولانی بدون برنامه چرخش کلید و تدابیر واکنش به نشت اطلاعات.",
        "اتوماسیون چرخش ۹۰ روزه کلیدها با پشتیبانی از دوره انتقال دوکلیده جهت پیشگیری از قطعی حین تعویض."
    ),
    "261": (
        "Shares database user credentials across multiple microservices, granting lateral access if any single service is breached.",
        "Provisions distinct database credentials and scoped schema permissions for every microservice to enforce defense-in-depth.",
        "استفاده از یک نام‌کاربری دیتابیس مشترک بین چند سرویس که نفوذ به یکی را به نفوذ به کل سیستم تبدیل می‌کند.",
        "تخصیص دسترسی‌ها و نام‌کاربری‌های مجزا در دیتابیس به ازای هر سرویس جهت مهار دامنه نفوذ (Blast Radius)."
    ),
    "273": (
        "Deploys code under the naive assumption that lack of reported attacks implies adequate production security posture.",
        "Adopts zero-trust architectural principles: assumes breach, verifies explicitly, and limits blast radius at every boundary.",
        "انتشار محصول با این فرض ساده‌لوحانه که گزارش نشدن حمله به معنی امن بودن سیستم در پروداکشن است.",
        "پیاده‌سازی معماری Zero-Trust: فرض بر نفوذ، اعتبارسنجی مداوم و مهار حداکثری دامنه نفوذ در تمام لایه‌ها."
    ),
    "282": (
        "Copies code snippets directly from LLMs into production without validating cryptographic safety or input boundaries.",
        "Audits every AI-generated component against secure coding guidelines, enforcing strict validation and sanitization.",
        "کپی مستقیم کدهای پیشنهادی مدل‌های زبانی در پروداکشن بدون بازبینی امنیتی توابع رمزنگاری و شرایط مرزی.",
        "ممیزی خط‌به‌خط کدهای تولیدشده توسط هوش مصنوعی بر اساس چک‌لیست‌های امنیتی و اعتبارسنجی کامل داده‌ها."
    ),
    "306": (
        "Launches production applications without performing structured pre-launch security audits against standard threat vectors.",
        "Verifies production readiness against a comprehensive 47-point security checklist covering identity, data, and compute.",
        "رونمایی از محصول بدون اجرای چک‌لیست رسمی ممیزی امنیت در برابر تهدیدات رایج اینترنتی.",
        "ارزیابی پایداری و امنیت محصول بر اساس چک‌لیست جامع ۴۷ بندی مهندسی پیش از عمومی‌سازی ترافیک."
    ),
    "318": (
        "Ignores newly disclosed Common Vulnerabilities and Exposures (CVEs) in deployed production dependencies.",
        "Configures continuous CVE monitoring with automated pull requests (Dependabot) and emergency security patch protocols.",
        "بی‌توجهی به هشدارهای امنیتی روز (CVE) در پکیج‌ها و کتابخانه‌های مستقر در محیط عملیاتی.",
        "پایش پیوسته آسیب‌پذیری‌های امنیتی CVE با ایجاد خودکار PR برای پچ‌های اضطراری در سریع‌ترین زمان."
    ),
    "322": (
        "Merges high-velocity AI-generated pull requests without automated static analysis security testing (SAST) gates.",
        "Blocks PR merges failing automated Semgrep/SonarQube SAST gates designed to catch insecure AI coding patterns.",
        "ادغام سریع کدهای تولیدی هوش مصنوعی بدون اعمال گیت‌های خودکار تست ایستا (SAST) و بررسی کیفیت.",
        "مسدودسازی خودکار PRهایی که در تست‌های ابزار Semgrep مردود شده یا الگوهای ناامن تولید کد دارند."
    ),

    # ==========================================
    # 03-DATABASE-STORAGE (33 episodes)
    # ==========================================
    "003": (
        "Spawns a new direct database connection per HTTP request without pooling; queries identical un-cached data on every page view.",
        "Routes database traffic through transaction poolers (PgBouncer/Supavisor) and caches hot read data in Redis/Upstash.",
        "ایجاد اتصال مستقیم جدید به ازای هر درخواست HTTP بدون استخر اتصالات و کوئری‌های تکراری بدون کش.",
        "هدایت ترافیک دیتابیس از طریق PgBouncer یا Supavisor و کش کردن داده‌های پرتکرار در ردیس."
    ),
    "045": (
        "References database connection credentials in client-accessible Next.js components, risking database string exposure.",
        "Imports the `server-only` package in database client files, guaranteeing compilation errors if imported into client bundles.",
        "استفاده از اطلاعات محرمانه دیتابیس در کامپوننت‌های فرانت‌اند نکست‌جی‌اس که خطر افشای رشته اتصال را به همراه دارد.",
        "استفاده از پکیج `server-only` در ماژول‌های اتصال دیتابیس تا هرگونه ایمپورت در کلاینت در زمان بیلد ارور دهد."
    ),
    "053": (
        "Executes unindexed filter queries that perform sequential full table scans across millions of rows, spiking database CPU to 100%.",
        "Analyzes query execution plans with `EXPLAIN ANALYZE` and adds covering composite B-tree indexes matching query predicates.",
        "اجرای کوئری‌های فاقد ایندکس که در میلیون‌ها سطر اسکن کامل انجام داده و مصرف پردازنده دیتابیس را به ۱۰۰٪ می‌رسانند.",
        "بررسی پلن اجرای کوئری با `EXPLAIN ANALYZE` و تعریف ایندکس‌های ترکیبی B-tree متناسب با فیلترهای جستجو."
    ),
    "066": (
        "Adds bespoke un-indexed columns to primary tables for one client, degrading query performance for all remaining tenants.",
        "Maintains clean schema normalization with JSONB attribute fields or dedicated tenant configuration extension tables.",
        "افزودن ستون‌های غیراستاندارد جدید به جدول اصلی برای یک مشتری خاص که سرعت دیتابیس را برای بقیه کند می‌کند.",
        "حفظ نرمال‌سازی اسکیما و استفاده از ستون‌های JSONB ایندکس‌شده یا جداول اکستنشن برای تنظیمات خاص مشتریان."
    ),
    "072": (
        "Reads from asynchronously replicated database read replicas immediately after writes, serving stale or conflicting state to users.",
        "Implements read-after-write consistency routing, directing queries immediately following mutations to the primary database node.",
        "خواندن اطلاعات بلافاصله پس از نوشتن از رپلیکاهای تاخیری که موجب نمایش اطلاعات قدیمی و تضاد داده‌ها می‌شود.",
        "هدایت هوشمند کوئری‌ها پس از ثبت تغییرات (Read-After-Write) به نود اصلی دیتابیس جهت تضمین پایداری وضعیت."
    ),
    "079": (
        "Relies on unverified nightly snapshot backups, discovering corruption only after catastrophic disk failure destroys 14 hours of data.",
        "Configures continuous Write-Ahead Log (WAL) archiving with Point-in-Time Recovery (PITR) and verifies automated test restores.",
        "اتکا به بکاپ‌های شبانه تست‌نشده و متوجه شدن خرابی فایل‌ها پس از حادثه و از دست رفتن ۱۴ ساعت از داده‌های کاربران.",
        "فعال‌سازی ذخیره‌سازی لاگ‌های WAL برای بازگردانی نقطه در زمان (PITR) و اعتبارسنجی خودکار تست‌های ریستور ماهانه."
    ),
    "094": (
        "Designs single-tenant database schemas that cannot support multi-tenancy without extensive destructive migrations.",
        "Incorporates tenant ID scoping into foundational database schema designs from inception, even for early single-tenant prototypes.",
        "طراحی اسکیما به شکل تک‌مشتری که بعداً برای افزودن چندسازمانی نیازمند بازنویسی فاجعه‌بار و پرریسک دیتابیس است.",
        "لحاظ کردن شناسه سازمان (tenant_id) در ساختار پایه‌ای جداول از همان روز اول جهت تضمین مقیاس‌پذیری آینده."
    ),
    "099": (
        "Exposes raw database connection strings containing administrative passwords in client-facing exception stack traces.",
        "Scrubs sensitive database connection strings and passwords from all application error boundaries and logging middleware.",
        "نمایش کانکشن‌استرینگ حاوی پسورد ادمین دیتابیس در پیام خطای نمایش‌داده‌شده به کاربر.",
        "پاکسازی کامل اطلاعات حساس و رمزهای اتصال از تمامی هندلرهای خطا و میان‌افزارهای لاگینگ سرور."
    ),
    "149": (
        "Connects autonomous AI agents directly to production databases without query timeout limits or sandboxed permissions.",
        "Routes agent queries through dedicated read-only connection pools bounded by strict 3-second query execution timeouts.",
        "اتصال مستقیم ایجنت‌های هوش مصنوعی به دیتابیس اصلی بدون تعیین سقف زمان اجرا و دسترسی‌های محدود.",
        "هدایت کوئری‌های ایجنت از طریق استخر اتصالات فقط-خواندنی با سقف زمان اجرای سخت‌گیرانه ۳ ثانیه‌ای."
    ),
    "151": (
        "Applies database schema migrations directly in production with locks that block read and write traffic during deployments.",
        "Employs the expand-and-contract migration pattern, adding non-breaking nullable columns before deprecating legacy fields.",
        "اعمال مایگریشن‌های سنگین با قفل کردن جدول در محیط عملیاتی که موجب توقف موقت برنامه در حین دیپلوی می‌شود.",
        "استفاده از الگوی Expand and Contract برای مایگریشن‌های بدون قطعی و افزودن فیلدهای جدید بدون مسدودسازی ترافیک."
    ),
    "153": (
        "Persists rapidly changing high-volume event logs in primary transactional tables, saturating relational buffer pool memory.",
        "Offloads append-only event streams and audit trails to dedicated time-series databases or object storage (ClickHouse/S3).",
        "ذخیره لاگ‌ها و رویدادهای پرتکرار در جداول تراکنشی اصلی که موجب اشباع بافر رم دیتابیس رابطه‌ای می‌شود.",
        "انتقال لاگ‌های رویدادی به پایگاه‌های داده سری‌زمانی اختصاصی (مانند ClickHouse) یا استوریج S3."
    ),
    "174": (
        "Postpones backup configuration decisions until after production deployment, risking irreversible data corruption.",
        "Establishes automated daily backup snapshots, geo-replicated offsite storage, and defines explicit RPO/RTO metrics.",
        "به تعویق انداختن استراتژی پشتیبان‌گیری تا پس از دیپلوی که ریسک نابودی کامل دیتابیس را به همراه دارد.",
        "راه‌اندازی بکاپ‌های روزانه خودکار، انتقال نسخه به سرور مجزا در دیتاسنتر دیگر و تعیین دقیق شاخص‌های RTO و RPO."
    ),
    "176": (
        "Fails to test database disaster recovery procedures, leaving engineering teams helpless during holiday cloud outages.",
        "Executes scheduled disaster recovery drills with automated database failover to secondary cloud regions.",
        "عدم اجرای مانور بحران برای بازگردانی دیتابیس که تیم را در زمان قطعی روزهای تعطیل سردرگم و ناتوان می‌گذارد.",
        "اجرای مانورهای دوره‌ای بازیابی بحران و تست سوییچ خودکار دیتابیس به ریجن ثانویه بدون از دست رفتن داده‌ها."
    ),
    "192": (
        "Assumes automated cloud provider snapshots guarantee recovery without ever executing an end-to-end database restore test.",
        "Executes automated monthly restore drills spinning up isolated test databases from production snapshots to verify integrity.",
        "فرض بر اینکه اسنپ‌شات‌های اتوماتیک کلود قطعی هستند بدون اینکه حتی یک‌بار فرآیند ریستور تست شده باشد.",
        "اجرای مانورهای خودکار ماهانه با بالا آوردن دیتابیس تستی از فایل پشتیبان برای اثبات سلامت داده‌ها."
    ),
    "193": (
        "Renames database columns in-place, instantly breaking deployed application instances running legacy query code.",
        "Performs three-phase column migrations: add new column, dual-write in application code, backfill data, then drop legacy column.",
        "تغییر نام مستقیم ستون در دیتابیس که بلافاصله کدهای در حال اجرای سرور را دچار خطای ۵۰۰ می‌کند.",
        "مایگریشن سه‌مرحله‌ای ستون‌ها: افزودن ستون جدید، نوشتن همزمان در هر دو ستون و در نهایت حذف ستون قدیمی."
    ),
    "196": (
        "Executes identical expensive database aggregation queries on every HTTP request without caching intermediate calculations.",
        "Caches aggregated metric calculations in Redis or uses materialized views refreshed periodically in the background.",
        "اجرای کوئری‌های محاسباتی سنگین در تمام درخواست‌های کاربران بدون ذخیره نتایج میانی.",
        "کش کردن نتایج آماری در ردیس یا استفاده از Materialized View با به‌روزرسانی دوره‌ای در پس‌زمینه."
    ),
    "210": (
        "Adopts reactive document databases without understanding consistency models, leading to data synchronization anomalies.",
        "Evaluates transactional guarantees, schema enforcement, and query constraints before committing data to reactive backends.",
        "انتخاب پایگاه‌های داده واکنشی بدون تسلط بر مدل سازگاری آن‌ها که باعث بروز ناهماهنگی در داده‌ها می‌شود.",
        "ارزیابی تضمین‌های تراکنشی ACID و محدودیت‌های کوئری قبل از انتقال منطق حساس کسب‌وکار به پایگاه‌های واکنشی."
    ),
    "211": (
        "Relies blindly on ORMs like Prisma without inspecting generated raw SQL, missing severe N+1 query performance disasters.",
        "Audits ORM query generation logs, replaces N+1 relationships with eager joins, and runs raw parameterized SQL where needed.",
        "اعتماد کور به ORMهایی مانند پریزما بدون مشاهده SQL تولیدی که خطاهای وحشتناک N+1 Query ایجاد می‌کند.",
        "بررسی لاگ کوئری‌های ORM، استفاده از Eager Loading برای ریشه‌کنی باگ N+1 و نگارش کوئری خام در جاهای حساس."
    ),
    "216": (
        "Stores high-resolution image binaries directly in database bytea/blob columns, inflating storage size and exhausting buffer pools.",
        "Offloads binary media files to dedicated S3/Object Storage with CDN edge distribution, storing only normalized URLs in the database.",
        "ذخیره مستقیم تصاویر حجیم در ستون‌های دیتابیس که موجب انفجار حجم دیتابیس و پر شدن رم سرور می‌شود.",
        "انتقال فایل‌های چندرسانه‌ای به Object Storage (S3/Cloudflare R2) و ذخیره آدرس لینک در پایگاه‌داده."
    ),
    "224": (
        "Adds random single-column indexes without analyzing query patterns, bloating disk overhead while queries remain slow.",
        "Designs composite multi-column indexes matching exact `WHERE`, `JOIN`, and `ORDER BY` clauses following leftmost prefix rules.",
        "تعریف بی‌هدف ایندکس‌های تک‌ستونی بدون بررسی نحوه کوئری که دیسک را پر کرده و تاثیری در سرعت ندارد.",
        "طراحی ایندکس‌های ترکیبی متناسب با ستون‌های جستجو، اتصال و مرتب‌سازی بر اساس قاعده پیشوند چپ."
    ),
    "229": (
        "Fails to enforce foreign key constraints at the database engine level, resulting in orphaned records and corrupted relational state.",
        "Enforces strict foreign key constraints with explicit `ON DELETE CASCADE` or `RESTRICT` policies in database schemas.",
        "عدم استفاده از کلیدهای خارجی (Foreign Keys) در دیتابیس که منجر به رکوردهای یتیم و داده‌های متناقض می‌شود.",
        "تعریف صریح کلیدهای خارجی به همراه سیاست‌های منطقی حذف مانند Cascade جهت حفظ یکپارچگی ارجاعی."
    ),
    "232": (
        "Deploys standalone vector databases for simple AI search features without evaluating operational complexity and cost overhead.",
        "Leverages `pgvector` extensions inside existing PostgreSQL clusters for small-to-medium vector workloads before scaling out.",
        "راه‌اندازی دیتابیس وکتوری مجزا برای پروژه‌های کوچک که هزینه و پیچیدگی بی‌مورد به زیرساخت اضافه می‌کند.",
        "استفاده از افزونه `pgvector` درون همان دیتابیس پستگرس برای حجم داده‌های اولیه تا زمان نیاز به مقیاس بالا."
    ),
    "237": (
        "Repeats un-cached database queries for static configuration tables on every single incoming web request.",
        "Implements in-memory or Redis caching with mutation-driven invalidation for static and slow-changing reference tables.",
        "اجرای مکرر کوئری دیتابیس برای جداول تنظیمات ثابت سیستم به ازای تک‌تک درخواست‌های ورودی کاربران.",
        "کش کردن داده‌های ثابت در حافظه یا ردیس با مکانیزم ابطال خودکار در زمان تغییر داده‌ها در دیتابیس."
    ),
    "252": (
        "Assumes database performance tested with 5 rows will sustain production concurrency under 50 simultaneous users.",
        "Executes realistic load tests using dirty seed datasets (100k+ rows) to expose unindexed queries and connection bottlenecks.",
        "فرض بر اینکه سرعت دیتابیس با ۵ سطر تستی در محیط محلی، زیر بار ۵۰ کاربر همزمان پایدار خواهد ماند.",
        "اجرای تست‌های بار با داده‌های حجیم (بالای ۱۰۰هزار سطر) برای کشف کوئری‌های فاقد ایندکس و گلوگاه اتصالات."
    ),
    "262": (
        "Runs pagination using offset-limit queries on tables with 10 million rows, forcing the database to scan millions of discarded rows.",
        "Implements cursor-based keyset pagination (`WHERE id > :last_id LIMIT 50`) for constant-time performance regardless of table size.",
        "استفاده از صفحه‌بندی آفست (Offset Pagination) در جداول میلیونی که دیتابیس را مجبور به اسکن تمام سطرها می‌کند.",
        "پیاده‌سازی صفحه‌بندی مبتنی بر نشانگر (Keyset/Cursor Pagination) جهت حفظ سرعت ثابت در حجم داده میلیونی."
    ),
    "264": (
        "Jumps between managed database platforms (Supabase, Firebase, Neon, Convex) without evaluating vendor lock-in or schema mobility.",
        "Standardizes on open-source relational primitives (PostgreSQL) to ensure zero-lockin database portability across cloud providers.",
        "جابجایی بدون برنامه بین سرویس‌های دیتابیس ابری بدون توجه به قفل شدن داده‌ها و دشواری مهاجرت.",
        "استانداردسازی معماری روی پستگرس متن‌باز جهت تضمین انتقال‌پذیری کامل به هر ارائه‌دهنده ابری دلخواه."
    ),
    "265": (
        "Treats Layer 13 Storage as a simple key-value store, ignoring transaction atomicity, durability, and isolation guarantees.",
        "Leverages transactional guarantees (`$transaction` / `BEGIN...COMMIT`) to ensure consistency across multi-step mutations.",
        "نگاه ساده به لایه سیزدهم ذخیره‌سازی و بی‌توجهی به اصول ACID و تراکنش‌های اتمیک در عملیات‌های حساس مالی.",
        "استفاده از تراکنش‌های اتمیک دیتابیس برای تضمین تغییر همزمان داده‌ها و جلوگیری از ایجاد مغایرت‌های مالی."
    ),
    "272": (
        "Binds application hosting tightly to co-located database servers, preventing independent horizontal scaling of compute and data.",
        "Decouples application server instances from managed database clusters over private subnets with connection poolers.",
        "چسباندن هاست برنامه به سرور دیتابیس که مانع از مقیاس‌پذیری مستقل لایه پردازش و داده می‌شود.",
        "جداسازی لایه سرورهای برنامه از کلاستر دیتابیس در شبکه خصوصی به همراه استخر اتصالات هوشمند."
    ),
    "277": (
        "Deploys database schemas generated blindly by AI without unique constraints, allowing duplicate records during race conditions.",
        "Enforces database composite unique constraints and check constraints to guarantee structural data integrity under concurrency.",
        "استقرار اسکیمای تولیدشده توسط هوش مصنوعی بدون قیدهای یکتا که موجب ثبت اطلاعات تکراری در شرایط مسابقه می‌شود.",
        "تعریف قیدهای یکتای ترکیبی (Unique Constraints) در دیتابیس برای جلوگیری قطعی از ورود داده‌های تکراری."
    ),
    "287": (
        "Designs bloated database tables with 47 un-normalized columns, dragging performance down on every row read.",
        "Applies normalization best practices: decomposes monolithic entities into cohesive relational models with foreign keys.",
        "طراحی جداول حجیم با ۴۷ ستون تفکیک‌نشده که سرعت خواندن هر سطر را به شدت کاهش می‌دهد.",
        "نرمال‌سازی اصولی دیتابیس: تفکیک موجودیت‌ها به جداول مرتبط همراه با روابط کلید خارجی جهت بهبود پرفورمنس."
    ),
    "288": (
        "Executes database queries directly from client components or frontend code, exposing database credentials and bypassing business logic.",
        "Enforces Layer 2 API isolation with server-side authentication, input validation, rate limiting, and zero direct database access from clients.",
        "برقراری ارتباط مستقیم فرانت‌اند با دیتابیس و دور زدن لایه‌های بیزینس لاجیک و اعتبارسنجی سرور.",
        "جداسازی کامل لایه دوم (API) با اعتبارسنجی ۱۰۰٪ داده‌ها در بک‌اند و مسدودسازی دسترسی مستقیم کلاینت به دیتابیس."
    ),
    "298": (
        "Deploys applications without configuring database connection leak alerts, crashing servers silently when connections remain open.",
        "Monitors database active connection metrics and enforces connection pool timeouts with automatic garbage collection of idle pools.",
        "عدم نظارت بر نشت اتصالات دیتابیس که به مرور زمان با باز ماندن اتصالات موجب خاموشی ناگهانی سرور می‌شود.",
        "پایش بلادرنگ اتصالات فعال، تنظیم مهلت بستن اتصالات بیکار و انتشار خودکار اتصالات رهاشده در کد."
    ),
    "320": (
        "Assumes database stability under 10 users translates linearly to production loads without index optimization or connection limits.",
        "Pre-calculates query latency under scale using realistic benchmarks and optimizes queries before onboarding production users.",
        "تصور اینکه کارکرد روان دیتابیس برای ۱۰ کاربر اولیه به معنی تاب‌آوری زیر بار ترافیک واقعی پروداکشن است.",
        "بنچمارک دقیق تاخیر کوئری‌ها با شبیه‌سازی ترافیک بالا و رفع گلوگاه‌های ایندکس پیش از ورود کاربران انبوه."
    ),

    # ==========================================
    # 04-CACHING-PERFORMANCE (12 episodes)
    # ==========================================
    "012": (
        "Sends identical repetitive prompts to expensive cloud LLMs on every request without caching deterministic model completions.",
        "Caches deterministic LLM completions in Redis using prompt hashes as cache keys, drastically slashing API costs and latency.",
        "ارسال مکرر پرامپت‌های مشابه به مدل‌های گران‌قیمت ابری بدون کش کردن پاسخ‌های قطعی تولیدشده.",
        "کش کردن خروجی‌های قطعی مدل در ردیس با کلید هش پرامپت جهت کاهش ۹۰ درصدی هزینه‌ها و تاخیر پاسخ."
    ),
    "019": (
        "Re-computes semantic similarity and vector lookups for identical queries instead of leveraging semantic cache layers.",
        "Deploys semantic vector caching (GPTCache/Redis) to return cached completions for semantically equivalent user questions.",
        "محاسبه مجدد سرچ معنایی و امبدینگ برای سوالات پرتکرار و یکسان کاربران بدون استفاده از کش معنایی.",
        "استفاده از کش برداری معنایی برای بازگرداندن فوری پاسخ به سوالات معادل با صرفه‌جویی چشمگیر در هزینه."
    ),
    "039": (
        "Ships frequent code updates without versioning cache keys, serving stale legacy assets and crashing frontend clients.",
        "Incorporates git commit deployment hashes into cache keys and asset URLs (`Cache-Busting`) to guarantee immediate cache updates.",
        "انتشار آپدیت‌های پیاپی بدون نسخه‌گذاری کلیدهای کش که موجب نمایش کدهای قدیمی و خطای کلاینت‌ها می‌شود.",
        "استفاده از هش کامیت در کلیدهای کش و آدرس فایل‌ها جهت بی‌اثرسازی آنی کش‌های قدیمی در هر انتشار جدید."
    ),
    "077": (
        "Puts Cloudflare in front of an application with naive default cache settings, accidentally caching dynamic user sessions at the edge.",
        "Configures explicit `Cache-Control: private, no-store` on authenticated routes while caching purely static assets at the CDN edge.",
        "قرار دادن کلودفلر جلوی برنامه با تنظیمات کش پیش‌فرض که موجب کش شدن اطلاعات محرمانه کاربران در لبه شبکه می‌شود.",
        "تنظیم هدرهای دقیق `Cache-Control: private, no-store` برای مسیرهای کاربری و کش کردن اختصاصی فایل‌های استاتیک در CDN."
    ),
    "104": (
        "Caches database query results using global static keys without tenant scoping, leaking Customer A's dashboard to Customer B.",
        "Prefixes all cache keys with tenant and user boundaries (`cache:tenant_{id}:user_{id}:dashboard`) to prevent cross-tenant data leaks.",
        "کش کردن نتایج کوئری دیتابیس با کلید عمومی بدون تفکیک سازمان که داشبورد مشتری الف را به مشتری ب نشان می‌دهد.",
        "پیشوندگذاری کلیدهای کش با شناسه دقیق سازمان و کاربر برای ریشه‌کنی قطعی خطر نشت اطلاعات بین مشتریان."
    ),
    "116": (
        "Hits primary databases directly for high-traffic public profile pages, buckling under sudden viral social media traffic spikes.",
        "Serves high-read public pages from distributed edge caches with stale-while-revalidate policies, shielding backend origins.",
        "پاسخگویی به بازدید صفحات عمومی مستقیماً از دیتابیس که با وایرال شدن پست در شبکه‌های اجتماعی سرور را می‌خواباند.",
        "کش کردن صفحات عمومی در لبه شبکه (Edge CDN) با استراتژی Stale-While-Revalidate جهت مهار ترافیک انفجاری."
    ),
    "171": (
        "Adds ad-hoc in-memory caching variables across controllers, causing inconsistent state across multiple server instances.",
        "Standardizes on centralized Redis clusters with explicit TTLs and event-driven cache invalidation patterns (Cache-Aside).",
        "تعریف متغیرهای کش پراکنده در رم سرور که در محیط‌های چندسروره باعث ناهماهنگی وضعیت داده‌ها می‌شود.",
        "استانداردسازی کش روی کلاستر مرکزی ردیس با زمان انقضای مشخص و الگوی ابطال مبتنی بر تغییر دیتابیس (Cache-Aside)."
    ),
    "186": (
        "Designs write-heavy workloads with aggressive read-caching architectures, causing cache thrashing and lock contention.",
        "Analyzes application read-write ratios to pick optimal caching topologies: Write-Through for reads vs append buffers for writes.",
        "طراحی معماری با کش سنگین برای سیستم‌هایی که ذاتاً تراکنش نوشتن بالایی دارند و باعث هدررفت رم می‌شود.",
        "تحلیل نسبت خواندن به نوشتن سیستم و انتخاب معماری مناسب: کش Write-Through یا بافرهای صف برای نوشتن."
    ),
    "197": (
        "Caches rapidly mutating transactional states like inventory balances, causing overselling and financial reconciliation bugs.",
        "Restricts caching to static, reference, or read-heavy data while reading volatile transactional state directly from ACID databases.",
        "کش کردن داده‌های فرار مانند موجودی انبار که موجب فروش بیش از ظرفیت و خطاهای مغایرت مالی می‌شود.",
        "پرهیز از کش کردن داده‌های متغیر و خواندن مستقیم وضعیت‌های حساس مالی از دیتابیس رابطه‌ای امن."
    ),
    "214": (
        "Adds Redis without connection pooling or serialization optimizations, spending more time in network roundtrips than SQL queries.",
        "Implements connection pooling, binary serialization (MessagePack/Protobuf), and batch pipelining for Redis interactions.",
        "افزودن ردیس بدون استخر اتصالات که زمان ارتباط شبکه با ردیس را از زمان کوئری دیتابیس طولانی‌تر می‌کند.",
        "پیاده‌سازی استخر اتصالات، فشرده‌سازی باینری داده‌ها و ارسال دسته‌ای دستورات (Pipeline) برای بهینه‌سازی ردیس."
    ),
    "263": (
        "Deploys single-region backends serving global users, imposing 300ms network round-trip latencies on overseas customers.",
        "Distributes static content and read replicas via edge networks and global CDNs to achieve sub-50ms latency worldwide.",
        "استقرار سرور در یک نقطه جغرافیایی که به کاربران سایر قاره‌ها تاخیر شبکه بالای ۳۰۰ میلی‌ثانیه تحمیل می‌کند.",
        "توزیع محتوا و رپلیکاهای فقط-خواندنی در لبه شبکه جهانی (Edge CDN) جهت کاهش تاخیر به زیر ۵۰ میلی‌ثانیه."
    ),
    "271": (
        "Treats Layer 10 Caching as a band-aid for broken database indexes rather than a deliberate architectural tier.",
        "Hardens database indexes first, then layers Redis caching with strict TTLs and distributed mutex locks against dogpiling.",
        "استفاده از کش برای پوشاندن ضعف ایندکس‌های خراب دیتابیس به جای طراحی اصولی لایه دهم کشینگ.",
        "اصلاح و بهینه‌سازی ایندکس‌های دیتابیس در گام اول، و سپس اعمال کش ردیس با قفل‌های توزیع‌شده ضد هجوم (Anti-Dogpile)."
    ),

    # ==========================================
    # 05-RATE-LIMITING-ABUSE (4 episodes)
    # ==========================================
    "103": (
        "Exposes origin servers directly to the internet without an edge WAF or DDoS mitigation, allowing trivial request loops to crash the app.",
        "Deploys Cloudflare/edge WAF with adaptive behavioral rate limiting and automated IP anomaly blacklisting.",
        "قرار دادن سرور اصلی مستقیماً در معرض اینترنت عمومی بدون WAF لبه که با یک حلقه ساده ۱۰هزار درخواست در ثانیه کل سیستم را از کار می‌اندازد.",
        "استقرار فایروال لبه (Cloudflare WAF) همراه با محدودسازی تطبیقی رفتار ترافیک و مسدودسازی خودکار آی‌پی‌های ناهنجار."
    ),
    "178": (
        "Drops abusive connections abruptly with opaque errors instead of standard HTTP rate limiting protocols.",
        "Enforces Token Bucket rate limiting returning HTTP 429 status codes with explicit `Retry-After` headers and graceful client backoff.",
        "قطع ناگهانی ارتباط در ترافیک‌های بالا با خطاهای گنگ بدون ارسال هدرهای استاندارد محدودسازی نرخ.",
        "پیاده‌سازی استاندارد با کد وضعیت HTTP 429 و هدرهای `Retry-After` با استفاده از الگوریتم سطل توکن در ردیس."
    ),
    "274": (
        "Omits gateway rate limiting, leaving expensive AI and payment endpoints unprotected against automated bot abuse.",
        "Applies multi-tiered rate limiting at API gateways: strict limits on auth/AI endpoints and relaxed thresholds for read APIs.",
        "فقدان لایه محدودسازی نرخ در گیت‌وی که اندپوینت‌های گران هوش مصنوعی و پرداخت را بی‌دفاع می‌گذارد.",
        "اعمال محدودسازی چندسطحی در گیت‌وی: محدودیت شدید روی اندپوینت‌های احراز هویت و مدل‌ها، و سقف‌های متعادل برای کوئری‌های عمومی."
    ),
    "304": (
        "Allows 50 simultaneous registrations from a single IP to exhaust database pools and trigger external verification costs.",
        "Throttles user registration endpoints by IP subnet and device fingerprint, queueing burst traffic via Redis queues.",
        "اجازه ثبت‌نام ۵۰ کاربر همزمان از یک آی‌پی که ظرفیت اتصالات دیتابیس را پر کرده و هزینه‌های گزاف پیامک ایجاد می‌کند.",
        "محدودسازی نرخ ثبت‌نام بر اساس ساب‌نت آی‌پی و اثرانگشت مرورگر، و صف‌بندی درخواست‌های همزمان در ردیس."
    ),

    # ==========================================
    # 06-OBSERVABILITY-LOGS (16 episodes)
    # ==========================================
    "023": (
        "Fails to capture structured telemetry, remaining completely blind to silent application failures that damage user trust.",
        "Instruments structured JSON logging with correlation IDs and business outcome tracking across all critical user journeys.",
        "عدم ثبت لاگ‌های ساختاریافته که تیم را از خطاهای خاموش پلتفرم و از بین رفتن اعتماد کاربران بی‌خبر می‌گذارد.",
        "پیاده‌سازی لاگینگ ساختاریافته JSON با شناسه پیگیری (Correlation ID) و پایش سلامت تمام مراحل حیاتی بیزینس."
    ),
    "071": (
        "Maintains status pages showing 'All Systems Operational' based on ping checks while core checkout workflows are broken.",
        "Deploys automated synthetic transaction canaries testing real login and payment workflows end-to-end around the clock.",
        "نمایش وضعیت سبز در Status Page صرفاً با پینگ سرور، در حالی که مسیر خرید کاربران کاملاً از کار افتاده است.",
        "اجرای ربات‌های تست مصنوعی (Synthetic Canaries) برای بررسی ۲۴ ساعته فرآیند لاگین و خرید به صورت سرتاسری."
    ),
    "121": (
        "Tracks vanity signup numbers while ignoring cohort retention metrics and user drop-off telemetry on core features.",
        "Instruments user engagement telemetry and cohort retention tracking to detect silent user abandonment early.",
        "تمرکز روی آمارهای تزئینی ثبت‌نام و ندیدن ریزش هفتگی کاربران به دلیل فقدان تله‌متری رفتار مشتریان.",
        "اندازه‌گیری دقیق کوهورت‌های بازگشت کاربران و ردگیری تعاملات جهت کشف زودهنگام دلایل ترک محصول."
    ),
    "128": (
        "Logs account deletion requests as simple text strings without immutable audit trails required by data protection regulations.",
        "Emits cryptographically verifiable audit logs for GDPR/CCPA deletion requests with automated verification receipts.",
        "ثبت درخواست‌های حذف حساب به شکل متن ساده بدون لاگ حسابرسی قانونی که ناقض الزامات GDPR است.",
        "ثبت لاگ‌های حسابرسی غیرقابل‌تغییر برای درخواست‌های حذف داده همراه با صدور شناسه پیگیری رسمی."
    ),
    "150": (
        "Relies purely on infrastructure CPU/RAM gauges while business metrics (conversion rates, checkout volume) plummet.",
        "Pairs infrastructure monitoring with business-level telemetry and anomaly alerts tracking transaction volumes and conversion rates.",
        "اتکا صرف به مصرف رم و سی‌پی‌یو بدون پایش متریک‌های کسب‌وکار در حالی که آمار خرید به شدت سقوط کرده است.",
        "ترکیب مانیتورینگ سخت‌افزار با تله‌متری بیزینسی و هشدار آنی در صورت افت ناگهانی تراکنش‌های خرید."
    ),
    "163": (
        "Fails to alert engineers when cross-tenant data leaks occur, learning about privacy breaches from furious customer emails.",
        "Instruments anomaly detection alerts on unexpected tenant ID mismatches and immediately terminates suspicious sessions.",
        "فقدان سیستم هشدار در زمان نشت داده بین سازمان‌ها و باخبر شدن از فاجعه صرفاً با ایمیل شکایت مشتریان.",
        "تنظیم سیستم هشدار بلادرنگ در صورت بروز مغایرت در شناسه سازمان و قطع فوری نشست‌های مشکوک."
    ),
    "180": (
        "Monitors only hard thrown exceptions in code while missing silent functional failures like payment webhooks returning 200 on failure.",
        "Instruments business-level telemetry and anomaly alerts tracking webhook ingestion rates and business outcome drop-offs.",
        "اتکا صرف به خطاهای پرتاب‌شده و ندیدن شکست‌های خاموش مانند وب‌هوک‌هایی که بدون پردازش کد ۲۰۰ می‌دهند.",
        "پایش متریک‌های بیزینسی، ردیابی افت ناگهانی وب‌هوک‌ها و هشدار بلادرنگ در صورت بروز مغایرت مالی."
    ),
    "183": (
        "Assumes error trackers catch every production failure without deploying end-to-end synthetic canary health checks.",
        "Deploys automated synthetic transaction canaries verifying payment webhook pipelines end-to-end around the clock.",
        "فرض بر اینکه ابزارهای مانیتورینگ همه خطاها را ثبت می‌کنند بدون اجرای تراکنش‌های تستی دوره‌ای.",
        "راه‌اندازی تست‌های قناری مصنوعی (Synthetic Monitoring) برای اعتبارسنجی ۲۴ ساعته وب‌هوک‌های مالی."
    ),
    "199": (
        "Floods log files with millions of unformatted string messages, making root cause analysis impossible during outages.",
        "Emits structured JSON logs containing standardized log levels, ISO timestamps, error stack traces, and request correlation IDs.",
        "پر کردن فایل‌های لاگ با میلیون‌ها خط متن نامنظم که ریشه‌یابی خطاها را در زمان بحران غیرممکن می‌کند.",
        "تولید لاگ‌های ساختاریافته JSON با سطوح لاگینگ مشخص، زمان‌بندی دقیق و شناسه ردگیری درخواست."
    ),
    "205": (
        "Leaves uncaught exceptions and unhandled promise rejections unhandled in Node.js, crashing the server process silently.",
        "Registers global process handlers for uncaughtException and unhandledRejection, logging context to Sentry with graceful restart.",
        "رها کردن خطاهای زمان اجرا در نودجی‌اس که موجب کرش ناگهانی و خاموش شدن بی‌صدای سرور می‌شود.",
        "تعریف هندلرهای سراسری برای uncaughtException، لاگ خطا به سنتری و ری‌استارت ایمن توسط PM2/داکر."
    ),
    "250": (
        "Charges flat subscription fees without tracking per-customer resource usage, operating heavy users at a net loss.",
        "Instruments per-tenant compute and API usage metrics to establish accurate unit economics and dynamic pricing tiers.",
        "تعیین هزینه اشتراک ثابت بدون اندازه‌گیری میزان مصرف مشتریان که موجب زیان‌ده شدن کاربران پرمصرف می‌شود.",
        "پایش دقیق میزان مصرف منابع و درخواست‌های API به ازای هر مشتری جهت تنظیم قیمت‌گذاری عادلانه و سودآور."
    ),
    "267": (
        "Treats Layer 12 Observability as an afterthought, shipping code without health checks or centralized error tracking.",
        "Establishes Layer 12 observability standards: `/healthz` endpoints, Sentry error capture, and OpenTelemetry distributed tracing.",
        "نگاه تزئینی به لایه دوازدهم مانیتورینگ و انتشار برنامه بدون مسیرهای بررسی سلامت و ردیابی خطا.",
        "پیاده‌سازی استانداردهای لایه ۱۲: اندپوینت `/healthz`، ثبت خطا در سنتری و ردگیری توزیع‌شده با OpenTelemetry."
    ),
    "295": (
        "Leaves debugging statements (`console.log`) and internal error details active in production frontend code.",
        "Strips `console.log` statements in production build pipelines and routes client errors to Sentry with PII scrubbing.",
        "رها کردن دستورات دیباگ و لاگ‌های کنسول در کد فرانت‌اند پروداکشن که ساختار داخلی را به کاربر نشان می‌دهد.",
        "حذف خودکار دستورات console.log در زمان بیلد نهایی و ارسال خطاهای مرورگر به سنتری با حذف داده‌های حساس."
    ),
    "303": (
        "Operates production servers without automated uptime alerting, discovering outages only when users complain on Twitter.",
        "Configures independent multi-region uptime checks pinging health endpoints every 60 seconds with PagerDuty SMS escalation.",
        "عدم استفاده از هشدارهای مانیتورینگ که باعث می‌شود تیم قطعی سرور را از اعتراضات کاربران در شبکه‌های اجتماعی بفهمد.",
        "تنظیم مانیتورینگ آپ‌تایم چندمنطقه‌ای با تست هر ۶۰ ثانیه و اتصال به سامانه پیامک و تلفن اضطراری آنکال."
    ),
    "313": (
        "Relies on customer support tickets to detect broken features instead of proactive error monitoring systems.",
        "Integrates proactive Real User Monitoring (RUM) and error threshold alerts that notify engineers within 60 seconds of spikes.",
        "اتکا به تیکت‌های پشتیبانی کاربران برای فهمیدن خرابی بخش‌های برنامه به جای سیستم‌های مانیتورینگ فعال.",
        "پیاده‌سازی مانیتورینگ زنده کاربران (RUM) و هشدار خودکار در صورت افزایش خطاها ظرف کمتر از ۶۰ ثانیه."
    ),
    "321": (
        "Runs applications without automated healthcheck probes, causing container orchestrators to route traffic to dead instances.",
        "Implements separate `/health/liveness` and `/health/readiness` probes for automated Kubernetes/Docker restart and routing.",
        "اجرای برنامه بدون اندپوینت بررسی سلامت که باعث می‌شود داکر ترافیک را به کانتینرهای ازکارافتاده بفرستد.",
        "پیاده‌سازی اندپوینت‌های استاندارد Liveness و Readiness برای ری‌استارت خودکار کانتینرهای معیوب."
    )
}

print(f"Loaded Part 1 definitions: {len(PART1_DATA)} episodes")
