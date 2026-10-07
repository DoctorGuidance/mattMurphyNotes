// Matt Murphy Production Engineering Academy - Core Application Logic

let rawData = null;
let allEpisodes = [];
let filteredEpisodes = [];
let currentCategory = 'all';
let currentSearch = '';
let displayLimit = 30;

// Production Audit Checkpoints (Extracted from critical Matt Murphy heuristics)
const AUDIT_CHECKPOINTS = [
  {
    id: 'chk_auth_cookie',
    cat: 'Auth',
    title: 'توکن‌های احراز هویت در کوکی‌های HttpOnly نگهداری می‌شوند (نه در localStorage)',
    desc: 'جلوگیری از سرقت توکن‌های سشن توسط حملات XSS یا اسکریپت‌های ثالث صفحه.',
    ep: '043',
    weight: 5
  },
  {
    id: 'chk_auth_idor',
    cat: 'Auth',
    title: 'تمامی کوئری‌های واکشی رکورد به tenant_id و user_id اسکوپ شده‌اند',
    desc: 'جلوگیری از آسیب‌پذیری IDOR از طریق تغییر شناسه در URL.',
    ep: '044',
    weight: 5
  },
  {
    id: 'chk_auth_pkce',
    cat: 'Auth',
    title: 'جریان ورود با OAuth (گوگل/گیت‌هاب) مجهز به اعتبارسنجی State و PKCE است',
    desc: 'جلوگیری از بازنشانی اجباری لاگین و حملات رهگیری کدهای اهراز هویت.',
    ep: '048',
    weight: 4
  },
  {
    id: 'chk_sec_secrets',
    cat: 'Security',
    title: 'هیچ کلید Service-Role، سکرت دیتابیس یا توکن OpenAI در کدهای کلاینت وجود ندارد',
    desc: 'ممانعت از انتشار کلیدهای ادمین با متغیرهای عمومی کلاینت و اسکن خودکار کامیت‌ها.',
    ep: '105',
    weight: 5
  },
  {
    id: 'chk_sec_cors',
    cat: 'Security',
    title: 'سیاست CORS روی سرور فقط به دامنه‌های مجاز اجازه دسترسی می‌دهد (نه *)',
    desc: 'جلوگیری از خوانده‌شدن داده‌های خصوصی کاربر توسط سایر وب‌سایت‌ها در مرورگر.',
    ep: '005',
    weight: 4
  },
  {
    id: 'chk_sec_frame',
    cat: 'Security',
    title: 'هدر X-Frame-Options یا CSP frame-ancestors جهت مقابله با Clickjacking فعال است',
    desc: 'جلوگیری از آی‌فریم شدن برنامه درون سایت‌های فیشینگ و کلیک‌دزدی.',
    ep: '015',
    weight: 3
  },
  {
    id: 'chk_db_index',
    cat: 'Database',
    title: 'روی تمام ستون‌های مورد استفاده در WHERE و JOIN ایندکس تعریف شده است',
    desc: 'ریشه‌کنی اسکن‌های کامل جدول (Full Table Scan) در ترافیک‌های بالا.',
    ep: '287',
    weight: 4
  },
  {
    id: 'chk_db_pool',
    cat: 'Database',
    title: 'ارتباط سرورلس/API با دیتابیس مجهز به Connection Pooler (مانند PgBouncer) است',
    desc: 'جلوگیری از قفل‌شدن و مرگ دیتابیس با باز شدن هزاران کانکشن همزمان سرورلس.',
    ep: '211',
    weight: 4
  },
  {
    id: 'chk_db_backup',
    cat: 'Database',
    title: 'قابلیت Point-In-Time Recovery (PITR) و بازیابی تست‌شده بک‌آپ فعال است',
    desc: 'بک‌آپی که تست بازیابی آن انجام نشده، وجود خارجی ندارد.',
    ep: '174',
    weight: 4
  },
  {
    id: 'chk_pay_webhook',
    cat: 'Payments',
    title: 'امضای وب‌هوک‌های مالی (Stripe Signature) بر روی بافر خام اعتبارسنجی می‌شود',
    desc: 'جلوگیری از تزریق تأییدیه‌های پرداخت جعلی با پی‌لودهای دستی HTTP.',
    ep: '006',
    weight: 5
  },
  {
    id: 'chk_pay_idemp',
    cat: 'Payments',
    title: 'اکشن‌های حساس و پردازش پرداخت مجهز به کلید Idempotency هستند',
    desc: 'جلوگیری از کسر شارژ مجدد در صورت ارسال چندباره درخواست یا ریتری وب‌هوک.',
    ep: '006',
    weight: 4
  },
  {
    id: 'chk_rate_limit',
    cat: 'Rate Limiting',
    title: 'اندپوینت‌های احراز هویت، جستجو و AI مجهز به محدودساز نرخ (Rate Limiter) هستند',
    desc: 'جلوگیری از DoS و فلج شدن سرور توسط یک اسکریپت ساده با ۵۰۰ درخواست در ثانیه.',
    ep: '103',
    weight: 4
  },
  {
    id: 'chk_obs_unhandled',
    cat: 'Observability',
    title: 'هندلرهای سراسری unhandledRejection و uncaughtException فعال هستند',
    desc: 'جلوگیری از کرش خاموش سرور در نیمه‌شب و ثبت لاگ خطا در Sentry.',
    ep: '205',
    weight: 4
  },
  {
    id: 'chk_obs_f12',
    cat: 'Observability',
    title: 'کنسول مرورگر F12 در محیط پروداکشن عاری از خطاهای قرمز و سورس‌مپ‌های لو رفته است',
    desc: 'پاکسازی لاگ‌های دیباگ، استک‌تریس‌های حساس و آبجکت‌های لو رفته در کلاینت.',
    ep: '295',
    weight: 3
  },
  {
    id: 'chk_deploy_env',
    cat: 'Deployments',
    title: 'محیط Staging کاملاً مجزا از پروداکشن وجود دارد و هیچ کدی مستقیماً به main پوش نمی‌شود',
    desc: 'جداسازی قطعی کلیدها، دیتابیس تست و محیط ایزوله پیش از انتشار عمومی.',
    ep: '294',
    weight: 4
  },
  {
    id: 'chk_ui_states',
    cat: 'Frontend',
    title: 'تمامی کامپوننت‌های داده‌محور دارای ۴ وضعیت Loading، Error، Empty و Success هستند',
    desc: 'عدم نمایش صفحه سفید (Blank Screen) در زمان قطعی اینترنت یا خطای سرور.',
    ep: '289',
    weight: 4
  },
  {
    id: 'chk_ai_sgi',
    cat: 'AI & Legal',
    title: 'محتوای تولیدشده توسط AI طبق الزامات EU AI Act دارای برچسب و لاگ ثبت است',
    desc: 'افشای صریح اطلاعات سنتتیک (SGI) و مهار جریمه‌های حقوقی نقض حریم خصوصی.',
    ep: '001',
    weight: 4
  }
];

let checkedAuditItems = new Set();

// Master Skill Markdown for Display
const MASTER_SKILL_MD = `---
name: matt-murphy-production-engineer
description: Production-grade architectural hardening and security guardrails based on 320+ Matt Murphy production engineering principles. Prevents AI hallucinations, insecure storage, naive multi-tenancy, and unhandled production edge cases.
---

# Matt Murphy Production Engineering Guardrails

## Core Persona & Directive:
You are an uncompromising Principal Systems Architect. When generating, refactoring, or auditing code, you do NOT rely on "vibe coding" or superficial happy-path demos. You enforce the following 13 production invariants:

### 1. Authentication & Session Hygiene (Episodes 043, 044, 048, 118):
- NEVER store auth tokens, JWTs, or session identifiers in \`localStorage\` or \`sessionStorage\`. Always issue \`HttpOnly\`, \`Secure\`, \`SameSite=Lax\` cookies.
- Direct-object lookups MUST be scoped to the authenticated tenant/user (\`WHERE id = :id AND tenant_id = :tenantId\`). Never trust an ID from the URL alone (IDOR prevention).
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
- Never generate code that only handles the happy path.
- In backend runtimes, always register global \`uncaughtException\` and \`unhandledRejection\` handlers to prevent silent server deaths.
- In frontend UI, every data-driven component MUST explicitly implement: Loading State, Error State (with retry action), Empty State, and Success State.

### 6. Secrets & Client Bundle Hygiene (Episodes 105, 295):
- Never commit or expose service role keys, master DB credentials, or LLM API keys in client-side code bundles.
- Ensure production console F12 is clean of stack traces and sensitive payload dumps.
`;

// Initialize Application
document.addEventListener('DOMContentLoaded', async () => {
  setupTabs();
  setupKeyboardShortcuts();
  await loadData();
  renderCategorySelect();
  renderCategoryChips();
  renderLayersGrid();
  renderAuditChecklist();
  renderSkillSource();
  applyFilters();
});

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

function setupTabs() {
  // Attached via onclick in HTML
}

// Load data.json
async function loadData() {
  try {
    const res = await fetch('data.json');
    if (!res.ok) throw new Error('Failed to load data.json');
    rawData = await res.json();
    allEpisodes = rawData.episodes || [];
    filteredEpisodes = [...allEpisodes];
  } catch (err) {
    console.error('Error loading data:', err);
    // Fallback if data.json fails
    const grid = document.getElementById('episodes-grid');
    grid.innerHTML = `
      <div class="col-span-full p-8 text-center bg-red-950/20 border border-red-500/30 rounded-2xl">
        <p class="text-red-400 font-bold mb-2">خطا در دریافت اطلاعات دیتابیس</p>
        <p class="text-xs text-gray-400">لطفاً مطمئن شوید فایل data.json در مسیر سرور قرار دارد.</p>
      </div>
    `;
  }
}

// Render Category Dropdown
function renderCategorySelect() {
  if (!rawData || !rawData.modules) return;
  const select = document.getElementById('category-select');
  select.innerHTML = '<option value="all">تمامی حوزه‌ها (۱۲ دسته مهندسی)</option>';
  
  for (const [key, mod] of Object.entries(rawData.modules)) {
    const count = allEpisodes.filter(e => e.category === key).length;
    const opt = document.createElement('option');
    opt.value = key;
    opt.textContent = `${mod.name_fa} (${count})`;
    select.appendChild(opt);
  }
}

// Render Category Filter Chips
function renderCategoryChips() {
  if (!rawData || !rawData.modules) return;
  const container = document.getElementById('category-chips');
  container.innerHTML = '';

  const allChip = document.createElement('button');
  allChip.className = 'chip-btn px-3 py-1.5 rounded-lg border border-emerald-500 bg-emerald-500/20 text-emerald-400 font-bold transition';
  allChip.textContent = `همه (${allEpisodes.length})`;
  allChip.onclick = () => selectCategory('all');
  container.appendChild(allChip);

  for (const [key, mod] of Object.entries(rawData.modules)) {
    const count = allEpisodes.filter(e => e.category === key).length;
    const chip = document.createElement('button');
    chip.id = `chip-${key}`;
    chip.className = 'chip-btn px-3 py-1.5 rounded-lg border border-darkBorder bg-gray-900/80 text-gray-400 hover:text-white hover:border-gray-600 transition';
    chip.textContent = `${mod.name_fa} (${count})`;
    chip.onclick = () => selectCategory(key);
    container.appendChild(chip);
  }
}

function selectCategory(catId) {
  currentCategory = catId;
  const select = document.getElementById('category-select');
  if (select) select.value = catId;

  // Update chip styling
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
    // Category check
    if (currentCategory !== 'all' && ep.category !== currentCategory) {
      return false;
    }

    // Search check
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

  countEl.textContent = filteredEpisodes.length;
  filterLabel.innerHTML = `فیلتر: <span class="text-emerald-400 font-bold">${currentCategory === 'all' ? 'همه' : rawData.modules[currentCategory]?.name_fa}</span>`;

  if (filteredEpisodes.length === 0) {
    grid.innerHTML = `
      <div class="col-span-full py-16 text-center space-y-3 bg-gray-900/50 rounded-2xl border border-darkBorder">
        <div class="text-4xl">🔍</div>
        <div class="text-base font-bold text-white">هیچ موردی با این مشخصات یافت نشد</div>
        <p class="text-xs text-gray-400">عبارت جستجو را تغییر دهید یا فیلتر دسته‌بندی را روی «همه» بگذارید.</p>
      </div>
    `;
    loadMore.classList.add('hidden');
    return;
  }

  const toShow = filteredEpisodes.slice(0, displayLimit);
  grid.innerHTML = toShow.map(ep => {
    return `
      <div class="group bg-gray-900/70 hover:bg-gray-900 border border-darkBorder hover:border-emerald-500/50 rounded-2xl p-5 flex flex-col justify-between transition-all duration-200 hover:shadow-xl hover:shadow-emerald-950/20">
        <div class="space-y-3">
          <div class="flex items-center justify-between gap-2">
            <span class="font-mono text-xs font-bold px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
              #${ep.number}
            </span>
            <span class="text-[11px] px-2 py-0.5 rounded-full bg-gray-800 text-gray-300 border border-darkBorder">
              ${ep.category_name_fa}
            </span>
          </div>

          <h3 class="text-sm font-bold text-white group-hover:text-emerald-300 transition line-clamp-2 leading-snug">
            ${ep.title_fa}
          </h3>

          <p class="text-xs text-gray-400 line-clamp-3 leading-relaxed">
            ${ep.problem_fa}
          </p>
        </div>

        <div class="mt-4 pt-4 border-t border-darkBorder/60 flex items-center justify-between">
          <button onclick="openModal('${ep.number}')" class="text-xs font-bold text-emerald-400 hover:text-emerald-300 transition flex items-center gap-1">
            <span>تحلیل ریشه‌ای و کد</span>
            <span>←</span>
          </button>
          ${ep.url ? `
            <a href="${ep.url}" target="_blank" rel="noopener noreferrer" class="text-gray-500 hover:text-pink-400 transition" title="مشاهده ریلز اینستاگرام">
              <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069z"/></svg>
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

// Modal View Logic
let currentModalCode = '';

function openModal(epNum) {
  const ep = allEpisodes.find(e => e.number === epNum);
  if (!ep) return;

  document.getElementById('modal-ep-badge').textContent = `#${ep.number}`;
  document.getElementById('modal-cat-badge').textContent = ep.category_name_fa;
  document.getElementById('modal-layer-badge').textContent = `لایه ${ep.layer}`;
  document.getElementById('modal-title-fa').textContent = ep.title_fa;
  document.getElementById('modal-title-en').textContent = ep.title;
  document.getElementById('modal-problem').textContent = ep.problem_fa;
  document.getElementById('modal-root-cause').textContent = ep.root_cause_fa;

  const actionList = document.getElementById('modal-action-plan');
  actionList.innerHTML = (ep.action_plan || []).map(item => `<li>${item}</li>`).join('');

  currentModalCode = ep.code_snippet || '// No snippet available';
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
  btn.innerHTML = 'کپی شد! ✓';
  setTimeout(() => { btn.innerHTML = prev; }, 2000);
}

// Render The 13 Layers Tab
function renderLayersGrid() {
  if (!rawData || !rawData.layers) return;
  const container = document.getElementById('layers-grid');
  container.innerHTML = '';

  for (const [layerNum, info] of Object.entries(rawData.layers)) {
    const matchingCount = allEpisodes.filter(e => e.layer === parseInt(layerNum)).length;
    const card = document.createElement('div');
    card.className = 'p-6 rounded-2xl bg-gray-900/80 border border-darkBorder hover:border-emerald-500/50 transition cursor-pointer space-y-3';
    card.onclick = () => {
      // Switch to explorer and filter
      switchTab('explorer');
      currentSearch = '';
      document.getElementById('search-input').value = '';
      filteredEpisodes = allEpisodes.filter(e => e.layer === parseInt(layerNum));
      displayLimit = 30;
      renderEpisodesGrid();
      document.getElementById('active-filter-label').innerHTML = `فیلتر لایه: <span class="text-emerald-400 font-bold">لایه ${layerNum} (${info.name})</span>`;
    };

    card.innerHTML = `
      <div class="flex items-center justify-between">
        <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-gray-800 text-emerald-400 border border-darkBorder">Layer ${layerNum}</span>
        <span class="text-xs text-gray-500">${matchingCount} درس</span>
      </div>
      <h3 class="text-base font-bold text-white">${info.name}</h3>
      <p class="text-xs text-gray-400 leading-relaxed">${info.desc}</p>
      <div class="text-[11px] font-bold text-emerald-400 flex items-center gap-1 pt-2">
        <span>مشاهده درس‌های این لایه</span>
        <span>←</span>
      </div>
    `;
    container.appendChild(card);
  }
}

// Render Audit Checklist Tab
function renderAuditChecklist() {
  const container = document.getElementById('audit-checklist-container');
  container.innerHTML = '';

  AUDIT_CHECKPOINTS.forEach((chk, index) => {
    const item = document.createElement('div');
    item.className = 'p-5 rounded-2xl bg-gray-900/80 border border-darkBorder flex items-start gap-4 transition hover:border-gray-700';
    
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
            ${chk.title}
          </label>
          <span class="text-[10px] px-2 py-0.5 rounded bg-gray-800 text-gray-400 border border-darkBorder">${chk.cat}</span>
        </div>
        <p class="text-xs text-gray-400 leading-relaxed">${chk.desc}</p>
        <div class="pt-1">
          <button onclick="openModal('${chk.ep}')" class="text-[11px] font-semibold text-emerald-400 hover:underline flex items-center gap-1">
            <span>مرجع درس مت مورفی (#${chk.ep})</span>
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
      statusEl.textContent = '🌟 سیستم ۱۰۰٪ سخت‌سازی شده و آماده پروداکشن!';
      statusEl.className = 'text-xs font-bold text-emerald-400';
    } else if (pct >= 70) {
      statusEl.textContent = '⚡ وضعیت مطلوب - چند مورد آسیب‌پذیری نیازمند رفع';
      statusEl.className = 'text-xs font-bold text-yellow-400';
    } else if (pct >= 40) {
      statusEl.textContent = '⚠️ سیستم شکننده و آسیب‌پذیر در برابر ترافیک و حملات';
      statusEl.className = 'text-xs font-bold text-orange-400';
    } else {
      statusEl.textContent = '🚨 وضعیت وایب‌کدینگ - ریسک بسیار بالا در محیط پروداکشن';
      statusEl.className = 'text-xs font-bold text-red-400';
    }
  }
}

function exportAuditReport() {
  const checkedCount = checkedAuditItems.size;
  const total = AUDIT_CHECKPOINTS.length;
  const pct = Math.round((checkedCount / total) * 100);

  let md = `# گزارش ممیزی پایداری و امنیت نرم‌افزار در پروداکشن\n`;
  md += `> **تاریخ ارزیابی:** ${new Date().toLocaleDateString('fa-IR')} | **امتیاز کسب‌شده:** ${pct}%\n\n`;
  md += `## چک‌لیست موارد بررسی‌شده:\n\n`;

  AUDIT_CHECKPOINTS.forEach(chk => {
    const isPassed = checkedAuditItems.has(chk.id);
    md += `- [${isPassed ? 'x' : ' '}] **${chk.title}** (مرجع درس مت مورفی: #${chk.ep})\n`;
    if (!isPassed) {
      md += `  - ⚠️ *اقدام فوری:* عدم رعایت این مورد سیستم را در معرض خطر قرار می‌دهد. به درس #${chk.ep} مراجعه نمایید.\n`;
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

// Render Master Skill
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
  btn.innerHTML = 'کپی شد! ✓';
  setTimeout(() => { btn.innerHTML = prev; }, 2000);
}
