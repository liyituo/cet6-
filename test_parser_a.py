import json, re

def parse_section_a(content, answers_str):
    # Extracts passage, word bank, and answers
    # Blanks are typically 26 to 35
    # Word bank is A) ... O) ...
    lines = content.strip().split('\n')
    passage_lines = []
    word_bank = {}
    in_word_bank = False

    # Look for word bank
    wb_pattern = re.findall(r'([A-O])[\)\.\s]+([a-zA-Z\s\-]+?)(?=(?:[A-O][\)\.\s])|$)', content)
    
    # Alternatively find the line where word bank starts
    wb_start_idx = -1
    for idx, l in enumerate(lines):
        if re.search(r'^[A-O][\)\.\s]\s*[a-zA-Z]+', l.strip()):
            wb_start_idx = idx
            break
        if re.search(r'\bA\)|\bA\.', l) and re.search(r'\b[B-O]\)', l):
            wb_start_idx = idx
            break
            
    if wb_start_idx != -1:
        passage_text = '\n'.join(lines[:wb_start_idx]).strip()
        wb_text = '\n'.join(lines[wb_start_idx:]).strip()
    else:
        passage_text = content
        wb_text = ""

    # Parse word bank entries
    raw_wb = re.findall(r'([A-O])[\)\.\s]+([a-zA-Z\-\'\s]+)', wb_text)
    clean_wb = {}
    for letter, word in raw_wb:
        w = word.strip().split()[0] if word.strip() else ""
        if w and letter not in clean_wb:
            clean_wb[letter] = w

    # Parse answers (10 letters)
    clean_ans = re.findall(r'[A-O]', answers_str)[:10]

    return {
        "passage": passage_text,
        "word_bank": clean_wb,
        "answers": clean_ans
    }

data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
answers = json.load(open('temp_astrbot/CET6_Answer.json', 'r', encoding='utf-8'))

sec_a_sample = data[0]['content']
ans_sample = answers['2018_06_1']['answers']['Section A']
parsed = parse_section_a(sec_a_sample, ans_sample)
print("Passage preview:", parsed['passage'][:200])
print("Word bank:", parsed['word_bank'])
print("Answers:", parsed['answers'])
