#!/usr/bin/env python3
"""
Syncs the true enterprise SKILL.md into app.js and site/app.js,
and adds cache-busting query strings to all assets.
"""

import os
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_MD_PATH = os.path.join(ROOT_DIR, 'skills', 'matt-murphy-production-engineer', 'SKILL.md')
APP_JS_PATH = os.path.join(ROOT_DIR, 'app.js')
SITE_APP_JS_PATH = os.path.join(ROOT_DIR, 'site', 'app.js')
INDEX_HTML_PATH = os.path.join(ROOT_DIR, 'index.html')
SITE_INDEX_HTML_PATH = os.path.join(ROOT_DIR, 'site', 'index.html')

VERSION = "3.2.1"

with open(SKILL_MD_PATH, 'r', encoding='utf-8') as f:
    skill_content = f.read()

# Escape backticks and ${} for JS template literal
escaped_skill = skill_content.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

js_replacement = f"const MASTER_SKILL_MD = `{escaped_skill}`;"

for p in [APP_JS_PATH, SITE_APP_JS_PATH]:
    with open(p, 'r', encoding='utf-8') as f:
        js = f.read()
    
    # Replace MASTER_SKILL_MD
    js = re.sub(r'const MASTER_SKILL_MD = `[\s\S]*?`;', js_replacement, js, count=1)
    
    # Cache-bust fetch('data.json')
    js = re.sub(r"fetch\('data\.json[^']*'\)", f"fetch('data.json?v={VERSION}')", js)
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f"Updated {p} with full SKILL.md and cache-buster v={VERSION}")

# Update HTML files with cache-busting
for hp in [INDEX_HTML_PATH, SITE_INDEX_HTML_PATH]:
    if not os.path.exists(hp):
        continue
    with open(hp, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = re.sub(r'src="app\.js[^"]*"', f'src="app.js?v={VERSION}"', html)
    
    with open(hp, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {hp} with script src=app.js?v={VERSION}")

print("Sync completed!")
