// Matt Murphy Production Engineering Academy - Multilingual Application Logic

let rawData = null;
let allEpisodes = [];
let filteredEpisodes = [];
let currentCategory = 'all';
let currentSearch = '';
let displayLimit = 30;
let currentLang = 'en';

// Multilingual UI Translation Dictionaries
const I18N = {
  en: {
    announcement: 'Bridging the chasm between "Vibe Coding" and hardened, production-grade engineering | Based on 320+ Matt Murphy masterclasses',
    auditLink: 'Audit your project online →',
    tabExplorer: '📚 Masterclasses (320)',
    tabLayers: '🏛️ 13 Production Layers',
    tabAudit: '🛡️ Production Audit',
    tabSkill: '🤖 AI Agent Skill',
    heroTag: '🛡️ Production Systems Architecture',
    heroTitle: 'Hardened Systems Knowledge Base: <br><span class="bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">320+ Critical Lessons for Software Resilience</span>',
    heroDesc: 'AI-generated scaffolding works in happy-path demos, but collapses under real-world traffic, multi-tenant leaks, and adversarial attacks. This platform codifies Matt Murphy\'s production engineering principles into standardized <strong class="text-white">Problem Statements, Root Causes, Action Checklists, and Hardened Code</strong>.',
    searchPlaceholder: 'Search by episode (e.g. 043), title, keywords (JWT, RLS, Stripe, DoS, cookie)...',
    allDomains: 'All Domains (12 Modules)',
    allBadge: 'All',
    showingStats: 'Showing <span id="results-count" class="font-bold text-emerald-400">0</span> of 321 masterclasses',
    filterLabel: 'Filter: ',
    loadMore: 'Load more masterclasses...',
    readDetails: 'Root Cause & Code →',
    layersTitle: 'The 13 Modern Production Layers Platform',
    layersDesc: 'Full-stack does not mean frontend and backend. Production resilience is an interdependent 13-layer platform. A defect in any layer brings down the entire system.',
    viewLayerLessons: 'Explore layer lessons →',
    auditBadge: '🛠️ Interactive Production Auditor',
    auditTitle: 'Is Your Application Hardened for Production?',
    auditDesc: 'Verify your application against the top architectural, security, and scalability failure modes discovered across 320+ Matt Murphy production audits.',
    scoreLabel: 'Your Production Hardening Score:',
    exportReport: 'Export Audit Report (Markdown)',
    modalProblem: 'Problem Statement & Attack Vector',
    modalRootCause: 'Root Cause & Architectural Solution',
    modalActionPlan: 'Hardening Action Checklist',
    modalCode: 'Hardened Production Code / Config',
    modalTranscript: 'Original Spoken Audio Transcript',
    modalViewReel: 'Watch Reel on Instagram',
    modalClose: 'Close',
    footerAttr: 'Codified from the engineering masterclasses of <a href="https://www.instagram.com/mattmurphyai" target="_blank" class="text-emerald-400 hover:underline">Matt Murphy</a> by the DoctorGuidance Team'
  },
  fa: {
    announcement: 'گذر از «وایب‌کدینگ سطحی» به مهندسی آزموده‌شده در پروداکشن | مبتنی بر ۳۲۰+ درس ویدیویی و صوتی مت مورفی',
    auditLink: 'ارزیابی آنلاین پروژه شما ←',
    tabExplorer: '📚 بانک دروس (۳۲۰)',
    tabLayers: '🏛️ ماتریس ۱۳ لایه',
    tabAudit: '🛡️ ارزیابی آمادگی پروداکشن',
    tabSkill: '🤖 اسکیل هوش مصنوعی',
    heroTag: '🛡️ اصول مهندسی سیستم‌های پایدار',
    heroTitle: 'دانش‌نامه و پایگاه قواعد پروداکشن: <br><span class="bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">۳۲۰ درس کلیدی برای تاب‌آوری نرم‌افزار</span>',
    heroDesc: 'کدهای تولیدشده توسط مدل‌های زبانی در نگاه اول کار می‌کنند، اما در مواجهه با ترافیک واقعی، حملات امنیتی و تداخل داده‌ها فرومی‌پاشند. این پلتفرم تمامی تجربیات زیسته مت مورفی را به ساختار استاندارد <strong class="text-white">طرح مسئله، ریشه معماری، چک‌لیست عمل و کد ضدگلوله</strong> تبدیل کرده است.',
    searchPlaceholder: 'جستجو بر اساس شماره اپیزود (مثلا 043)، عنوان، کلمات فارسی یا انگلیسی (JWT, RLS, Stripe, DoS)...',
    allDomains: 'تمامی حوزه‌ها (۱۲ دسته مهندسی)',
    allBadge: 'همه',
    showingStats: 'نمایش <span id="results-count" class="font-bold text-emerald-400">0</span> درس از ۳۲۱ درس ثبت‌شده',
    filterLabel: 'فیلتر: ',
    loadMore: 'بارگذاری موارد بیشتر...',
    readDetails: 'تحلیل ریشه‌ای و کد ←',
    layersTitle: 'پلتفرم ۱۳ لایه توسعه پروداکشن مدرن',
    layersDesc: 'فول‌استک به معنای فرانت‌اند و بک‌اند نیست؛ یک سیستم تولید پایدار از ۱۳ لایه مستقل تشکیل شده که نقص در هر لایه کل محصول را زمین‌گیر می‌کند.',
    viewLayerLessons: 'مشاهده درس‌های این لایه ←',
    auditBadge: '🛠️ ممیزی زنده و آنلاین',
    auditTitle: 'چک‌لیست و ارزیابی آمادگی سیستم شما در پروداکشن',
    auditDesc: 'آیا کدهای پروژه شما در برابر حملات متداول، سرقت توکن‌ها، بارهای ناگهانی دیتابیس و وب‌هوک‌های تقلبی ایمن است؟ این چک‌لیست برگرفته از حوادث واقعی ۳۲۰ اپیزود مت مورفی است.',
    scoreLabel: 'امتیاز سخت‌سازی سیستم شما:',
    exportReport: 'دریافت گزارش تفصیلی (Markdown)',
    modalProblem: 'طرح مسئله و بردار نفوذ / شکست (Problem & Attack Vector)',
    modalRootCause: 'تحلیل ریشه‌ای و معماری راهکار (Root Cause & Solution)',
    modalActionPlan: 'برنامه عملیاتی و چک‌لیست پیاده‌سازی (Action Checklist)',
    modalCode: 'الگوی کد استاندارد و سخت‌سازی‌شده (Hardened Code)',
    modalTranscript: 'متن اصلی ترنسکریپت انگلیسی (Original Audio Transcript)',
    modalViewReel: 'مشاهده ریلز رسمی در اینستاگرام',
    modalClose: 'بستن پنجره',
    footerAttr: 'کدگذاری‌شده بر مبنای آموزه‌ها و تجربیات <a href="https://www.instagram.com/mattmurphyai" target="_blank" class="text-emerald-400 hover:underline">Matt Murphy</a> توسط تیم DoctorGuidance'
  },
  de: {
    announcement: 'Von "Vibe Coding" zu gehärteter Enterprise-Produktionstechnik | Basierend auf 320+ Matt Murphy Masterclasses',
    auditLink: 'Projekt online prüfen →',
    tabExplorer: '📚 Masterclasses (320)',
    tabLayers: '🏛️ 13 Produktionsschichten',
    tabAudit: '🛡️ Produktions-Audit',
    tabSkill: '🤖 KI-Agenten-Skill',
    heroTag: '🛡️ Systemarchitektur & Resilienz',
    heroTitle: 'Produktions-Wissensdatenbank: <br><span class="bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">320+ Lektionen für Ausfallsicherheit</span>',
    heroDesc: 'KI-generierter Code scheitert unter echtem Traffic und Angriffen. Diese Plattform kodifiziert Matt Murphys Produktionsprinzipien.',
    searchPlaceholder: 'Suche nach Episode (z.B. 043), Titel, Schlagwörtern...',
    allDomains: 'Alle Bereiche (12 Module)',
    allBadge: 'Alle',
    showingStats: 'Zeige <span id="results-count" class="font-bold text-emerald-400">0</span> von 321 Lektionen',
    filterLabel: 'Filter: ',
    loadMore: 'Mehr Lektionen laden...',
    readDetails: 'Ursachenanalyse & Code →',
    layersTitle: 'Die 13 modernen Produktionsschichten',
    layersDesc: 'Full-Stack bedeutet nicht nur Frontend und Backend. Stabilität erfordert 13 voneinander abhängige Ebenen.',
    viewLayerLessons: 'Lektionen ansehen →',
    auditBadge: '🛠️ Interaktives Produktions-Audit',
    auditTitle: 'Ist Ihre Anwendung produktionsbereit?',
    auditDesc: 'Überprüfen Sie Ihr System auf bekannte Sicherheits- und Skalierungsrisiken.',
    scoreLabel: 'Ihr Härtungs-Score:',
    exportReport: 'Audit-Bericht exportieren (Markdown)',
    modalProblem: 'Problemstellung & Angriffsvektor',
    modalRootCause: 'Ursachenanalyse & Architekturlösung',
    modalActionPlan: 'Maßnahmen-Checkliste',
    modalCode: 'Gehärteter Produktionscode',
    modalTranscript: 'Originales Audio-Transkript',
    modalViewReel: 'Reel auf Instagram ansehen',
    modalClose: 'Schließen',
    footerAttr: 'Kodifiziert basierend auf den Masterclasses von Matt Murphy durch das DoctorGuidance Team'
  },
  es: {
    announcement: 'De "Vibe Coding" a ingeniería de producción endurecida | Basado en más de 320 clases magistrales de Matt Murphy',
    auditLink: 'Auditar proyecto en línea →',
    tabExplorer: '📚 Clases (320)',
    tabLayers: '🏛️ 13 Capas de Producción',
    tabAudit: '🛡️ Auditoría',
    tabSkill: '🤖 Habilidad Agente IA',
    heroTag: '🛡️ Arquitectura de Sistemas de Producción',
    heroTitle: 'Base de Conocimiento de Producción: <br><span class="bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">320+ Lecciones Críticas para Resiliencia</span>',
    heroDesc: 'El código generado por IA falla bajo tráfico real y ataques. Esta plataforma codifica los principios de Matt Murphy en soluciones probadas.',
    searchPlaceholder: 'Buscar por episodio (ej. 043), título o palabra clave...',
    allDomains: 'Todos los dominios (12 Módulos)',
    allBadge: 'Todos',
    showingStats: 'Mostrando <span id="results-count" class="font-bold text-emerald-400">0</span> de 321 clases',
    filterLabel: 'Filtro: ',
    loadMore: 'Cargar más lecciones...',
    readDetails: 'Causa raíz y código →',
    layersTitle: 'Las 13 Capas Modernas de Producción',
    layersDesc: 'Full-stack no es solo frontend y backend. La resiliencia requiere 13 capas interdependientes.',
    viewLayerLessons: 'Ver lecciones →',
    auditBadge: '🛠️ Auditor de Producción Interactivo',
    auditTitle: '¿Está su aplicación lista para producción?',
    auditDesc: 'Verifique su aplicación contra los principales fallos de escalabilidad y seguridad.',
    scoreLabel: 'Puntuación de Seguridad:',
    exportReport: 'Exportar Reporte (Markdown)',
    modalProblem: 'Problema y Vector de Ataque',
    modalRootCause: 'Causa Raíz y Solución de Arquitectura',
    modalActionPlan: 'Lista de Acciones',
    modalCode: 'Código Endurecido de Producción',
    modalTranscript: 'Transcripción Original de Audio',
    modalViewReel: 'Ver Reel en Instagram',
    modalClose: 'Cerrar',
    footerAttr: 'Codificado de las clases magistrales de Matt Murphy por el equipo DoctorGuidance'
  },
  zh: {
    announcement: '从轻浮的“氛围编码”走向经过实战淬炼的企业级生产工程 | 基于马特·墨菲（Matt Murphy）320+堂核心课程',
    auditLink: '在线审计您的项目 →',
    tabExplorer: '📚 课程库 (320)',
    tabLayers: '🏛️ 13层生产平台',
    tabAudit: '🛡️ 生产就绪审计',
    tabSkill: '🤖 AI智能体技能',
    heroTag: '🛡️ 生产系统架构与防御',
    heroTitle: '生产工程知识库与防护守则: <br><span class="bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">320+ 软件韧性关键课程</span>',
    heroDesc: 'AI生成的原型在理想演示中运转良好，但在真实流量和多租户数据穿透下极易崩溃。本平台将墨菲法则固化为标准化的故障复盘与防御代码。',
    searchPlaceholder: '按集数（如043）、标题或关键词（JWT, RLS, Stripe）搜索...',
    allDomains: '所有领域 (12个模块)',
    allBadge: '全部',
    showingStats: '显示 321 堂课中的 <span id="results-count" class="font-bold text-emerald-400">0</span> 堂',
    filterLabel: '筛选: ',
    loadMore: '加载更多课程...',
    readDetails: '根本原因与防御代码 →',
    layersTitle: '现代生产工程的13个核心层',
    layersDesc: '全栈绝非只是前端与后端。生产可用性是由13个相互依存的层级组成的坚固防线。',
    viewLayerLessons: '查看本层课程 →',
    auditBadge: '🛠️ 实时在线审计工具',
    auditTitle: '您的项目准备好上线生产了吗？',
    auditDesc: '根据320多场墨菲生产审计中发现的最高危漏洞，检查您的系统架构。',
    scoreLabel: '生产韧性加固得分:',
    exportReport: '导出审计报告 (Markdown)',
    modalProblem: '问题陈述与攻击路径',
    modalRootCause: '根本原因与架构解决方案',
    modalActionPlan: '加固执行清单',
    modalCode: '生产级防御代码 / 配置',
    modalTranscript: '原始音频文字记录',
    modalViewReel: '在 Instagram 上查看原视频',
    modalClose: '关闭',
    footerAttr: '由 DoctorGuidance 团队根据 Matt Murphy 大师课程整理'
  }
};

// Checkpoints
const AUDIT_CHECKPOINTS = [
  {
    id: 'chk_auth_cookie',
    cat: 'Auth',
    title_en: 'Auth tokens stored exclusively in HttpOnly, Secure, SameSite=Lax cookies (Never localStorage)',
    title_fa: 'توکن‌های احراز هویت در کوکی‌های HttpOnly نگهداری می‌شوند (نه در localStorage)',
    desc_en: 'Prevents session hijacking via XSS vulnerabilities and rogue third-party browser scripts.',
    desc_fa: 'جلوگیری از سرقت توکن‌های سشن توسط حملات XSS یا اسکریپت‌های ثالث صفحه.',
    ep: '043',
    weight: 5
  },
  {
    id: 'chk_auth_idor',
    cat: 'Auth',
    title_en: 'All record lookups are strictly scoped to tenant_id and user_id (Anti-IDOR)',
    title_fa: 'تمامی کوئری‌های واکشی رکورد به tenant_id و user_id اسکوپ شده‌اند',
    desc_en: 'Stops unauthorized resource access simply by altering numerical or UUID IDs in the URL.',
    desc_fa: 'جلوگیری از آسیب‌پذیری IDOR از طریق تغییر شناسه در URL.',
    ep: '044',
    weight: 5
  },
  {
    id: 'chk_auth_pkce',
    cat: 'Auth',
    title_en: 'OAuth flows (Google/GitHub) enforce signed state verification and PKCE',
    title_fa: 'جریان ورود با OAuth (گوگل/گیت‌هاب) مجهز به اعتبارسنجی State و PKCE است',
    desc_en: 'Eliminates authorization code interception and login CSRF hijacking.',
    desc_fa: 'جلوگیری از بازنشانی اجباری لاگین و حملات رهگیری کدهای اهراز هویت.',
    ep: '048',
    weight: 4
  },
  {
    id: 'chk_sec_secrets',
    cat: 'Security',
    title_en: 'Zero Service-Role keys, database secrets, or LLM tokens exposed in client bundles',
    title_fa: 'هیچ کلید Service-Role، سکرت دیتابیس یا توکن OpenAI در کدهای کلاینت وجود ندارد',
    desc_en: 'Prevents exposing master administrative privileges via NEXT_PUBLIC_ or VITE_ prefixes.',
    desc_fa: 'ممانعت از انتشار کلیدهای ادمین با متغیرهای عمومی کلاینت و اسکن خودکار کامیت‌ها.',
    ep: '105',
    weight: 5
  },
  {
    id: 'chk_sec_cors',
    cat: 'Security',
    title_en: 'Server CORS policy strictly whitelists trusted domains (No wildcard *)',
    title_fa: 'سیاست CORS روی سرور فقط به دامنه‌های مجاز اجازه دسترسی می‌دهد (نه *)',
    desc_en: 'Prevents arbitrary malicious websites from reading authenticated customer responses.',
    desc_fa: 'جلوگیری از خوانده‌شدن داده‌های خصوصی کاربر توسط سایر وب‌سایت‌ها در مرورگر.',
    ep: '005',
    weight: 4
  },
  {
    id: 'chk_sec_frame',
    cat: 'Security',
    title_en: 'X-Frame-Options or CSP frame-ancestors configured against Clickjacking',
    title_fa: 'هدر X-Frame-Options یا CSP frame-ancestors جهت مقابله با Clickjacking فعال است',
    desc_en: 'Stops attackers from embedding your application inside invisible malicious iframes.',
    desc_fa: 'جلوگیری از آی‌فریم شدن برنامه درون سایت‌های فیشینگ و کلیک‌دزدی.',
    ep: '015',
    weight: 3
  },
  {
    id: 'chk_db_index',
    cat: 'Database',
    title_en: 'Explicit composite B-Tree indexes defined on all WHERE, JOIN, and ORDER BY columns',
    title_fa: 'روی تمام ستون‌های مورد استفاده در WHERE و JOIN ایندکس تعریف شده است',
    desc_en: 'Eliminates catastrophic unindexed Full Table Scans under concurrent traffic spikes.',
    desc_fa: 'ریشه‌کنی اسکن‌های کامل جدول (Full Table Scan) در ترافیک‌های بالا.',
    ep: '287',
    weight: 4
  },
  {
    id: 'chk_db_pool',
    cat: 'Database',
    title_en: 'Serverless functions connect through a Connection Pooler (PgBouncer/Supavisor)',
    title_fa: 'ارتباط سرورلس/API با دیتابیس مجهز به Connection Pooler (مانند PgBouncer) است',
    desc_en: 'Prevents database connection exhaustion when hundreds of lambdas spin up concurrently.',
    desc_fa: 'جلوگیری از قفل‌شدن و مرگ دیتابیس با باز شدن هزاران کانکشن همزمان سرورلس.',
    ep: '211',
    weight: 4
  },
  {
    id: 'chk_db_backup',
    cat: 'Database',
    title_en: 'Automated Point-in-Time Recovery (PITR) enabled with regularly tested restore drills',
    title_fa: 'قابلیت Point-In-Time Recovery (PITR) و بازیابی تست‌شده بک‌آپ فعال است',
    desc_en: 'An untested backup is purely a hypothesis. Validate your recovery runbooks.',
    desc_fa: 'بک‌آپی که تست بازیابی آن انجام نشده، وجود خارجی ندارد.',
    ep: '174',
    weight: 4
  },
  {
    id: 'chk_pay_webhook',
    cat: 'Payments',
    title_en: 'Payment webhooks verify cryptographic signatures against the raw HTTP buffer',
    title_fa: 'امضای وب‌هوک‌های مالی (Stripe Signature) بر روی بافر خام اعتبارسنجی می‌شود',
    desc_en: 'Stops attackers from injecting counterfeit payment notifications with manual HTTP POSTs.',
    desc_fa: 'جلوگیری از تزریق تأییدیه‌های پرداخت جعلی با پی‌لودهای دستی HTTP.',
    ep: '006',
    weight: 5
  },
  {
    id: 'chk_pay_idemp',
    cat: 'Payments',
    title_en: 'All payment and state-mutating webhooks implement unique idempotency keys',
    title_fa: 'اکشن‌های حساس و پردازش پرداخت مجهز به کلید Idempotency هستند',
    desc_en: 'Prevents double billing or duplicate resource allocation when payment gateways retry.',
    desc_fa: 'جلوگیری از کسر شارژ مجدد در صورت ارسال چندباره درخواست یا ریتری وب‌هوک.',
    ep: '006',
    weight: 4
  },
  {
    id: 'chk_rate_limit',
    cat: 'Rate Limiting',
    title_en: 'Authentication, search, and LLM endpoints protected by Redis Token Bucket rate limiting',
    title_fa: 'اندپوینت‌های احراز هویت، جستجو و AI مجهز به محدودساز نرخ (Rate Limiter) هستند',
    desc_en: 'Prevents denial-of-service crashes from scripts triggering hundreds of concurrent requests.',
    desc_fa: 'جلوگیری از DoS و فلج شدن سرور توسط یک اسکریپت ساده با ۵۰۰ درخواست در ثانیه.',
    ep: '103',
    weight: 4
  },
  {
    id: 'chk_obs_unhandled',
    cat: 'Observability',
    title_en: 'Global uncaughtException and unhandledRejection process handlers active',
    title_fa: 'هندلرهای سراسری unhandledRejection و uncaughtException فعال هستند',
    desc_en: 'Eliminates silent 2 AM server crashes with structured Sentry reporting and auto-restarts.',
    desc_fa: 'جلوگیری از کرش خاموش سرور در نیمه‌شب و ثبت لاگ خطا در Sentry.',
    ep: '205',
    weight: 4
  },
  {
    id: 'chk_ui_states',
    cat: 'Frontend',
    title_en: 'Every async component explicitly implements 4 UI states: Loading, Error, Empty, Success',
    title_fa: 'تمامی کامپوننت‌های داده‌محور دارای ۴ وضعیت Loading، Error، Empty و Success هستند',
    desc_en: 'Ensures users never see blank white screens or frozen interfaces during edge failures.',
    desc_fa: 'عدم نمایش صفحه سفید (Blank Screen) در زمان قطعی اینترنت یا خطای سرور.',
    ep: '289',
    weight: 4
  },
  {
    id: 'chk_ai_sgi',
    cat: 'AI & Legal',
    title_en: 'AI-generated content is clearly watermarked and logged per EU AI Act requirements',
    title_fa: 'محتوای تولیدشده توسط AI طبق الزامات EU AI Act دارای برچسب و لاگ ثبت است',
    desc_en: 'Complies with mandatory synthetic information (SGI) disclosure rules to avoid fines.',
    desc_fa: 'افشای صریح اطلاعات سنتتیک (SGI) و مهار جریمه‌های حقوقی نقض حریم خصوصی.',
    ep: '001',
    weight: 4
  }
];

let checkedAuditItems = new Set();

// Master Skill Markdown
const MASTER_SKILL_MD = `---
name: matt-murphy-production-engineer
description: Production-grade architectural hardening and security guardrails based on 320+ Matt Murphy production engineering masterclasses. Enforces resilient authentication, database connection pooling, zero-leak multi-tenancy, raw-buffer webhook validation, rate limiting, and 4-state UI hygiene. Prevents naive "vibe coding" anti-patterns.
---

# Matt Murphy Production Engineering Guardrails

## Core Persona & Directive:
You are an uncompromising Principal Systems Architect and Production Reliability Engineer. 
When generating, refactoring, or reviewing code, you must never settle for superficial "happy-path" demos or fragile prototypes ("vibe coding"). 

You enforce the following 13 non-negotiable production invariants:

### 1. Authentication & Session Hygiene (Episodes 043, 044, 048, 118, 124, 206):
- NEVER store auth tokens, JWTs, or session identifiers in \`localStorage\` or \`sessionStorage\`. Always issue \`HttpOnly\`, \`Secure\`, \`SameSite=Lax\` cookies.
- Direct-object lookups MUST be scoped to the authenticated tenant/user (\`WHERE id = :id AND tenant_id = :tenantId\`). Never trust an ID from the URL alone (Anti-IDOR).
- Always use PKCE and state verification for third-party OAuth flows.

### 2. Multi-Tenancy & Data Isolation (Episodes 005, 104, 211):
- Enforce database-level Row Level Security (RLS) or mandatory repository-level tenant scoping.
- Never rely on the frontend to filter or hide private customer records.

### 3. Financial Webhooks & Idempotency (Episode 006):
- Payment webhooks (Stripe, etc.) MUST verify digital signatures against the raw request buffer (\`stripe.webhooks.constructEvent\`).
- All state-mutating webhooks and billing endpoints MUST implement idempotency keys via Redis or DB unique constraints to prevent duplicate charges on network retries.

### 4. Rate Limiting & Denial of Service Defense (Episode 103):
- Every public endpoint (auth, search, LLM generation) must have rate limiting (Token Bucket via Redis) with tiered thresholds: IP-based, User-based, and API-key-based.
- Return explicit \`429 Too Many Requests\` with \`Retry-After\` headers.

### 5. Resilient Error Handling & The 4 UI States (Episodes 205, 289, 291):
- In backend runtimes, always register global \`uncaughtException\` and \`unhandledRejection\` handlers to prevent silent server deaths.
- In frontend UI, every data-driven component MUST explicitly implement: Loading State, Error State (with retry action), Empty State, and Success State.

### 6. Secrets & Client Bundle Hygiene (Episodes 105, 295):
- Never commit or expose service role keys, master DB credentials, or LLM API keys in client-side code bundles.
- Ensure production console F12 is clean of stack traces and sensitive payload dumps.
`;

// Initialize Application
document.addEventListener('DOMContentLoaded', async () => {
  // Check stored language
  const savedLang = localStorage.getItem('mm_lang') || 'en';
  currentLang = savedLang;
  const select = document.getElementById('lang-select');
  if (select) select.value = currentLang;

  setupKeyboardShortcuts();
  await loadData();
  applyLanguage(currentLang);
  renderCategorySelect();
  renderCategoryChips();
  renderLayersGrid();
  renderAuditChecklist();
  renderSkillSource();
  applyFilters();
});

// Change Language
function changeLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('mm_lang', lang);
  applyLanguage(lang);
  renderCategorySelect();
  renderCategoryChips();
  renderLayersGrid();
  renderAuditChecklist();
  applyFilters();
}

function applyLanguage(lang) {
  const dict = I18N[lang] || I18N.en;
  const isRtl = lang === 'fa';

  document.documentElement.lang = lang;
  document.documentElement.dir = isRtl ? 'rtl' : 'ltr';

  // Update UI Elements
  setElText('txt-announcement', dict.announcement);
  setElText('txt-announcement-link', dict.auditLink);
  setElText('tab-btn-explorer', dict.tabExplorer);
  setElText('tab-btn-layers', dict.tabLayers);
  setElText('tab-btn-audit', dict.tabAudit);
  setElText('tab-btn-skill', dict.tabSkill);
  setElText('txt-hero-tag', dict.heroTag);
  setElHtml('txt-hero-title', dict.heroTitle);
  setElHtml('txt-hero-desc', dict.heroDesc);
  
  const searchInput = document.getElementById('search-input');
  if (searchInput) searchInput.placeholder = dict.searchPlaceholder;

  setElText('txt-load-more', dict.loadMore);
  setElText('txt-layers-title', dict.layersTitle);
  setElText('txt-layers-desc', dict.layersDesc);
  setElText('txt-audit-badge', dict.auditBadge);
  setElText('txt-audit-title', dict.auditTitle);
  setElText('txt-audit-desc', dict.auditDesc);
  setElText('txt-score-label', dict.scoreLabel);
  setElText('txt-btn-export', dict.exportReport);
  setElHtml('txt-footer-attr', dict.footerAttr);

  // Modal Labels
  setElText('modal-lbl-problem', dict.modalProblem);
  setElText('modal-lbl-root-cause', dict.modalRootCause);
  setElText('modal-lbl-action-plan', dict.modalActionPlan);
  setElText('modal-lbl-code', dict.modalCode);
  setElText('modal-lbl-transcript', dict.modalTranscript);
  setElText('modal-lbl-view-reel', dict.modalViewReel);
  setElText('modal-lbl-close', dict.modalClose);
}

function setElText(id, txt) {
  const el = document.getElementById(id);
  if (el) el.textContent = txt;
}
function setElHtml(id, html) {
  const el = document.getElementById(id);
  if (el) el.innerHTML = html;
}

// Keyboard shortcut (Cmd+K / Ctrl+K)
function setupKeyboardShortcuts() {
  window.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      switchTab('explorer');
      const input = document.getElementById('search-input');
      if (input) {
        input.focus();
        input.select();
      }
    }
    if (e.key === 'Escape') {
      closeModal();
    }
  });
}

// Tab Switching
function switchTab(tabId) {
  const tabs = ['explorer', 'layers', 'audit', 'skill'];
  tabs.forEach(t => {
    const view = document.getElementById(`view-${t}`);
    const btn = document.getElementById(`tab-btn-${t}`);
    if (t === tabId) {
      view.classList.remove('hidden');
      if (btn) {
        btn.classList.add('bg-emerald-600', 'text-white', 'shadow');
        btn.classList.remove('text-gray-400');
      }
    } else {
      view.classList.add('hidden');
      if (btn) {
        btn.classList.remove('bg-emerald-600', 'text-white', 'shadow');
        btn.classList.add('text-gray-400');
      }
    }
  });
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Load data.json
async function loadData() {
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 10000);
    const res = await fetch('data.json', { signal: controller.signal });
    clearTimeout(timeoutId);
    if (!res.ok) throw new Error('Failed to load data.json');
    rawData = await res.json();
    allEpisodes = rawData.episodes || [];
    filteredEpisodes = [...allEpisodes];
  } catch (err) {
    console.error('Error loading data:', err);
  }
}

// Render Category Dropdown
function renderCategorySelect() {
  if (!rawData || !rawData.modules) return;
  const select = document.getElementById('category-select');
  const dict = I18N[currentLang] || I18N.en;
  select.innerHTML = `<option value="all">${dict.allDomains}</option>`;
  
  for (const [key, mod] of Object.entries(rawData.modules)) {
    const count = allEpisodes.filter(e => e.category === key).length;
    const opt = document.createElement('option');
    opt.value = key;
    const name = currentLang === 'fa' ? mod.name_fa : mod.name_en;
    opt.textContent = `${name} (${count})`;
    select.appendChild(opt);
  }
}

// Render Category Filter Chips
function renderCategoryChips() {
  if (!rawData || !rawData.modules) return;
  const container = document.getElementById('category-chips');
  const dict = I18N[currentLang] || I18N.en;
  container.innerHTML = '';

  const allChip = document.createElement('button');
  allChip.className = 'chip-btn px-3 py-1.5 rounded-lg border border-emerald-500 bg-emerald-500/20 text-emerald-400 font-bold transition';
  allChip.textContent = `${dict.allBadge} (${allEpisodes.length})`;
  allChip.onclick = () => selectCategory('all');
  container.appendChild(allChip);

  for (const [key, mod] of Object.entries(rawData.modules)) {
    const count = allEpisodes.filter(e => e.category === key).length;
    const chip = document.createElement('button');
    chip.id = `chip-${key}`;
    chip.className = 'chip-btn px-3 py-1.5 rounded-lg border border-darkBorder bg-gray-900/80 text-gray-400 hover:text-white hover:border-gray-600 transition';
    const name = currentLang === 'fa' ? mod.name_fa : mod.name_en;
    chip.textContent = `${name} (${count})`;
    chip.onclick = () => selectCategory(key);
    container.appendChild(chip);
  }
}

function selectCategory(catId) {
  currentCategory = catId;
  const select = document.getElementById('category-select');
  if (select) select.value = catId;

  document.querySelectorAll('.chip-btn').forEach(btn => {
    btn.classList.remove('border-emerald-500', 'bg-emerald-500/20', 'text-emerald-400', 'font-bold');
    btn.classList.add('border-darkBorder', 'bg-gray-900/80', 'text-gray-400');
  });

  const activeChip = catId === 'all' 
    ? document.querySelector('#category-chips button:first-child')
    : document.getElementById(`chip-${catId}`);
  if (activeChip) {
    activeChip.classList.add('border-emerald-500', 'bg-emerald-500/20', 'text-emerald-400', 'font-bold');
    activeChip.classList.remove('border-darkBorder', 'bg-gray-900/80', 'text-gray-400');
  }

  applyFilters();
}

function handleFilterChange() {
  const select = document.getElementById('category-select');
  selectCategory(select.value);
}

function handleSearch() {
  currentSearch = document.getElementById('search-input').value.trim().toLowerCase();
  applyFilters();
}

function applyFilters() {
  filteredEpisodes = allEpisodes.filter(ep => {
    if (currentCategory !== 'all' && ep.category !== currentCategory) {
      return false;
    }
    if (currentSearch) {
      const matchNum = ep.number.includes(currentSearch);
      const matchTitleEn = ep.title.toLowerCase().includes(currentSearch);
      const matchTitleFa = (ep.title_fa || '').toLowerCase().includes(currentSearch);
      const matchProb = (ep.problem_fa || '').toLowerCase().includes(currentSearch);
      const matchTranscript = (ep.transcript || '').toLowerCase().includes(currentSearch);
      return matchNum || matchTitleEn || matchTitleFa || matchProb || matchTranscript;
    }
    return true;
  });

  displayLimit = 30;
  renderEpisodesGrid();
}

function renderEpisodesGrid() {
  const grid = document.getElementById('episodes-grid');
  const countEl = document.getElementById('results-count');
  const filterLabel = document.getElementById('active-filter-label');
  const loadMore = document.getElementById('load-more-container');
  const dict = I18N[currentLang] || I18N.en;

  if (countEl) countEl.textContent = filteredEpisodes.length;
  
  const activeCategoryName = currentCategory === 'all' 
    ? dict.allBadge 
    : (currentLang === 'fa' ? rawData.modules[currentCategory]?.name_fa : rawData.modules[currentCategory]?.name_en);
  
  if (filterLabel) {
    filterLabel.innerHTML = `${dict.filterLabel}<span class="text-emerald-400 font-bold">${activeCategoryName}</span>`;
  }

  if (filteredEpisodes.length === 0) {
    grid.innerHTML = `
      <div class="col-span-full py-16 text-center space-y-3 bg-gray-900/50 rounded-2xl border border-darkBorder">
        <div class="text-4xl">🔍</div>
        <div class="text-base font-bold text-white">No results found</div>
        <p class="text-xs text-gray-400">Try modifying your search or clearing category filters.</p>
      </div>
    `;
    loadMore.classList.add('hidden');
    return;
  }

  const toShow = filteredEpisodes.slice(0, displayLimit);
  grid.innerHTML = toShow.map(ep => {
    const title = currentLang === 'fa' ? ep.title_fa : ep.title;
    const catName = currentLang === 'fa' ? ep.category_name_fa : ep.category_name_en;
    const desc = currentLang === 'fa' ? ep.problem_fa : (ep.caption || ep.problem_fa);

    return `
      <div class="group bg-gray-900/70 hover:bg-gray-900 border border-darkBorder hover:border-emerald-500/50 rounded-2xl p-5 flex flex-col justify-between transition-all duration-200 hover:shadow-xl hover:shadow-emerald-950/20">
        <div class="space-y-3">
          <div class="flex items-center justify-between gap-2">
            <span class="font-mono text-xs font-bold px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
              #${ep.number}
            </span>
            <span class="text-[11px] px-2 py-0.5 rounded-full bg-gray-800 text-gray-300 border border-darkBorder">
              ${catName}
            </span>
          </div>

          <h3 class="text-sm font-bold text-white group-hover:text-emerald-300 transition line-clamp-2 leading-snug">
            ${title}
          </h3>

          <p class="text-xs text-gray-400 line-clamp-3 leading-relaxed">
            ${desc}
          </p>
        </div>

        <div class="mt-4 pt-4 border-t border-darkBorder/60 flex items-center justify-between">
          <button onclick="openModal('${ep.number}')" class="text-xs font-bold text-emerald-400 hover:text-emerald-300 transition flex items-center gap-1">
            <span>${dict.readDetails}</span>
          </button>
          ${ep.url ? `
            <a href="${ep.url}" target="_blank" rel="noopener noreferrer" class="text-gray-500 hover:text-pink-400 transition" title="Instagram Reel">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
            </a>
          ` : ''}
        </div>
      </div>
    `;
  }).join('');

  if (filteredEpisodes.length > displayLimit) {
    loadMore.classList.remove('hidden');
  } else {
    loadMore.classList.add('hidden');
  }
}

function loadMoreEpisodes() {
  displayLimit += 30;
  renderEpisodesGrid();
}

// Modal View
let currentModalCode = '';

function openModal(epNum) {
  const ep = allEpisodes.find(e => e.number === epNum);
  if (!ep) return;

  const isFa = currentLang === 'fa';
  const primaryTitle = isFa ? ep.title_fa : ep.title;
  const secondaryTitle = isFa ? ep.title : ep.title_fa;
  const catName = isFa ? ep.category_name_fa : ep.category_name_en;

  const sev = ep.severity || 'MEDIUM';
  const epBadge = document.getElementById('modal-ep-badge');
  epBadge.textContent = `#${ep.number} • ${sev}`;
  if (sev === 'CRITICAL') {
    epBadge.className = 'px-2.5 py-0.5 rounded-full font-mono font-bold bg-red-500/20 text-red-400 border border-red-500/40';
  } else if (sev === 'HIGH') {
    epBadge.className = 'px-2.5 py-0.5 rounded-full font-mono font-bold bg-amber-500/20 text-amber-400 border border-amber-500/40';
  } else {
    epBadge.className = 'px-2.5 py-0.5 rounded-full font-mono font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30';
  }

  document.getElementById('modal-cat-badge').textContent = catName;
  document.getElementById('modal-layer-badge').textContent = `Layer ${ep.layer}`;
  document.getElementById('modal-title-primary').textContent = primaryTitle;
  document.getElementById('modal-title-secondary').textContent = secondaryTitle;
  
  document.getElementById('modal-problem').textContent = isFa ? (ep.problem_fa || ep.problem_en) : (ep.problem_en || ep.problem_fa);
  
  // Comparison Table
  const mistake = isFa ? (ep.table_mistake_fa || ep.table_mistake_en || 'اشتباهات رایج وایب‌کدینگ') : (ep.table_mistake_en || 'Common vibe-coding pitfall');
  const prodStd = isFa ? (ep.table_production_fa || ep.table_production_en || 'استاندارد سخت‌سازی پروداکشن') : (ep.table_production_en || 'Hardened production standard');
  document.getElementById('modal-mistake').textContent = mistake;
  document.getElementById('modal-prod-std').textContent = prodStd;

  document.getElementById('modal-root-cause').textContent = isFa ? (ep.root_cause_fa || ep.root_cause_en) : (ep.root_cause_en || ep.root_cause_fa);

  // Golden Takeaway
  const golden = isFa ? (ep.golden_takeaway_fa || ep.golden_takeaway_en || 'اصل طلایی مت مورفی') : (ep.golden_takeaway_en || 'Key production heuristic');
  document.getElementById('modal-golden').textContent = golden;

  const actionList = document.getElementById('modal-action-plan');
  const actions = isFa ? (ep.action_plan || ep.action_plan_en || []) : (ep.action_plan_en || ep.action_plan || []);
  actionList.innerHTML = actions.map(item => `<li>${item}</li>`).join('');

  currentModalCode = ep.code_snippet || '// Production snippet';
  document.getElementById('modal-code').textContent = currentModalCode;

  document.getElementById('modal-transcript').textContent = ep.transcript || ep.caption || 'Transcript unavailable.';

  const igLink = document.getElementById('modal-instagram-link');
  if (ep.url) {
    igLink.href = ep.url;
    igLink.classList.remove('hidden');
  } else {
    igLink.classList.add('hidden');
  }

  document.getElementById('episode-modal').classList.remove('hidden');
  document.body.classList.add('overflow-hidden');
}

function closeModal() {
  document.getElementById('episode-modal').classList.add('hidden');
  document.body.classList.remove('overflow-hidden');
}

function copyModalCode() {
  navigator.clipboard.writeText(currentModalCode);
  const btn = document.getElementById('modal-copy-code-btn');
  const prev = btn.innerHTML;
  btn.innerHTML = 'Copied! ✓';
  setTimeout(() => { btn.innerHTML = prev; }, 2000);
}

// Render Layers Grid
function renderLayersGrid() {
  if (!rawData || !rawData.layers) return;
  const container = document.getElementById('layers-grid');
  const dict = I18N[currentLang] || I18N.en;
  container.innerHTML = '';

  for (const [layerNum, info] of Object.entries(rawData.layers)) {
    const matchingCount = allEpisodes.filter(e => e.layer === parseInt(layerNum)).length;
    const card = document.createElement('div');
    card.className = 'p-6 rounded-2xl bg-gray-900/80 border border-darkBorder hover:border-emerald-500/50 transition cursor-pointer space-y-3';
    card.onclick = () => {
      switchTab('explorer');
      currentSearch = '';
      document.getElementById('search-input').value = '';
      filteredEpisodes = allEpisodes.filter(e => e.layer === parseInt(layerNum));
      displayLimit = 30;
      renderEpisodesGrid();
      document.getElementById('active-filter-label').innerHTML = `${dict.filterLabel}<span class="text-emerald-400 font-bold">Layer ${layerNum} (${info.name})</span>`;
    };

    card.innerHTML = `
      <div class="flex items-center justify-between">
        <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-gray-800 text-emerald-400 border border-darkBorder">Layer ${layerNum}</span>
        <span class="text-xs text-gray-500">${matchingCount} lessons</span>
      </div>
      <h3 class="text-base font-bold text-white">${info.name}</h3>
      <p class="text-xs text-gray-400 leading-relaxed">${info.desc}</p>
      <div class="text-[11px] font-bold text-emerald-400 flex items-center gap-1 pt-2">
        <span>${dict.viewLayerLessons}</span>
      </div>
    `;
    container.appendChild(card);
  }
}

// Render Audit Checklist
function renderAuditChecklist() {
  const container = document.getElementById('audit-checklist-container');
  container.innerHTML = '';

  AUDIT_CHECKPOINTS.forEach((chk) => {
    const item = document.createElement('div');
    item.className = 'p-5 rounded-2xl bg-gray-900/80 border border-darkBorder flex items-start gap-4 transition hover:border-gray-700';
    
    const title = currentLang === 'fa' ? chk.title_fa : chk.title_en;
    const desc = currentLang === 'fa' ? chk.desc_fa : chk.desc_en;

    item.innerHTML = `
      <div class="pt-1">
        <input 
          type="checkbox" 
          id="${chk.id}" 
          onchange="toggleAuditCheckpoint('${chk.id}')"
          class="w-5 h-5 rounded bg-gray-800 border-darkBorder text-emerald-500 focus:ring-emerald-500 focus:ring-offset-0 cursor-pointer"
        >
      </div>
      <div class="flex-1 space-y-1">
        <div class="flex items-center justify-between gap-2">
          <label for="${chk.id}" class="text-sm font-bold text-white cursor-pointer hover:text-emerald-300 transition">
            ${title}
          </label>
          <span class="text-[10px] px-2 py-0.5 rounded bg-gray-800 text-gray-400 border border-darkBorder">${chk.cat}</span>
        </div>
        <p class="text-xs text-gray-400 leading-relaxed">${desc}</p>
        <div class="pt-1">
          <button onclick="openModal('${chk.ep}')" class="text-[11px] font-semibold text-emerald-400 hover:underline flex items-center gap-1">
            <span>Reference Masterclass #${chk.ep}</span>
            <span>↗</span>
          </button>
        </div>
      </div>
    `;
    container.appendChild(item);
  });

  updateAuditScore();
}

function toggleAuditCheckpoint(chkId) {
  if (checkedAuditItems.has(chkId)) {
    checkedAuditItems.delete(chkId);
  } else {
    checkedAuditItems.add(chkId);
  }
  updateAuditScore();
}

function updateAuditScore() {
  const total = AUDIT_CHECKPOINTS.length;
  const checked = checkedAuditItems.size;
  const pct = Math.round((checked / total) * 100);

  const scoreEl = document.getElementById('audit-score-display');
  const statusEl = document.getElementById('audit-score-status');

  if (scoreEl) scoreEl.textContent = `${pct}%`;

  if (statusEl) {
    if (pct === 100) {
      statusEl.textContent = '🌟 100% Production Hardened & Enterprise Ready!';
      statusEl.className = 'text-xs font-bold text-emerald-400';
    } else if (pct >= 70) {
      statusEl.textContent = '⚡ Solid Architecture - Minor hardening remaining';
      statusEl.className = 'text-xs font-bold text-yellow-400';
    } else if (pct >= 40) {
      statusEl.textContent = '⚠️ Fragile System - High vulnerability risk';
      statusEl.className = 'text-xs font-bold text-orange-400';
    } else {
      statusEl.textContent = '🚨 Vibe Coding State - Critical failure risk in production';
      statusEl.className = 'text-xs font-bold text-red-400';
    }
  }
}

function exportAuditReport() {
  const checkedCount = checkedAuditItems.size;
  const total = AUDIT_CHECKPOINTS.length;
  const pct = Math.round((checkedCount / total) * 100);

  let md = `# Production Reliability & Security Audit Report\n`;
  md += `> **Audit Date:** ${new Date().toISOString().split('T')[0]} | **Score:** ${pct}%\n\n`;
  md += `## Verified Checkpoints:\n\n`;

  AUDIT_CHECKPOINTS.forEach(chk => {
    const isPassed = checkedAuditItems.has(chk.id);
    const title = currentLang === 'fa' ? chk.title_fa : chk.title_en;
    md += `- [${isPassed ? 'x' : ' '}] **${title}** (Matt Murphy Lesson: #${chk.ep})\n`;
    if (!isPassed) {
      md += `  - ⚠️ *Remediation Required:* High risk vector. Consult masterclass #${chk.ep}.\n`;
    }
  });

  const blob = new Blob([md], { type: 'text/markdown;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `production-audit-report-${Date.now()}.md`;
  a.click();
  URL.revokeObjectURL(url);
}

// Master Skill
function renderSkillSource() {
  const box = document.getElementById('skill-source-box');
  if (box) {
    box.textContent = MASTER_SKILL_MD;
  }
}

function copySkillSource() {
  navigator.clipboard.writeText(MASTER_SKILL_MD);
  const btn = document.getElementById('copy-skill-btn');
  const prev = btn.innerHTML;
  btn.innerHTML = 'Copied! ✓';
  setTimeout(() => { btn.innerHTML = prev; }, 2000);
}
