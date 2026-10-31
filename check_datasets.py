import json, re

astr_data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
astr_answers = json.load(open('temp_astrbot/CET6_Answer.json', 'r', encoding='utf-8'))

with open('temp_sikefix/public/lessons-data.js', 'r', encoding='utf-8') as f:
    c = f.read()
start = c.find('[')
end = c.rfind(']') + 1
sike_data = json.loads(c[start:end])

print(f"Astrbot items: {len(astr_data)}")
print(f"Sikefix items: {len(sike_data)}")

# Map sikefix by year_month_set_passage
sike_map = {}
for item in sike_data:
    # id e.g. cet6_2018_06_1-p1
    sike_map[item['id']] = item

print(f"Sample sike keys: {list(sike_map.keys())[:10]}")
