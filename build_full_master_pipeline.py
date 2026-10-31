# -*- coding: utf-8 -*-
import json, re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

from test_recent_pipeline import build_recent_exams
from make_2021_2024_curated import get_2021_2024_curated_sets
from test_combine_all_24 import get_all_24_clean_exams
from process_all_readings import clean_text, parse_section_a, parse_section_b, parse_section_c

def get_all_exams_master():
    # 1. Base archive (2014 - 2021, 24 exams)
    base_24 = get_all_24_clean_exams()
    all_dict = {ex['id']: ex for ex in base_24}
    
    # 2. Add 2022 - 2024 recent exams from Astrbot
    astr_data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
    astr_answers = json.load(open('temp_astrbot/CET6_Answer.json', 'r', encoding='utf-8'))
    
    with open('temp_sikefix/public/lessons-data.js', 'r', encoding='utf-8') as f:
        c = f.read()
    sike_data = json.loads(c[c.find('['):c.rfind(']')+1])
    sike_map = {item['id']: item for item in sike_data}
    
    recent_astr = build_recent_exams()
    for eid, ex in recent_astr.items():
        all_dict[eid] = ex
        
    # 3. Add 2022_06_set2
    ans_a = astr_answers.get('2022_06_2', {}).get('answers', {}).get('Section A', '')
    ans_b = astr_answers.get('2022_06_2', {}).get('answers', {}).get('Section B', '')
    sec_a, sec_b = None, None
    for it in astr_data:
        meta = it.get('meta', {})
        fn = meta.get('filename', '')
        if '2022年6月英语六级真题 第二套' in fn:
            if it.get('type') == 'Section A':
                sec_a = parse_section_a(it.get('content', ''), ans_a)
            elif it.get('type') == 'Section B':
                sec_b = parse_section_b(it.get('content', ''), ans_b)
                
    sike_p1 = sike_map.get('cet6_2022_06_2-p1', {})
    sike_p2 = sike_map.get('cet6_2022_06_2-p2', {})
    
    # Load authentic passages for 2022_06_set2 from Astrbot 第一套
    p1_content, p2_content = "", ""
    for it in astr_data:
        meta = it.get('meta', {})
        fn = meta.get('filename', '')
        if '2022年6月英语六级真题第一套' in fn:
            if 'Passage 1' in it.get('type'):
                p1_content = it.get('content', '')
            elif 'Passage 2' in it.get('type'):
                p2_content = it.get('content', '')

    from process_all_readings import parse_section_c
    parsed_c1 = parse_section_c(p1_content, "BAADB", sike_p1)
    parsed_c2 = parse_section_c(p2_content, "BCDCD", sike_p2)
        
    if sec_a and sec_b and sike_p1 and sike_p2:
        all_dict['2022_06_set2'] = {
            "id": "2022_06_set2",
            "year": "2022",
            "month": "06",
            "set": "第2套",
            "title": "2022年6月 六级阅读真题 (第2套)",
            "theme": "精英大学价值质疑 / 气候变化与常识偏见",
            "section_a": sec_a,
            "section_b": sec_b,
            "section_c1": parsed_c1,
            "section_c2": parsed_c2
        }
        
    # 4. Add curated 2024.12, 2023.12, 2022.12
    curated_recent = get_2021_2024_curated_sets(sike_map)
    for c in curated_recent:
        all_dict[c['id']] = c
        
    master_list = list(all_dict.values())
    
    def master_sort_key(ex):
        y = int(ex.get('year', 0))
        m = int(ex.get('month', 0)) if str(ex.get('month', 0)).isdigit() else 0
        s = ex.get('set', '')
        return (-y, -m, s)
        
    master_list.sort(key=master_sort_key)
    return master_list

if __name__ == '__main__':
    all_ex = get_all_exams_master()
    print(f"\n==========================================")
    print(f"Total compiled master exams: {len(all_ex)}")
    print(f"==========================================")
    
    years_count = {}
    for ex in all_ex:
        yr = ex['year']
        years_count[yr] = years_count.get(yr, 0) + 1
        
    print("Yearly distribution:")
    for yr in sorted(years_count.keys(), reverse=True):
        print(f"  {yr}: {years_count[yr]} sets")
        
    # Check 2021-2024 specifically
    recent = [ex for ex in all_ex if int(ex['year']) >= 2021]
    print(f"\n2021-2024 Focus Sets Count: {len(recent)}")
    for ex in recent:
        eid = ex['id']
        sa = ex['section_a']
        sb = ex['section_b']
        sc1 = ex['section_c1']
        sc2 = ex['section_c2']
        sa_w = len(sa.get('word_bank', {}))
        sa_q = len(sa.get('questions', []))
        sb_p = len(sb.get('paragraphs', []))
        sb_q = len(sb.get('questions', []))
        sc1_q = len(sc1.get('questions', []))
        sc2_q = len(sc2.get('questions', []))
        print(f"  [★] {eid:18s} | {ex['title']} | A({sa_w},{sa_q}) B({sb_p},{sb_q}) C1({sc1_q}) C2({sc2_q})")
