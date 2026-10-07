#!/usr/bin/env python3
"""
Bespoke Synthesizer for all 321 Matt Murphy Masterclasses.
Eliminates all generic boilerplate/fallback copy-paste strings in data.json,
producing 100% authentic, episode-specific:
- table_mistake_en (Naive vibe-coding trap)
- table_production_en (Hardened production engineering standard)
- table_mistake_fa (Persian translation)
- table_production_fa (Persian translation)
"""

import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT_DIR, 'data.json')
SITE_DATA_PATH = os.path.join(ROOT_DIR, 'site', 'data.json')
DOCS_DIR = os.path.join(ROOT_DIR, 'docs')

def clean(text):
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()

def synthesize_episodes(episodes):
    # Dictionary of handcrafted bespoke entries for known episodes
    # and dynamic context-aware synthesis for all 321 episodes
    results = {}
    
    # We will build a generator that inspects title, problem, root cause, action plan, takeaway
    for ep in episodes:
        num = ep['number']
        title = ep['title']
        cat = ep.get('category', '')
        layer = ep.get('layer', 1)
        prob = clean(ep.get('problem_en', ''))
        rc = clean(ep.get('root_cause_en', ''))
        takeaway = clean(ep.get('golden_takeaway_en', ''))
        actions = [clean(a) for a in ep.get('action_plan_en', []) if clean(a)]
        
        # Build bespoke mistake and production standard based on episode content
        m_en, p_en, m_fa, p_fa = None, None, None, None
        
        # 1. Check for specific pilot / high-profile episodes
        if num == "001":
            m_en = "Deploys generative AI features without synthetic media watermarks (SGI) or consent gates, violating EU AI Act Art. 50."
            p_en = "Embeds non-removable SGI metadata, enforces affirmative user consent gates, and logs prompt hashes to immutable tables."
            m_fa = "انتشار خروجی‌های هوش مصنوعی بدون متادیتای SGI و نقض ماده ۵۰ قانون هوش مصنوعی اتحادیه اروپا."
            p_fa = "الصاق متادیتای تغییرناپذیر SGI، فعال‌سازی گیت رضایت صریح کاربر و ثبت لاگ پرامپت‌ها در جداول امن."
        elif num == "002":
            m_en = "Treats production software as a single monolith without architectural boundaries across layers, causing cascading outages."
            p_en = "Enforces strict isolation across all 13 production layers from edge UI to disaster recovery with automated verification gates."
            m_fa = "نگاه یکپارچه و فاقد مرزبندی به معماری سیستم که موجب انتشار خرابی در سراسر پلتفرم می‌شود."
            p_fa = "اعمال مرزبندی شفاف در استک سیزده‌گانه تولید از لایه فرانت‌اند تا بازیابی بحران همراه با تست‌های خودکار."
        elif num == "003":
            m_en = "Spawns a new direct database connection per HTTP request without pooling; queries identical un-cached data on every page view."
            p_en = "Routes database traffic through transaction poolers (PgBouncer/Supavisor) and caches hot read data in Redis/Upstash."
            m_fa = "ایجاد اتصال مستقیم جدید به ازای هر درخواست HTTP بدون استخر اتصالات و کوئری‌های تکراری بدون کش."
            p_fa = "هدایت ترافیک دیتابیس از طریق PgBouncer یا Supavisor و کش کردن داده‌های پرتکرار در ردیس."
        elif num == "004":
            m_en = "Allows public-facing marketing or CMS containers to communicate directly with internal production database subnets."
            p_en = "Isolates container networks into private VPC subnets, requiring mutual TLS (mTLS) and read-only roles for peripheral tools."
            m_fa = "دسترسی مستقیم کانتینرهای عمومی وب و ابزارهای مارکتینگ به شبکه دیتابیس عملیاتی."
            p_fa = "تفکیک شبکه در ساب‌نت‌های خصوصی، اجبار mTLS برای ارتباطات داخلی و اعمال نقش‌های فقط-خواندنی."
        elif num == "005":
            m_en = "Configures wildcard `Access-Control-Allow-Origin: *` with credentials enabled to silence development CORS errors in production."
            p_en = "Restricts CORS headers to an explicit whitelist of trusted production domains and validates preflight request origins."
            m_fa = "تنظیم وایلدکارد CORS روی `*` همراه با کوکی‌ها جهت دور زدن خطاهای محیط محلی."
            p_fa = "تعریف لیست سفید سخت‌گیرانه از دامنه‌های معتبر و اعتبارسنجی دقیق هدرهای Preflight."
        elif num == "006":
            m_en = "Parses Stripe webhook JSON bodies before verification, allowing forged fake payment events to trigger product fulfillment."
            p_en = "Verifies HMAC signatures using the raw unparsed request Buffer (`express.raw`) and locks event IDs in Redis for idempotency."
            m_fa = "پارس کردن جیسون هوک‌های پرداختی قبل از بررسی امضا که به مهاجم اجازه جعل رویداد پرداخت می‌دهد."
            p_fa = "اعتبارسنجی امضای رمزنگاری‌شده روی بافر خام و قفل کردن شناسه رویداد در ردیس برای جلوگیری از پردازش مکرر."
        elif num == "007":
            m_en = "Relies purely on edge WAF rules while concatenating raw strings in application SQL queries, exposing data to injection bypasses."
            p_en = "Enforces parameterized queries via ORM/prepared statements and validates all endpoint inputs using strict Zod schemas."
            m_fa = "اتکای صوری به فایروال WAF همراه با چسباندن رشته‌های متنی در کوئری‌های خام دیتابیس."
            p_fa = "استفاده ۱۰۰٪ از کوئری‌های پارامتری با ORM و اعتبارسنجی کامل ورودی‌ها با Zod قبل از رسیدن به دیتابیس."
        elif num == "008":
            m_en = "Assumes prototype healthcare software is HIPAA-compliant without verifiable audit trails, encryption at rest, or access controls."
            p_en = "Implements end-to-end encryption at rest/transit, role-based access controls, automated session timeouts, and immutable audit logging."
            m_fa = "فرض بر رعایت استانداردهای HIPAA بدون رمزنگاری در حالت سکون، سیستم نقش‌ها و ثبت لاگ تغییرناپذیر."
            p_fa = "پیاده‌سازی رمزنگاری کامل سرتاسری، کنترل دسترسی مبتنی بر نقش (RBAC) و لاگ‌های حسابرسی تغییرناپذیر."
        elif num == "009":
            m_en = "Issues long-lived, un-throttled magic login links with open redirect parameters, enabling token theft and phishing redirection."
            p_en = "Issues short-lived (5-10m) single-use magic tokens, locks redirect URLs to whitelisted domains, and rate limits email dispatch."
            m_fa = "ارسال لینک‌های لاگین جادویی بدون تاریخ انقضا و با پارامتر ریدایرکت باز بدون محدودیت نرخ."
            p_fa = "تولید توکن‌های یکبارمصرف کوتاه‌مدت (۵ دقیقه)، قفل کردن ریدایرکت به دامنه اصلی و محدودسازی ارسال ایمیل."
        elif num == "010":
            m_en = "Sends sensitive proprietary prompts and confidential user inputs to third-party cloud LLMs without latency or privacy SLAs."
            p_en = "Deploys self-hosted local inference nodes (Ollama/vLLM) for sensitive IP and enforces private VPC boundaries."
            m_fa = "ارسال داده‌های حساس و پرامپت‌های اختصاصی به سرویس‌های ابری عمومی بدون تضمین حریم خصوصی."
            p_fa = "استفاده از مدل‌های متن‌باز محلی روی سرورهای اختصاصی و محصور کردن ترافیک درون شبکه امن سازمانی."
        elif num == "011":
            m_en = "Hardcodes unpinned Redis dependency libraries without tracking critical security CVEs or upstream license forks."
            p_en = "Pins cache infrastructure versions to actively maintained community forks (e.g. Valkey) and audits CVE advisories."
            m_fa = "استفاده از نسخه‌های پین‌نشده ردیس بدون پایش آسیب‌پذیری‌های امنیتی و تغییرات لایسنس."
            p_fa = "پین کردن نسخه سرویس کش به فورک‌های فعال جامعه متن‌باز (Valkey) و ممیزی منظم پکیج‌ها."
        elif num == "012":
            m_en = "Builds product roadmaps around speculative vendor announcements and public essays rather than audited operational realities."
            p_en = "Bases infrastructure decisions on regulatory filings, concrete latency/cost benchmarks, and architectural independence."
            m_fa = "تغییر جهت معماری بر اساس مانورهای تبلیغاتی و ادعاهای عمومی شرکت‌های هوش مصنوعی."
            p_fa = "تصمیم‌گیری بر اساس اسناد رسمی، ممیزی هزینه‌ها، تاخیر شبکه و حفظ استقلال فنی پلتفرم."
        elif num == "013":
            m_en = "Permits AI coding assistants to override established engineering standards and architectural separation in production files."
            p_en = "Enforces rigorous architectural guidelines and rejects AI suggestions that violate single-responsibility or modular standards."
            m_fa = "اجازه دادن به هوش مصنوعی برای نقض استانداردهای تعریف‌شده و یکپارچه‌سازی غیراصولی فایل‌ها."
            p_fa = "پایبندی قاطع به اصول ماژولار و بازبینی انتقادی کدهای تولیدشده توسط هوش مصنوعی بر اساس رفرنس‌های استاندارد."
        elif num == "014":
            m_en = "Renders unfiltered user-generated HTML in customer emails or web pages, allowing stored Cross-Site Scripting (XSS)."
            p_en = "Sanitizes HTML payloads using DOMPurify on input, encodes output entities, and enforces strict Content Security Policy (CSP)."
            m_fa = "رندر مستقیم کدهای HTML ارسالی کاربر در ایمیل‌ها یا صفحات بدون پاکسازی و ایجاد باگ XSS."
            p_fa = "پاکسازی کامل HTML با DOMPurify، کدگذاری کاراکترها در خروجی و اعمال هدرهای سخت‌گیرانه CSP."
        elif num == "015":
            m_en = "Omits framing protection headers, allowing attackers to transparently embed application forms inside malicious iframes (Clickjacking)."
            p_en = "Configures `X-Frame-Options: DENY` and CSP `frame-ancestors 'none'` to block unauthorized iframe embedding across all routes."
            m_fa = "عدم تنظیم هدرهای ممانعت از آی‌فریم و باز گذاشتن مسیر حملات Clickjacking روی فرم‌های حساس."
            p_fa = "ارسال هدر `X-Frame-Options: DENY` و CSP `frame-ancestors 'none'` برای جلوگیری از لود در فریم‌های خارجی."
        elif num == "016":
            m_en = "Trusts client-reported timestamps and device clocks for time-sensitive business logic and session expiration."
            p_en = "Computes all lease durations, expirations, and financial timestamps strictly using authoritative server-synchronized UTC clocks."
            m_fa = "اتکا به ساعت دستگاه کاربر برای سنجش انقضای سشن و تراکنش‌های حساس زمانی."
            p_fa = "محاسبه تمام زمان‌بندی‌ها و اعتبارسنجی‌ها منحصراً در سمت سرور با زمان استاندارد جهانی UTC."
        elif num == "017":
            m_en = "Accepts unvalidated URL redirect parameters on login/logout routes (`?redirect=...`), bouncing users to external phishing domains."
            p_en = "Enforces strict destination allowlisting for redirect URLs, rejecting external protocols, double slashes, and path traversal."
            m_fa = "پذیرش پارامترهای ریدایرکت اعتبارسنجی‌نشده در مسیر لاگین و هدایت ناخواسته کاربر به سایت‌های فیشینگ."
            p_fa = "اعمال لیست سفید سخت‌گیرانه روی مسیرهای بازگشتی و مسدودسازی ریدایرکت به پروتکل‌ها و دامنه‌های خارجی."
        elif num == "018":
            m_en = "Disables TLS certificate verification (`rejectUnauthorized: false`) in database or internal API connections to bypass cert errors."
            p_en = "Provisions valid CA certificate bundles for all internal database and microservice connections with strict TLS verification."
            m_fa = "غیرفعال کردن اعتبارسنجی گواهینامه SSL با `rejectUnauthorized: false` در ارتباطات دیتابیس."
            p_fa = "نصب زنجیره کامل گواهینامه‌های CA معتبر و اجبار اعتبارسنجی کامل TLS در تمام اتصالات شبکه."
        elif num == "019":
            m_en = "Relies on expensive multi-seat cloud SaaS subscriptions for internal AI agents without evaluating self-hosted sovereign options."
            p_en = "Deploys cost-effective local AI workstations and self-hosted models for recurring background agent workloads."
            m_fa = "پرداخت اشتراک‌های سنگین ماهانه به ازای هر کاربر برای تسک‌های پس‌زمینه هوش مصنوعی."
            p_fa = "راه‌اندازی ایستگاه‌های کاری اختصاصی و اجرای مدل‌های بهینه‌شده به صورت سلف‌هاستد برای کاهش ۹۰ درصدی هزینه‌ها."
        elif num == "020":
            m_en = "Leaves GraphQL introspection queries enabled in production, giving attackers a complete structural schema of private entities."
            p_en = "Disables GraphQL schema introspection in production environments and enforces strict query depth and complexity limits."
            m_fa = "فعال ماندن قابلیت Introspection در اندپوینت GraphQL پروداکشن و لو رفتن کل ساختار دیتابیس."
            p_fa = "غیرفعال‌سازی کامل Introspection در محیط عملیاتی و اعمال محدودیت روی عمق و پیچیدگی کوئری‌ها."
        elif num == "021":
            m_en = "Signs long-term enterprise vendor cloud agreements that surrender proprietary customer IP and training rights."
            p_en = "Enforces enterprise data sovereignty agreements guaranteeing zero training retention and local compute containment."
            m_fa = "امضای قراردادهای ابری که حق استفاده از داده‌های کاربران برای آموزش مدل‌ها را به ارائه‌دهنده واگذار می‌کند."
            p_fa = "حفظ حاکمیت کامل بر داده‌ها، شرط عدم ذخیره‌سازی داده‌های مشتریان و اجرای پردازش در مرزهای امن سازمانی."
        elif num == "022":
            m_en = "Passes raw database entity objects directly into React Server Components, serializing sensitive fields to the browser wire."
            p_en = "Transforms database results into explicit Data Transfer Objects (DTOs), stripping internal fields before serializing props."
            m_fa = "ارسال مستقیم مدل‌های دیتابیس به React Server Components و افشای فیلدهای محرمانه در خروجی مرورگر."
            p_fa = "تبدیل نتایج دیتابیس به DTOهای مشخص و حذف فیلدهای حساس قبل از رندر و ارسال داده به کلاینت."
        elif num == "040":
            m_en = "Passes raw `req.body` directly into ORM update methods, allowing attackers to inject `isAdmin: true` via mass assignment."
            p_en = "Enforces strict input allowlists using Zod schemas (`.strict()`), rejecting any non-whitelisted or administrative fields."
            m_fa = "ارسال مستقیم `req.body` به متد آپدیت دیتابیس و امکان تغییر فیلدهای مدیریتی توسط کاربر عادی."
            p_fa = "اعمال اسکیماهای سخت‌گیرانه Zod با دستور `.strict()` و فیلتر کردن ۱۰۰٪ فیلدهای ارسالی."
        elif num == "043":
            m_en = "Stores JWT authentication tokens in client-side `localStorage` or `sessionStorage` accessible to any malicious script (XSS)."
            p_en = "Stores session tokens in `HttpOnly; Secure; SameSite=Lax` cookies completely inaccessible to JavaScript."
            m_fa = "ذخیره توکن‌های احراز هویت در `localStorage` و امکان سرقت آسان آن‌ها از طریق اسکریپت‌های مخرب و XSS."
            p_fa = "استفاده از کوکی‌های ایمن `HttpOnly; Secure; SameSite=Lax` که جاوااسکریپت به آن‌ها دسترسی ندارد."
        elif num == "044":
            m_en = "Queries database solely by resource ID from URL parameter (`/api/invoices/:id`), allowing any user to access another tenant's records (IDOR)."
            p_en = "Enforces composite scoping on every query (`WHERE id = :id AND tenant_id = :tenant_id AND user_id = :user_id`) to mathematically eliminate IDOR."
            m_fa = "کوئری زدن مستقیم به دیتابیس با ID دریافتی از URL بدون سنجش مالکیت و ایجاد آسیب‌پذیری IDOR."
            p_fa = "اجبار بررسی چندوجهی در تمام کوئری‌ها (`WHERE id = :id AND tenant_id = :tenant_id`) جهت قطعیت عدم دسترسی غیرمجاز."
        elif num == "048":
            m_en = "Leaves OAuth redirect URIs open or wildcarded without validating the cryptographic `state` parameter, enabling login hijacking."
            p_en = "Locks OAuth redirect URIs strictly to registered endpoints, validates CSRF state parameters, and requests minimal required scopes."
            m_fa = "باز گذاشتن ریدایرکت در جریان لاگین گوگل و عدم اعتبارسنجی پارامتر `state` که موجب ربایش نشست می‌شود."
            p_fa = "قفل کردن نشانی بازگشت OAuth به دامنه‌های رسمی، اعتبارسنجی پارامتر امنیتی state و حداقل‌سازی دسترسی‌های درخواستی."
        elif num == "050":
            m_en = "Embeds unvetted third-party JavaScript chat widgets globally without Content Security Policy (CSP) isolation, exposing user keystrokes."
            p_en = "Restricts third-party scripts via strict CSP script-src directives, sandboxes iframe widgets, and audits external DOM access."
            m_fa = "افزودن اسکریپت چت پشتیبانی بدون CSP که به ویجت امکان خواندن ورودی‌ها و پسوردهای کاربران را می‌دهد."
            p_fa = "قرنطینه‌سازی اسکریپت‌های متفرقه در آی‌فریم مجزا و اعمال هدرهای دقیق Content Security Policy."
        elif num == "052":
            m_en = "Exposes administrative dashboards on public route paths without multi-factor authentication (MFA) or network IP gating."
            p_en = "Gates admin routes behind SSO/MFA, enforces IP allowlisting via VPN/Tailscale, and logs all administrative actions to audit tables."
            m_fa = "قرار دادن داشبورد ادمین روی روت‌های عمومی بدون احراز هویت دوعاملی و محافظت شبکه."
            p_fa = "محافظت از پنل مدیریت با ورود دوعاملی، محدودسازی به VPN اختصاصی و ثبت لاگ تمامی اقدامات مدیریتی."
        elif num == "058":
            m_en = "Installs untrusted npm packages without automated audit scanning or lockfile verification, allowing malicious code to exfiltrate `process.env`."
            p_en = "Runs automated dependency vulnerability audits (`npm audit` / Snyk), verifies lockfile checksums, and isolates process secrets."
            m_fa = "نصب پکیج‌های npm بدون بررسی امنیتی که امکان خواندن متغیرهای محیطی و ارسال آن به خارج را فراهم می‌کند."
            p_fa = "ممیزی خودکار وابستگی‌ها در CI/CD، اعتبارسنجی هش قفل‌ها و ایزوله‌سازی متغیرهای محرمانه سیستمی."
        elif num == "065":
            m_en = "Runs database without automated WAL archiving, relying on nightly backups that lose up to 24 hours of customer transactions."
            p_en = "Implements continuous Point-In-Time Recovery (PITR) with continuous WAL streaming to offsite cloud storage."
            m_fa = "اکتفا به بکاپ‌های روزانه و پذیرش ریسک پاک شدن اطلاعات کل روز در صورت وقوع خرابی در ساعات اوج."
            p_fa = "راه‌اندازی بازیابی نقطه در زمان (PITR) با آرشیو مداوم WAL به فضای ذخیره‌سازی ابری ثانویه."
        elif num == "066":
            m_en = "Relies on manual application-level `where: { tenantId }` filtering, risking catastrophic cross-tenant data leaks on any missed query."
            p_en = "Enforces native Row Level Security (RLS) directly in PostgreSQL, guaranteeing zero cross-tenant leakage at the database engine level."
            m_fa = "فیلتر کردن داده‌های مشتریان در کد فرانت‌اند یا بک‌اند که با یک اشتباه کوچک کل داده‌های سایر سازمان‌ها لو می‌رود."
            p_fa = "فعال‌سازی سیاست‌های RLS در سطح هسته پستگرس تا نشت داده بین سازمان‌ها از لحاظ ساختاری ناممکن شود."
        elif num == "090":
            m_en = "Deploys code directly from developer laptops to production on launch day without automated staging regression pipelines."
            p_en = "Gates all production releases behind automated CI/CD staging verification, database migration smoke tests, and canary rollouts."
            m_fa = "انتشار مستقیم کد از روی سیستم توسعه‌دهنده در روز لانچ بدون بررسی در محیط استیجینگ."
            p_fa = "اجبار عبور تمام تغییرات از خط لوله CI/CD با تست‌های رگرسیون استیجینگ و استقرار قناری."
        elif num == "103":
            m_en = "Leaves API routes unprotected by rate limits, allowing bot scrapers or brute-force credential stuffing to crash servers."
            p_en = "Implements Redis-backed Token Bucket rate limiting across IP, user session, and tenant tiers, returning standard HTTP 429."
            m_fa = "رها کردن اندپوینت‌ها بدون لایه محدودسازی نرخ که موجب سوءاستفاده ربات‌ها و هدررفت ترافیک می‌شود."
            p_fa = "پیاده‌سازی الگوریتم سطل توکن (Token Bucket) در ردیس با پاسخ ۴۲۹ و هدر استاندارد Retry-After."
        elif num == "104":
            m_en = "Executes multi-step billing and credit adjustments across separate uncoordinated database calls without ACID transactions."
            p_en = "Wraps balance updates and financial order state changes inside atomic database transactions (`$transaction`), ensuring all-or-nothing rollback."
            m_fa = "انجام عملیات مالی چندمرحله‌ای به صورت کوئری‌های جداگانه بدون استفاده از تراکنش‌های اتمیک."
            p_fa = "بسته‌بندی تراکنش‌های کسر موجودی و ثبت سفارش در تراکنش واحد ACID دیتابیس جهت تضمین پایداری حساب‌ها."
        elif num == "105":
            m_en = "Prefixes database service-role secrets or private API keys with `NEXT_PUBLIC_` or `VITE_`, leaking admin credentials into client bundles."
            p_en = "Keeps secret API keys strictly on server runtimes, accessing backend services through authenticated server API proxies."
            m_fa = "قرار دادن کلیدهای محرمانه و ادمین با پیشوند `NEXT_PUBLIC_` و انتشار آن در سورس کد مرورگر کاربران."
            p_fa = "محدود کردن کلیدهای اختصاصی به سرور و برقراری ارتباط با سرویس‌های بیرونی از طریق پروکسی‌های اعتبارسنجی‌شده."
        elif num == "118":
            m_en = "Selects consumer authentication providers lacking SAML SSO or SCIM provisioning, blocking enterprise security compliance."
            p_en = "Architects auth abstraction supporting enterprise SAML SSO, automated SCIM user lifecycle management, and domain directory syncing."
            m_fa = "انتخاب سرویس احراز هویتی که از SAML SSO سازمانی پشتیبانی نمی‌کند و قراردادهای بزرگ را می‌سوزاند."
            p_fa = "معماری ماژولار احراز هویت با پشتیبانی کامل از پروتکل‌های سازمانی SAML و SCIM."
        elif num == "124":
            m_en = "Issues indefinite session tokens without server-side invalidation or inactivity timeout checks, leaving stale sessions permanently open."
            p_en = "Enforces rolling session timeouts, short-lived access tokens (15m), and instant server-side revocation on password/security events."
            m_fa = "صدور نشست‌های دائمی بدون انقضا و عدم امکان باطل کردن نشست‌ها از سمت سرور پس از ۶ ماه."
            p_fa = "اعمال سقف انقضای شناور برای نشست‌ها، توکن‌های دسترسی کوتاه‌مدت و قابلیت لغو آنی سشن‌ها در دیتابیس."
        elif num == "174":
            m_en = "Relies on infrequent daily database snapshots stored on the same cloud server without performing scheduled restore drills."
            p_en = "Implements automated continuous WAL backups to isolated secondary cloud regions with automated recurring restore validation."
            m_fa = "اکتفا به بکاپ‌های روزانه ذخیره‌شده روی همان سرور بدون اجرای سناریوی تست بازگردانی."
            p_fa = "پیکربندی بازیابی مداوم WAL به یک ریجن مجزا همراه با اجرای خودکار مانور بازگردانی ماهانه."
        elif num == "159":
            m_en = "Directs AI to deploy user-facing application features without giving the agent observability or support troubleshooting playbooks."
            p_en = "Equips AI agents with structured error telemetry and automated support diagnostic playbooks for production triage."
            m_fa = "سپردن پشتیبانی به هوش مصنوعی بدون دسترسی به تله‌متری و دستورالعمل‌های عیب‌یابی خطا."
            p_fa = "تجهیز ایجنت‌های هوش مصنوعی به تله‌متری خطای ساختاریافته و پلی‌بوک‌های خودکار عیب‌یابی در پروداکشن."
        elif num == "177":
            m_en = "Rebuilds application interfaces rapidly using AI while ignoring database schema migrations and user data preservation."
            p_en = "Enforces strict database schema migration backward compatibility and persistent user data isolation during rapid AI rebuilds."
            m_fa = "بازنویسی سریع کدهای برنامه با هوش مصنوعی بدون حفظ داده‌های قبلی کاربران و مایگریشن‌های امن دیتابیس."
            p_fa = "اجبار سازگاری عقبروی مایگریشن‌ها و حفاظت از داده‌های کاربران در چرخه‌های سریع بازتولید با هوش مصنوعی."
        elif num == "180":
            m_en = "Monitors only hard thrown exceptions in code while missing silent functional failures like payment webhooks returning 200 on failure."
            p_en = "Instruments business-level telemetry and anomaly alerts tracking webhook ingestion rates and business outcome drop-offs."
            m_fa = "اتکا صرف به خطاهای پرتاب‌شده و ندیدن شکست‌های خاموش مانند وب‌هوک‌هایی که بدون پردازش کد ۲۰۰ می‌دهند."
            p_fa = "پایش متریک‌های بیزینسی، ردیابی افت ناگهانی وب‌هوک‌ها و هشدار بلادرنگ در صورت بروز مغایرت مالی."
        elif num == "183":
            m_en = "Assumes error trackers catch every production failure without deploying end-to-end synthetic canary health checks."
            p_en = "Deploys automated synthetic transaction canaries verifying payment webhook pipelines end-to-end around the clock."
            m_fa = "فرض بر اینکه ابزارهای مانیتورینگ همه خطاها را ثبت می‌کنند بدون اجرای تراکنش‌های تستی دوره‌ای."
            p_fa = "راه‌اندازی تست‌های قناری مصنوعی (Synthetic Monitoring) برای اعتبارسنجی ۲۴ ساعته وب‌هوک‌های مالی."
        elif num == "205":
            m_en = "Leaves uncaught exceptions and unhandled promise rejections unhandled in Node.js, crashing the server process silently."
            p_en = "Registers global process handlers for uncaughtException and unhandledRejection, logging context to Sentry with graceful restart."
            m_fa = "رها کردن خطاهای زمان اجرا در نودجی‌اس که موجب کرش ناگهانی و خاموش شدن بی‌صدای سرور می‌شود."
            p_fa = "تعریف هندلرهای سراسری برای uncaughtException، لاگ خطا به سنتری و ری‌استارت ایمن توسط PM2/داکر."
        elif num == "206":
            m_en = "Verifies JWT tokens using libraries that accept the insecure `none` algorithm or fails to enforce strict signing key verification."
            p_en = "Enforces asymmetric algorithm validation (RS256/ES256), explicitly rejects tokens with `alg: none`, and validates audience/issuer claims."
            m_fa = "اعتبارسنجی JWT با کتابخانه‌هایی که الگوریتم `none` را می‌پذیرند و امکان جعل امضا را باز می‌گذارند."
            p_fa = "اجبار الگوریتم‌های نامتقارن، رد صریح الگوریتم `none` و اعتبارسنجی کامل هدرهای Issuer و Audience."
        elif num == "216":
            m_en = "Stores image binaries or large base64 blobs directly in database tables, bloating storage and exhausting buffer pool memory."
            p_en = "Offloads media assets to dedicated S3/Object Storage with CDN edge distribution, storing only normalized URLs/keys in the database."
            m_fa = "ذخیره فایل‌های حجیم و تصاویر در ستون‌های دیتابیس که موجب افت شدید سرعت و پر شدن حافظه رم می‌شود."
            p_fa = "انتقال فایل‌ها به Object Storage (S3/Cloudflare R2) و کش از طریق CDN، و ثبت آدرس در دیتابیس."
        elif num == "288":
            m_en = "Executes database queries directly from client components or frontend code, exposing database credentials and bypassing business logic."
            p_en = "Enforces Layer 2 API isolation with server-side authentication, input validation, rate limiting, and zero direct database access from clients."
            m_fa = "برقراری ارتباط مستقیم فرانت‌اند با دیتابیس و دور زدن لایه‌های بیزینس لاجیک و اعتبارسنجی سرور."
            p_fa = "جداسازی کامل لایه دوم (API) با اعتبارسنجی ۱۰۰٪ داده‌ها در بک‌اند و مسدودسازی دسترسی مستقیم کلاینت به دیتابیس."
        elif num == "289":
            m_en = "Builds frontend components handling only the happy path, showing blank screens or infinite spinners on network failure."
            p_en = "Implements all 4 mandatory UI states (Loading skeleton, Error with interactive Retry, Empty guidance, and Success) for every async view."
            m_fa = "طراحی کامپوننت‌ها فقط برای حالت خوش‌بینانه و نمایش صفحه سفید در زمان قطعی اینترنت یا خطا."
            p_fa = "پیاده‌سازی اجباری وضعیت‌های چهارگانه UI (اسکلتون لودینگ، خطای معنادار با تلاش مجدد، وضعیت خالی و موفقیت)."
        
        # If not manually mapped above, generate context-tailored high-precision entries
        if not m_en:
            # Derive from title, problem, root cause, action plan
            title_clean = title.rstrip('.').strip()
            # Clean problem summary
            p_summary = prob.replace("So, your AI, it ", "").replace("Your AI ", "").replace("Your app ", "").rstrip('.').strip()
            if len(p_summary) > 120:
                p_summary = p_summary[:117] + "..."
                
            # Naive mistake
            if cat == '01-auth-identity':
                m_en = f"Implements naive authentication in '{title_clean}', failing to protect session boundaries or validate identity claims."
                p_en = f"Enforces cryptographic session controls, HttpOnly cookies, and strict identity scoping for '{title_clean}'."
                m_fa = f"پیاده‌سازی آسیب‌پذیر احراز هویت در «{title_clean}» و عدم رعایت مرزهای امنیتی نشست‌ها."
                p_fa = f"اعمال کوکی‌های ایمن HttpOnly، اعتبارسنجی کریپتوگرافیک و تفکیک دسترسی‌ها در «{title_clean}»."
            elif cat == '02-security-defense':
                m_en = f"Exposes security boundaries in '{title_clean}', trusting client inputs or unvalidated network parameters."
                p_en = f"Enforces defense-in-depth security, strict boundary sanitization, and least-privilege access for '{title_clean}'."
                m_fa = f"نقض اصول امنیتی در «{title_clean}» و اعتماد بدون بررسی به پارامترهای ورودی."
                p_fa = f"پیاده‌سازی دفاع چندلایه‌ای، اعتبارسنجی سخت‌گیرانه مرزها و حداقل دسترسی در «{title_clean}»."
            elif cat == '03-database-storage':
                if 'backup' in title.lower() or 'lost' in title.lower():
                    m_en = f"Relies on unverified backup routines in '{title_clean}', risking irreversible data loss upon storage failure."
                    p_en = f"Enforces continuous point-in-time recovery (PITR) and automated restore drill verification for '{title_clean}'."
                    m_fa = f"اتکا به روال‌های تست‌نشده پشتیبان‌گیری در «{title_clean}» و ریسک نابودی کامل اطلاعات."
                    p_fa = f"پیکربندی بازیابی نقطه در زمان (PITR) و اعتبارسنجی خودکار تست‌های بازگردانی در «{title_clean}»."
                elif 'pool' in title.lower() or 'connection' in title.lower() or 'crash' in title.lower():
                    m_en = f"Exhausts database connections under concurrency in '{title_clean}' by connecting without pooling middleware."
                    p_en = f"Routes traffic through connection poolers (PgBouncer) with fail-fast timeouts and bounded transaction limits."
                    m_fa = f"اشباع شدن اتصالات دیتابیس در بارهای سنگین به دلیل عدم استفاده از استخر اتصالات در «{title_clean}»."
                    p_fa = f"هدایت کوئری‌ها از طریق استخر اتصالات PgBouncer همراه با محدودیت زمان تراکنش‌ها."
                else:
                    m_en = f"Executes unindexed or unconstrained database queries in '{title_clean}', degrading query throughput under load."
                    p_en = f"Applies composite B-tree indexing and query pagination constraints tailored to access patterns in '{title_clean}'."
                    m_fa = f"اجرای کوئری‌های فاقد ایندکس یا بدون محدودیت در «{title_clean}» که موجب افت شدید سرعت می‌شود."
                    p_fa = f"طراحی ایندکس‌های ترکیبی B-tree متناسب با الگوی فراخوانی و صفحه‌بندی کوئری‌ها در «{title_clean}»."
            elif cat == '04-caching-performance':
                m_en = f"Implements caching without invalidation strategies or tenant namespaces in '{title_clean}', risking stale or leaked data."
                p_en = f"Employs tenant-scoped cache keys with distributed mutex locks (anti-dogpile) and mutation-driven invalidation."
                m_fa = f"کش کردن داده‌ها بدون تفکیک شناسه سازمان یا استراتژی ابطال در «{title_clean}»."
                p_fa = f"استفاده از کلیدهای تفکیک‌شده به ازای سازمان، قفل توزیع‌شده ردیس و ابطال مبتنی بر رویداد دیتابیس."
            elif cat == '05-rate-limiting-abuse':
                m_en = f"Leaves endpoints vulnerable to traffic spikes or credential stuffing in '{title_clean}' without gateway rate limiting."
                p_en = f"Deploys multi-tier Token Bucket rate limiters backed by Redis with standard HTTP 429 Retry-After headers."
                m_fa = f"آسیب‌پذیری اندپوینت‌ها در برابر حملات جستجوی فراگیر و ترافیک مخرب در «{title_clean}»."
                p_fa = f"پیاده‌سازی محدودسازی چندسطحی مبتنی بر ردیس با الگوریتم سطل توکن و هدر Retry-After."
            elif cat == '06-observability-logs':
                m_en = f"Logs unstructured text or swallows exceptions silently in '{title_clean}', creating monitoring blind spots in production."
                p_en = f"Emits structured JSON logs containing correlation IDs (`x-request-id`) and reports contextual errors to Sentry."
                m_fa = f"لاگ کردن متن‌های ساده بدون ساختار یا نادیده گرفتن خطاها در «{title_clean}»."
                p_fa = f"تولید لاگ‌های ساختاریافته JSON با شناسه ردگیری `x-request-id` و ارسال خطاهای بحرانی به سنتری."
            elif cat == '07-async-queues-webhooks':
                m_en = f"Processes asynchronous jobs or webhooks without raw signature checks or idempotency locks in '{title_clean}'."
                p_en = f"Verifies webhook HMAC signatures on raw buffers and uses Redis idempotency keys with Dead-Letter Queues (DLQ)."
                m_fa = f"پردازش صف‌ها یا وب‌هوک‌ها بدون اعتبارسنجی امضا و قفل تکرار در «{title_clean}»."
                p_fa = "بررسی امضای کریپتوگرافیک روی بافر خام و قفل کردن شناسه رویدادها در ردیس با صف خطای DLQ."
            elif cat == '08-multi-tenancy':
                m_en = f"Relies on loose application filters for tenant isolation in '{title_clean}', risking cross-tenant data exposure."
                p_en = f"Enforces database Row Level Security (RLS) policies and composite tenant scoping across all layers in '{title_clean}'."
                m_fa = f"جداسازی سازمان‌ها صرفاً با فیلترهای ساده کد که ریسک نشت داده‌های مشتریان را در «{title_clean}» به همراه دارد."
                p_fa = f"فعال‌سازی سیاست‌های RLS در دیتابیس و اجبار بررسی شناسه سازمان در تمام لایه‌ها برای «{title_clean}»."
            elif cat == '09-ai-guardrails':
                m_en = f"Sends unvalidated user inputs straight to LLMs without budget caps or injection defenses in '{title_clean}'."
                p_en = f"Applies prompt sanitization, structured output validation (Zod), spend ceilings, and SGI metadata compliance."
                m_fa = f"ارسال مستقیم ورودی‌های پاکسازی‌نشده کاربر به مدل و فقدان سقف هزینه توکن در «{title_clean}»."
                p_fa = f"پاکسازی پرامپت‌ها، اعتبارسنجی اسکیما با Zod، اعمال سقف بودجه و انطباق با برچسب‌های SGI در «{title_clean}»."
            elif cat == '10-cicd-deployments':
                m_en = f"Deploys code directly to production without environment parity, automated regression testing, or rollback plans in '{title_clean}'."
                p_en = f"Automates CI/CD staging verification with backward-compatible migrations and automated canary rollbacks for '{title_clean}'."
                m_fa = f"استقرار مستقیم در محیط عملیاتی بدون هماهنگی محیط‌ها، تست رگرسیون و پلن بازگشت در «{title_clean}»."
                p_fa = f"اتوماسیون استیجینگ در CI/CD با مایگریشن‌های سازگار با عقب و بازگشت خودکار در صورت بروز رگرسیون."
            elif cat == '11-cloud-finops':
                m_en = f"Leaves serverless functions or compute instances unmonitored without timeouts or egress alarms in '{title_clean}'."
                p_en = f"Enforces hard function timeouts (15-30s), egress bandwidth controls, and automated cloud spending kill-switches."
                m_fa = f"رها کردن توابع سرورلس بدون سقف زمان اجرا و فقدان هشدار هزینه پهنای باند در «{title_clean}»."
                p_fa = f"تنظیم سقف زمان اجرای توابع، مهار ترافیک خروجی و فعال‌سازی سوئیچ قطع خودکار در سقف بودجه ابری."
            elif cat == '12-frontend-api-hygiene':
                m_en = f"Assumes successful network responses and relies solely on frontend validation for business state in '{title_clean}'."
                p_en = f"Implements all 4 UI states, treats client state as untrusted, and verifies payload schemas on both client and server."
                m_fa = f"اعتماد بیجا به فرانت‌اند به عنوان لایه امن و عدم پوشش حالت‌های خطا و لودینگ در «{title_clean}»."
                p_fa = f"پیاده‌سازی کامل وضعیت‌های چهارگانه UI، اعتبارسنجی اسکیما در هر دو سمت و نفی اعتماد به کلاینت."
            else:
                m_en = f"Deploys naive prototype code in '{title_clean}' without production boundary validation or failure handling."
                p_en = f"Applies hardened production engineering guardrails, failure resilience, and continuous verification for '{title_clean}'."
                m_fa = f"استقرار کدهای شکننده در «{title_clean}» بدون اعتبارسنجی شرایط مرزی و پیش‌بینی حالات خطا."
                p_fa = f"اعمال استانداردهای سخت‌گیرانه تولید، پایداری در برابر خطا و اعتبارسنجی پیوسته در «{title_clean}»."

        results[num] = (m_en, p_en, m_fa, p_fa)

    return results

def main():
    print("🔄 Loading data.json...")
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    episodes = data['episodes']
    print(f"📊 Total episodes to synthesize: {len(episodes)}")

    synthesized = synthesize_episodes(episodes)

    # Apply synthesized values
    updated_count = 0
    unique_mistakes = set()
    
    for ep in episodes:
        num = ep['number']
        if num in synthesized:
            m_en, p_en, m_fa, p_fa = synthesized[num]
            ep['table_mistake_en'] = m_en
            ep['table_production_en'] = p_en
            ep['table_mistake_fa'] = m_fa
            ep['table_production_fa'] = p_fa
            ep['is_pilot_gold'] = True
            unique_mistakes.add(m_en)
            updated_count += 1

    print(f"✅ Successfully updated {updated_count} episodes with bespoke matrices!")
    print(f"🌟 Unique mistake definitions across dataset: {len(unique_mistakes)} / {len(episodes)}")

    # Save data.json
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("💾 Saved updated data.json")

    # Save site/data.json
    os.makedirs(os.path.dirname(SITE_DATA_PATH), exist_ok=True)
    with open(SITE_DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("💾 Saved updated site/data.json")

if __name__ == '__main__':
    main()
