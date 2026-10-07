#!/usr/bin/env python3
import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT_DIR, 'data.json')
DOCS_DIR = os.path.join(ROOT_DIR, 'docs')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

ep_map = {e['number']: e for e in data['episodes']}

doc_files = []
for root, dirs, files in os.walk(DOCS_DIR):
    for f in files:
        if f.endswith('.md') and f != 'README.md':
            doc_files.append(os.path.join(root, f))

updated = 0
for dp in doc_files:
    fname = os.path.basename(dp)
    m = re.match(r'^(\d{3})_', fname)
    if not m:
        continue
    num = m.group(1)
    if num in ep_map:
        ep = ep_map[num]
        with open(dp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the table row under ## ❌ 2. Vibe-Coding Trap vs. Production Reality
        pattern = r'(## ❌ 2\. Vibe-Coding Trap vs\. Production Reality\s*\n\s*\|[^\n]+\|\s*\n\s*\|[^\n]+\|\s*\n\s*\|)[^\|]+(\|)[^\|\n]+(\|)'
        m_en = ep['table_mistake_en'].replace('|', '\\|')
        p_en = ep['table_production_en'].replace('|', '\\|')
        new_row = f"\\1 {m_en} \\2 {p_en} \\3"
        new_content, count = re.subn(pattern, new_row, content)
        if count > 0:
            with open(dp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated += 1

print(f"Updated {updated} / {len(doc_files)} docs files with bespoke comparison tables!")
