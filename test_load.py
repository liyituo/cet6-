# -*- coding: utf-8 -*-
"""
Full CET-6 Reading Comprehension Master Platform Builder (2014 - 2021)
Compiles all genuine CET-6 reading comprehension past papers from 2014 to 2021
into a single-file, production-grade, offline-first Web Application.
"""

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

def extract_word_bank(wb_text):
    raw_wb = re.findall(r'([A-O])[\)\.\s\uff09\u3001\uFF0E\-\:]+\s*([a-zA-Z\-\']+)', wb_text)
    clean_wb = {}
    for letter, word in raw_wb:
        w = word.strip().lower()
        if w and letter not in clean_wb:
            clean_wb[letter] = w
    return clean_wb

def load_data():
    # 1. Load Astrbot 2018-2021
    astr_data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
    astr_answers = json.load(open('temp_astrbot/CET6_Answer.json', 'r', encoding='utf-8'))

    # 2. Load Sikefix 2016-2021
    with open('temp_sikefix/public/lessons-data.js', 'r', encoding='utf-8') as f:
        c = f.read()
    start = c.find('[')
    end = c.rfind(']') + 1
    sike_data = json.loads(c[start:end])
    sike_map = {item['id']: item for item in sike_data}

    # 3. Load dictionary
    dict_map = {}
    if os.path.exists('words_data.json'):
        wdata = json.load(open('words_data.json', 'r', encoding='utf-8'))
        for item in wdata:
            w = item.get('w', '').strip().lower()
            if w and w not in dict_map:
                dict_map[w] = {
                    'p': item.get('p', ''),
                    't': item.get('t', '')
                }
    
    # Also load temp_astrbot/4-CET6-*.json for extended dictionary
    for fname in os.listdir('temp_astrbot'):
        if fname.startswith('4-CET6') and fname.endswith('.json'):
            ext_data = json.load(open(os.path.join('temp_astrbot', fname), 'r', encoding='utf-8'))
            for item in ext_data:
                w = item.get('word', '').strip().lower()
                if w and w not in dict_map:
                    trs = item.get('translations', [])
                    tr_text = '; '.join([f"{t.get('type', '')} {t.get('translation', '')}".strip() for t in trs]) if isinstance(trs, list) else str(trs)
                    dict_map[w] = {
                        'p': '',
                        't': tr_text
                    }

    print(f"Total vocabulary words in dictionary: {len(dict_map)}")
    return astr_data, astr_answers, sike_map, dict_map

if __name__ == '__main__':
    load_data()
