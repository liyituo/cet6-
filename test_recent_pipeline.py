# -*- coding: utf-8 -*-
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

astr_data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
astr_answers = json.load(open('temp_astrbot/CET6_Answer.json', 'r', encoding='utf-8'))

with open('temp_sikefix/public/lessons-data.js', 'r', encoding='utf-8') as f:
    c = f.read()
sike_data = json.loads(c[c.find('['):c.rfind(']')+1])
sike_map = {item['id']: item for item in sike_data}

from process_all_readings import clean_text, parse_section_a, parse_section_b, parse_section_c

def build_recent_exams():
    exams = {}
    
    # 1. 2024.06 Set 1
    # 2. 2024.06 Set 2
    # 3. 2023.06 Set 1
    # 4. 2023.03 Set 1
    # 5. 2022.06 Set 1
    # 6. 2021.06 Set 1
    # 7. 2021.06 Set 3
    
    for item in astr_data:
        meta = item.get('meta', {})
        yr = str(meta.get('year'))
        fn = meta.get('filename', '')
        t = item.get('type')
        c = item.get('content', '')
        
        # Identify exam ID
        eid = None
        ans_key = None
        sike_prefix = None
        title = None
        
        if '2024年6月第1套' in fn:
            eid = '2024_06_set1'
            ans_key = '2024_06_1'
            sike_prefix = 'cet6_2024_06_1'
            title = '2024年6月 六级阅读真题 (第1套)'
            theme = '音乐情绪认知 / 自主产权树 / 职场安全沟通'
        elif '2024年6月第2套' in fn:
            eid = '2024_06_set2'
            ans_key = '2024_06_2'
            sike_prefix = 'cet6_2024_06_2'
            title = '2024年6月 六级阅读真题 (第2套)'
            theme = '习惯养成障碍 / 城市绿道生态 / 数字注意力'
        elif '2023年06月' in fn:
            eid = '2023_06_set1'
            ans_key = '2023_06_1'
            sike_prefix = 'cet6_2023_06_1'
            title = '2023年6月 六级阅读真题 (第1套)'
            theme = '犬类智力演化 / 感恩心理力量 / 气候变化适应'
        elif '2023年03月' in fn:
            eid = '2023_03_set1'
            ans_key = '2023_06_1' # Astrbot stored 2023_03 under 2023_06 or answers
            sike_prefix = 'cet6_2023_03_1'
            title = '2023年3月 六级阅读真题 (第1套)'
            theme = '人类终极灭绝风险 / 旧金山贫富分化 / 认知科学'
        elif '2022年06月六级真题全3套' in fn:
            eid = '2022_06_set1'
            ans_key = '2022_06_1'
            sike_prefix = 'cet6_2022_06_1'
            title = '2022年6月 六级阅读真题 (第1套)'
            theme = '巴斯罗马温泉 / 远程医疗革命 / 科学数据共享'
        elif '2021.06六级真题第1套' in fn:
            eid = '2021_06_set1'
            ans_key = '2021_06_1'
            sike_prefix = 'cet6_2021_06_1'
            title = '2021年6月 六级阅读真题 (第1套)'
            theme = '热量守恒与减肥 / 马可尼与无线电争议 / 旅游税'
        elif '2021.06六级真题第3套' in fn:
            eid = '2021_06_set3'
            ans_key = '2021_06_3'
            sike_prefix = 'cet6_2021_06_3'
            title = '2021年6月 六级阅读真题 (第3套)'
            theme = '学校创意教育 / CGI虚拟数字人伦理 / 算法伦理'
            
        if not eid:
            continue
            
        if eid not in exams:
            parts = eid.split('_')
            exams[eid] = {
                "id": eid,
                "year": parts[0],
                "month": parts[1],
                "set": f"第{parts[2].replace('set','')}套",
                "title": title,
                "theme": theme,
                "section_a": None,
                "section_b": None,
                "section_c1": None,
                "section_c2": None,
            }
            
        ans_obj = astr_answers.get(ans_key, {}).get('answers', {})
        
        # OCR fixes
        c = re.sub(r'(?:^|\n)\s*3[Bb]\.\s*', '\n36. ', c)
        c = re.sub(r'(?:^|\n)\s*SS\.\s*', '\n55. ', c)
        
        if t == 'Section A':
            ans_str = ans_obj.get('Section A', '')
            parsed = parse_section_a(c, ans_str)
            if parsed and len(parsed['word_bank']) >= 10:
                exams[eid]['section_a'] = parsed
        elif t == 'Section B':
            ans_str = ans_obj.get('Section B', '')
            parsed = parse_section_b(c, ans_str)
            if parsed and len(parsed['paragraphs']) >= 10:
                exams[eid]['section_b'] = parsed
        elif t == 'Section C - Passage 1':
            ans_str = ans_obj.get('Section C1', '')
            sike_item = sike_map.get(f"{sike_prefix}-p1")
            parsed = parse_section_c(c, ans_str, sike_item)
            if parsed and len(parsed['questions']) == 5:
                exams[eid]['section_c1'] = parsed
            elif sike_item:
                parsed_c = {
                    "passage": parsed['passage'] if parsed else c[:1500],
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
                exams[eid]['section_c1'] = parsed_c
        elif t == 'Section C - Passage 2':
            ans_str = ans_obj.get('Section C2', '')
            sike_item = sike_map.get(f"{sike_prefix}-p2")
            parsed = parse_section_c(c, ans_str, sike_item)
            if parsed and len(parsed['questions']) == 5:
                exams[eid]['section_c2'] = parsed
            elif sike_item:
                parsed_c = {
                    "passage": parsed['passage'] if parsed else c[:1500],
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
                exams[eid]['section_c2'] = parsed_c
                
    for eid, ex in exams.items():
        sa = bool(ex['section_a'])
        sb = bool(ex['section_b'])
        sc1 = bool(ex['section_c1'])
        sc2 = bool(ex['section_c2'])
        print(f"[{eid}] A:{sa} B:{sb} C1:{sc1} C2:{sc2}")
        
    return exams

if __name__ == '__main__':
    build_recent_exams()
