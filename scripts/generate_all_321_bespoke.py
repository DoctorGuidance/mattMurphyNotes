#!/usr/bin/env python3
"""
Master Synthesizer and Validator for all 321 Matt Murphy Masterclasses.
Merges PART1_DATA and PART2_DATA, verifies 100% uniqueness and zero templated copy-pasting,
updates data.json and site/data.json, updates docs tables, and rebuilds the enterprise skill.
"""

import json
import os
import re
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT_DIR, 'data.json')
SITE_DATA_PATH = os.path.join(ROOT_DIR, 'site', 'data.json')

from bespoke_data_part1 import PART1_DATA
from bespoke_data_part2 import PART2_DATA

def main():
    print("🚀 Merging Part 1 and Part 2 bespoke datasets...")
    all_bespoke = {}
    all_bespoke.update(PART1_DATA)
    all_bespoke.update(PART2_DATA)

    print(f"📊 Total bespoke definitions loaded: {len(all_bespoke)}")

    # Load data.json
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    episodes = data['episodes']
    ep_numbers = [e['number'] for e in episodes]
    assert len(episodes) == 321, f"Expected 321 episodes in data.json, found {len(episodes)}"

    # Check key coverage
    missing = set(ep_numbers) - set(all_bespoke.keys())
    assert not missing, f"Missing bespoke entries for episodes: {missing}"
    extra = set(all_bespoke.keys()) - set(ep_numbers)
    assert not extra, f"Extra bespoke entries not in data.json: {extra}"

    print("✅ All 321 episode keys match data.json perfectly!")

    # Uniqueness assertions
    m_en_list = [all_bespoke[num][0] for num in ep_numbers]
    p_en_list = [all_bespoke[num][1] for num in ep_numbers]
    m_fa_list = [all_bespoke[num][2] for num in ep_numbers]
    p_fa_list = [all_bespoke[num][3] for num in ep_numbers]

    print(f"🔍 Validating uniqueness across {len(episodes)} masterclasses:")
    print(f"  - Unique table_mistake_en:     {len(set(m_en_list))} / 321")
    print(f"  - Unique table_production_en:  {len(set(p_en_list))} / 321")
    print(f"  - Unique table_mistake_fa:     {len(set(m_fa_list))} / 321")
    print(f"  - Unique table_production_fa:  {len(set(p_fa_list))} / 321")

    assert len(set(m_en_list)) == 321, f"Duplicate table_mistake_en found! Duplicates: {[x for x in m_en_list if m_en_list.count(x) > 1]}"
    assert len(set(p_en_list)) == 321, f"Duplicate table_production_en found! Duplicates: {[x for x in p_en_list if p_en_list.count(x) > 1]}"
    assert len(set(m_fa_list)) == 321, f"Duplicate table_mistake_fa found! Duplicates: {[x for x in m_fa_list if m_fa_list.count(x) > 1]}"
    assert len(set(p_fa_list)) == 321, f"Duplicate table_production_fa found! Duplicates: {[x for x in p_fa_list if p_fa_list.count(x) > 1]}"

    # Check for forbidden templated substrings
    for idx, (num, (m_en, p_en, m_fa, p_fa)) in enumerate(all_bespoke.items()):
        assert "Automates CI/CD staging verification" not in p_en, f"Templated string found in #{num} p_en"
        assert "Automates CI/CD staging verification" not in m_en, f"Templated string found in #{num} m_en"
        assert "{title" not in p_en and "{title" not in m_en, f"Template variable found in #{num}"
        assert "{title" not in p_fa and "{title" not in m_fa, f"Template variable found in #{num} FA"

    print("🛡️ All template repetition checks PASSED! Zero templated copy-pasting detected.")

    # Apply updates to episodes in data.json
    for ep in episodes:
        num = ep['number']
        m_en, p_en, m_fa, p_fa = all_bespoke[num]
        ep['table_mistake_en'] = m_en
        ep['table_production_en'] = p_en
        ep['table_mistake_fa'] = m_fa
        ep['table_production_fa'] = p_fa
        ep['is_pilot_gold'] = True

    # Save data.json
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("💾 Saved updated data.json")

    # Save site/data.json
    os.makedirs(os.path.dirname(SITE_DATA_PATH), exist_ok=True)
    with open(SITE_DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("💾 Saved updated site/data.json")

    # Update docs tables
    print("\n📝 Updating docs/*/*.md comparison tables...")
    subprocess.run([sys.executable, os.path.join(ROOT_DIR, 'scripts', 'update_docs_tables.py')], check=True)

    # Rebuild enterprise skill and references
    print("\n🛠️ Rebuilding enterprise skill rulebooks and anti-vibe-traps.md...")
    subprocess.run([sys.executable, os.path.join(ROOT_DIR, 'scripts', 'build_enterprise_skill.py')], check=True)

    print("\n🎉 MASTER SYNTHESIS & REBUILD COMPLETED SUCCESSFULLY!")

if __name__ == '__main__':
    main()
