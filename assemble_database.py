# -*- coding: utf-8 -*-
import json
import os
import re

def clean_text(text):
    if not text:
        return ""
    text = text.replace('\xa0', ' ').replace('\u3000', ' ')
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def build_exams_database():
    astr_data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
    astr_answers = json.load(open('temp_astrbot/CET6_Answer.json', 'r', encoding='utf-8'))

    with open('temp_sikefix/public/lessons-data.js', 'r', encoding='utf-8') as f:
        c = f.read()
    start = c.find('[')
    end = c.rfind(']') + 1
    sike_data = json.loads(c[start:end])
    sike_map = {item['id']: item for item in sike_data}

    # Helper functions
    from process_all_readings import parse_section_a, parse_section_b, parse_section_c

    exams = {}

    # 1. Process Astrbot 2018 - 2021
    for item in astr_data:
        meta = item.get('meta', {})
        yr = meta.get('year')
        mo = meta.get('month', '6')
        st = meta.get('set_index', '1')
        t = item.get('type')
        
        if yr not in ['2018', '2019', '2020', '2021']:
            continue
            
        # Clean month and set
        mo_str = "12" if mo == "12" else ("06" if mo == "6" else ("09" if "9" in str(mo) else ("07" if "7" in str(mo) else "06")))
        st_num = str(st) if str(st).isdigit() else "1"
        exam_id = f"{yr}_{mo_str}_set{st_num}"

        if exam_id not in exams:
            exams[exam_id] = {
                "id": exam_id,
                "year": yr,
                "month": mo_str,
                "set": f"第{st_num}套",
                "title": f"{yr}年{int(mo_str)}月 六级阅读真题 (第{st_num}套)",
                "section_a": None,
                "section_b": None,
                "section_c1": None,
                "section_c2": None,
            }
            
        ans_key = f"{yr}_{mo_str}_{st_num}"
        ans_obj = astr_answers.get(ans_key, {}).get('answers', {})
        content = item.get('content', '')
        
        if t == 'Section A':
            ans_str = ans_obj.get('Section A', '')
            parsed = parse_section_a(content, ans_str)
            if parsed and len(parsed['word_bank']) >= 10:
                exams[exam_id]['section_a'] = parsed
        elif t == 'Section B':
            ans_str = ans_obj.get('Section B', '')
            parsed = parse_section_b(content, ans_str)
            if parsed and len(parsed['paragraphs']) >= 5:
                exams[exam_id]['section_b'] = parsed
        elif t == 'Section C - Passage 1':
            ans_str = ans_obj.get('Section C1', '')
            sike_id = f"cet6_{yr}_{mo_str}_{st_num}-p1"
            sike_item = sike_map.get(sike_id)
            parsed = parse_section_c(content, ans_str, sike_item)
            if parsed and len(parsed['questions']) == 5:
                exams[exam_id]['section_c1'] = parsed
        elif t == 'Section C - Passage 2':
            ans_str = ans_obj.get('Section C2', '')
            sike_id = f"cet6_{yr}_{mo_str}_{st_num}-p2"
            sike_item = sike_map.get(sike_id)
            parsed = parse_section_c(content, ans_str, sike_item)
            if parsed and len(parsed['questions']) == 5:
                exams[exam_id]['section_c2'] = parsed

    print(f"Base exams count from Astrbot: {len(exams)}")
    return exams

if __name__ == '__main__':
    res = build_exams_database()
    print("Keys:", sorted(res.keys()))
