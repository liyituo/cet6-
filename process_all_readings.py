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

def parse_section_a(content, answers_str):
    content = clean_text(content)
    lines = content.split('\n')
    
    # Locate word bank
    wb_start_idx = -1
    for idx, l in enumerate(lines):
        if re.search(r'^[A-O][\)\.\s\uff09\u3001\uFF0E]', l.strip()):
            wb_start_idx = idx
            break
        if re.search(r'\bA[\)\.\uff09]', l) and re.search(r'\b[B-O][\)\.\uff09]', l):
            wb_start_idx = idx
            break
            
    if wb_start_idx != -1:
        passage_text = '\n'.join(lines[:wb_start_idx]).strip()
        wb_text = '\n'.join(lines[wb_start_idx:]).strip()
    else:
        # Fallback regex split
        parts = re.split(r'(?=(?:^|\n)\s*[A-O][\)\.\uff09])', content, maxsplit=1)
        passage_text = parts[0].strip()
        wb_text = parts[1].strip() if len(parts) > 1 else ""

    # Parse word bank entries
    raw_wb = re.findall(r'([A-O])[\)\.\s\uff09\u3001\uFF0E\-\:]+\s*([a-zA-Z\-\']+)', wb_text)
    clean_wb = {}
    for letter, word in raw_wb:
        w = word.strip().lower()
        if w and letter not in clean_wb:
            clean_wb[letter] = w

    # Clean answers (10 letters A-O)
    clean_ans = re.findall(r'[A-O]', answers_str)[:10]

    # Strip header directions if present
    passage_text = re.sub(r'^.*?Questions\s+\d+\s+to\s+\d+\s+are\s+based\s+on\s+the\s+following\s+passage\.?\s*', '', passage_text, flags=re.I|re.DOTALL).strip()

    # The 10 blanks in Section A are strictly sequential Q26 through Q35
    ordered_blanks = list(range(26, 36))

    questions = []
    for idx, b_num in enumerate(ordered_blanks):
        ans_letter = clean_ans[idx] if idx < len(clean_ans) else ""
        word = clean_wb.get(ans_letter, "")
        questions.append({
            "num": b_num,
            "answer": ans_letter,
            "word": word
        })

    return {
        "passage": passage_text,
        "word_bank": clean_wb,
        "questions": questions
    }

def parse_section_b(content, answers_str):
    content = clean_text(content)
    lines = content.split('\n')
    
    q_start_idx = -1
    for idx, line in enumerate(lines):
        if re.match(r'^(?:36|46)\.\s+', line.strip()):
            q_start_idx = idx
            break
            
    if q_start_idx != -1:
        passage_text = '\n'.join(lines[:q_start_idx]).strip()
        questions_text = '\n'.join(lines[q_start_idx:]).strip()
    else:
        parts = re.split(r'(?=(?:^|\n)\s*(?:36|46)\.\s+)', content, maxsplit=1)
        passage_text = parts[0].strip()
        questions_text = parts[1].strip() if len(parts) > 1 else ""
        
    q_matches = re.findall(r'(?:^|\n)(\d+)\.\s*(.+?)(?=(?:\n\d+\.|\Z))', questions_text, re.DOTALL)
    clean_ans = re.findall(r'[A-Z]', answers_str)[:len(q_matches)]
    
    questions = []
    for idx, (q_num, q_stem) in enumerate(q_matches):
        ans = clean_ans[idx] if idx < len(clean_ans) else ""
        questions.append({
            "num": int(q_num),
            "stem": q_stem.strip().replace('\n', ' '),
            "answer": ans
        })
        
    # Split paragraphs by label (supports 【 A 】, [A], P), and standalone letter)
    pattern = r'(?:^|\n|\.|\?|\!)\s*(?:【\s*([A-Z])\s*】|\[\s*([A-Z])\s*\]|\b([A-Z])\)\s+|\b([A-Z])\b\s+(?=[A-Z][a-z]))\s*'
    para_splits = re.split(pattern, passage_text)
    paragraphs = []
    title = ""
    
    # If first chunk has title
    if para_splits and len(para_splits) > 1:
        first_chunk = para_splits[0].strip()
        if len(first_chunk) < 200:
            title = first_chunk.split('\n')[0].strip()

    i = 1
    while i < len(para_splits):
        label = None
        for g in range(4):
            if i + g < len(para_splits) and para_splits[i + g] and len(para_splits[i + g]) == 1 and para_splits[i + g].isupper():
                label = para_splits[i + g]
                break
        
        text_chunk = ""
        next_i = i + 4
        for j in range(i + 1, min(i + 6, len(para_splits))):
            if para_splits[j] and len(para_splits[j]) > 30:
                text_chunk = para_splits[j].strip()
                next_i = j + 1
                break
                
        if label and text_chunk:
            paragraphs.append({
                "label": label,
                "text": text_chunk
            })
        i = next_i

    return {
        "title": title or "Long Reading",
        "paragraphs": paragraphs,
        "questions": questions
    }

def parse_section_c(content, answers_str, sike_item=None):
    content = clean_text(content)
    lines = content.split('\n')
    
    q_start_idx = -1
    for idx, line in enumerate(lines):
        if re.match(r'^(?:46|51|56|61)\.\s+', line.strip()):
            q_start_idx = idx
            break
            
    if q_start_idx != -1:
        passage_text = '\n'.join(lines[:q_start_idx]).strip()
        questions_text = '\n'.join(lines[q_start_idx:]).strip()
    else:
        parts = re.split(r'(?=(?:^|\n)\s*(?:46|51|56|61)\.\s+)', content, maxsplit=1)
        passage_text = parts[0].strip()
        questions_text = parts[1].strip() if len(parts) > 1 else ""

    passage_clean_lines = []
    for l in passage_text.split('\n'):
        if re.search(r'Passage (?:One|Two)|Questions \d+ to \d+ are based', l, re.I):
            continue
        passage_clean_lines.append(l)
    passage_text = '\n'.join(passage_clean_lines).strip()
    
    raw_qs = re.split(r'(?:^|\n)(\d+)\.\s*', questions_text)
    clean_ans = re.findall(r'[A-D]', answers_str)[:5]
    
    sike_q_map = {}
    if sike_item and 'questions' in sike_item:
        for sq in sike_item['questions']:
            sike_q_map[str(sq.get('number'))] = sq
            
    questions = []
    idx = 1
    while idx < len(raw_qs):
        q_num = raw_qs[idx]
        q_body = raw_qs[idx+1] if (idx+1) < len(raw_qs) else ""
        
        opt_matches = list(re.finditer(r'(?:^|\n)\s*([A-D])[\)\.\s\uff09]\s*(.+?)(?=(?:\n\s*[A-D][\)\.\s\uff09]|\Z))', q_body, re.DOTALL))
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

print("Parser module ready.")
