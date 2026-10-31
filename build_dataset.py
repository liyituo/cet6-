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

def build():
    # 1. Load Astrbot data
    astr_data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
    astr_answers = json.load(open('temp_astrbot/CET6_Answer.json', 'r', encoding='utf-8'))

    # 2. Load Sikefix data
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
            w = item.get('word', '').lower()
            if w:
                dict_map[w] = {
                    'phonetic': item.get('phonetic', ''),
                    'trans': item.get('trans', [])
                }

    print(f"Loaded dictionary words: {len(dict_map)}")
    print(f"Loaded astr items: {len(astr_data)}")
    print(f"Loaded sike lessons: {len(sike_data)}")

if __name__ == '__main__':
    build()
