import json

data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
print(f"Total: {len(data)}")
for i, d in enumerate(data):
    m = d.get('meta', {})
    t = d.get('type')
    fn = m.get('filename', '')
    yr = m.get('year')
    mo = m.get('month')
    st = m.get('set_index')
    print(f"{i:2d}: {yr}-{mo} (Set {st}) | {t:22s} | file: {fn}")
