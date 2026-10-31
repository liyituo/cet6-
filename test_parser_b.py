import json, re

def parse_section_b(content, answers_str):
    lines = content.strip().split('\n')
    
    # Find where questions start: lines starting with 36., 37., etc. (or 46. in older tests)
    q_start_idx = -1
    for idx, line in enumerate(lines):
        if re.match(r'^(?:36|46)\.\s+', line.strip()):
            q_start_idx = idx
            break
            
    if q_start_idx != -1:
        passage_text = '\n'.join(lines[:q_start_idx]).strip()
        questions_text = '\n'.join(lines[q_start_idx:]).strip()
    else:
        passage_text = content
        questions_text = ""
        
    # Parse questions
    q_matches = re.findall(r'(?:^|\n)(\d+)\.\s*(.+?)(?=(?:\n\d+\.|\Z))', questions_text, re.DOTALL)
    questions = []
    
    # Parse answers
    clean_ans = re.findall(r'[A-Z]', answers_str)[:len(q_matches)]
    
    for idx, (q_num, q_stem) in enumerate(q_matches):
        ans = clean_ans[idx] if idx < len(clean_ans) else ""
        questions.append({
            "num": int(q_num),
            "stem": q_stem.strip().replace('\n', ' '),
            "answer": ans
        })
        
    # Parse paragraphs
    # Paragraphs look like 【 A 】, [A], or ^[A-Z]\s+
    para_splits = re.split(r'(?:^|\n)(?:【\s*([A-Z])\s*】|\[\s*([A-Z])\s*\]|\u25a0\s*([A-Z])\s*\u25a0)\s*', passage_text)
    paragraphs = []
    # If the first piece has title
    title = ""
    if len(para_splits) > 1 and not (para_splits[1] or para_splits[2] or para_splits[3]):
        title = para_splits[0].strip()
    
    # Group paragraphs
    # re.split with 3 capturing groups creates [pre, g1, g2, g3, text, g1, g2, g3, text, ...]
    i = 1
    while i < len(para_splits):
        label = para_splits[i] or para_splits[i+1] or para_splits[i+2]
        p_text = para_splits[i+3] if (i+3) < len(para_splits) else ""
        if label:
            paragraphs.append({
                "label": label,
                "text": p_text.strip()
            })
        i += 4

    return {
        "title": title or "Long Reading",
        "paragraphs": paragraphs,
        "questions": questions
    }

data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
answers = json.load(open('temp_astrbot/CET6_Answer.json', 'r', encoding='utf-8'))

sec_b_sample = data[1]['content']
ans_sample = answers['2018_06_1']['answers']['Section B']
parsed_b = parse_section_b(sec_b_sample, ans_sample)
print("Title:", parsed_b['title'])
print(f"Total paragraphs: {len(parsed_b['paragraphs'])}")
for p in parsed_b['paragraphs'][:3]:
    print(f"  [{p['label']}] {p['text'][:60]}...")
print(f"Total questions: {len(parsed_b['questions'])}")
for q in parsed_b['questions'][:3]:
    print(f"  Q{q['num']}: {q['stem'][:50]}... Ans: {q['answer']}")
