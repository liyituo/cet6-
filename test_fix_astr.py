# -*- coding: utf-8 -*-
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

from process_all_readings import clean_text, parse_section_a, parse_section_b, parse_section_c

def load_and_fix_astrbot():
    astr_data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
    astr_answers = json.load(open('temp_astrbot/CET6_Answer.json', 'r', encoding='utf-8'))

    with open('temp_sikefix/public/lessons-data.js', 'r', encoding='utf-8') as f:
        c = f.read()
    sike_data = json.loads(c[c.find('['):c.rfind(']')+1])
    sike_map = {item['id']: item for item in sike_data}

    # Group Astrbot items by exam key
    exams = {}

    for item in astr_data:
        meta = item.get('meta', {})
        yr = meta.get('year')
        mo = meta.get('month', '')
        st = meta.get('set_index', '1')
        fn = meta.get('filename', '')
        t = item.get('type')

        if yr not in ['2018', '2019', '2020', '2021']:
            continue

        # Determine month
        if '12' in mo or '12月' in fn:
            mo_str = '12'
        elif '07' in fn or '7月' in fn:
            mo_str = '07'
        elif '09' in fn or '9月' in fn:
            mo_str = '09'
        else:
            mo_str = '06'

        # Determine set index
        if '第二套' in fn or '第2套' in fn:
            st_num = '2'
        elif '第三套' in fn or '第3套' in fn:
            st_num = '3'
        elif '第一套' in fn or '第1套' in fn:
            st_num = '1'
        else:
            st_num = str(st) if str(st).isdigit() else '1'

        exam_id = f"{yr}_{mo_str}_set{st_num}"

        if exam_id not in exams:
            exams[exam_id] = {
                "id": exam_id,
                "year": yr,
                "month": mo_str,
                "set": f"第{st_num}套",
                "title": f"{yr}年{int(mo_str)}月 阅读 (第{st_num}套)",
                "theme": "真题阅读",
                "section_a": None,
                "section_b": None,
                "section_c1": None,
                "section_c2": None,
            }

        ans_key = f"{yr}_{mo_str}_{st_num}"
        ans_obj = astr_answers.get(ans_key, {}).get('answers', {})
        content = item.get('content', '')

        # Fix OCR quirks in content
        content = re.sub(r'(?:^|\n)\s*3[Bb]\.\s*', '\n36. ', content)
        content = re.sub(r'(?:^|\n)\s*SS\.\s*', '\n55. ', content)
        content = re.sub(r'Questions 51 to SS', 'Questions 51 to 55', content)

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
            elif sike_item and sike_item.get('questions'):
                # Fallback to Sikefix questions directly
                parsed_c = {
                    "passage": parsed['passage'] if parsed else content[:1500],
                    "main_idea_zh": sike_item.get('mainIdeaZh', ''),
                    "main_idea_en": sike_item.get('mainIdeaEn', ''),
                    "questions": [{
                        "num": int(q['number']),
                        "stem": q['stem'],
                        "options": q['options'],
                        "answer": q['answer'],
                        "question_zh": q.get('questionZh', ''),
                        "answer_zh": q.get('answerZh', ''),
                        "explanation": q.get('explanation', '')
                    } for q in sike_item['questions']]
                }
                exams[exam_id]['section_c1'] = parsed_c
        elif t == 'Section C - Passage 2':
            ans_str = ans_obj.get('Section C2', '')
            sike_id = f"cet6_{yr}_{mo_str}_{st_num}-p2"
            sike_item = sike_map.get(sike_id)
            parsed = parse_section_c(content, ans_str, sike_item)
            if parsed and len(parsed['questions']) == 5:
                exams[exam_id]['section_c2'] = parsed
            elif sike_item and sike_item.get('questions'):
                parsed_c = {
                    "passage": parsed['passage'] if parsed else content[:1500],
                    "main_idea_zh": sike_item.get('mainIdeaZh', ''),
                    "main_idea_en": sike_item.get('mainIdeaEn', ''),
                    "questions": [{
                        "num": int(q['number']),
                        "stem": q['stem'],
                        "options": q['options'],
                        "answer": q['answer'],
                        "question_zh": q.get('questionZh', ''),
                        "answer_zh": q.get('answerZh', ''),
                        "explanation": q.get('explanation', '')
                    } for q in sike_item['questions']]
                }
                exams[exam_id]['section_c2'] = parsed_c

    print(f"Loaded {len(exams)} total exam slots.")
    complete = []
    incomplete = []
    for eid, ex in exams.items():
        if ex['section_a'] and ex['section_b'] and ex['section_c1'] and ex['section_c2']:
            complete.append(eid)
        else:
            missing = [k for k in ['section_a', 'section_b', 'section_c1', 'section_c2'] if not ex[k]]
            incomplete.append((eid, missing))

    print(f"Complete exams count: {len(complete)}")
    for c in sorted(complete):
        print(f"  [OK] {c}")
    print(f"Incomplete exams count: {len(incomplete)}")
    for inc, m in sorted(incomplete):
        print(f"  [MISSING] {inc}: {m}")

    return exams

if __name__ == '__main__':
    load_and_fix_astrbot()
