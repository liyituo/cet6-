import json
import re

data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
answers = json.load(open('temp_astrbot/CET6_Answer.json', 'r', encoding='utf-8'))

# Look at 2021_6, 2020_12, 2019_12, 2018_12
for item in data:
    meta = item.get('meta', {})
    yr = meta.get('year')
    mo = meta.get('month')
    st = meta.get('set_index')
    t = item.get('type')
    if yr in ['2021', '2020', '2019', '2018']:
        ans_key = f"{yr}_{int(mo):02d}_{st}" if mo.isdigit() else f"{yr}_{mo}_{st}"
        ans_obj = answers.get(ans_key, {}).get('answers', {})
        # print first 100 chars
        content = item.get('content', '')
        # print summary
        # check questions
        q_nums = re.findall(r'\b(\d+)\.\s', content)
        # check word bank for Section A
        has_wb = bool(re.search(r'[A-O]\)\s*\w+', content))
        # check paragraph labels for Section B
        has_labels = bool(re.search(r'\[[A-Z]\]|【\s*[A-Z]\s*】', content))
        # print
        # print(f"{yr}-{mo} Set {st} | {t} | Qs: {q_nums[:5]}..{q_nums[-3:] if q_nums else []} | AnsKey: {ans_key} -> {ans_obj.get(t, '')[:15]}")
