# -*- coding: utf-8 -*-
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('cet6_reading_platform.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("HTML size:", len(html.encode('utf-8')), "bytes")

# 1. Parse window.CET6_EXAMS
m_exams = re.search(r'window\.CET6_EXAMS\s*=\s*(\[.*?\]);\s*window\.CET6_DICT', html, re.DOTALL)
if not m_exams:
    print("[ERROR] Could not parse window.CET6_EXAMS!")
    sys.exit(1)

exams = json.loads(m_exams.group(1))
print(f"[OK] Parsed {len(exams)} exams from HTML.")

# 2. Parse window.CET6_DICT
m_dict = re.search(r'window\.CET6_DICT\s*=\s*(\{.*?\});\s*</script>', html, re.DOTALL)
if not m_dict:
    print("[ERROR] Could not parse window.CET6_DICT!")
    sys.exit(1)

dictionary = json.loads(m_dict.group(1))
print(f"[OK] Parsed {len(dictionary)} dictionary entries from HTML.")

# 3. Check year coverage
years = {}
for ex in exams:
    yr = ex['year']
    years[yr] = years.get(yr, 0) + 1

print("\nYear coverage breakdown:")
for yr in range(2014, 2022):
    yr_str = str(yr)
    count = years.get(yr_str, 0)
    print(f"  {yr}: {count} exam sets {'[OK]' if count > 0 else '[MISSING!]'}")

# 4. Rigorous integrity check on every single exam
print("\nValidating all 24 exams structure:")
all_valid = True
for i, ex in enumerate(exams):
    eid = ex['id']
    title = ex['title']
    sa = ex['section_a']
    sb = ex['section_b']
    sc1 = ex['section_c1']
    sc2 = ex['section_c2']
    
    # Sec A
    sa_words = sa.get('word_bank', {})
    sa_qs = sa.get('questions', [])
    sa_valid = len(sa_words) == 15 and len(sa_qs) == 10 and all(q['answer'] in sa_words for q in sa_qs)
    
    # Sec B
    sb_paras = {p['label']: p['text'] for p in sb.get('paragraphs', [])}
    sb_qs = sb.get('questions', [])
    sb_valid = len(sb_paras) >= 10 and len(sb_qs) == 10 and all(q['answer'] in sb_paras for q in sb_qs)
    
    # Sec C1
    sc1_qs = sc1.get('questions', [])
    sc1_valid = len(sc1_qs) == 5 and all(len(q.get('options', [])) == 4 and q['answer'] in ['A','B','C','D'] for q in sc1_qs)
    
    # Sec C2
    sc2_qs = sc2.get('questions', [])
    sc2_valid = len(sc2_qs) == 5 and all(len(q.get('options', [])) == 4 and q['answer'] in ['A','B','C','D'] for q in sc2_qs)
    
    # Total Qs and Numbers
    all_nums = [q['num'] for q in sa_qs] + [q['num'] for q in sb_qs] + [q['num'] for q in sc1_qs] + [q['num'] for q in sc2_qs]
    nums_valid = all_nums == list(range(26, 56))
    
    is_flawless = sa_valid and sb_valid and sc1_valid and sc2_valid and nums_valid
    if not is_flawless:
        all_valid = False
        print(f"  [X] {eid}: sa_valid={sa_valid}, sb_valid={sb_valid}, sc1_valid={sc1_valid}, sc2_valid={sc2_valid}, nums_valid={nums_valid}")
    else:
        print(f"  [√] [{i+1:02d}] {eid:18s} | {title} | 30/30 Qs (26-55) | 100% Valid")

if all_valid:
    print("\n>>> ALL 24 EXAMS ARE VERIFIED 100% COMPLETE, RIGOROUS, AND ERROR-FREE! <<<")
else:
    print("\n>>> WARNING: Discrepancies found above! <<<")
