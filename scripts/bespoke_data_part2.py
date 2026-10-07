#!/usr/bin/env python3
"""
Bespoke matrices for Part 2:
Modules:
- 07-async-queues-webhooks (19 episodes)
- 08-multi-tenancy (6 episodes)
- 09-ai-guardrails (46 episodes)
- 10-cicd-deployments (39 episodes)
- 11-cloud-finops (32 episodes)
- 12-frontend-api-hygiene (37 episodes)
Total: 179 episodes
"""

PART2_DATA = {
    # ==========================================
    # 07-ASYNC-QUEUES-WEBHOOKS (19 episodes)
    # ==========================================
    "006": (
        "Parses Stripe webhook JSON bodies before verification, allowing forged fake payment events to trigger product fulfillment.",
        "Verifies HMAC signatures using the raw unparsed request Buffer (`express.raw`) and locks event IDs in Redis for idempotency.",
        "پارس کردن جیسون هوک‌های پرداختی قبل از بررسی امضا که به مهاجم اجازه جعل رویداد پرداخت می‌دهد.",
        "اعتبارسنجی امضای رمزنگاری‌شده روی بافر خام و قفل کردن شناسه رویداد در ردیس برای جلوگیری از پردازش مکرر."
    ),
    "028": (
        "Processes payment transactions without idempotency keys, charging user credit cards twice during network retry storms.",
        "Attaches client-generated idempotency keys (`idempotency_key`) to payment mutations, rejecting duplicate charges in Redis.",
        "پردازش تراکنش‌های پرداخت بدون کلیدهای تکرارناپذیری که در زمان قطعی موقت شبکه کارت مشتری را دو بار شارژ می‌کند.",
        "استفاده از کلیدهای تکرارناپذیری (`idempotency_key`) در تراکنش‌ها و رد کردن درخواست‌های تکراری با قفل ردیس."
    ),
    "046": (
        "Reads purchase prices directly from client request bodies, allowing attackers to buy $500 items for $1 via API tampering.",
        "Creates checkout sessions strictly on the server using database Price IDs, verifying payment state via signed webhooks.",
        "خواندن قیمت محصول از فرانت‌اند در درخواست پرداخت که به خریدار اجازه می‌دهد قیمت ۵۰۰ دلاری را به ۱ دلار تغییر دهد.",
        "ایجاد نشست خرید منحصراً در سمت سرور با شناسه‌های رسمی قیمت (Price ID) و تایید وضعیت پرداخت از طریق وب‌هوک."
    ),
    "062": (
        "Accepts incoming webhooks without verifying digital signatures, letting attackers inject counterfeit payment confirmations.",
        "Validates cryptographic webhook signatures against the raw unparsed payload buffer before dispatching business logic.",
        "پذیرش وب‌هوک‌های ورودی بدون اعتبارسنجی امضای دیجیتال که به نفوذگر امکان تزریق پرداخت‌های جعلی را می‌دهد.",
        "اعتبارسنجی امضای کریپتوگرافیک بافر خام وب‌هوک پیش از ارسال داده‌ها به بخش منطق تجاری برنامه."
    ),
    "075": (
        "Dispatches separate payout micro-transactions for each event, burning significant revenue on fixed processor transaction fees.",
        "Batches user payouts and transfers into scheduled settlement windows, minimizing flat-rate transaction fee overhead.",
        "ارسال تراکنش‌های خرد و مجزا برای هر واریزی که بخش بزرگی از درآمد را صرف کارمزدهای ثابت بانکی می‌کند.",
        "تجمیع واریزی‌ها در بازه‌های زمانی مشخص (Batching) جهت کاهش شدید هزینه‌های کارمزد درگاه‌های پرداخت."
    ),
    "076": (
        "Executes heavy webhook processing directly inside synchronous HTTP handler threads, crashing the server under event spikes.",
        "Enqueues incoming webhook payloads into asynchronous Redis queues (BullMQ/SQS) with Dead-Letter Queues (DLQ) for retries.",
        "اجرای عملیات سنگین وب‌هوک‌ها درون ترد اصلی وب‌سرور که در زمان هجوم رویدادها موجب کرش سرور می‌شود.",
        "انتقال وب‌هوک‌ها به صف‌های پس‌زمینه (BullMQ/SQS) با مدیریت خطای DLQ و پاسخ سریع ۲۰۰ به سرور ارسال‌کننده."
    ),
    "084": (
        "Spawns unbounded concurrent background workers during viral traffic bursts, overwhelming and crashing downstream databases.",
        "Enforces worker pool concurrency limits with token buckets and backpressure controls to protect downstream services.",
        "اجرای همزمان و بدون سقف ورکرها در زمان ترافیک بالا که موجب اشباع و قطعی کامل دیتابیس مقصد می‌شود.",
        "اعمال سقف همزمانی برای ورکرها با الگوی کنترل فشار معکوس (Backpressure) جهت محافظت از دیتابیس."
    ),
    "098": (
        "Executes external automated actions immediately upon AI agent tool calls without security verification or human oversight.",
        "Places high-impact asynchronous tool executions behind signed webhook authorization gates with step-up verification.",
        "اجرای فوری عملیات‌های بیرونی توسط ابزارهای هوش مصنوعی بدون تایید امنیتی یا نظارت انسانی.",
        "قرار دادن ابزارهای حساس در صف تایید امنیتی همراه با احراز هویت دومرحله‌ای قبل از اجرای نهایی."
    ),
    "107": (
        "Executes synchronous multi-page web scraping in foreground HTTP requests, hitting gateway timeouts and hanging user browsers.",
        "Delegates web extraction workloads to background queue workers, notifying clients asynchronously via WebSockets or polling.",
        "اجرای اسکرپینگ چند صفحه‌ای به صورت همزمان در درخواست کاربر که موجب تایم‌اوت مرورگر و مسدود شدن سرور می‌شود.",
        "انتقال پردازش‌های سنگین استخراج داده به صف‌های پس‌زمینه و اعلام نتیجه به کلاینت از طریق وب‌سوکت یا پولینگ."
    ),
    "122": (
        "Provisions paid user features immediately on frontend redirect without awaiting cryptographically verified webhook receipts.",
        "Gates premium feature provisioning strictly on verified asynchronous `checkout.session.completed` webhook receipts.",
        "فعال‌سازی اشتراک پولی بلافاصله پس از ریدایرکت مرورگر بدون دریافت و اعتبارسنجی تاییدیه قطعی وب‌هوک درگاه.",
        "وابسته‌سازی فعال‌سازی قابلیت‌های پریمیوم صرفاً به دریافت موفق وب‌هوک رسمی پرداخت از سوی درگاه بانکی."
    ),
    "123": (
        "Collects multi-state e-commerce revenue without calculating dynamic jurisdictional sales tax, incurring massive tax penalties.",
        "Integrates automated sales tax webhooks (Stripe Tax/TaxJar) calculating precise jurisdictional liability per transaction.",
        "فروش محصول به استان‌ها و ایالت‌های مختلف بدون محاسبه مالیات محلی که جریمه‌های سنگین مالیاتی به همراه دارد.",
        "اتصال به وب‌هوک‌های محاسبه خودکار مالیات بر ارزش افزوده در هر خرید متناسب با آدرس دقیق مشتری."
    ),
    "127": (
        "Misses silent webhook ingestion drops, losing thousands of dollars in unbilled subscription renewals without alerts.",
        "Monitors webhook ingestion telemetry and alerts engineers if payment event arrival rates drop below expected thresholds.",
        "غفلت از قطع شدن وب‌هوک‌های تمدید اشتراک که باعث تمدید نشدن فاکتورها و از دست رفتن درآمد بدون خبر می‌شود.",
        "پایش پیوسته نرخ دریافت وب‌هوک‌ها و هشدار فوری به تیم در صورت افت غیرعادی رویدادهای مالی."
    ),
    "129": (
        "Leaves payment dispute webhooks unhandled, resulting in automated account freezes and lost dispute challenge windows.",
        "Listens for `charge.dispute.created` webhooks, notifying support teams instantly and automating evidence submission pipelines.",
        "عدم پردازش وب‌هوک‌های مغایرت و ادعای کلاهبرداری بانکی که موجب مسدودی حساب پذیرنده توسط استرایپ می‌شود.",
        "شنود رویدادهای ایجاد ادعا (Dispute) و ارسال خودکار مدارک و اعلان فوری به تیم مالی جهت مهار خسارت."
    ),
    "166": (
        "Fails to monitor failed webhook retries, leaving payment discrepancies unresolved for six hours during production outages.",
        "Routes failed webhook events to Dead-Letter Queues (DLQ) with PagerDuty alerts after three automated exponential backoff attempts.",
        "نادیده گرفتن وب‌هوک‌های شکست‌خورده که مغایرت‌های مالی را به مدت ۶ ساعت در قطعی‌ها پنهان نگه می‌دارد.",
        "انتقال رویدادهای ناموفق به صف خطای اختصاصی (DLQ) پس از ۳ بار تلاش مجدد با هشدار فوری به مهندس آنکال."
    ),
    "185": (
        "Ignores drops in payment processing success rates, mistaking third-party payment gateway outages for normal sales slumps.",
        "Tracks end-to-end checkout conversion rates and alerts on statistical drops in payment provider authorization ratios.",
        "بی‌توجهی به افت آمار پرداخت‌های موفق و اشتباه گرفتن قطعی درگاه با کاهش عادی فروش در روزهای تعطیل.",
        "رصد مداوم نرخ موفقیت تراکنش‌های درگاه پرداخت و هشدار بلادرنگ در صورت افت آماری غیرطبیعی."
    ),
    "223": (
        "Fails to handle transient payment gateway 500 errors gracefully, abandoning transactions instead of retrying securely.",
        "Applies automated exponential backoff with jitter on transient gateway failures while preserving idempotency tokens.",
        "رها کردن تراکنش‌های پرداخت با اولین خطای موقت ۵۰۰ درگاه بدون تلاش مجدد اصولی.",
        "اعمال تلاش مجدد با تاخیر تصادفی نمایی (Exponential Backoff with Jitter) همراه با حفظ کلید تکرارناپذیری."
    ),
    "248": (
        "Holds HTTP connections open for 45 seconds while processing heavy tasks, hitting edge proxy connection timeouts.",
        "Responds immediately with HTTP 202 Accepted, delegating heavy operations to background queues with status polling.",
        "باز نگه داشتن ارتباط HTTP به مدت ۴۵ ثانیه برای یک پردازش سنگین که باعث قطعی ارتباط توسط کلودفلر می‌شود.",
        "پاسخ فوری با کد وضعیت ۲۰۲ Accepted و ارسال تسک سنگین به صف پس‌زمینه با قابلیت استعلام وضعیت."
    ),
    "266": (
        "Freezes user HTTP requests during slow generative AI completions, crashing when browsers timeout after 30 seconds.",
        "Streams long-running AI completions over Server-Sent Events (SSE) or offloads to async workers with progress callbacks.",
        "فریز کردن درخواست وب کاربر در زمان پردازش‌های طولانی هوش مصنوعی که منجر به خطای تایم‌اوت مرورگر می‌شود.",
        "ارسال استریم نتایج با Server-Sent Events (SSE) یا استفاده از ورکر پس‌زمینه همراه با گزارش پیشرفت کار."
    ),
    "275": (
        "Executes long-running video or AI processing pipelines inside serverless functions, hitting hard Vercel execution limits.",
        "Offloads long-running processing tasks to dedicated long-lived container workers (Fly/ECS) decoupled via message queues.",
        "اجرای پردازش‌های سنگین ویدیویی در توابع سرورلس که با رسیدن به سقف زمان اجرای سرورلس قطع می‌شوند.",
        "انتقال پردازش‌های طولانی‌مدت به کانتینرهای اختصاصی دائم‌کار از طریق سیستم صف پیام مستقل."
    ),

    # ==========================================
    # 08-MULTI-TENANCY (6 episodes)
    # ==========================================
    "061": (
        "Attempts to build multi-tenant SaaS platforms by creating separate databases per tenant, creating operational maintenance nightmares.",
        "Employs shared database architectures with strict PostgreSQL Row-Level Security (RLS) enforcing tenant isolation at scale.",
        "تلاش برای پیاده‌سازی سیستم چندسازمانی با ساخت دیتابیس مجزا برای هر مشتری که نگهداری آن کابوس عملیاتی است.",
        "استفاده از معماری دیتابیس مشترک با امنیت سطر دیتابیس (Row-Level Security) جهت ایزولاسیون کامل و مقیاس‌پذیر."
    ),
    "156": (
        "Shares global database tables across tenants without automated tenant-scoping assertions, risking cross-tenant data leaks.",
        "Enforces tenant context scoping on all queries and validates tenant isolation using automated multi-tenant regression suites.",
        "اشتراک‌گذاری جداول عمومی بین سازمان‌ها بدون بررسی اجباری شناسه سازمان که ریسک نشت داده‌ها را به همراه دارد.",
        "اجبار شناسه سازمان در تمام کوئری‌ها و اعتبارسنجی ایزولاسیون با تست‌های خودکار رگرسیون چندسازمانی."
    ),
    "190": (
        "Deploys PostgreSQL Row-Level Security policies without verifying that application database users bypass superuser privileges.",
        "Runs application database connections under dedicated non-superuser roles with `FORCE ROW LEVEL SECURITY` enabled on tables.",
        "فعال‌سازی سیاست‌های RLS در حالی که برنامه با کاربر Superuser به دیتابیس وصل می‌شود و تمام RLSها دور زده می‌شوند.",
        "اتصال برنامه به دیتابیس با کاربر غیر-Superuser و فعال‌سازی اجباری `FORCE ROW LEVEL SECURITY` روی تمام جداول."
    ),
    "221": (
        "Relies on fragile application-level ORM filters (`where: { tenantId }`), risking catastrophic data leaks if a single query forgets it.",
        "Enforces tenant isolation natively at the database engine level via PostgreSQL Row-Level Security (RLS) policies.",
        "اتکا به فیلترهای ساده کد در ORM که اگر در یک کوئری فراموش شود کل اطلاعات مشتریان دیگر افشا می‌شود.",
        "اعمال ایزولاسیون سازمان‌ها مستقیماً در هسته دیتابیس با سیاست‌های سفت‌وسخت Row-Level Security (RLS)."
    ),
    "225": (
        "Treats multi-tenant architecture as a purely technical decision, ignoring enterprise customer compliance and silo requirements.",
        "Supports flexible tenant isolation tiers: cost-effective shared pooling for standard users and dedicated silo databases for enterprise tiers.",
        "نگاه صرفاً فنی به چندمستأجری بدون توجه به الزامات قانونی و امنیتی سازمان‌های بزرگ برای تفکیک فیزیکی داده‌ها.",
        "ارائه مدل‌های منعطف: دیتابیس مشترک با RLS برای مشتریان عادی و دیتابیس اختصاصی (Silo) برای مشتریان اینترپرایز."
    ),
    "270": (
        "Builds multi-tenant platforms without scoping file storage or cache keys, allowing users to view peer organization assets.",
        "Enforces composite tenant namespaces across all 13 layers: database tables, Redis cache keys, S3 storage prefixes, and logs.",
        "ساخت پلتفرم چندسازمانی بدون تفکیک پوشه‌های استوریج و کلیدهای کش که فایل‌های یک سازمان را به دیگری لو می‌دهد.",
        "تفکیک سازمان‌ها در تمامی ۱۳ لایه: جداول دیتابیس، کلیدهای کش ردیس، پیشوندهای استوریج S3 و فایل‌های لاگ."
    ),

    # ==========================================
    # 09-AI-GUARDRAILS (46 episodes)
    # ==========================================
    "001": (
        "Deploys generative AI features without synthetic media watermarks (SGI) or consent gates, violating EU AI Act Art. 50.",
        "Embeds non-removable SGI metadata, enforces affirmative user consent gates, and logs prompt hashes to immutable tables.",
        "انتشار خروجی‌های هوش مصنوعی بدون متادیتای SGI و نقض ماده ۵۰ قانون هوش مصنوعی اتحادیه اروپا.",
        "الصاق متادیتای تغییرناپذیر SGI، فعال‌سازی گیت رضایت صریح کاربر و ثبت لاگ پرامپت‌ها در جداول امن."
    ),
    "008": (
        "Assumes prototype healthcare AI software is HIPAA-compliant without verifiable audit trails, encryption at rest, or access controls.",
        "Implements end-to-end encryption at rest/transit, role-based access controls, automated session timeouts, and immutable audit logging.",
        "فرض بر رعایت استانداردهای HIPAA بدون رمزنگاری در حالت سکون، سیستم نقش‌ها و ثبت لاگ تغییرناپذیر.",
        "پیاده‌سازی رمزنگاری کامل سرتاسری، کنترل دسترسی مبتنی بر نقش (RBAC) و لاگ‌های حسابرسی تغییرناپذیر."
    ),
    "013": (
        "Leaves 1,400 lines of complex application code in a single monolithic file because an AI assistant advised against refactoring.",
        "Enforces enterprise modular architecture, decomposing monolithic files into typed, isolated domain services regardless of AI bias.",
        "رها کردن ۱۴۰۰ خط کد در یک فایل تکی به این دلیل که هوش مصنوعی توصیه به دست نزدن به آن کرده است.",
        "اعمال استانداردهای معماری تمیز و تفکیک فایل‌های بزرگ به سرویس‌های ماژولار و تایپ‌شده فارغ از سوگیری مدل."
    ),
    "014": (
        "Postpones fundamental legal compliance documents (Privacy Policy, Terms of Service, DPA) until after achieving product revenue.",
        "Establishes a 90-day compliance calendar with automated compliance platforms and quarterly privacy reviews.",
        "به تعویق انداختن مستندات قانونی اساسی (حریم خصوصی، قوانین خدمات، توافق DPA) تا بعد از درآمدزایی.",
        "تنظیم تقویم ۹۰ روزه انطباق قانونی با ابزارهای خودکار و بازبینی دوره‌ای سیاست‌های حریم خصوصی."
    ),
    "025": (
        "Believes vendor marketing hype around new frontier models without running deterministic regression benchmarks against private data.",
        "Establishes internal automated evaluation test suites to benchmark speed, cost, and hallucination rates before switching models.",
        "باور کردن ادعاهای تبلیغاتی مدل‌های جدید بدون اجرای بنچمارک‌های رگرسیون روی داده‌های واقعی شرکت.",
        "راه‌اندازی مجموعه تست‌های ارزیابی داخلی جهت سنجش سرعت، هزینه و خطای مدل قبل از تغییر ارائه‌دهنده."
    ),
    "029": (
        "Upgrades production LLM models instantly on release day, breaking downstream schema parsers with unannounced prompt drift.",
        "Pins exact model version snapshots (`gpt-4o-2024-08-06`) and verifies structured output schemas in staging prior to production promotion.",
        "تعویض آنی نسخه مدل در روز اول انتشار که به دلیل تغییر نامحسوس ساختار پاسخ‌ها، کدهای فرانت‌اند را می‌شکند.",
        "استفاده از اسنپ‌شات‌های نسخه‌دار مدل‌ها و راستی‌آزمایی خروجی‌های ساختاریافته در استیجینگ قبل از اعمال در پروداکشن."
    ),
    "030": (
        "Exposes proprietary system prompts and confidential business logic in client-side code, allowing trivial prompt reverse-engineering.",
        "Encapsulates system prompts behind authenticated backend API proxies, returning only sanitized domain responses to clients.",
        "قرار دادن پرامپت‌های اختصاصی و بیزینس لاجیک محرمانه در کلاینت که سرقت و کپی آن را بسیار آسان می‌کند.",
        "محصور کردن پرامپت‌ها در لایه امن سرور بک‌اند و بازگرداندن صرفاً نتایج پالایش‌شده به کلاینت."
    ),
    "036": (
        "Runs autonomous AI agents on borrowed master API credentials with unrestricted tool execution permissions across production.",
        "Scopes AI agent credentials to least-privilege, short-lived tokens with strict read-only boundaries and human approval gates.",
        "اجرای ایجنت‌های هوش مصنوعی با کلیدهای مستر ادمین که به ایجنت دسترسی نامحدود به دیتابیس و کارهای حساس می‌دهد.",
        "محدودسازی دسترسی ایجنت‌ها به توکن‌های کوتاه‌مدت با کمترین سطح دسترسی و گیت تایید انسانی برای تغییرات مهم."
    ),
    "042": (
        "Relies on vibe coding assumptions and blind generative iterations without understanding fundamental software engineering trade-offs.",
        "Grounds software construction in timeless engineering principles: mathematical invariants, algorithmic efficiency, and race safety.",
        "اتکای صرف به کدنویسی حسی (Vibe Coding) بدون درک اصول بنیادین و بده‌بستان‌های معماری نرم‌افزار.",
        "اتصال محکم توسعه نرم‌افزار به اصول مهندسی: ناورداهای ریاضی، پیچیدگی محاسباتی و ایمنی همزمانی."
    ),
    "051": (
        "Overloads AI agent context windows with 47 simultaneous skill instructions, causing severe attention degradation and instruction drift.",
        "Dynamically activates domain skills on-demand using intent classifiers, keeping agent active context lean and focused.",
        "پر کردن کانتکست هوش مصنوعی با ۴۷ مهارت همزمان که تمرکز مدل را به شدت کاهش داده و دستورات را نادیده می‌گیرد.",
        "فراخوانی پویای مهارت‌ها صرفاً بر اساس نیاز لحظه‌ای و تمیز نگه داشتن کانتکست کاری مدل."
    ),
    "060": (
        "Allows AI agents to fetch arbitrary user-supplied URLs without validation, opening critical Server-Side Request Forgery (SSRF) bypasses.",
        "Blocks internal VPC subnets, loopback addresses (`127.0.0.1`), and cloud metadata endpoints (`169.254.169.254`) from agent requests.",
        "اجازه به ایجنت‌ها برای وب‌گردی و واکشی هر لینک دلخواه کاربر که راه نفوذ SSRF به شبکه داخلی سرور را باز می‌کند.",
        "مسدودسازی دسترسی ایجنت به شبکه‌های داخلی، آدرس لوکال‌هاست و اندپوینت اطلاعات ابری سرور (`169.254.169.254`)."
    ),
    "063": (
        "Binds application architectures to proprietary cloud AI orchestration services that deprecate and rename features abruptly.",
        "Builds AI agent workflows using modular, open abstractions (LangGraph/Custom State Machines) decoupled from proprietary cloud silos.",
        "چسباندن سیستم به سرویس‌های ارکستراسیون اختصاصی ابر که با تغییر یا توقف ناگهانی سرویس کل پروژه را مختل می‌کنند.",
        "توسعه فرآیندهای ایجنت با الگوهای ماژولار و مستقل از ابر جهت حفظ مالکیت و قابلیت انتقال سیستم."
    ),
    "073": (
        "Spends thousands of dollars on unmonitored AI token usage without tracking token consumption per user, feature, or endpoint.",
        "Instruments per-user and per-feature token telemetry, enforcing automated spend alerts and strict monthly quota limits.",
        "هدررفت هزاران دلار در مصرف توکن‌های هوش مصنوعی بدون ردیابی دقیق اینکه کدام کاربر یا بخش برنامه هزینه را ایجاد کرده است.",
        "ثبت دقیق مصرف توکن به تفکیک کاربر و اندپوینت همراه با سقف بودجه مشخص و قطع خودکار در سقف مصرف."
    ),
    "081": (
        "Releases AI-generated features directly to paying customers without running adversarial evaluation suites or red-teaming.",
        "Runs automated evaluation pipelines testing prompts against prompt injection attacks, schema violations, and toxic outputs.",
        "انتشار قابلیت‌های هوش مصنوعی به مشتریان بدون انجام تست‌های ارزیابی خصمانه و ارزیابی نفوذپذیری پرامپت.",
        "راه‌اندازی پایپ‌لاین‌های خودکار ارزیابی برای بررسی مقاومت سیستم در برابر تزریق پرامپت و خروجی‌های نامعتبر."
    ),
    "085": (
        "Assumes Model Context Protocol (MCP) servers solve all agent integration hurdles without securing local socket tool execution.",
        "Applies rigorous sandbox isolation, input validation, and execution rate limits to all Model Context Protocol (MCP) tool endpoints.",
        "فرض بر اینکه MCP همه مشکلات را حل می‌کند بدون توجه به خطرات اجرای ابزارهای محلی روی سیستم عامل سرور.",
        "قرنطینه‌سازی محیط اجرای ابزارهای MCP، اعتبارسنجی ورودی‌ها و تعیین سقف مجاز برای فراخوانی توابع سیستمی."
    ),
    "087": (
        "Leaves AI agent instructions hardcoded in database strings for six months without version control or continuous regression testing.",
        "Versions system prompts in Git repositories with automated evaluation tests run on every pull request to prevent performance drift.",
        "رها کردن پرامپت‌های ایجنت در دیتابیس برای ماه‌ها بدون نسخه‌گذاری گیت و بدون تست‌های منظم رگرسیون.",
        "نسخه‌گذاری پرامپت‌ها در مخزن گیت و اجرای تست‌های خودکار کیفیت در هر PR برای پیشگیری از افت کیفیت پاسخ‌ها."
    ),
    "088": (
        "Bloats products with decorative AI novelty features while core user workflows remain buggy, slow, and unverified.",
        "Focuses engineering bandwidth on hardening core business value paths, stripping gimmicky AI add-ons that fail to drive retention.",
        "پر کردن محصول با ویژگی‌های تزئینی و کم‌ارزش هوش مصنوعی در حالی که بخش‌های اصلی سیستم پر از باگ و کند است.",
        "تمرکز تمام توان مهندسی روی سخت‌سازی جریان اصلی ارزش محصول و حذف قابلیت‌های بیهوده‌ای که آورده‌ای ندارند."
    ),
    "095": (
        "Builds autonomous agents that forget task objectives halfway through execution due to unstructured, unbounded context growth.",
        "Implements structured state machines with explicit task scratchpads and periodic context summarization checkpoints.",
        "ساخت ایجنت‌هایی که در میانه راه هدف اصلی را فراموش می‌کنند چون کانتکست بیش از حد طولانی و شلوغ شده است.",
        "استفاده از ماشین‌های وضعیت ساختاریافته (State Machine) و خلاصه‌سازی دوره‌ای کانتکست جهت حفظ هدف نهایی."
    ),
    "097": (
        "Believes product ideas constitute defensible moats rather than continuous production execution speed and engineering rigor.",
        "Treats high-velocity, production-hardened engineering execution and customer retention loops as the only sustainable business moat.",
        "تصور اینکه ایده محصول مزیت رقابتی است، در حالی که بدون کیفیت اجرای مهندسی ایده هیچ ارزشی ندارد.",
        "تمرکز بر سرعت بالای اجرای مهندسی مقاوم، نگه‌داشت مشتریان و کیفیت زیرساخت به عنوان تنها مزیت واقعی رقابتی."
    ),
    "100": (
        "Ignores international data sovereignty laws, storing EU citizen personal data in un-audited US cloud regions without consent.",
        "Enforces regional data residency routing, cryptographic pseudonymization, and Article 50 AI Act transparency metadata.",
        "بی‌توجهی به قوانین حاکمیت داده و ذخیره اطلاعات شهروندان اروپا در سرورهای نامعتبر بدون رضایت و برچسب هوش مصنوعی.",
        "رعایت ایزولاسیون جغرافیایی داده‌ها، رمزنگاری و ثبت متادیتای شفافیت ماده ۵۰ قانون هوش مصنوعی اروپا."
    ),
    "108": (
        "Ships AI-generated UIs lacking accessibility standards, exposing companies to ADA lawsuits and locking out 1.3 billion users.",
        "Audits interfaces for WCAG AA compliance: enforces semantic HTML, full keyboard navigation, color contrast, and ARIA labels.",
        "انتشار فرانت‌اند تولیدی هوش مصنوعی بدون استانداردهای دسترس‌پذیری که موجب شکایت‌های حقوقی ADA می‌شود.",
        "ممیزی کامل رابط کاربری با استانداردهای WCAG AA: المان‌های معنایی، کار با کیبورد و کنتراست مناسب رنگ‌ها."
    ),
    "111": (
        "Designs APIs exclusively for human browser interaction, breaking automated AI agent integrations with unstructured HTML.",
        "Exposes machine-readable, schema-validated OpenAPI specifications and structured JSON endpoints for agent consumers.",
        "طراحی اندپوینت‌ها صرفاً برای مرورگرهای انسانی بدون ارائه ساختار شفاف که اتصال ایجنت‌های هوشمند را ناممکن می‌کند.",
        "ارائه مستندات استاندارد OpenAPI و خروجی‌های ساختاریافته JSON جهت تعامل روان با ایجنت‌های هوش مصنوعی."
    ),
    "113": (
        "Hardcodes single-currency assumptions and language strings into database schemas, blocking global market expansion.",
        "Architects internationalization (i18n) from inception: UTC timestamps, multi-currency decimal handling, and locale routing.",
        "هاردکد کردن زبان و واحد پولی در دیتابیس که گسترش برنامه به بازارهای جهانی را ناممکن می‌سازد.",
        "معماری بین‌المللی (i18n) از روز اول: زمان‌های UTC، پشتیبانی از واحدهای پولی با اعداد اعشاری دقیق و چندزبانی."
    ),
    "114": (
        "Relies on increasing LLM reasoning capabilities to fix broken code architectures, neglecting foundational engineering rigor.",
        "Applies rigorous software engineering constraints: deterministic static analysis, end-to-end integration tests, and typing.",
        "امید بستن به مدل‌های زبانی قوی‌تر برای درست کردن معماری خراب کد به جای اعمال اصول مهندسی نرم‌افزار.",
        "اعمال چارچوب‌های سخت‌گیرانه مهندسی: تحلیل ایستای کد، تست‌های یکپارچگی سرتاسری و سیستم تایپینگ سخت‌گیرانه."
    ),
    "115": (
        "Ships AI-scaffolded prototypes to production without basic defensive hardening: no input validation, error redaction, or headers.",
        "Applies pre-launch hardening gates: strict Zod input schemas, generic error boundaries, and OWASP security response headers.",
        "عرضه پروتوتایپ‌های تولیدی هوش مصنوعی به پروداکشن بدون اعتبارسنجی ورودی، ماسک خطا و هدرهای امنیتی.",
        "اعمال گیت‌های سخت‌سازی قبل از انتشار: اسکیماهای Zod، مخفی‌سازی پیام‌های خطای سرور و هدرهای امنیتی OWASP."
    ),
    "119": (
        "Deploys healthcare applications processing Protected Health Information (PHI) to non-compliant clouds without BAAs or audit logs.",
        "Executes Business Associate Agreements (BAAs), isolates PHI in dedicated encrypted partitions, and audits access trails.",
        "راه‌اندازی اپلیکیشن سلامت بدون قرارداد رسمی BAA با کلود و ذخیره اطلاعات بیماران بدون تفکیک و لاگ حسابرسی.",
        "عقد توافق‌نامه‌های BAA، رمزنگاری و تفکیک کامل داده‌های پزشکی (PHI) و ثبت لاگ‌های قانونی دسترسی."
    ),
    "126": (
        "Mistakes raw LLM code generation speed for production readiness without applying engineering verification or security audits.",
        "Pairs rapid LLM code generation with rigorous AI-directed engineering: deterministic testing, compliance checks, and hardening.",
        "اشتباه گرفتن سرعت بالای تولید کد هوش مصنوعی با آمادگی برای پروداکشن بدون بازبینی امنیتی و تست.",
        "ترکیب سرعت تولید کد هوش مصنوعی با مهندسی کنترل‌شده: تست‌های قطعی، ممیزی امنیتی و سخت‌سازی زیرساخت."
    ),
    "130": (
        "Charges paying customers for AI software before establishing registered business entities, exposing founders to personal liability.",
        "Registers formal business entities, establishes dedicated commercial banking pipelines, and enforces terms of service.",
        "دریافت وجه از مشتریان قبل از ثبت رسمی شرکت که موسسان را در معرض مسئولیت‌های سنگین حقوقی شخصی قرار می‌دهد.",
        "ثبت قانونی شرکت، افتتاح حساب‌های تجاری مستقل و اعمال شرایط رسمی خدمات قبل از شروع درآمدزایی."
    ),
    "144": (
        "Copies unverified coding tricks from social media into production without assessing race conditions or security boundaries.",
        "Evaluates third-party code patterns against formal production engineering criteria before adoption into mission-critical repos.",
        "کپی کردن راهکارهای اینستاگرامی در پروداکشن بدون سنجش شرایط مسابقه، نشت داده و مرزهای امنیتی.",
        "ارزیابی دقیق الگوهای کدنویسی بر اساس استانداردهای مهندسی سیستم پیش از استفاده در کدهای حساس بیزینس."
    ),
    "148": (
        "Deletes user records from primary tables while leaving orphaned PII in vector embeddings and LLM training caches.",
        "Automates comprehensive data deletion pipelines purging user PII across relational tables, vector stores, and cache layers.",
        "حذف کاربر از جدول اصلی در حالی که اطلاعات هویتی او در پایگاه برداری و کش‌های مدل زبانی باقی مانده است.",
        "اتوماسیون پاکسازی کامل اطلاعات کاربر از جداول رابطه‌ای، پایگاه‌های داده وکتوری و لایه‌های کش ردیس."
    ),
    "152": (
        "Builds commercial AI products based on toy introductory tutorials without implementing production failure recovery patterns.",
        "Architects production-grade agent workflows with circuit breakers, graceful degradation fallbacks, and human escalation gates.",
        "ساخت محصول تجاری بر پایه آموزش‌های ساده و مقدماتی بدون پیش‌بینی سناریوهای خرابی و بازیابی خطا.",
        "طراحی معماری ایجنت با فیوز قطع مدار (Circuit Breaker)، راهکارهای جایگزین در خرابی و ارجاع به اپراتور انسانی."
    ),
    "159": (
        "Relies on AI coding tools to design business logic architectures, resulting in tangled domain models and circular dependencies.",
        "Designs core domain models and transactional boundaries using domain-driven design before delegating implementation to AI.",
        "واگذاری طراحی معماری بیزینس لاجیک به هوش مصنوعی که منجر به وابستگی‌های چرخشی و کدهای نامفهوم می‌شود.",
        "طراحی اصولی مرزهای دامنه و مدل‌های بیزینس با متدولوژی DDD قبل از سپردن کدنویسی به هوش مصنوعی."
    ),
    "162": (
        "Deploys AI-generated APIs that unconditionally trust all incoming client payloads without schema validation or sanitization.",
        "Enforces strict server-side schema validation using Zod on every endpoint, rejecting un-whitelisted parameters by default.",
        "انتشار APIهای هوش مصنوعی که کورکورانه به تمام داده‌های ارسالی کلاینت بدون اعتبارسنجی اعتماد می‌کنند.",
        "اعمال اعتبارسنجی ۱۰۰٪ داده‌ها با Zod در سمت سرور و رد خودکار فیلدهای پیش‌بینی‌نشده در تمامی اندپوینت‌ها."
    ),
    "168": (
        "Executes synchronous AI model calls inside checkout transaction flows, causing 12-second latency and cart abandonments.",
        "Decouples AI enhancements from checkout paths, executing them asynchronously in background queues to keep checkouts sub-second.",
        "فراخوانی همزمان مدل هوش مصنوعی در فرآیند پرداخت که تاخیر ۱۲ ثانیه‌ای ایجاد کرده و خریداران را فراری می‌دهد.",
        "جداسازی پردازش‌های هوش مصنوعی از مسیر پرداخت و اجرای پس‌زمینه آن‌ها جهت حفظ سرعت زیر ۱ ثانیه خرید."
    ),
    "170": (
        "Chases every new developer tool release without standardizing internal coding workflows, fragmenting engineering velocity.",
        "Standardizes engineering workflows on a proven toolchain with shared linters, formatting rules, and CI automation.",
        "دنبال کردن وسواسی ابزارهای جدید بدون تثبیت جریان کاری تیم که موجب سردرگمی و افت سرعت توسعه می‌شود.",
        "استانداردسازی ابزارهای توسعه روی الگوهای اثبات‌شده همراه با لینترهای مشترک و اتوماسیون CI یکپارچه."
    ),
    "177": (
        "Leaves prototype mock data and temporary development shortcuts in production releases, causing intermittent customer data glitches.",
        "Audits codebases for prototype artifacts before launch, replacing mock data with resilient transactional database queries.",
        "رها کردن داده‌های ساختگی (Mock) و کدهای موقت در پروداکشن که منجر به خطاهای عجیب و متناقض برای کاربران می‌شود.",
        "پاکسازی کامل کدهای ماک و موقت قبل از دیپلوی و جایگزینی آن‌ها با کوئری‌های واقعی و امن پایگاه‌داده."
    ),
    "236": (
        "Evaluates AI model output quality solely by manual eyeballing, missing subtle hallucinations and regression bugs in edge cases.",
        "Implements automated Model-as-a-Judge evaluation suites benchmarking outputs against golden datasets on every prompt change.",
        "بررسی چشمی و دستی خروجی‌های هوش مصنوعی که باگ‌های ظریف و خطاهای توهم مدل در سناریوهای لبه را پنهان می‌کند.",
        "راه‌اندازی تست‌های ارزیابی خودکار (Model-as-a-Judge) و مقایسه خروجی با دیتاست‌های مرجع در هر تغییر پرامپت."
    ),
    "238": (
        "Streams raw, unvalidated LLM generation directly to frontend users, exposing users to prompt injection leaks and broken formatting.",
        "Validates and parses LLM outputs against strict JSON schemas (Zod) with regex sanitization before rendering in the UI.",
        "نمایش مستقیم و خام خروجی مدل به کاربر بدون اعتبارسنجی که خطرات نشت پرامپت و قالب‌بندی شکسته ایجاد می‌کند.",
        "پارس و اعتبارسنجی ساختار خروجی مدل با اسکیماهای Zod و پاکسازی عبارات نامعتبر قبل از رندر در UI."
    ),
    "240": (
        "Dumps entire chat history transcripts into AI context windows on every interaction, burning tokens and diluting agent attention.",
        "Implements hierarchical memory systems: compact working memory scratchpads combined with semantic vector retrieval for history.",
        "ارسال کل تاریخچه چت در کانتکست مدل در هر پیام که هزینه‌ها را سرسام‌آور کرده و دقت مدل را کاهش می‌دهد.",
        "پیاده‌سازی حافظه سلسله‌مراتبی: حافظه کوتاه‌مدت فشرده همراه با بازیابی وکتوری معنایی برای تاریخچه‌های گذشته."
    ),
    "241": (
        "Deploys chaotic multi-agent networks where agents talk in unconstrained loops, generating massive token bills without completing tasks.",
        "Structures multi-agent workflows as deterministic supervisor-worker state machines with strict turn limits and goal gates.",
        "راه‌اندازی شبکه‌ای از ایجنت‌ها که در حلقه‌های بی‌پایان با هم صحبت می‌کنند و بدون حل مسئله هزاران دلار توکن می‌سوزانند.",
        "معماری ایجنت‌ها به عنوان ماشین‌های وضعیت با ناظر مرکزی، سقف مشخص گفتگو و گیت‌های تایید پایان کار."
    ),
    "246": (
        "Routes all application requests to expensive frontier models, running up massive operating costs for trivial classification tasks.",
        "Implements model routing gateways: fast, low-cost models (8B) for classification and frontier models solely for complex reasoning.",
        "ارسال تمام درخواست‌ها به مدل‌های گران‌قیمت پرچمدار حتی برای کارهای ساده‌ای مثل دسته‌بندی متن.",
        "پیاده‌سازی گیت‌وی مسیریابی مدل‌ها: استفاده از مدل‌های سبک و ارزان برای کارهای اولیه و مدل‌های قوی صرفاً برای منطق پیچیده."
    ),
    "259": (
        "Abandons software engineering rigor for vibe coding, deploying un-tested AI code that crashes under real concurrency.",
        "Enforces software engineering foundations: unit test suites, integration tests, strict typing, and concurrency stress testing.",
        "کنار گذاشتن مهندسی نرم‌افزار به بهانه Vibe Coding که کدهای شکننده‌ای تولید می‌کند که زیر اولین بار ترافیک می‌شکنند.",
        "پایبندی به اصول مهندسی: تست‌های واحد و یکپارچگی، تایپینگ قوی و تست استرس سیستم زیر بار همزمانی بالا."
    ),
    "281": (
        "Launches commercial SaaS software without terms of service or privacy disclosures, risking legal action and payment processor bans.",
        "Publishes clear, legally compliant Terms of Service and Privacy Policies disclosing data practices before accepting customer signups.",
        "عرضه عمومی نرم‌افزار بدون قوانین استفاده و سیاست حریم خصوصی که ریسک پیگرد قانونی و مسدودی درگاه را دارد.",
        "انتشار شفاف قوانین استفاده و بیانیه حریم خصوصی منطبق با قوانین تجارت الکترونیک قبل از ثبت‌نام کاربران."
    ),
    "302": (
        "Operates in complete developer isolation, missing out on shared architectural lessons and production engineering patterns.",
        "Engages in senior engineering peer reviews and production post-mortems to continuously level up architectural judgment.",
        "کار کردن در انزوای کامل و غفلت از تجربیات معماری و الگوهای اثبات‌شده سایر مهندسان ارشد در پروداکشن.",
        "مشارکت در جلسات نقد معماری، بازبینی کد و مطالعه تحلیل حوادث (Post-mortem) جهت ارتقای خرد مهندسی."
    ),
    "309": (
        "Deploys no-code visual AI prototypes straight to enterprise customers without auditing backend security or API boundaries.",
        "Hardens visual AI exports by decoupling business logic into secure backend APIs with server-side authentication and rate limits.",
        "ارائه مستقیم پروتوتایپ‌های ابزارهای بصری هوش مصنوعی به مشتریان بدون ممیزی امنیت بک‌اند و مرزهای API.",
        "سخت‌سازی کدهای خروجی ابزارهای بصری با انتقال منطق تجاری به بک‌اند امن همراه با احراز هویت و ریت‌لیمیت."
    ),
    "310": (
        "Focuses on social media vanity metrics while production error rates and unhandled exceptions spike unnoticed in backend systems.",
        "Directs focus to real engineering KPIs: system uptime, p99 latency, error rates, and deterministic test suite passes.",
        "تمرکز بر آمارهای شبکه‌های اجتماعی در حالی که خطاهای سرور و کرش‌های برنامه در بک‌اند اوج گرفته است.",
        "تمرکز روی شاخص‌های واقعی مهندسی: آپ‌تایم سیستم، تاخیر صدک ۹۹، نرخ خطاها و تست‌های موفقیت‌آمیز پایپ‌لاین."
    ),

    # ==========================================
    # 10-CICD-DEPLOYMENTS (39 episodes)
    # ==========================================
    "002": (
        "Treats production software as a single monolith without architectural boundaries across layers, causing cascading outages.",
        "Enforces strict isolation across all 13 production layers from edge UI to disaster recovery with automated verification gates.",
        "نگاه یکپارچه و فاقد مرزبندی به معماری سیستم که موجب انتشار خرابی در سراسر پلتفرم می‌شود.",
        "اعمال مرزبندی شفاف در استک سیزده‌گانه تولید از لایه فرانت‌اند تا بازیابی بحران همراه با تست‌های خودکار."
    ),
    "074": (
        "Pushes 47 disparate code files directly to production in a single un-reviewed commit, making bug isolation impossible.",
        "Breaks feature changes into small, atomic pull requests protected by feature flags and automated CI verification gates.",
        "ارسال ۴۷ فایل دستکاری‌شده به پروداکشن در یک کامیت واحد بدون بازبینی که عیب‌یابی را غیرممکن می‌کند.",
        "تقسیم تغییرات به PRهای کوچک و اتمیک با فیچر فلگ و سپردن تست‌های اعتبارسنجی به گیت‌های خودکار CI."
    ),
    "092": (
        "Uses AI coding tools to bypass staging environments, deploying unverified prototype code straight to paying users.",
        "Enforces automated CI/CD staging environments where AI-authored code passes automated regression tests before production release.",
        "دور زدن محیط استیجینگ با تکیه بر کد هوش مصنوعی و فرستادن کدهای تست‌نشده مستقیماً به دست کاربران.",
        "ایجاد محیط‌های خودکار استیجینگ که در آن کدهای هوش مصنوعی قبل از انتشار، تست‌های رگرسیون را با موفقیت پاس کنند."
    ),
    "096": (
        "Treats business software as disposable weekend scripts without continuous integration, automated builds, or rollback plans.",
        "Adopts enterprise CI/CD standards: automated test pipelines, reproducible Docker builds, and instant canary rollback capabilities.",
        "نگاه سرسری به نرم‌افزار کسب‌وکار به عنوان اسکریپت‌های موقت بدون خط استقرار، بیلد خودکار و پلن بازگشت.",
        "به‌کارگیری استانداردهای CI/CD: پایپ‌لاین تست خودکار، ایمیج‌های تکرارپذیر داکر و امکان بازگشت آنی قناری (Canary Rollback)."
    ),
    "135": (
        "Pushes code commits directly to production branches without branch protection rules, automated tests, or review gates.",
        "Enforces protected main branches requiring green CI build checks, automated linting, and peer approvals before deployment.",
        "پوش مستقیم کامیت‌ها روی برنچ اصلی بدون قوانین محافظت، تست‌های خودکار و بدون نیاز به تایید همکاران.",
        "قفل کردن برنچ اصلی، اجبار پاس شدن تست‌های CI، لینترهای خودکار و تاییدیه قبل از امکان مرج و استقرار."
    ),
    "137": (
        "Allows developers to merge AI-generated code without automated security testing, flooding codebases with security anti-patterns.",
        "Integrates automated static analysis (SAST) and secret scanning into pull request pipelines to verify all AI-generated code.",
        "ادغام مستقیم کدهای تولیدی هوش مصنوعی توسط برنامه‌نویسان بدون تست امنیتی که آسیب‌پذیری‌ها را وارد سیستم می‌کند.",
        "یکپارچه‌سازی اسکنرهای تست استاتیک (SAST) و اسکن کلیدها در پایپ‌لاین PR برای بررسی کدهای تولیدی هوش مصنوعی."
    ),
    "142": (
        "Waits for the first major production outage before writing operational runbooks, panicking when user databases crash.",
        "Authors clear incident response runbooks with documented rollback steps, database failover procedures, and on-call escalation paths.",
        "انتظار تا زمان وقوع اولین فاجعه در پروداکشن برای نوشتن دستورالعمل بحران و دستپاچگی تیم در زمان خوابیدن دیتابیس.",
        "نگارش دستورالعمل‌های شفاف مدیریت بحران (Runbooks) با مراحل مشخص بازگشت نسخه و سوئیچ اضطراری دیتابیس."
    ),
    "143": (
        "Demos software using carefully manicured local databases, watching the product crash when exposed to real production data.",
        "Enforces environment parity between staging and production, testing releases against realistic, anonymized production datasets.",
        "دموی نرم‌افزار با داده‌های ترومیز محیط محلی و کرش کردن فاجعه‌بار برنامه در مواجهه با داده‌های واقعی پروداکشن.",
        "هماهنگ‌سازی محیط‌های تست و پروداکشن و اعتبارسنجی قابلیت‌ها با دیتاست‌های مشابه دنیای واقعی."
    ),
    "158": (
        "Fears Friday deployments due to missing test suites and lack of automated rollback capabilities.",
        "Builds automated regression test suites and zero-downtime blue/green deployment pipelines that make deployments routine any day.",
        "ترس از دیپلوی در روزهای آخر هفته به دلیل فقدان تست‌های خودکار و ناتوانی در بازگردانی سریع نسخه در صورت خرابی.",
        "ایجاد تست‌های رگرسیون مطمئن و خطوط استقرار بدون قطعی (Blue/Green) که دیپلوی را در هر ساعتی عادی و امن می‌سازد."
    ),
    "169": (
        "Burns expensive managed cloud CI runner minutes on long build matrices instead of using cost-effective dedicated runners.",
        "Deploys dedicated self-hosted CI runners on fixed-cost compute instances ($20/mo), achieving unlimited pipeline execution.",
        "هدر دادن بودجه روی دقایق گران‌قیمت رانرهای کلود برای بیلدهای طولانی به جای استفاده از رانرهای اختصاصی.",
        "راه‌اندازی رانرهای اختصاصی گیت‌هاب روی سرورهای با هزینه ثابت ماهانه جهت اجرای نامحدود بیلدهای سنگین."
    ),
    "172": (
        "Exhausts GitHub Actions free tier minutes mid-month due to un-cached dependency installations and serial test execution.",
        "Implements dependency caching (`actions/cache`), Docker layer caching, and parallelized test jobs to cut CI runtimes by 70%.",
        "تمام شدن سقف دقایق رایگان گیت‌هاب اکشنز در اواسط ماه به دلیل نصب تکراری پکیج‌ها و اجرای غیرهمزمان تست‌ها.",
        "استفاده از کش پکیج‌ها و لایه‌های داکر و موازی‌سازی اجرای تست‌ها جهت کاهش ۷۰ درصدی زمان و مصرف دقایق CI."
    ),
    "173": (
        "Follows over-engineered enterprise DevOps dogma for early-stage prototypes, stalling feature delivery for months.",
        "Adopts pragmatic trunk-based development with ephemeral preview environments, balancing engineering velocity with reliability.",
        "تقلید کورکورانه از متدولوژی‌های پیچیده دوآپس سازمان‌های بزرگ برای محصولات نوپا که توسعه را ماه‌ها فلج می‌کند.",
        "استفاده از روش چابک Trunk-Based Development و محیط‌های پیش‌نمایش موقت جهت حفظ تعادل بین سرعت و پایداری."
    ),
    "189": (
        "Deploys updates simultaneously to 100% of production traffic, exposing all users immediately to uncaught regressions.",
        "Implements canary deployments: routes 5% of production traffic to new versions, monitoring error metrics before full rollout.",
        "انتشار آپدیت به صورت همزمان به ۱۰۰٪ کاربران که در صورت وجود باگ کل پایگاه مشتریان را دچار اختلال می‌کند.",
        "پیاده‌سازی دیپلوی قناری (Canary): هدایت ۵٪ ترافیک به نسخه جدید و پایش متریک‌های خطا پیش از ارتقای عمومی."
    ),
    "200": (
        "Makes infrastructure hosting decisions based on internet hype rather than calculating operational maintenance and egress costs.",
        "Evaluates hosting trade-offs systematically: balancing managed convenience against self-hosted control and compute margins.",
        "انتخاب زیرساخت و هاستینگ بر اساس موج‌های تبلیغاتی اینترنت به جای محاسبه دقیق هزینه‌های نگهداری و ترافیک.",
        "ارزیابی ساختاریافته گزینه‌های هاستینگ با مقایسه راحتی سرویس‌های ابری در برابر استقلال و سودآوری سرورهای اختصاصی."
    ),
    "204": (
        "Suffers 45-minute deployment build times caused by un-cached monolithic Docker builds and sequential test execution.",
        "Optimizes Docker build pipelines with multi-stage BuildKit caching and parallel test matrix jobs, cutting deploy time to 4 minutes.",
        "تحمل زمان ۴۵ دقیقه‌ای برای هر دیپلوی به دلیل ایمیج‌های سنگین فاقد کش داکر و اجرای تک‌به‌تک تست‌ها.",
        "بهینه‌سازی پایپ‌لاین داکر با کش چندمرحله‌ای BuildKit و موازی‌سازی تست‌ها جهت کاهش زمان بیلد به زیر ۴ دقیقه."
    ),
    "209": (
        "Adopts high-risk deployment models without understanding coupling between application code and database schema states.",
        "Selects deployment patterns (Rolling, Blue/Green, Canary) aligned with backward-compatible database schema migrations.",
        "استفاده از روش‌های پرریسک دیپلوی بدون درک وابستگی متقابل کدهای سرور با وضعیت فیلدهای دیتابیس.",
        "انتخاب مدل استقرار (Rolling یا Blue/Green) همگام با مایگریشن‌های سازگار با عقب در پایگاه‌داده."
    ),
    "217": (
        "Pulls in 300 unvetted third-party npm dependencies, creating a massive attack surface for supply chain compromises.",
        "Audits the dependency tree, removes redundant packages, and pins exact versions with lockfile integrity verification.",
        "نصب بی‌رویه ۳۰۰ پکیج شخص‌ثالث که راه حملات زنجیره تامین را به قلب نرم‌افزار باز می‌کند.",
        "ممیزی درخت وابستگی‌ها، حذف پکیج‌های غیرضروری و قفل کردن نسخه‌های دقیق با اعتبارسنجی فایل lockfile."
    ),
    "231": (
        "Maintains long-lived diverging feature branches for weeks, causing nightmare merge conflicts and broken deployments.",
        "Practices trunk-based development with short-lived feature branches (<24h) and feature flags for incomplete capabilities.",
        "نگه‌داشتن برنچ‌های طولانی‌مدت به مدت چند هفته که منجر به تداخل‌های وحشتناک مرج و دیپلوی‌های معیوب می‌شود.",
        "توسعه بر پایه برنچ اصلی (Trunk-Based) با برنچ‌های کوتاه‌مدت کمتر از ۲۴ ساعت و استفاده از فیچر فلگ."
    ),
    "233": (
        "Allows high-velocity AI code generation to overwhelm traditional manual PR review processes, creating code review backlogs.",
        "Automates PR review triage with AI linters, automated test suites, and strict architectural boundary checkers.",
        "تولید پرحجم کدهای هوش مصنوعی که تیم را در صف طولانی بازبینی دستی گرفتار کرده و باعث کندی انتشار می‌شود.",
        "اتوماسیون بازبینی با لینترهای هوشمند، تست‌های خودکار و ابزارهای بررسی شرایط مرزی معماری در گیت‌هاب."
    ),
    "235": (
        "Hits the deploy button without verifying database migrations, environment variables, or build health.",
        "Automates a strict 9-point pre-flight deployment checklist in CI: schema check, secret scans, build verification, and smoke tests.",
        "زدن دکمه دیپلوی با حدس و گمان بدون بررسی سلامت مایگریشن‌ها، متغیرهای محیطی و تست بیلد.",
        "اتوماسیون چک‌لیست ۹ مرحله‌ای پیش‌پرواز در CI: بررسی اسکیما، اسکن کلیدها، تست بیلد و تست‌های پایه‌ای کارکرد."
    ),
    "239": (
        "Applies database schema changes via the Supabase web dashboard in production, causing environmental drift from local code.",
        "Manages Supabase schema migrations as versioned SQL migration files committed to Git and applied via CI pipelines.",
        "تغییر ساختار دیتابیس از طریق داشبورد وب سوپابیس در پروداکشن که موجب ناهماهنگی آن با کدهای لوکال می‌شود.",
        "مدیریت تغییرات دیتابیس به صورت فایل‌های مایگریشن SQL در گیت و اعمال خودکار آن‌ها از طریق خط استقرار CI."
    ),
    "245": (
        "Postpones CI/CD pipeline automation until late in product development, suffering manual deployment errors every week.",
        "Establishes automated git-push CI/CD pipelines from Day 1 of development, making production releases effortless.",
        "به تعویق انداختن خطوط خودکار استقرار تا اواخر پروژه و تحمل خطاهای دستی مکرر در هر دیپلوی هفتگی.",
        "راه‌اندازی خطوط خودکار استقرار با هر push گیت از همان روز اول جهت حذف خطاهای انسانی در انتشار."
    ),
    "251": (
        "Allows AI to generate large production components without writing unit tests, accumulating silent architectural debt.",
        "Mandates test-driven verification for AI-generated code, requiring unit and integration tests before merging changes.",
        "تولید کامپوننت‌های بزرگ با هوش مصنوعی بدون نوشتن حتی یک تست که بدهی فنی پنهان ایجاد می‌کند.",
        "اجبار توسعه تست‌محور (TDD) برای کدهای هوش مصنوعی و الزام تست‌های واحد و یکپارچگی قبل از ادغام کدها."
    ),
    "253": (
        "Continues rushing new features after reaching 1,000 active users while ignoring database query degradation and stability.",
        "Shifts focus at 1k users from feature addition to operational reliability: index optimization, caching, and regression testing.",
        "ادامه افزودن قابلیت‌های جدید پس از رسیدن به ۱۰۰۰ کاربر فعال و بی‌توجهی به کندی دیتابیس و افت پایداری.",
        "تغییر اولویت پس از جذب ۱۰۰۰ کاربر به سمت پایداری: بهینه‌سازی ایندکس‌ها، کشینگ و رفع خطاهای گزارش‌شده."
    ),
    "256": (
        "Rolls out major application updates to all users at once, risking widespread customer churn during regressions.",
        "Automates phased rollouts (5% -> 25% -> 100%) with automated rollbacks triggered if error rates exceed 0.1%.",
        "انتشار سراسری تغییرات بزرگ به تمام کاربران به صورت یکجا که در صورت بروز باگ موجب ریزش گسترده مشتریان می‌شود.",
        "اتوماسیون عرضه مرحله‌ای ترافیک (۵٪ به ۲۵٪ به ۱۰۰٪) با بازگشت خودکار در صورت عبور نرخ خطا از ۰.۱ درصد."
    ),
    "268": (
        "Hires dedicated DevOps teams prematurely for simple prototypes, wasting capital on unnecessary infrastructure overhead.",
        "Leverages developer-friendly platform-as-a-service primitives (Railway, Fly, Vercel) with Git-driven deployment automation.",
        "استخدام زودهنگام تیم اختصاصی دوآپس برای پروژه‌های اولیه و هدر دادن سرمایه روی زیرساخت‌های غیرضروری.",
        "استفاده از پلتفرم‌های مدرن PaaS (مانند Railway یا Vercel) با اتوماسیون استقرار گیت بدون نیاز به تیم بزرگ دوآپس."
    ),
    "278": (
        "Operates microservices with inconsistent release pipelines, resulting in version mismatches and broken API contracts.",
        "Standardizes CI/CD release pipeline definitions across all repositories using reusable GitHub Actions workflow templates.",
        "استفاده از روش‌های ناهماهنگ دیپلوی در میکروسرویس‌ها که موجب ناهماهنگی نسخه‌ها و شکستن قراردادهای API می‌شود.",
        "استانداردسازی پایپ‌لاین‌های استقرار در تمامی مخازن با استفاده از تمپلیت‌های مشترک و آزموده در گیت‌هاب اکشنز."
    ),
    "279": (
        "Develops directly against production databases, risking accidental table drops and catastrophic customer data corruption.",
        "Enforces strict three-tier environment isolation (Dev, Staging, Production) with isolated database clusters and credentials.",
        "کدنویسی مستقیم متصل به دیتابیس عملیاتی که ریسک حذف تصادفی جداول و تخریب اطلاعات کاربران را دارد.",
        "تفکیک سخت‌گیرانه محیط‌های توسعه، استیجینگ و پروداکشن با دیتابیس‌ها و کلیدهای دسترسی کاملاً مستقل."
    ),
    "283": (
        "Treats Layer 5 Staging Parity as optional, testing migrations on production databases during live customer traffic.",
        "Mandates staging dry-runs for all database migrations and configuration updates prior to production execution.",
        "اختیاری دانستن لایه پنجم استیجینگ و اجرای مایگریشن‌های حساس روی دیتابیس پروداکشن حین استفاده کاربران.",
        "اجبار اجرای آزمایشی تمام مایگریشن‌ها و تغییرات در محیط استیجینگ قبل از اعمال نهایی در پروداکشن."
    ),
    "289": (
        "Rely on paying users to discover broken workflows in production due to lack of automated regression testing.",
        "Deploys automated Playwright end-to-end integration test suites in CI verifying critical user journeys before every release.",
        "تبدیل کاربران به تیم تست نرم‌افزار به دلیل فقدان تست‌های رگرسیون که باعث کشف باگ‌ها توسط مشتری می‌شود.",
        "راه‌اندازی تست‌های خودکار سرتاسری Playwright در CI جهت اعتبارسنجی فرآیندهای حیاتی پیش از هر انتشار."
    ),
    "291": (
        "Tests software only on the happy path, releasing code that crashes on empty database states or network timeouts.",
        "Tests edge cases, network timeouts, invalid inputs, and dirty data conditions in CI before approving pull requests.",
        "تست نرم‌افزار صرفاً در مسیر خوش‌بینانه و انتشار کدهایی که با دیتابیس خالی یا قطعی اینترنت کرش می‌کنند.",
        "تست سناریوهای لبه، تایم‌اوت شبکه، ورودی‌های خراب و وضعیت‌های خطای سرور در خط استقرار پیش از تایید کد."
    ),
    "294": (
        "Runs development, staging, and production setups all locally on developer laptops, suffering 'works on my machine' bugs.",
        "Containerizes applications using Docker Compose and mirrors cloud infrastructure in isolated staging environments.",
        "اجرای تمام محیط‌ها روی لپ‌تاپ برنامه‌نویس که به باگ‌های همیشگی «روی سیستم من کار می‌کرد» ختم می‌شود.",
        "کانتینری‌سازی سرویس‌ها با Docker Compose و شبیه‌سازی دقیق زیرساخت کلود در محیط استیجینگ."
    ),
    "297": (
        "Prepares investor demos using pristine sanitized data, hiding severe database deadlocks and slow queries under dirty inputs.",
        "Fuzz-tests staging environments with dirty, realistic production datasets to uncover unhandled errors prior to launch.",
        "آماده‌سازی دموی سرمایه‌گذار با داده‌های فوق‌العاده تمیز که بن‌بست‌های دیتابیس و باگ‌های داده واقعی را مخفی می‌کند.",
        "تست سیستم با داده‌های واقعی، ناقص و حجیم در محیط استیجینگ برای کشف خطاهای زمان اجرا قبل از رونمایی."
    ),
    "300": (
        "Deploys code under the assumption that local macOS/Windows execution guarantees identical behavior on Linux production hosts.",
        "Enforces reproducible Docker builds that compile and execute code inside identical Linux container runtimes across all stages.",
        "تصور اینکه کارکرد کد روی مک یا ویندوز محلی به معنی کارکرد یکسان روی سرورهای لینوکس پروداکشن است.",
        "اجبار بیلد کانتینری داکر جهت تضمین رفتار کاملاً یکسان کد روی محیط لینوکس در تمام مراحل توسعه و پروداکشن."
    ),
    "301": (
        "Deploys code blindly with manual git pulls on servers, suffering deployment outages with zero understanding of changes.",
        "Adopts immutable preview deployments (Vercel/Netlify) and atomic deployment rollouts to eliminate deployment roulette.",
        "دیپلوی کورکورانه با دستور git pull مستقیم روی سرور که در صورت بروز خطا علت خرابی را کاملاً مبهم می‌گذارد.",
        "استفاده از دیپلوی‌های تغییرناپذیر پیش‌نمایش و ارتقای اتمیک نسخه جهت پایان دادن به قمار در دیپلوی."
    ),
    "305": (
        "Accumulates 847 transitive npm dependencies, ignoring known security CVEs and supply chain injection risks.",
        "Runs automated `npm audit` gates in CI and schedules monthly dependency pruning to eliminate unmaintained libraries.",
        "انباشت ۸۴۷ پکیج فرعی در پروژه و بی‌توجهی به آسیب‌پذیری‌های امنیتی شناخته‌شده در زنجیره تامین.",
        "اعمال گیت‌های خودکار `npm audit` در پایپ‌لاین CI و ممیزی ماهانه وابستگی‌ها برای حذف پکیج‌های ناامن."
    ),
    "315": (
        "Deploys non-deterministic build artifacts that work or break randomly depending on upstream package updates.",
        "Enforces deterministic builds using pinned package lockfiles, base Docker image SHAs, and reproducible artifact caches.",
        "استقرار بیلدهای غیرقطعی که بسته به آپدیت تصادفی پکیج‌های اینترنتی گاهی کار می‌کنند و گاهی می‌شکنند.",
        "تضمین بیلدهای قطعی با قفل کردن هش ایمیج‌های پایه داکر، فایل‌های lockfile و کش تکرارپذیر بیلد."
    ),
    "316": (
        "Installs dozens of redundant utility packages, inflating frontend bundle sizes and slowing page load speeds.",
        "Audits bundle sizes using Webpack/Vite bundle analyzers, replacing heavy external packages with native JavaScript APIs.",
        "نصب ده‌ها پکیج غیرضروری که حجم باندل فرانت‌اند را سنگین کرده و سرعت لود صفحه را برای کاربر کند می‌کند.",
        "ممیزی حجم فایل‌ها با آنالایزرهای بیلد و جایگزینی پکیج‌های سنگین با قابلیت‌های بومی جاوااسکریپت مدرن."
    ),
    "317": (
        "Relies on polished pitch deck demos while skipping resilience testing, watching software fail when real users enter unpredicted inputs.",
        "Runs automated chaos engineering and edge-case fuzzing against application APIs prior to opening public user access.",
        "اتکا به دموی صیقلی برای سرمایه‌گذاران بدون تست تاب‌آوری، که با اولین ورودی غیرمنتظره کاربر واقعی سقوط می‌کند.",
        "اجرای تست‌های آشوب (Chaos Engineering) و ارسال داده‌های مخرب و غیرعادی به API قبل از شروع ثبت‌نام عمومی."
    ),

    # ==========================================
    # 11-CLOUD-FINOPS (32 episodes)
    # ==========================================
    "010": (
        "Transfers massive data volumes across unmonitored cloud NAT gateways, incurring shocking four-figure bandwidth billing surprises.",
        "Keeps database and compute traffic inside private VPC subnets with VPC endpoints, eliminating costly NAT gateway egress fees.",
        "انتقال حجم بالای داده‌ها از طریق گیت‌وی‌های عمومی کلود که قبض‌های سرسام‌آور پهنای باند ایجاد می‌کند.",
        "محصور کردن ترافیک دیتابیس در ساب‌نت‌های خصوصی VPC و استفاده از VPC Endpoints جهت حذف هزینه‌های اضافه ترافیک."
    ),
    "021": (
        "Sends proprietary corporate intellectual property to public multi-tenant cloud LLMs, violating corporate confidentiality agreements.",
        "Deploys self-hosted local inference nodes (vLLM/Ollama) inside private enterprise VPCs for sensitive corporate IP.",
        "ارسال اطلاعات محرمانه سازمانی به مدل‌های ابری عمومی که توافق‌نامه‌های رازداری مشتریان را نقض می‌کند.",
        "استقرار نودهای اختصاصی پردازش هوش مصنوعی درون شبکه خصوصی سازمانی (Private VPC) برای داده‌های حساس."
    ),
    "031": (
        "Pitches enterprise buyers without SOC 2 certification, losing six-figure deals at the security review stage.",
        "Automates continuous compliance monitoring (Vanta/Drata) and implements audited security policies to achieve SOC 2 Type II.",
        "مذاکره با مشتریان بزرگ سازمانی بدون گواهی‌های امنیتی SOC 2 که موجب لغو قراردادها در مرحله ممیزی می‌شود.",
        "پیاده‌سازی مانیتورینگ پیوسته امنیت (با ابزارهای خودکار) و اعمال کنترل‌های استاندارد برای اخذ گواهی SOC 2."
    ),
    "041": (
        "Builds simple local business automation tools on expensive multi-region enterprise cloud architectures, burning profit margins.",
        "Leverages cost-effective serverless primitives with generous free tiers, keeping operational hosting costs below $10/month.",
        "ساخت ابزارهای ساده اتوماسیون روی زیرساخت‌های پیچیده و گران ابری که تمام حاشیه سود پروژه را می‌بلعد.",
        "استفاده از راهکارهای ارزان سرورلس و پلن‌های اقتصادی هاستینگ برای نگه داشتن هزینه ماهانه زیر ۱۰ دلار."
    ),
    "102": (
        "Operates AI applications without measuring per-user cost of goods sold (COGS), operating power users at a net financial loss.",
        "Instruments per-user token and infrastructure cost metering, aligning customer pricing tiers with underlying compute expenses.",
        "ارائه سرویس هوش مصنوعی بدون محاسبه بهای تمام‌شده مصرف هر کاربر که باعث زیان‌ده شدن کاربران پرمصرف می‌شود.",
        "محاسبه دقیق هزینه توکن و پردازش به ازای هر کاربر و تنظیم پلن‌های قیمتی متناسب با هزینه واقعی زیرساخت."
    ),
    "109": (
        "Reinvents commoditized infrastructure components in-house, spending hundreds of engineering hours on solved problems.",
        "Adopts proven managed platforms for commodity infrastructure, reserving custom engineering capacity for differentiated core IP.",
        "صرف صدها ساعت زمان مهندسی برای ساخت مجدد چرخ و ابزارهایی که سرویس‌های استاندارد آن وجود دارد.",
        "استفاده از پلتفرم‌های آماده برای زیرساخت‌های استاندارد و تمرکز توان مهندسی روی مزیت رقابتی اصلی بیزینس."
    ),
    "110": (
        "Leaves cloud resources unmonitored without automated spending kill-switches, discovering runaway bills only after credit cards are charged.",
        "Configures strict cloud budget alarms with automated webhook kill-switches that suspend runaway compute jobs at budget thresholds.",
        "رها کردن سرورهای ابری بدون سقف بودجه که تیم را با برداشت‌های نجومی از کارت اعتباری غافلگیر می‌کند.",
        "تنظیم هشدارهای سقف بودجه در کلود با سوییچ قطع خودکار که در صورت رد شدن از بودجه سرویس‌های پرمصرف را متوقف می‌کند."
    ),
    "120": (
        "Hosts customer status pages on the primary application infrastructure, going dark and leaving users uninformed during outages.",
        "Deploys independent, externally hosted status pages (Instatus/Statuspage) with automated incident notifications.",
        "قرار دادن صفحه گزارش وضعیت برنامه روی همان سرورهای اصلی که در زمان قطعی، صفحه وضعیت هم خاموش می‌شود.",
        "استقرار صفحه وضعیت روی هاست مستقل خارجی با ارسال خودکار پیامک و ایمیل اطلاع‌رسانی در زمان قطعی."
    ),
    "133": (
        "Leaves serverless functions configured with default 15-minute execution timeouts, accumulating massive bills during hanging loops.",
        "Enforces hard function timeouts (15-30 seconds) and memory limits across all serverless function definitions.",
        "تنظیم سقف تایم‌اوت توابع سرورلس روی ۱۵ دقیقه که در زمان بروز حلقه بی‌نهایت قبض‌های فاجعه‌بار تولید می‌کند.",
        "تنظیم سقف زمان اجرای سخت‌گیرانه (۱۵ تا ۳۰ ثانیه) و محدودسازی حافظه رم برای تمام توابع سرورلس."
    ),
    "134": (
        "Deploys generative AI features without spend caps per user session, allowing malicious scrapers to drain thousands in API credits.",
        "Enforces session-based token quotas and rate limits on AI features, terminating sessions when usage caps are reached.",
        "ارائه قابلیت‌های هوش مصنوعی بدون سقف مصرف در هر نشست که به اسکریپت‌ها اجازه تخلیه اعتبار حساب را می‌دهد.",
        "تعیین سقف توکن به ازای هر کاربر و نشست و مسدودسازی خودکار درخواست‌ها در صورت عبور از سقف مصرف مجاز."
    ),
    "147": (
        "Accepts commercial payments before establishing formal terms of service, refund policies, and dispute documentation.",
        "Publishes clear, legally binding terms of service, acceptable use policies, and refund guidelines prior to onboarding paying users.",
        "دریافت وجه از خریداران بدون انتشار قوانین استفاده، سیاست مرجوعی و مستندات قانونی رفع مغایرت.",
        "انتشار شفاف قوانین خدمات، سیاست‌های بازگشت وجه و ضوابط حقوقی پذیرش محصول قبل از شروع فروش رسمی."
    ),
    "155": (
        "Attempts to close enterprise accounts without standard security questionnaire documentation or verifiable uptime records.",
        "Prepares enterprise procurement packages: architectural security whitepapers, SOC 2 reports, and 99.9% uptime SLA commitments.",
        "مذاکره برای قراردادهای بزرگ سازمانی بدون مستندات امنیتی مدون و سوابق قابل‌اثبات پایداری سیستم.",
        "آماده‌سازی بسته تدارکات سازمانی: گزارش‌های ممیزی امنیتی، تاییدیه SOC 2 و قرارداد سطح خدمات (SLA) ۹۹.۹ درصدی."
    ),
    "179": (
        "Runs 12-second generative AI tasks in standard synchronous HTTP serverless routes, failing under 10-second edge platform timeouts.",
        "Streams long-running completions using Server-Sent Events (SSE) or offloads tasks to asynchronous queues with progress updates.",
        "اجرای کارهای ۱۲ ثانیه‌ای هوش مصنوعی در مسیرهای سرورلس که با محدودیت ۱۰ ثانیه‌ای تایم‌اوت پلتفرم کلاینت قطع می‌شود.",
        "ارسال استریم پاسخ با Server-Sent Events (SSE) یا انتقال کار به صف پس‌زمینه همراه با گزارش پیشرفت."
    ),
    "182": (
        "Exhausts platform concurrency limits (10 concurrent serverless invocations), dropping incoming user requests with 504 errors.",
        "Buffers incoming requests via message queues and uses connection poolers to smooth traffic bursts within platform limits.",
        "اشباع شدن سقف همزمانی توابع سرورلس (مثلاً ۱۰ درخواست همزمان) و پس زدن درخواست‌های کاربران با ارور ۵۰۴.",
        "بافر کردن درخواست‌ها با صف‌های پیام و استفاده از استخر اتصالات جهت مدیریت یکنواخت ترافیک در سقف پلن."
    ),
    "184": (
        "Attempts to solve backend scaling bottlenecks by adding complex microservices before optimizing monolithic database queries.",
        "Follows structured scaling decision trees: optimizes queries and indexes first, adds caching second, scales hardware last.",
        "تلاش برای رفع کندی سرور با شکستن ناشیانه برنامه به میکروسرویس‌های پیچیده قبل از بهینه‌سازی کوئری‌ها.",
        "پیروی از درخت تصمیم‌گیری اصولی مقیاس‌پذیری: ابتدا بهینه‌سازی کوئری و ایندکس، سپس کش ردیس، و در آخر ارتقای سرور."
    ),
    "188": (
        "Selects serverless database providers on impulsive trends without analyzing connection pooling overhead or cold-start latencies.",
        "Benchmarks database providers against real workload profiles, evaluating cold-start penalty, pooling limits, and query latency.",
        "انتخاب دیتابیس‌های ابری بر اساس هایپ روز بدون بررسی تاخیر شروع سرد (Cold Start) و نحوه مدیریت اتصالات.",
        "بنچمارک دقیق ارائه‌دهندگان دیتابیس بر اساس ترافیک واقعی، سنجش تاخیر شروع سرد و محدودیت‌های اتصال همزمان."
    ),
    "202": (
        "Migrates to self-hosted infrastructure under the illusion of 'free compute', underestimating engineering maintenance hours.",
        "Calculates Total Cost of Ownership (TCO) including maintenance, security patch management, and on-call engineer overhead.",
        "مهاجرت به سرورهای محلی به هوای هاستینگ رایگان بدون محاسبه زمان و هزینه سنگین نگهداری مهندسی.",
        "محاسبه دقیق هزینه کل مالکیت (TCO) با احتساب زمان نگهداری سرور، پچ‌های امنیتی و هزینه مهندس آنکال."
    ),
    "203": (
        "Discovers cloud bills doubled unexpectedly due to abandoned unattached storage volumes, zombie instances, and NAT data transfer.",
        "Automates weekly cloud resource hygiene scans with automated teardown of unattached disks and idle staging compute nodes.",
        "دو برابر شدن ناگهانی قبض کلود به دلیل دیسک‌های رهاشده متصل‌نشده، سرورهای زامبی و پهنای باند گیت‌وی NAT.",
        "اتوماسیون اسکن هفتگی منابع کلود و پاکسازی خودکار دیسک‌های یتیم و سرورهای استیجینگ بدون استفاده."
    ),
    "207": (
        "Fails to profile system throughput under load, learning about memory leaks and CPU saturation only when user traffic surges.",
        "Executes synthetic stress tests using k6/Locust to identify memory leaks, event loop blockages, and CPU bottlenecks before launch.",
        "عدم پروفایل کردن توان پردازشی سیستم زیر بار که موجب نشت حافظه و قفل شدن سرور در ترافیک واقعی می‌شود.",
        "اجرای تست‌های استرس با k6 برای کشف نشت حافظه، مسدود شدن Event Loop و گلوگاه‌های پردازنده پیش از لانچ."
    ),
    "208": (
        "Prices software arbitrarily without factoring in underlying compute, storage, and AI model token consumption margins.",
        "Models product pricing around gross margin economics, incorporating variable compute and AI inference costs into plan tiers.",
        "قیمت‌گذاری دل‌بخواهی محصول بدون در نظر گرفتن هزینه واقعی مصرف رم، دیسک و توکن‌های مدل در هر پلن.",
        "مدل‌سازی مالی قیمت‌گذاری بر اساس حاشیه سود ناخالص و پوشش هزینه‌های متغیر پردازش و توکن در پلن‌های اشتراک."
    ),
    "222": (
        "Picks serverless database engines without testing compatibility with application transaction patterns and relational constraints.",
        "Evaluates serverless database compatibility against relational constraints, transaction isolation levels, and migration tools.",
        "انتخاب موتور دیتابیس سرورلس بدون تست سازگاری آن با تراکنش‌های پیچیده و قیود رابطه‌ای برنامه.",
        "ارزیابی انطباق دیتابیس سرورلس با سطوح ایزولاسیون تراکنش‌ها، ابزارهای مایگریشن و قیود کلید خارجی."
    ),
    "242": (
        "Connects frontend clients directly to AI provider endpoints without a gateway layer, creating an open wallet for billing abuse.",
        "Deploys an AI API gateway (LiteLLM/Portkey) enforcing per-user rate limits, budget ceilings, and caching in front of model calls.",
        "اتصال کلاینت مستقیماً به کلید هوش مصنوعی بدون لایه گیت‌وی که کارت بانکی شرکت را در معرض مصرف نامحدود می‌گذارد.",
        "استقرار گیت‌وی هوش مصنوعی (LiteLLM/Portkey) همراه با سقف مصرف کاربر، سقف بودجه و کش هوشمند پرامپت‌ها."
    ),
    "247": (
        "Pays $900/month for managed database clusters for an early-stage app with modest read traffic, burning startup runway.",
        "Right-sizes early-stage infrastructure on dedicated VPS nodes (Hetzner/Fly) running pooled PostgreSQL at a fraction of the cost.",
        "پرداخت ماهانه ۹۰۰ دلار برای دیتابیس مدیریت‌شده در ابتدای کار که سرمایه استارتاپ را بیهوده هدر می‌دهد.",
        "انتخاب سرورهای اختصاصی با اندازه بهینه (Hetzner/Fly) با پستگرس مدیریت‌شده داخلی با هزینه بسیار پایین‌تر."
    ),
    "255": (
        "Serves 1,000,000 viral page views directly from application servers, causing database collapse and massive compute bills.",
        "Caches public viral pages at edge CDN nodes, serving millions of hits from cache with zero origin database load.",
        "پاسخگویی به ۱ میلیون بازدید وایرال مستقیماً از سرورهای اصلی که دیتابیس را خوابانده و هزینه‌های گزاف ایجاد می‌کند.",
        "کش کردن صفحات پربازدید در شبکه لبه CDN و تحویل میلیون‌ها بازدید از کش بدون تحمیل فشار به دیتابیس اصلی."
    ),
    "257": (
        "Spends $4,000/month on repetitive API calls that query identical context data on every prompt invocation.",
        "Implements prompt compression, prompt caching, and semantic response caching to eliminate redundant token consumption.",
        "صرف ۴۰۰۰ دلار در ماه برای فراخوانی‌های تکراری API که پرامپت‌ها و داده‌های مشابه را بارها و بارها ارسال می‌کنند.",
        "پیاده‌سازی فشرده‌سازی پرامپت، کش پرامپت ارائه‌دهنده و کش معنایی برای حذف مصرف توکن‌های تکراری."
    ),
    "258": (
        "Promises enterprise security compliance to prospective clients without implementing verified SOC 2 control frameworks.",
        "Implements formal SOC 2 controls: automated access reviews, encrypted backups, centralized logging, and vendor risk assessments.",
        "دادن وعده امنیت سازمانی به مشتریان بدون پیاده‌سازی کنترل‌های فنی و گواهی‌های اعتبارسنجی‌شده SOC 2.",
        "پیاده‌سازی کنترل‌های استاندارد SOC 2: بررسی دسترسی‌ها، بکاپ‌های رمزنگاری‌شده، لاگینگ متمرکز و ممیزی فروشندگان."
    ),
    "269": (
        "Treats Layer 11 Cloud FinOps as an afterthought, ignoring runaway egress bandwidth and unbudgeted cloud infrastructure.",
        "Enforces Layer 11 FinOps discipline: hard function execution timeouts, egress traffic monitoring, and cloud budget kill-switches.",
        "بی‌توجهی به لایه یازدهم مدیریت مالی کلود (FinOps) و غفلت از هزینه‌های سرسام‌آور پهنای باند و منابع بدون سقف.",
        "اعمال اصول لایه ۱۱: سقف زمان اجرای توابع، پایش ترافیک خروجی شبکه و فعال‌سازی سوئیچ قطع خودکار در سقف بودجه."
    ),
    "280": (
        "Deploys serverless containers without setting upper concurrency bounds, accumulating runaway bills during denial-of-wallet attacks.",
        "Sets explicit maximum concurrency limits, execution memory caps, and automated billing threshold alarms on serverless containers.",
        "استقرار کانتینرهای سرورلس بدون تعیین سقف همزمانی که در زمان حملات ترافیکی هزینه‌های کمرشکن ایجاد می‌کند.",
        "تعیین سقف همزمانی ماکزیمم، تعیین سقف حافظه رم و ایجاد هشدارهای خودکار در صورت عبور از بودجه مجاز."
    ),
    "286": (
        "Invests thousands in complex enterprise compliance certifications before validating product-market fit with paying customers.",
        "Prioritizes core technical hygiene (RLS, encryption, backups, auth) to establish practical security before purchasing formal badges.",
        "سرمایه‌گذاری سنگین روی گواهی‌های پیچیده سازمانی پیش از اعتبارسنجی تقاضای بازار و جذب مشتری اولیه.",
        "تمرکز روی بهداشت فنی اصلی (رمزنگاری، بکاپ، RLS و احراز هویت) جهت ایجاد امنیت واقعی قبل از خرید مدارک پرهزینه."
    ),
    "307": (
        "Allows autonomous AI agent loops to make unconstrained recursive API calls, draining hundreds of dollars in minutes.",
        "Implements recursion depth limits and hard monetary spend ceilings that kill automated agent loops if budgets are exceeded.",
        "اجازه به ایجنت‌های هوش مصنوعی برای اجرای حلقه‌های بازگشتی نامحدود که صدها دلار را در چند دقیقه می‌سوزانند.",
        "تعیین سقف عمق تکرار برای ایجنت‌ها و تنظیم سقف مالی سخت‌گیرانه برای متوقف کردن فوری حلقه در صورت گذر از بودجه."
    ),
    "311": (
        "Treats individual API call costs as negligible, failing to anticipate exponential cost scaling when user volumes multiply.",
        "Calculates blended unit economics per user session, optimizing expensive prompts and caching high-frequency queries.",
        "ناچیز شمردن هزینه هر درخواست API و غفلت از رشد تصاعدی و سرسام‌آور هزینه‌ها با افزایش تعداد کاربران.",
        "محاسبه دقیق بهای تمام‌شده هر نشست کاربری، بهینه‌سازی پرامپت‌های سنگین و کش کردن پاسخ‌های پرتکرار."
    ),
    "319": (
        "Operates metered API services without tracking cumulative monthly spend per customer, risking unpaid platform charges.",
        "Maintains real-time user credit balances in Redis, declining incoming requests when customer account balances reach zero.",
        "ارائه خدمات پردازشی بدون رصد مانده اعتبار مشتری که موجب مصرف خدمات بیش از موجودی و تحمیل ضرر می‌شود.",
        "محاسبه بلادرنگ موجودی کاربر در ردیس و رد کردن درخواست‌ها به محض رسیدن اعتبار حساب به صفر."
    ),

    # ==========================================
    # 12-FRONTEND-API-HYGIENE (37 episodes)
    # ==========================================
    "032": (
        "Replaces mature SaaS tools with flimsy, unmaintained internal prototypes that crash and consume excessive engineering maintenance time.",
        "Scopes internal builds strictly to core differentiated workflows, maintaining enterprise architectural hygiene and testing.",
        "جایگزینی نرم‌افزارهای پایدار با پروتوتایپ‌های داخلی شکننده که با خرابی‌های مکرر وقت ارزشمند تیم را تلف می‌کنند.",
        "محدود کردن پروژه‌های داخلی به نیازهای استراتژیک شرکت و توسعه آن‌ها با استانداردهای مهندسی و تست پایدار."
    ),
    "034": (
        "Clutters user interfaces with decorative AI gimmicks that confuse users instead of solving real core workflow bottlenecks.",
        "Designs streamlined user workflows focused on ergonomics, minimizing cognitive load and friction in core tasks.",
        "شلوغ کردن صفحه با دکمه‌های پر زرق‌وبرق هوش مصنوعی که به جای حل مشکل اصلی، کاربر را سردرگم می‌کنند.",
        "طراحی متمرکز بر ارگونومی و تجربه کاربری ساده و حذف حواشی متنی و دکمه‌های تزئینی ناکارآمد."
    ),
    "038": (
        "Builds sophisticated technical features without designing clear user onboarding flows or communicating measurable value propositions.",
        "Pairs technical engineering with seamless onboarding UX, guided empty states, and frictionless conversion paths.",
        "ساخت قابلیت‌های پیچیده فنی بدون طراحی فرآیند آنبوردینگ کاربر و عدم انتقال ارزش واقعی محصول.",
        "ترکیب مهندسی فنی با تجربه آنبوردینگ روان، وضعیت‌های خالی راهنما و تسهیل مسیر تبدیل کاربر به مشتری."
    ),
    "049": (
        "Uses the identical LLM to both write code and review pull requests, perpetuating shared blind spots across architectures.",
        "Employs diverse review personas, automated static analysis tools, and human engineering judgment to audit code independently.",
        "استفاده از همان مدل هوش مصنوعی برای کدنویسی و بازبینی کد که باعث تکرار و نادیده گرفته شدن خطاهای مشابه می‌شود.",
        "استفاده از مدل‌های مستقل با پرامپت‌های نقادانه، ابزارهای تحلیل ایستای کد و نظارت مستقیم مهندسی انسان."
    ),
    "054": (
        "Prompts a single AI session to generate entire full-stack applications in one prompt, producing tangled spaghetti architectures.",
        "Deconstructs software architectures into modular, independently testable layers with explicit typed contract boundaries.",
        "تولید کل اپلیکیشن فرانت‌اند و بک‌اند در یک پرامپت تکی که کدهایی درهم‌تنیده و غیرقابل توسعه تولید می‌کند.",
        "تفکیک معماری به لایه‌های مستقل و تست‌پذیر با قراردادهای مشخص و اینترفیس‌های تایپ‌شده."
    ),
    "056": (
        "Renders un-sanitized user prompts or LLM output directly into the DOM, opening severe Cross-Site Scripting (XSS) vectors.",
        "Sanitizes all dynamic content with DOMPurify and enforces strict Content Security Policy (CSP) headers against script execution.",
        "رندر کردن مستقیم پرامپت‌های ورودی یا خروجی هوش مصنوعی در صفحه بدون پاکسازی که منجر به حملات XSS می‌شود.",
        "پاکسازی محتوا با ابزار DOMPurify و اعمال هدرهای سخت‌گیرانه سیاست امنیت محتوا (CSP) برای مسدودسازی اسکریپت مخرب."
    ),
    "064": (
        "Wraps responsive websites in naive mobile WebViews, shipping laggy touch interactions, zoom bugs, and broken offline experiences.",
        "Optimizes mobile experiences: removes tap delays, disables unintended viewport zooming, and handles offline network states gracefully.",
        "بسته‌بندی سایت در وب‌ویوی ساده موبایل که موجب لگ لمسی، باگ‌های زوم ناخواسته و صفحه سفید در قطعی اینترنت می‌شود.",
        "بهینه‌سازی تجربه موبایل: حذف تاخیر تاچ، غیرفعال‌سازی زوم ناخواسته در اینپوت‌ها و مدیریت وضعیت آفلاین شبکه."
    ),
    "068": (
        "Accepts every ad-hoc client customization request, fracturing the codebase into unmaintainable customer-specific forks.",
        "Maintains an opinionated core product architecture, satisfying custom requirements via configurable extension hooks.",
        "پذیرش کلیه درخواست‌های سلیقه‌ای مشتریان که به انشعاب‌های متعدد و کدهای غیرقابل نگهداری منجر می‌شود.",
        "حفظ یکپارچگی سورس اصلی و پاسخ به نیازهای خاص مشتریان از طریق هوک‌ها و تنظیمات افزونه‌ای بدون دستکاری هسته."
    ),
    "070": (
        "Forks the entire repository and deployment pipeline for each new tenant, creating unmaintainable code divergence.",
        "Architects single-codebase multi-tenancy with dynamic tenant configuration inheritance and feature flags.",
        "انشعاب مخزن کد به ازای هر مشتری جدید که کپی کردن باگ‌ها و نگهداری چند پایپ‌لاین موازی را تحمیل می‌کند.",
        "توسعه تک‌مخزنی با چندمستأجری پویا: تنظیمات اختصاصی به ازای سازمان، فیچر فلگ‌ها و یک پایپ‌لاین مشترک."
    ),
    "083": (
        "Permits non-technical founders to deploy code without senior engineering oversight, shipping critical security vulnerabilities.",
        "Establishes senior engineering code review standards and automated CI/CD guardrail gates before production merges.",
        "انتشار کد در پروداکشن توسط افراد غیرفنی بدون نظارت مهندس ارشد که رخنه‌های امنیتی خطرناک ایجاد می‌کند.",
        "تعیین استانداردهای بازبینی کد توسط مهندس ارشد و استقرار گیت‌های محافظتی در خط CI قبل از ادغام تغییرات."
    ),
    "089": (
        "Builds complex UI features based on assumptions without tracking real user behavior or feature adoption metrics.",
        "Instruments frontend feature telemetry and event tracking to validate user engagement before iterating on interfaces.",
        "ساخت فیچرهای پیچیده در رابط کاربری بر اساس حدس و گمان بدون ثبت تله‌متری رفتار واقعی کاربران.",
        "پیاده‌سازی تله‌متری و رهگیری تعاملات کاربر برای سنجش میزان استقبال واقعی قبل از توسعه بیشتر."
    ),
    "091": (
        "Builds applications in complete isolation without incorporating distribution mechanics or shareable viral loops into the UI.",
        "Embeds viral sharing hooks, dynamic Open Graph social preview cards, and referral mechanics directly into the user experience.",
        "توسعه محصول در انزوا بدون قرار دادن سازوکارهای وایرال، معرفی به دوستان و پیش‌نمایش در شبکه‌های اجتماعی.",
        "تعبیه دکمه‌های اشتراک‌گذاری، کارت‌های پیش‌نمایش Open Graph و لینک‌های معرف درون رابط کاربری."
    ),
    "093": (
        "Builds developer tools with poor ergonomics: opaque error messages, missing TypeScript types, and uncopyable code samples.",
        "Optimizes developer experience: clear typed contracts, informative error messages with remediation hints, and copyable snippets.",
        "طراحی ابزارهای توسعه‌دهنده با تجربه کاربری ضعیف: خطاهای گنگ، عدم پشتیبانی از تایپ‌اسکریپت و نمونه کدهای ناقص.",
        "ارتقای تجربه توسعه‌دهنده (DX): تایپ‌های کامل تایپ‌اسکریپت، پیام‌های خطای راهنما و قطعه‌کدهای آماده کپی."
    ),
    "101": (
        "Builds businesses entirely dependent on closed third-party SaaS APIs that suddenly raise pricing or deprecate endpoints.",
        "Abstracts external third-party dependencies behind internal facade interfaces to preserve data ownership and vendor mobility.",
        "وابسته‌سازی ۱۰۰٪ کسب‌وکار به پلتفرم‌های انحصاری خارجی که با تغییر تعرفه یا بستن API کل بیزینس را نابود می‌کنند.",
        "طراحی لایه‌های واسط داخلی (Facade) برای سرویس‌های خارجی جهت حفظ استقلال و امکان تعویض ارائه‌دهنده."
    ),
    "106": (
        "Rushes to build shiny new frontend features while existing customer workflows suffer from reported, unaddressed regressions.",
        "Prioritizes stabilizing existing user journeys and fixing reported bugs before commencing new UI feature development.",
        "شروع فیچرهای جدید و براق در حالی که بخش‌های قبلی برنامه پر از باگ است و صدای مشتریان درآمده است.",
        "اولویت‌بخشی قطعی به پایداری سیستم و رفع رگرسیون‌های موجود قبل از دست زدن به توسعه امکانات جدید."
    ),
    "112": (
        "Deploys rapid weekend prototypes directly to enterprise users without refactoring fragile client-side state logic.",
        "Refactors rapid UI prototypes into robust state-driven architectures with strict typing, error boundaries, and unit tests.",
        "ارائه مستقیم پروتوتایپ‌های تند توسعه‌یافته به کاربران تجاری بدون بازنویسی استیت‌های شکننده کلاینت.",
        "ریفکتور پروتوتایپ‌ها به معماری‌های پایدار با مدیریت وضعیت مطمئن، مرزهای خطا و تست‌های واحد."
    ),
    "117": (
        "Ships frontend applications missing global error boundaries, causing whole pages to crash to blank white screens on minor exceptions.",
        "Wraps critical UI components in React Error Boundaries that display graceful fallback UIs with retry buttons upon crashes.",
        "فقدان مرزهای خطای سراسری (Error Boundaries) که با یک خطای کوچک در یک کامپوننت کل صفحه را سفید می‌کند.",
        "قرار دادن کامپوننت‌ها درون React Error Boundary جهت نمایش رابط کاربری جایگزین همراه با دکمه تلاش مجدد."
    ),
    "125": (
        "Displays fabricated, static social proof testimonials on marketing pages, destroying customer trust upon inspection.",
        "Renders authentic, verifiable customer metrics and dynamic social proof backed by real customer case studies.",
        "نمایش نظرات ساختگی و فیک در صفحات فرانت‌اند که به محض متوجه شدن کاربر اعتماد به برند را کاملاً نابود می‌کند.",
        "نمایش آمار و نظرات واقعی و قابل‌اثبات مشتریان همراه با لینک و داده‌های تاییدشده در رابط کاربری."
    ),
    "131": (
        "Over-engineers simple client ordering workflows with confusing multi-step modals and slow network roundtrips.",
        "Implements streamlined checkout interfaces with optimistic UI updates and real-time status feedback for users.",
        "پیچیده کردن فرآیند خرید کاربر با پنجره‌های تودرتو و تبادل‌های کند شبکه که موجب انصراف خریدار می‌شود.",
        "پیاده‌سازی فرآیند خرید تک‌مرحله‌ای با به‌روزرسانی‌های خوش‌بینانه UI و بازخورد بلادرنگ وضعیت سفارش."
    ),
    "138": (
        "Handles credit card checkout with custom form inputs, risking PCI compliance violations and failing 3D Secure verification.",
        "Integrates Stripe Elements using server-created payment intents, handling 3D Secure challenges natively and securely.",
        "دریافت شماره کارت در اینپوت‌های معمولی فرم که نقض استانداردهای PCI بوده و تاییدیه امنیتی 3D Secure را رد می‌کند.",
        "استفاده از کامپوننت‌های استاندارد Stripe Elements با Payment Intent سمت سرور جهت پردازش امن و سازگار با رمز پویا."
    ),
    "140": (
        "Renders thousands of un-virtualized DOM elements in high-frequency dashboard tables, freezing client browser threads.",
        "Implements DOM list virtualization (`@tanstack/react-virtual`) rendering only elements visible within the active viewport.",
        "رندر کردن هزاران سطر در جدول داشبورد به طور همزمان در DOM که موجب فریز شدن و لگ شدید مرورگر می‌شود.",
        "استفاده از تکنیک مجازی‌سازی لیست‌ها (Virtualization) برای رندر اختصاصی سطرهای درون صفحه نمایش کاربر."
    ),
    "146": (
        "Treats UI design as pure aesthetics, ignoring technical state transitions and error recovery workflows.",
        "Approaches UI engineering from first principles: modeling state machines that handle loading, errors, network drops, and retries.",
        "نگاه صرفاً گرافیکی به طراحی رابط کاربری و بی‌توجهی به مدیریت وضعیت‌ها و بازیابی از شرایط خطا.",
        "مهندسی UI از اصول بنیادین: مدل‌سازی ماشین وضعیت برای پوشش لودینگ، خطاهای سرور، قطعی نت و تلاش مجدد."
    ),
    "154": (
        "Abandons product onboarding optimization post-launch, suffering massive drop-offs between signup and first value delivery.",
        "Instruments user onboarding funnels, minimizing time-to-first-value with interactive guides and friction-free setup.",
        "رها کردن بهینه‌سازی مسیر شروع کار کاربر که موجب ریزش شدید بین ثبت‌نام و اولین استفاده مفید می‌شود.",
        "بهینه‌سازی قیف آنبوردینگ و به حداقل رساندن زمان رسیدن به اولین ارزش واقعی محصول برای کاربر."
    ),
    "164": (
        "Launches products without answering foundational launch criteria: payment validation, data privacy, and failure recovery.",
        "Verifies production readiness against core pre-launch criteria: payment webhooks, GDPR deletion paths, and uptime alerting.",
        "عرضه محصول بدون پاسخ به سوالات اساسی: کارکرد پرداخت، حفاظت از داده‌ها و بازیابی در زمان خرابی.",
        "اعتبارسنجی سیستم در برابر الزامات حیاتی لانچ: وب‌هوک‌های مالی، پاکسازی قانونی حساب‌ها و مانیتورینگ آپ‌تایم."
    ),
    "181": (
        "Relies on server-side logs alone while remaining completely blind to client-side JavaScript crashes and broken layouts.",
        "Integrates Sentry browser SDK with session replay and breadcrumbs to monitor real user exceptions in production.",
        "اتکا صرف به لاگ‌های سرور و بی‌خبری کامل از کرش‌های جاوااسکریپت و به هم ریختگی‌های صفحه در مرورگر کاربران.",
        "نصب اس‌دی‌کی مرورگر سنتری همراه با ضبط نشست (Session Replay) برای ثبت و بازبینی خطاهای فرانت‌اند کاربران."
    ),
    "195": (
        "Deletes only primary user records upon account deletion requests, leaving orphaned PII in related database tables.",
        "Executes cascading foreign key deletions or automated GDPR erasure workflows that purge user data across all tables.",
        "حذف کاربر صرفاً از جدول اصلی در زمان درخواست خروج و باقی ماندن اطلاعات هویتی در سایر جداول دیتابیس.",
        "اجرای حذف آبشاری روی کلیدهای خارجی یا روال‌های خودکار پاکسازی داده‌های هویتی مطابق با استانداردهای GDPR."
    ),
    "198": (
        "Writes technical documentation loaded with internal jargon that confuses prospective customers and support staff.",
        "Produces clean, user-centric documentation with searchable troubleshooting guides, interactive examples, and clear workflows.",
        "نگارش مستندات با ادبیات گنگ فنی سازندگان که مشتریان و تیم پشتیبانی را سردرگم می‌کند.",
        "تدوین مستندات شفاف و کاربرمحور با راهنماهای رفع مشکل، نمونه‌های تعاملی و مسیرهای گام‌به‌گام."
    ),
    "212": (
        "Omits browser security headers, exposing users to Cross-Site Scripting (XSS), MIME-type sniffing, and clickjacking.",
        "Enforces essential HTTP security response headers: strict CSP, `X-Content-Type-Options: nosniff`, and `X-Frame-Options: DENY`.",
        "عدم ارسال هدرهای امنیتی مرورگر که کاربران را در معرض حملات تزریق اسکریپت و جعل کلیک قرار می‌دهد.",
        "ارسال هدرهای استاندارد امنیتی در تمام پاسخ‌ها: سیاست امنیت محتوا (CSP)، مسدودسازی جعل نوع فایل و ضد آی‌فریم."
    ),
    "220": (
        "Hides administrative action buttons in the frontend UI while leaving backend API endpoints accessible without authorization.",
        "Enforces strict role-based authorization checks inside backend route controllers, treating all client requests as untrusted.",
        "مخفی کردن دکمه‌های ادمین در ظاهر سایت در حالی که اندپوینت‌های بک‌اند بدون احراز دسترسی باز هستند.",
        "اعمال بررسی دسترسی درون تک‌تک کنترلرهای بک‌اند و نفی هرگونه اعتماد به پنهان‌سازی ظاهری در کلاینت."
    ),
    "234": (
        "Treats the frontend as a trusted security layer, relying on client-side price calculations and permission checks.",
        "Treats the frontend strictly as an untrusted display layer, re-calculating prices and re-validating permissions on the server.",
        "نگاه به فرانت‌اند به عنوان لایه قابل‌اعتماد و اتکا به محاسبات قیمت و مجوزهای کلاینت در پردازش‌ها.",
        "نگاه به فرانت‌اند صرفاً به عنوان لایه نمایش و محاسبه مجدد قیمت‌ها و اعتبارسنجی ۱۰۰٪ مجوزها در سرور."
    ),
    "254": (
        "Shares raw desktop web URLs on mobile marketing channels, landing mobile users on un-responsive, broken desktop layouts.",
        "Implements universal mobile deep-linking and responsive viewport routing to ensure seamless mobile onboarding experiences.",
        "ارسال لینک‌های دسکتاپ در کانال‌های تبلیغاتی موبایل که کاربران را به صفحات واکنش‌ناگرا و شکسته هدایت می‌کند.",
        "پیاده‌سازی لینک‌های هوشمند عمیق (Deep Linking) و هدایت خودکار به صفحات کاملاً واکنش‌گرا در موبایل."
    ),
    "284": (
        "Exposes private API secret keys in client-side bundles by prefixing sensitive tokens with public build prefixes (`NEXT_PUBLIC_`).",
        "Keeps private API secrets on server backends, exposing lightweight proxy endpoints to frontend clients.",
        "لو دادن کلیدهای محرمانه با تعریف آن‌ها در متغیرهای فرانت‌اند (`NEXT_PUBLIC_`) که در سورس مرورگر لو می‌روند.",
        "نگهداری کلیدهای محرمانه منحصراً در بک‌اند و ایجاد اندپوینت‌های واسط امن برای ارتباط فرانت‌اند."
    ),
    "290": (
        "Builds frontend components that handle only the happy path, showing blank screens or infinite spinners on network failure.",
        "Implements all 4 mandatory UI states (Loading skeleton, Error with interactive Retry, Empty guidance, and Success) for every view.",
        "طراحی کامپوننت‌ها فقط برای حالت خوش‌بینانه و نمایش صفحه سفید یا لودینگ ابدی در زمان قطعی شبکه.",
        "پیاده‌سازی اجباری وضعیت‌های چهارگانه UI (اسکلتون لودینگ، خطای معنادار با تلاش مجدد، وضعیت خالی و موفقیت)."
    ),
    "292": (
        "Accumulates chaotic frontend global state variables that cause random UI glitches and stale data across pages.",
        "Adopts structured server-state caching libraries (`@tanstack/react-query`) with automatic background refetching and cache invalidation.",
        "انباشت متغیرهای سراسری نامنظم در فرانت‌اند که باعث بروز گلیچ‌های تصویری و نمایش داده‌های قدیمی می‌شود.",
        "استفاده از کتابخانه‌های استاندارد مدیریت وضعیت سرور (React Query) با قابلیت کشینگ و به‌روزرسانی خودکار."
    ),
    "293": (
        "Equates full-stack development with knowing React and Node.js, ignoring the remaining 11 critical production engineering tiers.",
        "Masters the full 13-layer production stack from DNS routing and WAFs down to database connection pooling and disaster recovery.",
        "تقلیل مفهوم فول‌استک به نوشتن فرانت‌اند و بک‌اند و نادیده گرفتن ۱۱ لایه حیاتی دیگر در مهندسی سیستم.",
        "تسلط بر استک سیزده‌گانه تولید: از روتینگ DNS و فایروال تا استخر اتصالات دیتابیس و بازیابی پس از بحران."
    ),
    "296": (
        "Builds bespoke forms and buttons for every new page, creating an inconsistent and unmaintainable user interface.",
        "Standardizes frontend interfaces on a cohesive design system (shadcn/ui, Tailwind) with reusable typed component primitives.",
        "طراحی دستی و پراکنده فرم‌ها و دکمه‌ها در هر صفحه که ظاهری نامنظم و کدهایی سخت برای نگهداری ایجاد می‌کند.",
        "استانداردسازی رابط کاربری با دیزاین سیستم یکپارچه و کامپوننت‌های تایپ‌شده و قابل‌استفاده مجدد."
    ),
    "312": (
        "Submits mobile wrapper applications to Apple App Store review without account deletion options, facing immediate rejection.",
        "Audits mobile submissions against App Store Review Guidelines: implements in-app account deletion and explicit privacy disclosures.",
        "ارسال اپلیکیشن به اپ استور اپل بدون دکمه حذف حساب درون برنامه که به ریجکت قطعی برنامه منجر می‌شود.",
        "انطباق اپلیکیشن با قوانین بررسی اپ استور: دکمه حذف کامل حساب کاربری در تنظیمات و شفافیت در دسترسی‌ها."
    )
}

print(f"Loaded Part 2 definitions: {len(PART2_DATA)} episodes")
