import json
import re
from process_all_readings import parse_section_a, parse_section_b, parse_section_c

astr_data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
astr_answers = json.load(open('temp_astrbot/CET6_Answer.json', 'r', encoding='utf-8'))

with open('temp_sikefix/public/lessons-data.js', 'r', encoding='utf-8') as f:
    c = f.read()
start = c.find('[')
end = c.rfind(']') + 1
sike_data = json.loads(c[start:end])
sike_map = {item['id']: item for item in sike_data}

exams = {}

for item in astr_data:
    meta = item.get('meta', {})
    yr = meta.get('year')
    mo = meta.get('month', '6')
    st = meta.get('set_index', '1')
    t = item.get('type')
    
    # We focus on 2018-2021
    if yr not in ['2018', '2019', '2020', '2021']:
        continue
        
    mo_num = f"{int(mo):02d}" if str(mo).isdigit() else str(mo)
    exam_id = f"{yr}_{mo_num}_set{st}"
    if exam_id not in exams:
        exams[exam_id] = {
            "year": yr,
            "month": mo_num,
            "set": f"第{st}套",
            "title": f"{yr}年{mo}月六级真题 (第{st}套)",
            "section_a": None,
            "section_b": None,
            "section_c1": None,
            "section_c2": None,
        }
        
    ans_key = f"{yr}_{mo_num}_{st}"
    ans_obj = astr_answers.get(ans_key, {}).get('answers', {})
    content = item.get('content', '')
    
    if t == 'Section A':
        ans_str = ans_obj.get('Section A', '')
        parsed = parse_section_a(content, ans_str)
        exams[exam_id]['section_a'] = parsed
    elif t == 'Section B':
        ans_str = ans_obj.get('Section B', '')
        parsed = parse_section_b(content, ans_str)
        exams[exam_id]['section_b'] = parsed
    elif t == 'Section C - Passage 1':
        ans_str = ans_obj.get('Section C1', '')
        sike_id = f"cet6_{yr}_{mo_num}_{st}-p1"
        sike_item = sike_map.get(sike_id)
        parsed = parse_section_c(content, ans_str, sike_item)
        exams[exam_id]['section_c1'] = parsed
    elif t == 'Section C - Passage 2':
        ans_str = ans_obj.get('Section C2', '')
        sike_id = f"cet6_{yr}_{mo_num}_{st}-p2"
        sike_item = sike_map.get(sike_id)
        parsed = parse_section_c(content, ans_str, sike_item)
        exams[exam_id]['section_c2'] = parsed

print(f"Total parsed exam sets (2018-2021): {len(exams)}")
for eid, ex in sorted(exams.items()):
    sec_a_ok = ex['section_a'] is not None and len(ex['section_a']['questions']) == 10
    sec_b_ok = ex['section_b'] is not None and len(ex['section_b']['questions']) == 10
    sec_c1_ok = ex['section_c1'] is not None and len(ex['section_c1']['questions']) == 5
    sec_c2_ok = ex['section_c2'] is not None and len(ex['section_c2']['questions']) == 5
    print(f"  {eid:16s} | Sec A: {sec_a_ok} (wb: {len(ex['section_a']['word_bank']) if ex['section_a'] else 0}) | Sec B: {sec_b_ok} (paras: {len(ex['section_b']['paragraphs']) if ex['section_b'] else 0}) | Sec C1: {sec_c1_ok} | Sec C2: {sec_c2_ok}")
