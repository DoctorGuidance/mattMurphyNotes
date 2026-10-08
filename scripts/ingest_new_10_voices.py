"""
Ingest newly extracted 10 masterclasses (Episodes 323 to 332) from NotebookLM,
save exact transcripts to D:\download\mattmurphy_voices,
enrich data.json and site/data.json with bespoke architectural schemas,
generate single-lesson markdown documentation in docs/,
and prepare the system for full enterprise skill compilation.
"""

import os
import json
import re

VOICES_DIR = r"D:\download\mattmurphy_voices"
DATA_PATH = "data.json"
SITE_DATA_PATH = "site/data.json"
DOCS_DIR = "docs"

NEW_MASTERCLASSES = [
    {
        "number": "323",
        "title": "Direct the Machine: Clarity is the New Programming Language",
        "title_fa": "هدایت ماشین: وضوح ذهنی زبان برنامه‌نویسی جدید است",
        "url": "https://www.instagram.com/reel/323/",
        "category": "09-ai-guardrails",
        "category_name_en": "AI Guardrails, LLM Security & Compliance",
        "category_name_fa": "مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی",
        "category_color": "#8b5cf6",
        "layer": 2,
        "severity": "CRITICAL",
        "transcript": (
            "The youngest self-made billionaire in AI history just named the one skill that matters the most. "
            "It's not Python. It's not machine learning. It is the ability to direct AI exactly what to build. "
            "Alexander Wang started scale AI at 19 years old. Built the data infrastructure that half of the industry is running on. "
            "Became the youngest self-made billionaire on the planet. He now runs AI at Meta. So when he names a skill, people listen. "
            "These are exact words. If you're 13 years old today, spend all of your time vibe coding. Not Python, not computer sciences, "
            "100% vibe coding by telling AI what to build in plain English. AI now writes about one in three lines of code at Microsoft and Google. "
            "Wang said, that 3 to 5 years it will write 100%. The new programming language it's not Python it's clarity. "
            "The people who can say exactly what they want will build the next decade of systems. That's the entire channel right here. "
            "That is every fix that I've ever posted. That is the 13 layer program. That is the faction community that you're in. "
            "The skill underneath all of it is the same one Wayne just put on stage. Direct the machine, tell it what to build, "
            "tell it what to fix, know enough about the system to know whether it did it right or not. So, everyone on Earth is learning AI tools. "
            "Almost nobody is learning the skill of what's underneath them. The real advantage is not which model you use, "
            "it's how clearly you think and how precisely you instruct the AI. So, the people who learn this now have a 6 months window "
            "in front of everyone else. It's not going to stay open though. Every shift in technology works the exact same way. "
            "The people who move in early win. And this is not news to anyone in this community, but now the youngest billionaire in AI is saying it to everyone, too."
        ),
        "problem_en": "Developers waste effort memorizing ephemeral syntax while lacking the precision, clarity, and system verification skills required to instruct autonomous AI agents without introducing fatal architectural regressions.",
        "problem_fa": "توسعه‌دهندگان وقت خود را صرف حفظ کردن دستورات و سینتکس زودگذر می‌کنند در حالی که وضوح ذهنی و توانایی اعتبارسنجی سیستم را برای هدایت دقیق مدل‌های هوش مصنوعی ندارند.",
        "root_cause_en": "Treating AI assistance as passive auto-complete rather than maintaining strict architectural control, failing to formulate explicit multi-layer specifications, and lacking domain depth to verify code correctness.",
        "root_cause_fa": "نگاه منفعلانه به ابزارهای هوش مصنوعی به عنوان ابزار تکمیل کد و عدم تعیین نیازمندی‌های صریح معماری و ضعف در بازرسی کیفی خروجی‌ها.",
        "action_plan_en": [
            "Decompose systems into precise, unambiguous architectural contracts and formal interfaces before prompting AI.",
            "Enforce rigorous verification gates: test suites, static analysis, and runtime telemetry for every AI-generated artifact.",
            "Master cross-layer systems fundamentals to evaluate generated code beyond immediate happy-path execution."
        ],
        "action_plan": [
            "شکستن سیستم به قراردادهای دقیق معماری و رابط‌های صریح پیش از صدور دستور به هوش مصنوعی.",
            "اجرای دروازه‌های اعتبارسنجی سخت‌گیرانه شامل تست، تحلیل ایستا و لاگ‌های زمان اجرا برای کدهای تولیدی هوش مصنوعی.",
            "تسلط عمیق بر مبانی لایه‌های زیرساختی برای تشخیص باگ‌های پنهان فراتر از مسیر خوش‌بینانه."
        ],
        "golden_takeaway_en": "The new programming language is clarity: the ultimate edge is not the model you use, but how clearly you think, how precisely you instruct the machine, and whether you possess the depth to verify it.",
        "golden_takeaway_fa": "زبان برنامه‌نویسی جدید «وضوح اندیشه» است؛ برتری مطلق نه در انتخاب مدل، بلکه در دقت دستوردهی، مدل‌سازی معماری و توانایی راستی‌آزمایی خروجی‌هاست.",
        "table_mistake_en": "Passive vibe coding: accepting unverified AI code blindly and letting the agent dictate system design.",
        "table_mistake_fa": "وایب‌کدینگ منفعلانه: پذیرش کورکورانه کدهای هوش مصنوعی بدون بازرسی و واگذاری طراحی سیستم به مدل.",
        "table_production_en": "Directive specification: formulating exact multi-layer invariants and inspecting every generated boundary with automated gates.",
        "table_production_fa": "هدایت سیستماتیک و مهندسی: فرمول‌بندی ناورداهای چندلایه‌ای و بازرسی تک‌تک مرزهای تولید شده با دروازه‌های خودکار.",
        "code_snippet": (
            "// PRODUCTION STANDARD: Directive Agent Specification Contract\n"
            "interface SystemDirectiveContract {\n"
            "  domainInvariants: string[];\n"
            "  inputValidationSchema: ZodSchema;\n"
            "  deterministicErrorHandling: boolean;\n"
            "  verificationGate: () => Promise<VerificationReport>;\n"
            "}\n\n"
            "export async function executeAgentWorkflow(spec: SystemDirectiveContract) {\n"
            "  // Fail closed if domain invariants or verification checks fail\n"
            "  const report = await spec.verificationGate();\n"
            "  if (!report.passed) throw new ArchitecturalInvariantViolation(report.failures);\n"
            "  return report.artifact;\n"
            "}"
        )
    },
    {
        "number": "324",
        "title": "The 3-Week Production Failure: Consultant Vetting & Track Record Gate",
        "title_fa": "شکست سه‌هفته‌ای در پروداکشن: ممیزی مشاوران و اعتبارسنجی کارنامه عملیاتی",
        "url": "https://www.instagram.com/reel/324/",
        "category": "10-cicd-deployments",
        "category_name_en": "Testing, Staging & CI/CD",
        "category_name_fa": "تست، محیط‌های کاری، CI/CD و خط لوله استقرار",
        "category_color": "#10b981",
        "layer": 7,
        "severity": "CRITICAL",
        "transcript": (
            "So, I took a call this morning to fix an AI deployment that failed three weeks after its launch. "
            "It's the third call like this in two weeks that I've received. And every single one of them hired somebody who had apparently never deployed AI into production. "
            "The pattern, it's always the same. Someone with a LinkedIn headline and a slide deck sold the client an AI strategy that their AI wrote. "
            "They ran a few workshops, built a prototype in the sandbox, showed a demo that looked impressive on a screen share. "
            "Then they deployed it and within three weeks the system is always down. The data pipeline is completely broken and the client is calling me to fix it now. "
            "And I've seen this pattern before. Not in AI though. In social media. In 2010, every business and brand needed a social media strategy, right? "
            "Well, nobody even knew what that meant. So, a wave of consultants appeared overnight. Many of them fresh out of school, no real world experience, "
            "but they had followers and they had frameworks and they had confidence and they knew how to use the social media tools. "
            "Is any of this sounding familiar yet? What they did not have was a track record of results and the businesses that hired them spent the next two years "
            "recovering from strategies that were never strategies. The same wave is happening right now in AI. The titles have changed. The dynamics they did not. "
            "Someone who has never shipped or supported a production system is selling production strategy right now. Someone who has never managed a data pipeline "
            "is advising on data architecture right now. And someone who has never handled a compliance audit is promising HIPPA readiness. "
            "Consultant vetting is more important now than it's ever been. A social media post that can be deleted, but a bad AI deployment can destroy your entire business. "
            "The cleanup work is always more expensive than the build, folks. And the client always asks the same question. How do I make sure this does not happen again? "
            "Well, I'm going to be answering those questions throughout the week. Let's rock."
        ),
        "problem_en": "Companies hire superficial AI consultants who present slick slide decks and sandbox demos, resulting in total system outages and broken data pipelines within weeks of production launch.",
        "problem_fa": "سازمان‌ها فریب ارائه‌ها و دموهای پر زرق و برق در محیط‌های آزمایشی را می‌خورند و کار را به افرادی می‌سپارند که هرگز سیستمی را در محیط واقعی لانچ و نگهداری نکرده‌اند؛ نتیجه آن قطعی کامل سرویس پس از ۳ هفته است.",
        "root_cause_en": "Confusing sandbox prototypes with hardened production engineering, lacking criteria for operational resilience, and failing to audit real-world production track records.",
        "root_cause_fa": "اشتباه گرفتن نمونه اولیه سندباکس با مهندسی پروداکشن، نادیده گرفتن تاب‌آوری خطوط داده و عدم ممیزی پیشینه عملیاتی استقرارها.",
        "action_plan_en": [
            "Audit verified production case studies with measurable SLA history and incident response track records before hiring.",
            "Require proof-of-concept validation under real traffic loads, simulated network partitions, and strict edge-case stress tests.",
            "Establish contractual acceptance gates tied to post-launch MTTR, data pipeline integrity, and zero-downtime cutover."
        ],
        "action_plan": [
            "ممیزی دقیق سوابق مستند پروداکشن و کارنامه مدیریت حوادث و SLA مشاوران پیش از بستن قرارداد.",
            "الزام اثبات کارکرد نمونه اولیه زیر بار ترافیک واقعی، شبیه‌سازی قطعی شبکه و آزمون‌های فشار لبه.",
            "تعریف گیت‌های تحویل مبتنی بر شاخص‌های پایداری، تمامیت پایپ‌لاین‌های داده و استقرار بدون قطعی."
        ],
        "golden_takeaway_en": "A bad social media post can be deleted, but a botched AI deployment destroys core business operations: the cleanup work is always far more expensive than building it right.",
        "golden_takeaway_fa": "یک پست اشتباه در شبکه‌های اجتماعی حذف می‌شود، اما یک استقرار معیوب هوش مصنوعی کسب‌وکار را نابود می‌کند؛ هزینه پاکسازی فاجعه همواره سنگین‌تر از ساخت اصولی است.",
        "table_mistake_en": "Hiring consultants based on slide decks, social followers, and sandbox screen shares without production lineage.",
        "table_mistake_fa": "استخدام مشاوران بر اساس اسلایدهای چشم‌نواز، فالوور و دموهای سندباکس بدون سابقه واقعی پروداکشن.",
        "table_production_en": "Production track record gating: validating live pipeline telemetry, zero-leak isolation, and verified SLA history.",
        "table_production_fa": "دروازه اعتبارسنجی کارنامه: اعتبارسنجی تله‌متری پایپ‌لاین زنده، ایزولاسیون کامل و شواهد پایداری عملیاتی.",
        "code_snippet": (
            "// PRODUCTION STANDARD: Deployment Verification & Acceptance Gate\n"
            "export interface ProductionReadinessGate {\n"
            "  verifiedProductionSla: number; // e.g. 99.95%\n"
            "  pipelineResilienceTested: boolean;\n"
            "  dataIntegrityAudited: boolean;\n"
            "  rollbackPlanSimulated: boolean;\n"
            "}\n\n"
            "export function validateConsultantArchitecture(gate: ProductionReadinessGate): boolean {\n"
            "  if (!gate.pipelineResilienceTested || !gate.rollbackPlanSimulated) {\n"
            "    throw new Error('REJECT: Architecture lacks proven production resilience and rollback gates.');\n"
            "  }\n"
            "  return true;\n"
            "}"
        )
    },
    {
        "number": "325",
        "title": "Frontier API Margin Trap: The Math of Self-Hosting Sovereign Models",
        "title_fa": "تله حاشیه سود APIهای تجاری: محاسبات مالی و مهندسی میزبانی مدل‌های مستقل",
        "url": "https://www.instagram.com/reel/325/",
        "category": "11-cloud-finops",
        "category_name_en": "Cloud Infrastructure & FinOps",
        "category_name_fa": "معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه",
        "category_color": "#06b6d4",
        "layer": 6,
        "severity": "HIGH",
        "transcript": (
            "Every dollar you spend on a Frontier API is a dollar that builds someone else's valuation. Not your product, not your margin, but their IPO. "
            "So, here's what the math actually looks like when you run it yourself. A midsize team sends 50 million tokens a month through a Frontier API. "
            "At current pricing, that's 1,500 to 3,000 a month, depending on the model and the ratio of input to output tokens. "
            "But that's $18 to $36,000 a year and the price goes up every time they add a capability you didn't ask for and bundle it into a tier that you can't opt out of. "
            "So the same workload on a self-hosted stack runs $200 to $400 a month in compute. A VPS with enough memory for a 13 billion parameter model. "
            "The model is free. The inference framework is free. The infrastructure software is free. So year one including setup and configuration is likely under $6,000. "
            "Year two, five grand. And that number does not change when someone else decides to charge more for reasoning or context windows or whatever features they're dropping. "
            "But the real cost of API dependency is not on the invoice. It is the leverage you are surrendering. When your business logic lives in prompts sent to someone else's server, "
            "that someone else sees your logic, your competitive strategy, your customer patterns, your pricing experience, your IP. "
            "So, every query teaches their model something about your specific market. So, when you run it yourself, that intelligence stays inside your house. "
            "The frontier companies are not selling you AI. They're selling you convenience. And the price of convenience is everything that makes your business different "
            "from the one using the same API with the same prompts on the same platform. So, own the model, own the data, own the margin, or let the Frontier AI own you."
        ),
        "problem_en": "Over-relying on proprietary frontier APIs drains company margins ($18k–$36k/year for 50M tokens/month) and leaks sensitive proprietary prompts and customer intelligence to model vendors.",
        "problem_fa": "اتکای صرف به APIهای غول‌های فناوری حاشیه سود را می‌بلعد (۱۸ تا ۳۶ هزار دلار سالانه برای ۵۰ میلیون توکن) و منطق تجاری و داده‌های کاربران را در اختیار پلتفرم خارجی می‌گذارد.",
        "root_cause_en": "Trading long-term margin and intellectual property sovereignty for initial integration convenience, failing to analyze open-weight model unit economics.",
        "root_cause_fa": "قربانی کردن حاشیه سود پایدار و استقلال مالکیت فکری به بهای راحتی کوتاه‌مدت، و عدم تحلیل اقتصاد توکن در مدل‌های بازمتن.",
        "action_plan_en": [
            "Benchmark target inference tasks against quantized open-weight models (e.g. 13B/70B) running on self-managed GPU compute.",
            "Deploy local inference engines (vLLM, Ollama) on fixed-cost VPS/dedicated hardware to cap annual costs under $6,000.",
            "Enforce zero-leak architecture: route proprietary prompts, RAG documents, and financial workflows exclusively through internal VPC inference."
        ],
        "action_plan": [
            "ارزیابی عملکرد مدل‌های متن‌باز کوانتیزه‌شده روی سرورهای اختصاصی در برابر تسک‌های مورد نیاز محصول.",
            "استقرار موتورهای استنتاج محلی مانند vLLM روی سرورهای ابری با هزینه ثابت و کاهش هزینه‌های سالانه به زیر ۶۰۰۰ دلار.",
            "اعمال معماری بدون نشت داده: هدایت تمام پرامپت‌ها و داده‌های مالی کاربران از شبکه داخلی VPC بدون خروج به سرویس‌های عمومی."
        ],
        "golden_takeaway_en": "Frontier AI vendors sell convenience at the cost of your margin and IP: own the model, own the infrastructure, and own the data—or let big AI own your business.",
        "golden_takeaway_fa": "شرکت‌های تجاری هوش مصنوعی راحتی را در ازای مالکیت فکری و حاشیه سود شما می‌فروشند؛ مالک مدل، زیرساخت و داده‌های خود باشید، وگرنه تحت انقیاد آن‌ها خواهید بود.",
        "table_mistake_en": "Routing high-volume proprietary workflows to metered third-party APIs, surrendering IP and paying 5x–10x markup.",
        "table_mistake_fa": "ارسال حجم بالای پرامپت‌های حساس بیزینس به API متری شرکت‌های خارجی، پرداخت هزینه‌های ۱۰ برابری و نشت IP.",
        "table_production_en": "Self-hosted sovereign inference with fixed compute costs ($200–$400/mo) and complete data isolation within private VPC.",
        "table_production_fa": "استقرار محلی موتورهای استنتاج بازمتن با هزینه ثابت ماهانه و ایزولاسیون کامل داده‌ها درون شبکه خصوصی.",
        "code_snippet": (
            "# PRODUCTION STANDARD: Sovereign vLLM Deployment Script (Docker Compose)\n"
            "version: '3.8'\n"
            "services:\n"
            "  sovereign-llm:\n"
            "    image: vllm/vllm-openai:latest\n"
            "    runtime: nvidia\n"
            "    environment:\n"
            "      - MODEL=meta-llama/Llama-3.1-8B-Instruct\n"
            "      - MAX_MODEL_LEN=8192\n"
            "      - GPU_MEMORY_UTILIZATION=0.90\n"
            "    ports:\n"
            "      - \"127.0.0.1:8000:8000\" # Strictly localhost / internal VPC\n"
            "    deploy:\n"
            "      resources:\n"
            "        reservations:\n"
            "          devices:\n"
            "            - driver: nvidia\n"
            "              count: 1\n"
            "              capabilities: [gpu]\n"
            "    restart: unless-stopped"
        )
    },
    {
        "number": "326",
        "title": "Flat Network Blast Radius: Microsegmentation, mTLS & Least Privilege",
        "title_fa": "شعاع انفجار شبکه فلت: ریزبخش‌بندی شبکه، احراز هویت متقابل و حداقل دسترسی",
        "url": "https://www.instagram.com/reel/326/",
        "category": "02-security-defense",
        "category_name_en": "Application Security & Defense",
        "category_name_fa": "امنیت نرم‌افزار، حملات و دفاع لایه‌ای",
        "category_color": "#ef4444",
        "layer": 8,
        "severity": "CRITICAL",
        "transcript": (
            "Your AI deployed multiple services on the same network. The marketing dashboard, the admin API, and the production database all communicate freely. "
            "A vulnerability in one gives access to them all. So, a network where everything trusts everything is one breach away from losing everything. "
            "It's time to do something about it. Step one, your marketing tool has a known vulnerability. An attacker exploits it and gains a shell on that container. "
            "From there, they can reach the admin API because both services share a network with no segmentation. So the admin API connects to the production database "
            "with credentials that are stored in environment variables that an attacker can now read. So one compromised marketing widget escalated to full database access. "
            "So direct your AI to segment your network so each service can only reach the specific services that it needs. Marketing can't reach the database. "
            "The admin API cannot reach marketing and that is a win. Step two, service to service communication inside your network happens without authentication. "
            "So any process on the network can call any internal endpoint. An attacker who compromises one service makes unauthenticated requests to every other service. "
            "So direct your AI to require mutual TLS or service tokens for every internal API call. No internal request should be trusted because of its network location alone. Never. "
            "And number three, your AI deployed every service with the same permissions. The marketing container has the same network access as the database container. "
            "If a service does not need to reach the internet, should not be able to. If it does not need to write to the database, its credentials should be read only. "
            "So direct your AI to apply the principle of least privilege to every container, service account, and network rule. "
            "One breach should give an attacker one service, not your entire operation. And that is a win."
        ),
        "problem_en": "AI-generated deployments configure flat shared networks where frontend widgets, admin APIs, and databases trust each other implicitly, allowing an attacker who compromises a minor service to seize the entire database.",
        "problem_fa": "ابزارهای هوش مصنوعی سرویس‌ها را روی یک شبکه فلت مشترک می‌گذارند؛ نفوذ به یک ابزار بازاریابی ساده، امکان دسترسی مستقیم و استخراج کامل دیتابیس را برای مهاجم فراهم می‌سازد.",
        "root_cause_en": "Zero network segmentation, trusting traffic based solely on internal network location, and granting identical broad IAM and network capabilities to all containers.",
        "root_cause_fa": "عدم تفکیک شبکه‌ای کانتینرها، اعتماد بی‌جا به ترافیک داخلی به صرف موقعیت شبکه و صدور دسترسی‌های یکسان برای تمام سرویس‌ها.",
        "action_plan_en": [
            "Implement VPC microsegmentation and isolated Docker/Kubernetes network bridges restricting marketing from reaching internal data tiers.",
            "Mandate mutual TLS (mTLS) or signed short-lived service tokens for 100% of internal service-to-service RPC calls.",
            "Enforce least-privilege egress controls: block outbound internet access for database containers and issue read-only DB credentials where writes are unneeded."
        ],
        "action_plan": [
            "پیاده‌سازی ریزبخش‌بندی (Microsegmentation) و پل‌های شبکه‌ای مجزا تا سرویس‌های ظاهری دسترسی فیزیکی به دیتابیس نداشته باشند.",
            "الزام برقراری mTLS یا توکن‌های سرویسی امضاشده برای ۱۰۰٪ ارتباطات داخلی سرور-به-سرور.",
            "اعمال حداقل اختیارات (Least Privilege): مسدودسازی کامل اینترنت خروجی برای دیتابیس و اعطای دسترسی‌های فقط‌خواندنی."
        ],
        "golden_takeaway_en": "A flat network that trusts everything is one breach away from losing everything: enforce network segmentation, zero-trust mTLS, and least privilege so one breach yields one service, not your company.",
        "golden_takeaway_fa": "شبکه‌ای که به همه اعتماد دارد با یک رخنه کل سیستم را بر باد می‌دهد؛ با ریزبخش‌بندی، mTLS و حداقل اختیارات اطمینان یابید که یک نفوذ فقط یک سرویس را آلوده می‌کند نه کل کسب‌وکار را.",
        "table_mistake_en": "Flat Docker/VPC network where all services share credentials, communicate without tokens, and have unrestricted egress.",
        "table_mistake_fa": "شبکه فلت که کانتینر مارکتینگ، ادمین و دیتابیس روی یک پل مشترک بدون احراز هویت با هم حرف می‌زنند.",
        "table_production_en": "Microsegmented subnets with Calico/Docker network isolation, mandatory mTLS tokens, and egress firewalls.",
        "table_production_fa": "زیرشبکه‌های ایزوله با فایروال‌های سخت‌گیرانه، توکن‌های mTLS برای هر فراخوانی داخلی و مسدودسازی دسترسی مستقیم.",
        "code_snippet": (
            "# PRODUCTION STANDARD: Docker Compose Network Microsegmentation\n"
            "networks:\n"
            "  frontend-tier:\n"
            "    internal: false\n"
            "  backend-tier:\n"
            "    internal: true\n"
            "  data-tier:\n"
            "    internal: true\n\n"
            "services:\n"
            "  marketing-ui:\n"
            "    networks: [frontend-tier]\n"
            "  api-service:\n"
            "    networks: [frontend-tier, backend-tier]\n"
            "  database:\n"
            "    networks: [data-tier] # Inaccessible from marketing-ui directly"
        )
    },
    {
        "number": "327",
        "title": "The Wildcard CORS Breach: Explicit Allowlists & Safe Credential Handling",
        "title_fa": "رخنه CORS از طریق وایلدکارد: لیست مجاز صریح و مدیریت ایمن کوکی‌ها",
        "url": "https://www.instagram.com/reel/327/",
        "category": "02-security-defense",
        "category_name_en": "Application Security & Defense",
        "category_name_fa": "امنیت نرم‌افزار، حملات و دفاع لایه‌ای",
        "category_color": "#ef4444",
        "layer": 8,
        "severity": "CRITICAL",
        "transcript": (
            "Your AI configured CORS on your API. The browser asked which origins are allowed and your server said all of them. "
            "So an attacker just read your user's private data from a completely different website. Your CORS policy allowed it. "
            "So your API trusts every origin on the internet because your AI set access control allow origin to the wild card. "
            "An API that trusts every origin trusts the attacker's origin too. So here are three steps to get it fixed. "
            "Step one, the wildcard header tells every browser that any website can read responses from your API. "
            "So an attacker hosts a page that makes requests to your API using your user's cookies. The browser sends the credentials. "
            "Your API returns the data and the attacker's page reads it. So your user never leaves the attacker's website. "
            "You need to direct your AI to replace the wild card with an explicit allow list of your own domains. That is the win. "
            "Step two, your AI may have added access control allow credentials alongside the wild card. "
            "This tells the browser to include cookies with cross origin requests. The wild card with credentials is the most dangerous CORS configuration possible. "
            "Don't do it. Every website on the internet can make authenticated requests to your API and read the full response. "
            "So, direct your AI to set credentials to true only when the origin header matches your allow list. That's a win. "
            "And step three, your API reflects the origin header back as the access control allow origin value without checking it. "
            "This is functionally identical to a wild card, but passes automated scans that flag wild cards. "
            "So, an attacker sets their origin, your API echoes it back and the browser fully trusts it. "
            "So direct your AI to validate the origin header against a hard-coded allow list before reflecting it. "
            "Your API has a guest list. Right now, everyone is on it, and that is not a win."
        ),
        "problem_en": "AI assistants configure wildcard CORS headers (Access-Control-Allow-Origin: *), combine them with credentials, or echo arbitrary Origin headers, allowing malicious websites to harvest private user data via CSRF/cross-origin requests.",
        "problem_fa": "هوش مصنوعی هدرهای CORS را با ستاره (*) تنظیم می‌کند یا اوریجین مهاجم را عینا بازتاب می‌دهد؛ در نتیجه وب‌سایت مهاجم کوکی‌های کاربر را ارسال کرده و پاسخ‌های محرمانه API را می‌خواند.",
        "root_cause_en": "Defaulting to permissive CORS settings to bypass local development browser errors, combined with naive origin reflection that bypasses simplistic static scanners.",
        "root_cause_fa": "تنظیم CORS روی مقادیر باز برای حل سریع خطاهای مرورگر در محیط لوکال و اکو کردن خودکار اوریجین ورودی جهت دور زدن اسکنرهای امنیتی.",
        "action_plan_en": [
            "Replace wildcard origins with an immutable, strict allowlist of validated production domains.",
            "Reject Access-Control-Allow-Credentials when incoming requests do not strictly match the domain allowlist.",
            "Sanitize and validate Origin headers against exact regex/whitelist rules before dynamic reflection, returning null for unverified domains."
        ],
        "action_plan": [
            "جایگزینی هدر ستاره با لیست سفید قطعی و صریح دامنه‌های مجاز پروداکشن.",
            "غیرفعال‌سازی Access-Control-Allow-Credentials در صورت عدم تطابق دقیق درخواست با لیست مجاز دامنه‌ها.",
            "اعتبارسنجی دقیق هدر Origin قبل از بازتاب در پاسخ و بازگرداندن هدر خالی یا خطای 403 برای مبداهای ناشناس."
        ],
        "golden_takeaway_en": "Your API must have a strict guest list: wildcard CORS or unvalidated origin reflection hands your authenticated user data directly to any malicious site on the web.",
        "golden_takeaway_fa": "اندپوینت‌های شما باید لیست مهمانان اختصاصی داشته باشند؛ تنظیم ستاره در CORS یا بازتاب کورکورانه هدر Origin، اطلاعات محرمانه کاربران را تقدیم سایت‌های مخرب می‌کند.",
        "table_mistake_en": "Setting Access-Control-Allow-Origin: * or echoing req.headers.origin blindly with allowCredentials: true.",
        "table_mistake_fa": "قرار دادن * در Access-Control-Allow-Origin یا اکو کردن هر Origin ورودی همراه با فعال‌سازی کوکی‌ها.",
        "table_production_en": "Explicit domain allowlist, strict regex matching for trusted origins, and credentials set exclusively for verified peers.",
        "table_production_fa": "تعریف لیست سفید سخت‌گیرانه دامنه‌ها، اعتبارسنجی مبدا با Regex دقیق و فعال‌سازی کوکی تنها برای کلاینت‌های مجاز.",
        "code_snippet": (
            "// PRODUCTION STANDARD: Hardened Express CORS Middleware\n"
            "import cors from 'cors';\n\n"
            "const ALLOWED_ORIGINS = new Set([\n"
            "  'https://app.productiondomain.com',\n"
            "  'https://admin.productiondomain.com'\n"
            "]);\n\n"
            "export const secureCors = cors({\n"
            "  origin: (origin, callback) => {\n"
            "    // Allow non-browser server-to-server or strictly allowed web origins\n"
            "    if (!origin || ALLOWED_ORIGINS.has(origin)) {\n"
            "      callback(null, true);\n"
            "    } else {\n"
            "      callback(new Error('CORS Policy: Origin strictly blocked by security rule.'));\n"
            "    }\n"
            "  },\n"
            "  credentials: true,\n"
            "  methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],\n"
            "  allowedHeaders: ['Content-Type', 'Authorization', 'X-Requested-With']\n"
            "});"
        )
    },
    {
        "number": "328",
        "title": "The 4-Step Sovereign VPS AI Pipeline: Model, Train, Host, API",
        "title_fa": "پایپ‌لاین ۴ مرحله‌ای استقلال هوش مصنوعی روی سرور: مدل، آموزش، میزبانی و ساخت API",
        "url": "https://www.instagram.com/reel/328/",
        "category": "11-cloud-finops",
        "category_name_en": "Cloud Infrastructure & FinOps",
        "category_name_fa": "معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه",
        "category_color": "#06b6d4",
        "layer": 6,
        "severity": "HIGH",
        "transcript": (
            "Someone just yesterday in my comments asked me to show the full VPS pipeline. "
            "How to take an AI model from Hugging Face, train it on your data, host it on your own server, and expose an API your product can call all day long. "
            "So here it is. Step one is the model. Hugging Face is the largest open repository of AI models on the internet. "
            "Thousands of models, most of them are free. You're not building a model from scratch. "
            "You're selecting one that already does 80% of what you need and fine-tuning it on your data to close that gap. "
            "Step two is training. Fine-tuning means taking a pre-trained model and running it against your own data set, "
            "your customer support transcripts, your medical records, your legal contracts, your product data, all of it. "
            "The model learns the patterns in your domain. This runs on a local GPU, could be a rented one from a cloud provider or one sitting on your desk. "
            "Step three, hosting. The fine-tuned model runs on a server that you control, a VPS with a GPU, a local machine with 3090, a 4090, a 5080. "
            "You deploy it using an inference framework like vLLM or Ollama. The model loads into memory and waits for requests. "
            "And step four is the API. You wrap the inference endpoint in a REST API. Your product calls it the same way it would call an OpenAI or Anthropic. "
            "Same request format, same response format, except the model, it's yours. The data stays on your network. "
            "Cost is totally fixed and no one changes the terms after you ship it. "
            "That is the VPS pipeline: model, training, hosting, API. Four steps between dependency and full ownership. Go check it out."
        ),
        "problem_en": "Engineering teams assume building proprietary AI requires millions in R&D, leaving them trapped in costly third-party API dependencies that throttle unit economics.",
        "problem_fa": "تیم‌های نرم‌افزاری تصور می‌کنند راه‌اندازی هوش مصنوعی اختصاصی نیازمند میلیون‌ها دلار بودجه است؛ در نتیجه وابسته به اشتراک‌های گران و ریسک‌های پلتفرمی می‌شوند.",
        "root_cause_en": "Unfamiliarity with modern open-weight fine-tuning pipelines and standardized inference runtimes (vLLM, Ollama) that turn commodity GPUs into drop-in OpenAI-compatible endpoints.",
        "root_cause_fa": "عدم آگاهی از اکوسیستم فاین‌تیونینگ مدل‌های متن‌باز و موتورهای استنتاج استاندارد مانند vLLM که هر کارت گرافیک معمولی را به یک سرور API پرسرعت تبدیل می‌کنند.",
        "action_plan_en": [
            "Source high-performing open-weight base models from Hugging Face (e.g. Llama 3, Mistral, GLM) matching target domain capabilities.",
            "Fine-tune with LoRA/QLoRA on private domain datasets (support tickets, contracts, domain logs) using rented spot GPUs or local hardware.",
            "Deploy inference engines (vLLM / Ollama) behind a hardened reverse proxy with standard OpenAI-compatible REST schemas."
        ],
        "action_plan": [
            "انتخاب مدل‌های پایه متن‌باز از Hugging Face که ۸۰٪ نیاز تخصصی پروژه را پوشش می‌دهند.",
            "فاین‌تیونینگ اختصاصی با متدهای LoRA/QLoRA روی داده‌های واقعی سازمان مانند گزارش‌ها، قراردادها و مستندات.",
            "میزبانی مدل با موتورهای سریع مانند vLLM روی سرورهای ابری با هزینه ثابت و ایجاد اندپوینت سازگار با استانداردهای REST."
        ],
        "golden_takeaway_en": "Four steps stand between API dependency and complete AI sovereignty: select the base model, fine-tune on domain data, host on private compute, and expose an internal REST API.",
        "golden_takeaway_fa": "تنها چهار گام میان وابستگی پرهزینه و حاکمیت کامل بر هوش مصنوعی فاصله است: انتخاب مدل پایه، فاین‌تیونینگ روی داده‌های خود، میزبانی روی سرور اختصاصی و ارائه API سازگار.",
        "table_mistake_en": "Treating proprietary frontier APIs as the only viable deployment model, bleeding margins on repetitive queries.",
        "table_mistake_fa": "تصور اینکه تنها راه پیاده‌سازی هوش مصنوعی پرداخت اشتراک ماهانه به غول‌های ابری و نشت داده است.",
        "table_production_en": "4-step self-hosted pipeline: Hugging Face model + domain fine-tuning + vLLM on private VPS + internal REST API.",
        "table_production_fa": "پایپ‌لاین ۴ مرحله‌ای مستقل: انتخاب مدل متن‌باز + فاین‌تیونینگ با داده بومی + اجرای vLLM روی سرور اختصاصی + اتصال API امن.",
        "code_snippet": (
            "# PRODUCTION STANDARD: 4-Step Sovereign Inference Pipeline Deployment\n"
            "# 1. Select Model: huggingface-cli download meta-llama/Meta-Llama-3-8B-Instruct\n"
            "# 2. Fine-tune: unsloth / trl with QLoRA on domain dataset\n"
            "# 3. Serve via vLLM:\n"
            "python -m vllm.entrypoints.openai.api_server \\\n"
            "  --model ./fine-tuned-model \\\n"
            "  --host 127.0.0.1 \\\n"
            "  --port 8000 \\\n"
            "  --max-model-len 8192 \\\n"
            "  --tensor-parallel-size 1\n"
            "# 4. Internal API client consumes standard /v1/chat/completions securely."
        )
    },
    {
        "number": "329",
        "title": "Default Open S3 Buckets: Separation of Assets, Randomized IDs & Audit Logs",
        "title_fa": "باکت‌های ابری باز پیش‌فرض: تفکیک فایل‌ها، شناسه‌های تصادفی و لاگ دسترسی",
        "url": "https://www.instagram.com/reel/329/",
        "category": "03-database-storage",
        "category_name_en": "Database & Storage Engineering",
        "category_name_fa": "پایگاه‌داده، روابط، ایندکس و پایداری داده",
        "category_color": "#3b82f6",
        "layer": 3,
        "severity": "CRITICAL",
        "transcript": (
            "Your AI needed a place to store file uploads. So, it created an S3 bucket, a Google Cloud Storage bucket, or an Azure blob container, right? "
            "It set the permissions to public so the application could serve files without authentication errors. The uploads work, so does every unauthorized download. "
            "You don't want me to tell you what an attacker did, but they just downloaded your entire user database from a cloud storage bucket you forgot was public. "
            "So, your AI created the bucket with default permissions like they all do. Default means wide open and open means everyone gets in. "
            "So let's lock it down. Step one, your AI created a storage bucket and set the access control to public read because the application needed to serve images. "
            "But the same bucket also stores database backups, user exports, and configuration files. "
            "So any attacker who finds the bucket URL downloads everything in it. So, direct your AI to separate public assets from private data into different buckets. "
            "Public assets get public read. Everything else gets private with pre-signed URLs that expire. That is a win. "
            "Step two, your bucket name is predictable. Company name-uploads, company name-backups. "
            "So, attackers, they enumerate common naming patterns and scan for open buckets at scale all day long. "
            "So direct your AI to use randomized bucket names that do not contain your company name, an environment name, or a data purpose. "
            "And step three, your AI never enabled access logging on your bucket. So an attacker has been downloading files for weeks and you have no record of it at all. "
            "No IP addresses, no timestamps, no file access history. "
            "So direct your AI to enable server access logging and configure alerts for unusual download code patterns or access from unexpected IP ranges. "
            "Your cloud storage should store your data and not serve it to anyone who asks for it. Get it tied up."
        ),
        "problem_en": "AI tools configure single cloud storage buckets with public-read permissions to bypass upload errors, unintentionally exposing database backups, private user exports, and system configs to automated internet crawlers.",
        "problem_fa": "هوش مصنوعی برای حل خطاهای آپلود، پرمیشن باکت S3 را روی عمومی (Public Read) می‌گذارد و بک‌آپ‌های دیتابیس و داده‌های کاربران را در کنار تصاویر عمومی ذخیره می‌کند که باعث افشای کل اطلاعات می‌شود.",
        "root_cause_en": "Mixing public media and confidential backups in the same storage container, using predictable bucket names (company-backups), and omitting server access logging.",
        "root_cause_fa": "ترکیب فایل‌های عمومی و بک‌آپ‌های حساس در یک باکت، استفاده از نام‌های قابل پیش‌بینی برای باکت و عدم فعال‌سازی لاگینگ دسترسی سرور.",
        "action_plan_en": [
            "Segregate storage into strictly separated buckets: public CDN assets vs. private air-gapped data served exclusively via expiring pre-signed URLs.",
            "Apply high-entropy randomized suffixes to all bucket identifiers (e.g. `data-7f9a2b8e4c1d`) to prevent dictionary enumeration attacks.",
            "Enable S3/GCS Server Access Logging and real-time CloudWatch/Alertmanager triggers on suspicious egress volumes and anomalous IP ranges."
        ],
        "action_plan": [
            "تفکیک کامل باکت‌ها: نگهداری تصاویر در باکت عمومی و انتقال بک‌آپ‌ها به باکت خصوصی با دسترسی منحصراً از طریق لینک‌های امضاشده موقت (Pre-signed URLs).",
            "استفاده از شناسه‌های تصادفی با آنتروپی بالا برای نام باکت‌ها جهت مهار حملات پویش خودکار و کشف نام.",
            "فعال‌سازی لاگ دسترسی سرور (Server Access Logging) و هشدارهای بلادرنگ برای حجم دانلود غیرعادی یا دسترسی از آی‌پی‌های مشکوک."
        ],
        "golden_takeaway_en": "Your cloud storage should store data, not serve it to anyone who asks: isolate public assets from private records, randomize bucket identifiers, and enforce expiring pre-signed URLs.",
        "golden_takeaway_fa": "فضای ذخیره‌سازی ابری باید حافظ داده باشد نه توزیع‌کننده آن به عموم؛ داده‌های حساس را با لینک‌های موقت محافظت کنید، نام باکت‌ها را غیرقابل حدس بسازید و لاگ‌ها را پایش نمایید.",
        "table_mistake_en": "Creating a single public bucket for both user images and DB backups with predictable names like company-backups.",
        "table_mistake_fa": "استفاده از یک باکت پابلیک واحد برای تصاویر و بک‌آپ‌های دیتابیس با نام‌های قابل حدس مانند company-backups.",
        "table_production_en": "Dual-bucket topology: public CDN bucket for static media + private bucket with expiring pre-signed URLs (TTL < 15m) and access logging.",
        "table_production_fa": "توپولوژی دوباکتی: باکت استاتیک عمومی CDN برای تصاویر + باکت کاملاً خصوصی با لینک موقت انقضادار (زیر ۱۵ دقیقه) و ثبت تمام لاگ‌ها.",
        "code_snippet": (
            "// PRODUCTION STANDARD: Secure Pre-Signed URL Generator for Private Assets\n"
            "import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';\n"
            "import { getSignedUrl } from '@aws-sdk/s3-request-presigner';\n\n"
            "const s3 = new S3Client({ region: process.env.AWS_REGION });\n"
            "const PRIVATE_BUCKET = process.env.RANDOMIZED_PRIVATE_BUCKET_ID!; // e.g. 'vault-8f3a9e2c'\n\n"
            "export async function generateSecureDownloadUrl(fileKey: string, tenantId: string): Promise<string> {\n"
            "  // Enforce tenant isolation in the key prefix\n"
            "  const fullKey = `tenants/${tenantId}/${fileKey}`;\n"
            "  const command = new GetObjectCommand({ Bucket: PRIVATE_BUCKET, Key: fullKey });\n"
            "  // Short-lived pre-signed URL: strictly 15 minutes TTL\n"
            "  return await getSignedUrl(s3, command, { expiresIn: 900 });\n"
            "}"
        )
    },
    {
        "number": "330",
        "title": "Dedicated Server vs On-Demand VPS: The Infrastructure Ownership Threshold",
        "title_fa": "سرور اختصاصی در برابر سرور متری ابری: آستانه مالکیت زیرساخت و مهاجرت اقتصادی",
        "url": "https://www.instagram.com/reel/330/",
        "category": "11-cloud-finops",
        "category_name_en": "Cloud Infrastructure & FinOps",
        "category_name_fa": "معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه",
        "category_color": "#06b6d4",
        "layer": 6,
        "severity": "MEDIUM",
        "transcript": (
            "Every single time I post about AI sovereignty, the same questions arrive in my comments. "
            "Should I buy my own hardware and host it or should I rent a VPS that only spins up when I need it? "
            "Well, the answer is you need to understand both options before you choose either one. So, let's start with a dedicated server. "
            "This is a machine that you own or lease at a fixed rate. It's physical hardware that has to sit somewhere. "
            "It runs whether you use it or not. So, you pay the same amount every month regardless of your traffic. "
            "Nobody changes the terms. Nobody raises the price based on your usage. And nobody decides what you can or cannot run on it. "
            "So, if you have a sustained workload, like something that processes data every single day or serves traffic around the clock or runs inference on your own models, "
            "this is likely the most cost-effective path over time. And it is the only path where you fully control the infrastructure underneath your application. "
            "That's a win. An on-demand VPS is a machine that exists only when you need it. You spin it up, you run your workload, you spin it down, you pay for what you used. "
            "Nothing runs when you're not using it. So if your workloads are unpredictable, seasonal, or experimental, this solution makes a lot of sense. "
            "That way you're not paying for idle hardware. But you also don't own anything. "
            "So that provider who sets the price and that provider who controls the terms, that provider can change both of those things anytime they want. "
            "So here's where the conversation starts to get real. Most builders start with the rental. That's fine. The danger is never leaving it. "
            "The longer you run a sustained workload on someone else's metered infrastructure, the more you're going to pay for the privilege of not owning what you already built. "
            "So dedicated server at a provider like Hetzner costs less than most people spend on a single cloud VPS doing the same job. "
            "The difference, you own the stack. You configure it. You decide what runs on it and what does not. "
            "So renting, it's not wrong at all. But if your workload runs every single day and you're still paying per hour for someone else's hardware, "
            "you're not scaling, you're subscribing. So you need to know both options. Then you choose the one that best matches what you're actually building. That is the win."
        ),
        "problem_en": "Startups keep sustained 24/7 workloads on metered hourly cloud VPS instances indefinitely, incurring huge ongoing operational overhead rather than migrating to fixed-cost dedicated bare metal.",
        "problem_fa": "کسب‌وکارها پردازش‌های شبانه‌روزی و پیوسته خود را برای مدت‌های طولانی روی سرورهای متری ابری اجرا می‌کنند و به جای مقیاس‌پذیری واقعی، مبالغ هنگفتی را بابت اشتراک منابع ابری هدر می‌دهند.",
        "root_cause_en": "Failing to recognize the workload inflection point: on-demand instances are optimal for bursts and experiments, but financially punitive for constant 24/7 inference and baseline data processing.",
        "root_cause_fa": "عدم تفکیک بار کاری تصادفی و تجربی از بار کاری پایدار ۲۴ ساعته؛ سرور متری برای آزمایش عالی است اما برای پردازش پیوسته ضرر خالص است.",
        "action_plan_en": [
            "Audit cloud resource telemetry to identify workloads operating with >60% continuous 24/7 CPU/GPU utilization.",
            "Establish an infrastructure migration policy: transition sustained workloads to fixed-cost dedicated bare metal (e.g. Hetzner, OVH).",
            "Retain metered on-demand instances strictly for unpredictable elastic bursts, non-critical dev environments, and temporary spikes."
        ],
        "action_plan": [
            "ممیزی تله‌متری مصرف سرورها و شناسایی پردازش‌هایی که بیش از ۶۰٪ توان مداوم را در طول شبانه‌روز مصرف می‌کنند.",
            "انتقال پردازش‌های پایدار ۲۴ ساعته به سرورهای اختصاصی (Dedicated Bare Metal) با هزینه ثابت ماهانه بدون تغییر شرایط سرویس.",
            "نگه‌داشتن نمونه‌های متری و سرورلس صرفاً برای بارهای غیرمنتظره، دوره‌های فصلی یا محیط‌های آزمایشی موقت."
        ],
        "golden_takeaway_en": "If your workload runs 24/7 and you are still paying by the hour for someone else's metered hardware, you are not scaling—you are subscribing.",
        "golden_takeaway_fa": "اگر پردازش‌های سیستم شما به طور شبانه‌روزی اجرا می‌شوند و هنوز دارید ساعتی پول سخت‌افزار دیگران را می‌دهید، شما در حال رشد نیستید، بلکه فقط مشترک آن‌ها شده‌اید.",
        "table_mistake_en": "Running continuous 24/7 AI inference and database workloads on metered hourly VPS instances indefinitely.",
        "table_mistake_fa": "اجرای دائمی و ۲۴ ساعته پایگاه‌های داده و مدل‌های استنتاج روی سرورهای ابری متری و گران‌قیمت.",
        "table_production_en": "Workload-driven infrastructure tiering: dedicated bare metal for sustained 24/7 baseline + elastic VPS for burst spikes.",
        "table_production_fa": "لایه‌بندی هوشمند زیرساخت: سرور اختصاصی برای بار کاری پایدار با هزینه ثابت + سرور متری صرفاً برای پیک‌های ترافیکی ناگهانی.",
        "code_snippet": (
            "# PRODUCTION STANDARD: Infrastructure Cost Arbitrage Analysis\n"
            "# Sustained Workload Rule:\n"
            "# If HoursActivePerMonth > 500 (~70% of month):\n"
            "#   DedicatedServerMonthlyCost ($45 - $90 fixed) < CloudVpsMeteredCost ($220+ variable)\n"
            "# Decision Matrix:\n"
            "def select_compute_tier(monthly_hours_active: int, is_burst: bool) -> str:\n"
            "    if is_burst or monthly_hours_active < 300:\n"
            "        return 'ON_DEMAND_EPHEMERAL_VPS'  # Scale to zero when idle\n"
            "    return 'DEDICATED_BARE_METAL'          # Fixed contract, full hardware sovereignty"
        )
    },
    {
        "number": "331",
        "title": "The Big AI Agent Land Grab: Operating Systems vs Sovereign Control",
        "title_fa": "تسخیر شرکتی ایجنت‌های هوش مصنوعی: سیستم‌عامل‌های اجاره‌ای در برابر حاکمیت سازمانی",
        "url": "https://www.instagram.com/reel/331/",
        "category": "09-ai-guardrails",
        "category_name_en": "AI Guardrails, LLM Security & Compliance",
        "category_name_fa": "مهار مدل‌های هوش مصنوعی، پرامپت و الزامات قانونی",
        "category_color": "#8b5cf6",
        "layer": 2,
        "severity": "CRITICAL",
        "transcript": (
            "Meta, OpenAI, and a startup named Instinct, valued at $10 billion, all launched Autonomous AI agents just last week. "
            "And every single one of them showed small business owners in their premier launch videos. And I'll tell you that wasn't a coincidence. "
            "It's a land grab. You see, Meta launched Muse for small business. It connects to Shopify, Stripe, Slack, QuickBooks, Notion, all of them. "
            "And it learns your brand voice. It manages your operations. It runs inside of Meta's ecosystems on Meta's terms. "
            "OpenAI launched DOT. Insert Elon jokes here, right? Always on agents powered by Astra. "
            "Each one runs on its own cloud infrastructure with connections to over 4,000 apps working in the background making files and reports before you even ask. "
            "And the AI startup Instinct raised a billion at a $10 billion valuation. It'll book your travel, cancel your subscriptions, make phone calls on your behalf. "
            "It coordinates with other people's agents through a trusted network. Little bit different. "
            "All three companies, three architectures, same target: your small to medium business. "
            "And every one of them requires the exact same thing. Full access to your IP, your operations, your data, your customer information, "
            "your financial information and all of your workflows. The agent does not work without all that data. "
            "The question is not whether autonomous agents are useful. They are. The question is whether the agent running your business reports to you "
            "or does it report to the company that built it. So whether your operational data trains their next model might be an issue. "
            "Whether the pricing stays the same after you are fully dependent and cannot operate without them? That's a question. "
            "These companies are not launching agents. They're launching operating systems for your specific business on someone else's infrastructure under someone else's terms. "
            "The people in the faction community are already building around this, right? Not renting it from big AI, but building it on their own, their own stack, their own terms. "
            "The agent race is not about who builds the best agent. It's about who owns it. And big AI, it's about to own everything about your business."
        ),
        "problem_en": "Autonomous corporate AI agents require complete integration into core financial, customer, and operational databases (Stripe, QuickBooks, Slack), handing vendors total operational lock-in and intelligence exposure.",
        "problem_fa": "ایجنت‌های خودکار شرکت‌های بزرگ برای فعالیت نیاز به دسترسی به تمام ابزارهای مالی و مشتریان دارند؛ واگذاری این دسترسی کسب‌وکار را وابسته و داده‌ها را در اختیار رقبا می‌گذارد.",
        "root_cause_en": "Treating autonomous agents as harmless productivity tools rather than recognizing them as third-party operating systems embedding deeply inside company workflows on vendor-controlled terms.",
        "root_cause_fa": "ساده‌انگاری ایجنت‌های هوش مصنوعی به عنوان ابزار کاربردی بدون درک اینکه آن‌ها در واقع سیستم‌عامل کسب‌وکار شما را بر روی سرورهای دیگران پیاده می‌کنند.",
        "action_plan_en": [
            "Prohibit connecting third-party cloud agents directly to production financial databases or customer CRM read/write tokens.",
            "Build internal agent orchestration frameworks on private infrastructure using open-weight models and self-managed tool connectors.",
            "Establish strict data boundary proxies: sanitize and tokenize customer identities before passing execution requests to external models."
        ],
        "action_plan": [
            "ممنوعیت اتصال مستقیم ایجنت‌های ابری خارجی به پایگاه‌های داده مالی، حسابداری و CRM مشتریان.",
            "پیاده‌سازی ایجنت‌های سازمانی روی زیرساخت و سرورهای داخلی شرکت با استفاده از مدل‌های بازمتن و کانکتورهای اختصاصی.",
            "قرار دادن پراکسی‌های امنیتی برای ناشناس‌سازی داده‌ها و توکنایز کردن اطلاعات حساس پیش از ارسال به هر سرویس خارجی."
        ],
        "golden_takeaway_en": "The agent race is not about who builds the smartest agent, it is about who owns it: do not let corporate AI become the proprietary operating system of your business.",
        "golden_takeaway_fa": "رقابت بر سر ساخت باهوش‌ترین ایجنت نیست، بلکه بر سر این است که چه کسی مالک آن است؛ اجازه ندهید هوش مصنوعی پلتفرم‌های خارجی به سیستم‌عامل کسب‌وکار شما تبدیل شود.",
        "table_mistake_en": "Granting proprietary cloud agents full read/write access to Stripe, QuickBooks, and Slack workflows on external vendor terms.",
        "table_mistake_fa": "دادن دسترسی مستقیم و نامحدود خواندن و نوشتن به ایجنت‌های ابری روی حسابداری، درگاه‌های پرداخت و ارتباطات داخلی.",
        "table_production_en": "Sovereign agent architecture: self-hosted tool calling, private execution boundaries, and zero data leakage to external models.",
        "table_production_fa": "معماری ایجنت‌های مستقل سازمانی: اجرای محلی ابزارها، مرزهای ایزوله و عدم خروج داده‌های حیاتی به پلتفرم‌های تجاری.",
        "code_snippet": (
            "// PRODUCTION STANDARD: Sovereign Tool Execution Guardrail\n"
            "interface ToolExecutionPolicy {\n"
            "  requiresHumanApproval: boolean;\n"
            "  dataClassification: 'PUBLIC' | 'CONFIDENTIAL' | 'RESTRICTED';\n"
            "  allowedInVpcOnly: boolean;\n"
            "}\n\n"
            "export async function executeAgentTool(toolName: string, params: Record<string, any>, policy: ToolExecutionPolicy) {\n"
            "  // Never execute financial or restricted operations without local human sign-off\n"
            "  if (policy.dataClassification === 'RESTRICTED' && !params.humanApprovedToken) {\n"
            "    throw new SecurityException('BLOCKED: Automated agent action violates sovereign financial policy.');\n"
            "  }\n"
            "  return await localToolRegistry.dispatch(toolName, params);\n"
            "}"
        )
    },
    {
        "number": "332",
        "title": "Open-Weight Economics: GLM 5.3 & The 80% Workload Sovereign Replacement",
        "title_fa": "اقتصاد مدل‌های بازمتن: مدل GLM 5.3 و جایگزینی ۸۰٪ بار کاری گران‌قیمت",
        "url": "https://www.instagram.com/reel/332/",
        "category": "11-cloud-finops",
        "category_name_en": "Cloud Infrastructure & FinOps",
        "category_name_fa": "معماری ابری، سرورلس، تاب‌آوری و مدیریت هزینه",
        "category_color": "#06b6d4",
        "layer": 6,
        "severity": "HIGH",
        "transcript": (
            "Everyone's always arguing about Claude versus ChatGPT. Meanwhile, a model most of you have never even heard of just processed 2 million tokens for just 7 cents. "
            "Every week, another Frontier model drops. Another pricing tier, another big press release about new capabilities that no one's using. "
            "And every single week, the same builders are paying these same companies to process the same data on someone else's infrastructure. "
            "But something happened in my comments this week that I'm not going to ignore. Multiple people have told me they're running GLM 5.3 for 80% of their daily workload, "
            "not as a backup plan, not as an experiment, as their primary model. And I'm here for it. And the cost so low it barely registers as a line item. "
            "2 million tokens for 7 cents, that's not a typo. It's not a promotional rate. That is the actual cost of running a model that handles a vast majority of what most developers "
            "send to our Frontier APIs every single day. And here's what matters more than the price. The model's open weight. Can run it locally. "
            "You can fine-tune it on your own data. You can deploy it on the same stack I showed you just last week: Ubuntu, Docker, vLLM, right? "
            "Your rules. No one raises the price. No one changes the terms. No one trains their next model on your queries. "
            "So the frontier companies need you to believe that only their model can do the real work, that open weight means worse for them, that cheaper means weaker. "
            "But the people in my comments are telling a totally different story. They're running these models in production today. "
            "And the output is replacing 80% of their frontier API spend, which is what everybody's looking for. "
            "This is not about finding the best model. This is about finding the model that gives you the best outcome for your business at a cost that does not make you a dependency "
            "of someone else's pricing team. The frontier model race is a total distraction. But the sovereign ownership race is what matters the most in the future."
        ),
        "problem_en": "Teams waste thousands on top-tier proprietary frontier APIs for routine operational tasks (classification, entity extraction, data cleansing) that open-weight models execute at 1/100th of the price.",
        "problem_fa": "تیم‌ها مبالغ سنگینی بابت مدل‌های گران‌قیمت تجاری برای کارهای روزمره مانند استخراج داده و دسته‌بندی می‌پردازند در حالی که مدل‌های بازمتن با کسری از این هزینه همان کار را انجام می‌دهند.",
        "root_cause_en": "Falling for marketing hype that only expensive frontier models can perform production work, failing to implement tiered multi-model routing architectures.",
        "root_cause_fa": "باور به شعارهای بازاریابی مبنی بر اینکه فقط مدل‌های فوق‌العاده گران توانایی کار در محیط پروداکشن را دارند و عدم پیاده‌سازی معماری مسیریابی چندمدلی.",
        "action_plan_en": [
            "Implement an intelligent LLM router: divert 80% of structured, repetitive, or extraction workloads to self-hosted open-weight models (GLM, Llama).",
            "Reserve expensive proprietary reasoning models strictly as an exceptional fallback for high-complexity ambiguity.",
            "Run self-hosted vLLM containers on fixed compute, locking in 2 million tokens for pennies and insulating the company from vendor pricing hikes."
        ],
        "action_plan": [
            "پیاده‌سازی مسیریاب هوشمند مدل‌ها: هدایت ۸۰٪ کارهای ساختاریافته و روتین به مدل‌های بازمتن روی سرورهای خودی.",
            "استفاده از مدل‌های گران‌قیمت تجاری صرفاً به عنوان لایه نهایی برای مسائل پیچیده و با ابهام بالا.",
            "استقرار کانتینرهای vLLM روی زیرساخت خودی برای تثبیت هزینه‌ها و بی‌نیازی از تغییرات قیمت شرکت‌های خارجی."
        ],
        "golden_takeaway_en": "The frontier model race is a distraction: the sovereign ownership race is what builds enduring enterprise value by replacing 80% of API costs with open-weight efficiency.",
        "golden_takeaway_fa": "مسابقه مدل‌های تجاری یک فریب و انحراف است؛ برنده واقعی کسی است که در مسابقه استقلال زیرساختی شرکت کند و ۸۰٪ هزینه‌های خود را با مدل‌های بازمتن صفر نماید.",
        "table_mistake_en": "Routing simple extraction, summarization, and parsing requests to top-tier frontier APIs at maximum dollar rates.",
        "table_mistake_fa": "فرستادن کارهای ساده روزمره مانند استخراج متن و دسته‌بندی به گران‌ترین مدل‌های تجاری و پرداخت دلاری سنگین.",
        "table_production_en": "Intelligent tiered routing: 80% handled by local open-weight inference (GLM/Llama via vLLM) + 20% routed to frontier models conditionally.",
        "table_production_fa": "مسیریابی چندلایه‌ای: پردازش ۸۰٪ تسک‌ها با مدل‌های بازمتن محلی و هدایت هوشمند تنها ۲۰٪ موارد خاص به مدل‌های بیرونی.",
        "code_snippet": (
            "// PRODUCTION STANDARD: Tiered Sovereign LLM Routing Engine\n"
            "export async function routeLlmRequest(task: { prompt: string; complexity: 'SIMPLE' | 'COMPLEX' }) {\n"
            "  if (task.complexity === 'SIMPLE') {\n"
            "    // 80% of workload routed to sovereign open-weight cluster (2M tokens for ~7c)\n"
            "    return await fetch('http://sovereign-vllm.internal:8000/v1/chat/completions', {\n"
            "      method: 'POST',\n"
            "      headers: { 'Content-Type': 'application/json' },\n"
            "      body: JSON.stringify({ model: 'THUDM/glm-4-9b-chat', messages: [{ role: 'user', content: task.prompt }] })\n"
            "    });\n"
            "  }\n"
            "  // 20% complex reasoning fallback\n"
            "  return await callFrontierApi(task.prompt);\n"
            "}"
        )
    }
]

def main():
    print(f"Ingesting {len(NEW_MASTERCLASSES)} new masterclasses (323-332)...")
    
    # 1. Save transcripts to D:\download\mattmurphy_voices
    os.makedirs(VOICES_DIR, exist_ok=True)
    for mc in NEW_MASTERCLASSES:
        num = mc["number"]
        clean_name = re.sub(r'[^a-zA-Z0-9]', '_', mc["title"])[:50]
        out_path = os.path.join(VOICES_DIR, f"{num}_{clean_name}.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(mc["transcript"])
    print(f"  [OK] Saved transcripts to {VOICES_DIR}")

    # 2. Update data.json
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_nums = {e["number"]: idx for idx, e in enumerate(data["episodes"])}
    
    for mc in NEW_MASTERCLASSES:
        episode_obj = {
            "number": mc["number"],
            "title": mc["title"],
            "title_fa": mc["title_fa"],
            "url": mc["url"],
            "category": mc["category"],
            "category_name_fa": mc["category_name_fa"],
            "category_name_en": mc["category_name_en"],
            "category_color": mc["category_color"],
            "layer": mc["layer"],
            "problem_en": mc["problem_en"],
            "problem_fa": mc["problem_fa"],
            "root_cause_en": mc["root_cause_en"],
            "root_cause_fa": mc["root_cause_fa"],
            "action_plan_en": mc["action_plan_en"],
            "action_plan": mc["action_plan"],
            "code_snippet": mc["code_snippet"],
            "transcript": mc["transcript"],
            "has_transcript": True,
            "severity": mc["severity"],
            "golden_takeaway_en": mc["golden_takeaway_en"],
            "golden_takeaway_fa": mc["golden_takeaway_fa"],
            "table_mistake_en": mc["table_mistake_en"],
            "table_mistake_fa": mc["table_mistake_fa"],
            "table_production_en": mc["table_production_en"],
            "table_production_fa": mc["table_production_fa"],
            "is_pilot_gold": True
        }
        
        if mc["number"] in existing_nums:
            data["episodes"][existing_nums[mc["number"]]] = episode_obj
        else:
            data["episodes"].append(episode_obj)

    data["total_episodes"] = len(data["episodes"])
    
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  [OK] Updated {DATA_PATH} (Total: {data['total_episodes']} episodes)")

    # 3. Update site/data.json
    os.makedirs(os.path.dirname(SITE_DATA_PATH), exist_ok=True)
    with open(SITE_DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  [OK] Synchronized {SITE_DATA_PATH}")

    # 4. Generate Single-Lesson Markdown in docs/
    for mc in NEW_MASTERCLASSES:
        cat = mc["category"]
        num = mc["number"]
        clean_slug = re.sub(r'[^a-z0-9]+', '-', mc["title"].lower()).strip('-')
        doc_dir = os.path.join(DOCS_DIR, cat)
        os.makedirs(doc_dir, exist_ok=True)
        doc_path = os.path.join(doc_dir, f"lesson-{num}-{clean_slug}.md")

        md_content = f"""# Masterclass #{num}: {mc['title']}

**Module**: `{mc['category_name_en']}` | **Layer**: `Layer {mc['layer']:02d}` | **Severity**: `{mc['severity']}`

---

## 🚨 Problem Statement
{mc['problem_en']}

### تشریح به زبان فارسی
{mc['problem_fa']}

---

## 🔍 Root Cause Analysis
{mc['root_cause_en']}

### ریشه خطا به فارسی
{mc['root_cause_fa']}

---

## ⚖️ Production Comparison Matrix
| Architectural Dimension | Vibe Coding Anti-Pattern (Trap) | Production Engineering Standard (Verified) |
| :--- | :--- | :--- |
| **Operational Standard** | {mc['table_mistake_en']} | {mc['table_production_en']} |
| **تحلیل استاندارد فارسی** | {mc['table_mistake_fa']} | {mc['table_production_fa']} |

---

## 🛠️ Step-by-Step Action Plan
"""
        for step in mc['action_plan_en']:
            md_content += f"1. {step}\n"
        
        md_content += "\n### گام‌های عملیاتی فارسی\n"
        for step in mc['action_plan']:
            md_content += f"- {step}\n"

        md_content += f"""
---

## 💻 Hardened Production Code Pattern
```typescript
{mc['code_snippet']}
```

---

## 🎙️ Word-for-Word Audio Transcript
> "{mc['transcript']}"

---

## 💡 Golden Takeaway
> **"{mc['golden_takeaway_en']}"**
>
> *{mc['golden_takeaway_fa']}*
"""
        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(md_content)

    print(f"  [OK] Created markdown docs in {DOCS_DIR} for all new masterclasses.")

if __name__ == "__main__":
    main()
