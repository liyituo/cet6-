# -*- coding: utf-8 -*-
"""
CET-6 Authentic Past Exam High-Frequency Vocabulary Miner
Mines word frequencies, paper coverage, Section A word-bank appearances,
question/option appearances, and authentic exam example sentences across:
  - 33 reading exams (via build_full_master_pipeline.get_all_exams_master)
  - 27 listening exam question sets (via temp_astrbot/listening_questions_v3.json)
Does NOT touch words_data.json IDs or synthetic listening transcripts.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding='utf-8')
from build_full_master_pipeline import get_all_exams_master

# Surface forms that are independent words/adverbs and must NOT stem onto another CET-6 headword
BLOCKED_SURFACE = {
    'according', 'accordingly', 'hardly', 'lately', 'nearly', 'barely',
    'scarcely', 'shortly', 'presently', 'evening', 'evenings', 'being',
    'beings', 'means', 'left', 'leaves', 'used', 'using'
}

IRREGULAR_MAP = {
    "arose": "arise", "arisen": "arise", "awoke": "awake", "awoken": "awake",
    "bore": "bear", "borne": "bear", "born": "bear", "beat": "beat", "beaten": "beat",
    "began": "begin", "begun": "begin", "bent": "bend", "bet": "bet", "bound": "bind",
    "bit": "bite", "bitten": "bite", "bled": "bleed", "blew": "blow", "blown": "blow",
    "broke": "break", "broken": "break", "bred": "breed", "brought": "bring",
    "broadcast": "broadcast", "built": "build", "burnt": "burn", "burned": "burn",
    "burst": "burst", "bought": "buy", "cast": "cast", "caught": "catch",
    "chose": "choose", "chosen": "choose", "clung": "cling", "crept": "creep",
    "dealt": "deal", "dug": "dig", "dove": "dive", "dived": "dive", "drew": "draw", "drawn": "draw",
    "dreamt": "dream", "drank": "drink", "drunk": "drink", "drove": "drive", "driven": "drive",
    "dwelt": "dwell", "ate": "eat", "eaten": "eat", "fell": "fall", "fallen": "fall",
    "fed": "feed", "felt": "feel", "fought": "fight", "fled": "flee", "flung": "fling",
    "flew": "fly", "flown": "fly", "forbade": "forbid", "forbidden": "forbid",
    "forecast": "forecast", "forgot": "forget", "forgotten": "forget",
    "forgave": "forgive", "forgiven": "forgive", "froze": "freeze", "frozen": "freeze",
    "ground": "grind", "grew": "grow", "grown": "grow", "hung": "hang", "hanged": "hang",
    "hid": "hide", "hidden": "hide", "held": "hold", "hurt": "hurt", "knelt": "kneel",
    "knit": "knit", "laid": "lay", "led": "lead", "leant": "lean", "leapt": "leap",
    "learnt": "learn", "lent": "lend", "let": "let", "lay": "lie", "lain": "lie",
    "lit": "light", "lost": "lose", "mistook": "mistake", "mistaken": "mistake",
    "overcame": "overcome", "overtook": "overtake", "overtaken": "overtake",
    "paid": "pay", "pleaded": "plead", "pled": "plead", "quit": "quit",
    "rode": "ride", "ridden": "ride", "rang": "ring", "rung": "ring",
    "rose": "rise", "risen": "rise", "sank": "sink", "sunk": "sink",
    "shook": "shake", "shaken": "shake", "shed": "shed", "shone": "shine", "shot": "shoot",
    "showed": "show", "shown": "show", "shrank": "shrink", "shrunk": "shrink", "shut": "shut",
    "sang": "sing", "sung": "sing", "slid": "slide", "sought": "seek", "sold": "sell",
    "sowed": "sow", "sown": "sow", "spat": "spit", "split": "split", "spoilt": "spoil",
    "spread": "spread", "sprang": "spring", "sprung": "spring", "stole": "steal", "stolen": "steal",
    "stuck": "stick", "stung": "sting", "stank": "stink", "stunk": "stink",
    "strode": "stride", "struck": "strike", "stricken": "strike", "strung": "string",
    "strove": "strive", "striven": "strive", "swore": "swear", "sworn": "swear",
    "swept": "sweep", "swelled": "swell", "swollen": "swell", "swam": "swim", "swum": "swim",
    "swung": "swing", "tore": "tear", "torn": "tear", "threw": "throw", "thrown": "throw",
    "thrust": "thrust", "trod": "tread", "trodden": "tread", "underwent": "undergo", "undergone": "undergo",
    "undertook": "undertake", "undertaken": "undertake", "upset": "upset",
    "woke": "wake", "woken": "wake", "wore": "wear", "worn": "wear", "wove": "weave", "woven": "weave",
    "wept": "weep", "withdrew": "withdraw", "withdrawn": "withdraw",
    "withheld": "withhold", "withstood": "withstand", "wrung": "wring",
    "analyses": "analysis", "crises": "crisis", "criteria": "criterion",
    "phenomena": "phenomenon", "media": "medium", "stimuli": "stimulus",
    "fungi": "fungus", "alumni": "alumnus", "hypotheses": "hypothesis",
    "theses": "thesis", "indices": "index", "appendices": "appendix",
    "formulae": "formula", "curricula": "curriculum", "bacteria": "bacterium",
}

RUBRIC_META_RE = re.compile(r'\b(author|passage|learn from|inferred from|refer to)\b', re.I)
POS_RE = re.compile(r'(?:^|[;\s,/])(vt\.|vi\.|v\.|n\.|adj\.|adv\.|a\.|ad\.|prep\.|conj\.|pron\.|num\.|art\.|int\.)', re.I)


def extract_primary_pos(trans_text):
    if not trans_text:
        return 'other'
    m = POS_RE.search(trans_text)
    if not m:
        return 'other'
    tag = m.group(1).lower()
    if tag in ('vt.', 'vi.', 'v.'):
        return 'v'
    if tag == 'n.':
        return 'n'
    if tag in ('adj.', 'a.'):
        return 'adj'
    if tag in ('adv.', 'ad.'):
        return 'adv'
    return 'other'


def is_clean_sentence(s):
    if not s or not (40 <= len(s) <= 155):
        return False
    if '__' in s or '\ufffd' in s:
        return False
    if re.match(r'^(\d+\.|[A-O]\)|\([A-O]\)|Section\s+[A-C])', s, re.I):
        return False
    if not re.search(r'[a-zA-Z]{3,}', s):
        return False
    # Require mostly normal printable ASCII + common punctuation
    ascii_chars = sum(1 for ch in s if 32 <= ord(ch) <= 126 or ch in '’‘“”—–')
    if ascii_chars / len(s) < 0.92:
        return False
    return True


def build():
    with open('words_data.json', 'r', encoding='utf-8') as f:
        wdata = json.load(f)

    word_to_id = {w['w'].strip().lower(): w['id'] for w in wdata}
    id_to_w = {w['id']: w for w in wdata}

    cache_lemma = {}

    def match_word_id(tok):
        w = tok.lower()
        if w in BLOCKED_SURFACE:
            return None
        if w in cache_lemma:
            return cache_lemma[w]
        if w in word_to_id:
            cache_lemma[w] = word_to_id[w]
            return cache_lemma[w]
        if w in IRREGULAR_MAP and IRREGULAR_MAP[w] in word_to_id:
            cache_lemma[w] = word_to_id[IRREGULAR_MAP[w]]
            return cache_lemma[w]

        cands = []
        if w.endswith('ies') and len(w) > 4:
            cands.append(w[:-3] + 'y')
        if w.endswith('ied') and len(w) > 4:
            cands.append(w[:-3] + 'y')
        if w.endswith('ves') and len(w) > 4:
            cands.extend([w[:-3] + 'f', w[:-3] + 'fe'])
        if w.endswith('es') and len(w) > 3:
            cands.extend([w[:-2], w[:-1]])
        if w.endswith('s') and not w.endswith('ss') and len(w) > 3:
            cands.append(w[:-1])
        if w.endswith('ing') and len(w) > 5:
            b = w[:-3]
            cands.extend([b, b + 'e'])
            if len(b) >= 2 and b[-1] == b[-2]:
                cands.append(b[:-1])
        if w.endswith('ed') and len(w) > 4:
            b = w[:-2]
            cands.extend([b, b + 'e', w[:-1]])
            if len(b) >= 2 and b[-1] == b[-2]:
                cands.append(b[:-1])
        if w.endswith('ly') and len(w) > 4:
            b = w[:-2]
            cands.extend([b, b + 'e'])
            if b.endswith('i'):
                cands.append(b[:-1] + 'y')
            if w.endswith('ally') and len(w) > 6:
                cands.append(w[:-4] + 'ic')

        for c in cands:
            if c in word_to_id:
                cache_lemma[w] = word_to_id[c]
                return cache_lemma[w]

        cache_lemma[w] = None
        return None

    total_hits = Counter()
    paper_sets = defaultdict(set)
    reading_hits = Counter()
    listening_hits = Counter()
    wordbank_hits = Counter()
    option_hits = Counter()
    examples = {}

    def scan_text(text, paper_id, category, source_label):
        if not text or not isinstance(text, str):
            return
        scan_str = RUBRIC_META_RE.sub(' ', text) if category == 'question' else text
        for sent in re.split(r'(?<=[.!?])\s+|\n+', scan_str):
            s_clean = re.sub(r'\s+', ' ', sent).strip()
            toks = re.findall(r"[A-Za-z]{2,}", s_clean)
            for tok in toks:
                wid = match_word_id(tok)
                if wid is None:
                    continue
                total_hits[wid] += 1
                paper_sets[wid].add(paper_id)
                if category == 'listen_opt':
                    listening_hits[wid] += 1
                    option_hits[wid] += 1
                else:
                    reading_hits[wid] += 1
                    if category == 'option':
                        option_hits[wid] += 1
                if (
                    wid not in examples
                    and category in ('reading', 'option', 'listen_opt')
                    and is_clean_sentence(s_clean)
                    and re.search(r'\b' + re.escape(tok) + r'\b', s_clean, re.I)
                ):
                    examples[wid] = {"s": source_label, "kw": tok, "en": s_clean}

    # 1. Scan 33 Reading Exams (already sorted newest year/month first by get_all_exams_master)
    exams = get_all_exams_master()
    for ex in exams:
        pid = 'R_' + str(ex['id'])
        lbl = f"{ex.get('year', '')}.{str(ex.get('month', '')).zfill(2)} 阅读"

        sa = ex.get('section_a', {})
        if isinstance(sa, dict):
            scan_text(sa.get('passage', ''), pid, 'reading', lbl)
            wb = sa.get('word_bank', {})
            wb_vals = wb.values() if isinstance(wb, dict) else (wb if isinstance(wb, list) else [])
            for w_item in wb_vals:
                w_str = w_item.get('word', '') if isinstance(w_item, dict) else str(w_item)
                wid = match_word_id(re.sub(r'[^A-Za-z]', '', w_str))
                if wid is not None:
                    wordbank_hits[wid] += 1
                    total_hits[wid] += 1
                    reading_hits[wid] += 1
                    paper_sets[wid].add(pid)

        for sk in ['section_b', 'section_c1', 'section_c2']:
            sec = ex.get(sk, {})
            if not isinstance(sec, dict):
                continue
            scan_text(sec.get('passage', ''), pid, 'reading', lbl)
            for p in sec.get('paragraphs', []):
                scan_text(p.get('text', '') if isinstance(p, dict) else str(p), pid, 'reading', lbl)
            for q in sec.get('questions', []):
                if isinstance(q, dict):
                    scan_text(q.get('q', '') or q.get('question', '') or q.get('stem', ''), pid, 'question', lbl)
                    for o in q.get('options', []):
                        scan_text(o.get('text', '') if isinstance(o, dict) else str(o), pid, 'option', lbl)

    # 2. Scan 27 Listening Exam Question Options (newest first)
    with open('temp_astrbot/listening_questions_v3.json', 'r', encoding='utf-8') as f:
        lq = json.load(f)

    for lid in sorted(lq.keys(), reverse=True):
        lobj = lq[lid]
        pid = 'L_' + lid
        parts_id = lid.split('_')
        lbl = f"{parts_id[0]}.{parts_id[1].zfill(2)} 听力"
        for sec in lobj.get('sections', {}).values():
            for q in sec.get('questions', []):
                opts = q.get('options', {})
                opt_vals = opts.values() if isinstance(opts, dict) else opts
                for o in opt_vals:
                    scan_text(str(o), pid, 'listen_opt', lbl)

    matched = [wid for wid in id_to_w if total_hits[wid] > 0]
    ranked = sorted(
        matched,
        key=lambda wid: (
            -(len(paper_sets[wid]) * 3 + total_hits[wid] + wordbank_hits[wid] * 8 + option_hits[wid] * 2),
            -total_hits[wid],
            wid,
        ),
    )

    hf_data = {}
    for rank_idx, wid in enumerate(ranked, 1):
        if rank_idx <= 150:
            tier = 1
        elif rank_idx <= 350:
            tier = 2
        elif rank_idx <= 600:
            tier = 3
        else:
            tier = 0

        wb_cnt = int(wordbank_hits[wid])
        qf_cnt = int(option_hits[wid])
        w_obj = id_to_w[wid]

        entry = {
            "r": rank_idx,
            "f": int(total_hits[wid]),
            "p": len(paper_sets[wid]),
            "rf": int(reading_hits[wid]),
            "lf": int(listening_hits[wid]),
            "wb": wb_cnt,
            "qf": qf_cnt,
            "tier": tier,
            "pos": extract_primary_pos(w_obj.get('t', '')),
        }
        if (tier in (1, 2, 3) or wb_cnt > 0 or qf_cnt >= 3) and wid in examples:
            entry["ex"] = examples[wid]

        hf_data[str(wid)] = entry

    with open('high_freq_data.json', 'w', encoding='utf-8') as f:
        json.dump(hf_data, f, ensure_ascii=False, separators=(',', ':'))

    size_kb = os.path.getsize('high_freq_data.json') / 1024
    t1 = sum(1 for v in hf_data.values() if v['tier'] == 1)
    t2 = sum(1 for v in hf_data.values() if v['tier'] == 2)
    t3 = sum(1 for v in hf_data.values() if v['tier'] == 3)
    wb_total = sum(1 for v in hf_data.values() if v['wb'] > 0)
    ex_total = sum(1 for v in hf_data.values() if 'ex' in v)
    print(f"Generated high_freq_data.json ({size_kb:.1f} KB)")
    print(f"Total matched words: {len(hf_data)} / {len(wdata)}")
    print(f"Tiers: tier1={t1}, tier2={t2}, tier3={t3} (Top600={t1+t2+t3}), wordbank={wb_total}, examples={ex_total}")
    print("Top 10:", [(id_to_w[int(k)]['w'], v['r'], v['f'], v['p']) for k, v in list(hf_data.items())[:10]])


if __name__ == '__main__':
    build()
