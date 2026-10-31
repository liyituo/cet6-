import json

def main():
    data = json.load(open('temp_astrbot/CET6_Perfect_Fixed.json', 'r', encoding='utf-8'))
    print(f"Total items: {len(data)}")
    summary = {}
    for i, d in enumerate(data):
        m = d.get('meta', {})
        yr = m.get('year')
        mo = m.get('month')
        st = m.get('set', '1')
        key = f"{yr}_{mo}"
        t = d.get('type')
        summary.setdefault(key, []).append((t, len(d.get('content', ''))))
    
    for k in sorted(summary.keys()):
        print(f"=== {k} ({len(summary[k])} parts) ===")
        for t, l in summary[k]:
            print(f"  {t} [len: {l}]")

    print("\n--- SAMPLE ITEM 0 ---")
    print("Meta:", data[0].get('meta'))
    print("Type:", data[0].get('type'))
    print("Content preview:\n", data[0].get('content')[:300])

if __name__ == '__main__':
    main()
