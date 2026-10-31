# -*- coding: utf-8 -*-
import csv
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
from build_full_master_pipeline import get_all_exams_master

def main():
    print("Extracting all text from 33 exams...")
    exams = get_all_exams_master()
    all_text = ""
    for ex in exams:
        for sk in ['section_a', 'section_b', 'section_c1', 'section_c2']:
            sec = ex.get(sk, {})
            if not isinstance(sec, dict): continue
            if 'passage' in sec and isinstance(sec['passage'], str):
                all_text += " " + sec['passage']
            if 'paragraphs' in sec and isinstance(sec['paragraphs'], list):
                for p in sec['paragraphs']:
                    if isinstance(p, dict):
                        all_text += " " + p.get('text', '')
                    elif isinstance(p, str):
                        all_text += " " + p
            for q in sec.get('questions', []):
                if isinstance(q, dict):
                    all_text += " " + str(q.get('q', ''))
                    opts = q.get('options', [])
                    if isinstance(opts, list):
                        for o in opts:
                            if isinstance(o, dict):
                                all_text += " " + str(o.get('text', ''))
                            else:
                                all_text += " " + str(o)
            if 'word_bank' in sec:
                for opt in sec['word_bank']:
                    all_text += " " + (opt.get('word', '') if isinstance(opt, dict) else str(opt))

    exam_words = set(re.findall(r'[a-zA-Z]{2,}', all_text.lower()))
    print(f"Total unique words in exam texts: {len(exam_words)}")

    # Load custom word lists
    custom_dict = {}
    if os.path.exists('words_data.json'):
        wdata = json.load(open('words_data.json', 'r', encoding='utf-8'))
        for item in wdata:
            w = item.get('w', '').strip().lower()
            if w:
                custom_dict[w] = {
                    'p': item.get('p', ''),
                    't': item.get('t', '').replace('\n', ' ')
                }

    if os.path.exists('temp_astrbot/4-CET6-顺序.json'):
        astr = json.load(open('temp_astrbot/4-CET6-顺序.json', 'r', encoding='utf-8'))
        for item in astr:
            w = item.get('word', '').strip().lower()
            if w and (w not in custom_dict or not custom_dict[w]['t']):
                trs = item.get('translations', [])
                tr_text = '; '.join([f"{t.get('type', '')} {t.get('translation', '')}".strip() for t in trs]) if isinstance(trs, list) else str(trs)
                custom_dict[w] = {
                    'p': '',
                    't': tr_text
                }

    # Load ECDICT
    ecdict_dict = {}
    exchange_map = {} # Maps inflected form -> root word (e.g. 'declined' -> 'decline')
    exam_tags = {'zk', 'gk', 'cet4', 'cet6', 'ky'}

    if os.path.exists('ecdict.csv'):
        print("Parsing ECDICT database...")
        with open('ecdict.csv', 'r', encoding='utf-8', errors='ignore') as f:
            reader = csv.DictReader(f)
            for row in reader:
                w = row.get('word', '').strip().lower()
                if not w or len(w) < 2: continue
                tag = row.get('tag', '')
                tags = set(tag.split())
                is_exam = bool(tags & exam_tags)
                is_in_text = (w in exam_words)
                
                # Check exchange field for inflections
                # e.g. p:past/d:done/i:ing/3:3rd/r:er/t:est/s:plural/0:root
                exchange = row.get('exchange', '')
                if exchange:
                    for part in exchange.split('/'):
                        if ':' in part:
                            ptype, pword = part.split(':', 1)
                            pword = pword.strip().lower()
                            if pword and pword != w:
                                exchange_map[pword] = w

                if is_exam or is_in_text:
                    p = row.get('phonetic', '').strip()
                    raw_t = row.get('translation', '').strip()
                    # Clean translation string
                    raw_t = raw_t.replace('\\n', ' | ').replace('\n', ' | ')
                    raw_t = re.sub(r'\[网络\].*?(?=\||$)', '', raw_t) # remove clutter
                    raw_t = re.sub(r'\s+', ' ', raw_t).strip(' |;')
                    if raw_t:
                        ecdict_dict[w] = {
                            'p': p,
                            't': raw_t
                        }

    # Combine all
    combined = {}
    # First priority: ECDICT (has rich translations for inflected forms too!)
    for w, val in ecdict_dict.items():
        combined[w] = val

    # Merge custom (has authoritative CET6 translations)
    for w, val in custom_dict.items():
        if w not in combined:
            combined[w] = val
        else:
            if not combined[w]['p'] and val['p']:
                combined[w]['p'] = val['p']
            # If ECDICT translation was minimal, supplement with CET6 translation
            if len(val.get('t', '')) > len(combined[w]['t']):
                combined[w]['t'] = val['t']

    print(f"Total merged dictionary entries: {len(combined)}")
    covered = exam_words.intersection(set(combined.keys()))
    print(f"Direct coverage on exam words: {len(covered)} / {len(exam_words)} ({len(covered)/len(exam_words)*100:.2f}%)")

    # For any still missing exam words, check exchange_map to assign root translation
    missing = exam_words - set(combined.keys())
    print(f"Initial missing words count: {len(missing)}")
    recovered_count = 0
    for mw in missing:
        if mw in exchange_map:
            root = exchange_map[mw]
            if root in combined:
                combined[mw] = {
                    'p': combined[root].get('p', ''),
                    't': f"(原形 {root}) " + combined[root].get('t', '')
                }
                recovered_count += 1
    
    print(f"Recovered through inflection exchange map: {recovered_count}")
    final_covered = exam_words.intersection(set(combined.keys()))
    print(f"Final coverage on exam words: {len(final_covered)} / {len(exam_words)} ({len(final_covered)/len(exam_words)*100:.2f}%)")

    still_missing = exam_words - set(combined.keys())
    print(f"Still missing words ({len(still_missing)}):", sorted(list(still_missing))[:30])

    # Save to compressed clean JSON
    out_file = 'comprehensive_cet6_dict.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(combined, f, ensure_ascii=False, separators=(',', ':'))

    size_mb = os.path.getsize(out_file) / (1024*1024)
    print(f"Saved {out_file} ({size_mb:.2f} MB)")

if __name__ == '__main__':
    main()
