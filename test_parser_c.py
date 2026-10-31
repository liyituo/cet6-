import json, re

def parse_section_c(content, answers_str, sike_item=None):
    lines = content.strip().split('\n')
    
    # Find questions start
    q_start_idx = -1
    for idx, line in enumerate(lines):
        if re.match(r'^(?:46|51|56|61)\.\s+', line.strip()):
            q_start_idx = idx
            break
            
    if q_start_idx != -1:
        passage_text = '\n'.join(lines[:q_start_idx]).strip()
        questions_text = '\n'.join(lines[q_start_idx:]).strip()
    else:
        passage_text = content
        questions_text = ""
        
    # Clean passage text: remove 【 Passage One 】 or Questions 46 to 50... header
    passage_clean_lines = []
    for l in passage_text.split('\n'):
        if re.search(r'Passage (?:One|Two)|Questions \d+ to \d+ are based', l, re.I):
            continue
        passage_clean_lines.append(l)
    passage_text = '\n'.join(passage_clean_lines).strip()
    
    # Parse questions
    # Split questions by \n\d+\.
    raw_qs = re.split(r'(?:^|\n)(\d+)\.\s*', questions_text)
    # raw_qs format: [preamble, '46', q_content, '47', q_content, ...]
    questions = []
    clean_ans = re.findall(r'[A-D]', answers_str)[:5]
    
    # Map from sike_item if available
    sike_q_map = {}
    if sike_item and 'questions' in sike_item:
        for sq in sike_item['questions']:
            sike_q_map[str(sq.get('number'))] = sq
            
    idx = 1
    while idx < len(raw_qs):
        q_num = raw_qs[idx]
        q_body = raw_qs[idx+1] if (idx+1) < len(raw_qs) else ""
        
        # Split stem and options A) B) C) D)
        opt_matches = list(re.finditer(r'(?:^|\n)\s*([A-D])[\)\.\s]\s*(.+?)(?=(?:\n\s*[A-D][\)\.\s]|\Z))', q_body, re.DOTALL))
        if opt_matches:
            stem = q_body[:opt_matches[0].start()].strip().replace('\n', ' ')
            options = []
            for om in opt_matches:
                options.append({
                    "label": om.group(1),
                    "text": om.group(2).strip().replace('\n', ' ')
                })
        else:
            stem = q_body.strip()
            options = []
            
        ans_idx = (idx - 1) // 2
        correct_ans = clean_ans[ans_idx] if ans_idx < len(clean_ans) else ""
        
        sq = sike_q_map.get(str(q_num), {})
        
        questions.append({
            "num": int(q_num),
            "stem": stem,
            "options": options,
            "answer": correct_ans or sq.get('answer', ''),
            "question_zh": sq.get('questionZh', ''),
            "answer_zh": sq.get('answerZh', ''),
            "explanation": sq.get('explanation', '')
        })
        idx += 2
        
    return {
        "passage": passage_text,
        "main_idea_zh": sike_item.get('mainIdeaZh', '') if sike_item else '',
        "main_idea_en": sike_item.get('mainIdeaEn', '') if sike_item else '',
        "questions": questions
    }

data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
answers = json.load(open('temp_astrbot/CET6_Answer.json', 'r', encoding='utf-8'))

with open('temp_sikefix/public/lessons-data.js', 'r', encoding='utf-8') as f:
    c = f.read()
start = c.find('[')
end = c.rfind(']') + 1
sike_data = json.loads(c[start:end])
sike_map = {item['id']: item for item in sike_data}

sec_c1_sample = data[2]['content']
ans_sample = answers['2018_06_1']['answers']['Section C1']
sike_sample = sike_map.get('cet6_2018_06_1-p1')

parsed_c = parse_section_c(sec_c1_sample, ans_sample, sike_sample)
print("Passage preview:", parsed_c['passage'][:150])
print("Main Idea ZH:", parsed_c['main_idea_zh'][:80])
print(f"Total questions: {len(parsed_c['questions'])}")
for q in parsed_c['questions']:
    print(f"Q{q['num']}: {q['stem'][:40]}... Ans: {q['answer']} | Expl: {q['explanation'][:40]}...")
