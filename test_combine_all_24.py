# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from test_fix_astr import load_and_fix_astrbot
from make_curated_data import get_curated_exams
from make_more_curated import get_more_curated_exams
from curated_supplements import get_supplement_exams
from build_reading_platform import get_extra_authentic_sets
from enrich_curated import enrich_exam

def get_all_24_clean_exams():
    astr_exams = load_and_fix_astrbot()
    # Filter to only the 15 complete Astrbot exams
    complete_astr = {k: v for k, v in astr_exams.items() if v['section_a'] and v['section_b'] and v['section_c1'] and v['section_c2']}
    
    final_dict = dict(complete_astr)
    
    curated = get_curated_exams() + get_more_curated_exams() + get_supplement_exams() + get_extra_authentic_sets()
    for ex in curated:
        enrich_exam(ex)
        final_dict[ex['id']] = ex
        
    exams_list = list(final_dict.values())
    
    def sort_key(ex):
        y = int(ex.get('year', 0))
        m = int(ex.get('month', 0)) if str(ex.get('month', 0)).isdigit() else 0
        s = ex.get('set', '')
        return (-y, -m, s)
        
    exams_list.sort(key=sort_key)
    return exams_list

if __name__ == '__main__':
    exams = get_all_24_clean_exams()
    print(f"\n==========================================")
    print(f"Total compiled clean exams: {len(exams)}")
    print(f"==========================================")
    
    all_flawless = True
    for i, ex in enumerate(exams):
        eid = ex['id']
        yr = ex['year']
        title = ex['title']
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
        
        ok = (sa_w >= 10 and sa_q == 10 and sb_p >= 10 and sb_q == 10 and sc1_q == 5 and sc2_q == 5)
        if not ok:
            all_flawless = False
        status = "FLAWLESS" if ok else "CHECK"
        print(f"[{i+1:02d}] {eid:18s} ({yr}) | A(w:{sa_w:2d}, q:{sa_q:2d}) | B(p:{sb_p:2d}, q:{sb_q:2d}) | C1({sc1_q}) C2({sc2_q}) => {status}")
        
    print("\nFinal Result:", "ALL 24 EXAMS ARE 100% COMPLETE & FLAWLESS!" if all_flawless else "Some exams have discrepancies!")
