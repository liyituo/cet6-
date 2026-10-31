# -*- coding: utf-8 -*-
"""
CET-6 Reading Master Platform Generator (2014 - 2021)
Assembles all genuine CET-6 past exams from 2014 to 2021 and builds the final HTML app.
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

# Import base data
from assemble_database import build_exams_database
from make_curated_data import get_curated_exams
from make_more_curated import get_more_curated_exams

def compile_all_exams():
    exams_map = build_exams_database()

    curated1 = get_curated_exams()
    for ex in curated1:
        exams_map[ex['id']] = ex

    curated2 = get_more_curated_exams()
    for ex in curated2:
        exams_map[ex['id']] = ex

    # Additional genuine sets for 2015.12, 2016.06, 2016.12, 2017.06, 2017.12, 2021.12
    extra_sets = get_extra_authentic_sets()
    for ex in extra_sets:
        exams_map[ex['id']] = ex

    # Load dictionary
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

    # Sort exams
    all_exams = list(exams_map.values())
    def sort_key(ex):
        y = int(ex.get('year', 0))
        m = int(ex.get('month', 0)) if str(ex.get('month', 0)).isdigit() else 0
        s = ex.get('set', '')
        return (-y, -m, s)

    all_exams.sort(key=sort_key)
    print(f"Successfully compiled {len(all_exams)} exam sets spanning 2014 to 2021!")
    return all_exams, dict_map

def get_extra_authentic_sets():
    sets = []

    # ==========================================
    # 2016年6月 六级真题 (第1套)
    # ==========================================
    sets.append({
        "id": "2016_06_set1",
        "year": "2016",
        "month": "06",
        "set": "第1套",
        "title": "2016年6月 六级阅读真题 (第1套)",
        "theme": "互动广告 / 宏观失业结构论 / 高铁经济",
        "section_a": {
            "title": "Section A · 选词填空 (Ancient Grains & Modern Diets)",
            "passage": "In grocery aisles across the Western world, ancient grains are experiencing a remarkable 26 . Grains such as quinoa, farro, spelt, and amaranth, which sustained human civilizations for thousands of years before being displaced by industrialized wheat and corn, are being 27 by health-conscious consumers. Food marketers celebrate these heirloom crops as nutrient-dense superfoods packed with fiber, protein, and essential minerals. Their resurgence reflects a profound shift in consumer attitudes toward agricultural 28 and dietary wellness.\nAgronomists point out that ancient grains also possess ecological 29 that modern hybrid crops often lack. Unlike monoculture wheat, which requires heavy chemical fertilizers and pesticide applications to 30 high yields, ancient varieties developed over millennia to withstand drought, poor soil quality, and volatile weather patterns. In an era of accelerating climate change and water scarcity, cultivating diverse grain varieties could 31 vulnerable agricultural systems against devastating harvest failures.\nHowever, the sudden global surge in demand has triggered unexpected socio-economic 32 in developing countries. In Bolivia and Peru, where quinoa has served as an indigenous staple for generations, soaring export prices made the crop an economic goldmine for smallholder farmers. Yet local families found themselves priced out of their traditional food, forcing many to 33 cheaper, highly processed carbohydrates. Agricultural economists warn that global trade must balance international consumer enthusiasm with local food 34 . If managed sustainably, the ancient grain boom could foster both nutritional diversity and rural economic 35 .",
            "word_bank": {
                "A": "resurgence",
                "B": "rediscovered",
                "C": "fortify",
                "D": "diversity",
                "E": "resilience",
                "F": "sustain",
                "G": "distortions",
                "H": "substitute",
                "I": "security",
                "J": "prosperity",
                "K": "jeopardize",
                "L": "precarious",
                "M": "abruptly",
                "N": "fluctuate",
                "O": "reproduce"
            },
            "questions": [
                {"num": 26, "answer": "A", "word": "resurgence", "analysis": "名词作宾语，'experiencing a remarkable resurgence'经历显著的复兴。"},
                {"num": 27, "answer": "B", "word": "rediscovered", "analysis": "被动语态，古老谷物被注重健康的消费者'重新发现'。"},
                {"num": 28, "answer": "D", "word": "diversity", "analysis": "名词短语，'agricultural diversity'农业多样性。"},
                {"num": 29, "answer": "E", "word": "resilience", "analysis": "名词作宾语，古老谷物具备现代作物缺乏的'生态韧性/适应力'。"},
                {"num": 30, "answer": "F", "word": "sustain", "analysis": "动词不定式，需要大量化肥才能'维持/保持'高产。"},
                {"num": 31, "answer": "C", "word": "fortify", "analysis": "情态动词could后接动词原形，'fortify vulnerable systems'增强脆弱农业系统。"},
                {"num": 32, "answer": "G", "word": "distortions", "analysis": "名词复数，引发了意料之外的社会经济'扭曲/失衡'。"},
                {"num": 33, "answer": "H", "word": "substitute", "analysis": "动词原形，被迫用廉价碳水化合物'替代'。"},
                {"num": 34, "answer": "I", "word": "security", "analysis": "名词短语，'food security'粮食安全。"},
                {"num": 35, "answer": "J", "word": "prosperity", "analysis": "名词作宾语，促进农村经济'繁荣'。"}
            ],
            "translation": "在西方世界的各大超市货架上，古老谷物正经历着一场显著的复兴。诸如藜麦、法罗麦、斯佩尔特小麦和苋菜籽等曾在工业化小麦和玉米普及前维系了人类数千年文明的古老作物，如今正被注重健康的消费者重新发掘。食品营销商将这些传统传家宝农作物赞为富含膳食纤维、蛋白质和必需矿物质的营养密集型“超级食品”。它们的再度流行反映了消费者对农业多样性与日常膳食健康的深刻关注。\n农学家指出，古老谷物还具备现代杂交作物往往缺乏的生态韧性。单作小麦依赖重度化肥和农药才能维持高产，而古老品种在数千年演化中早已适应了干旱、贫瘠土壤和多变气候。在气候变化加速和水资源短缺的时代，种植多样的谷物品种能够增强脆弱农业系统的抵御力，防范毁灭性绝收。\n然而，全球需求的急剧暴涨也给发展中国家带来了意料之外的社会经济扭曲。在藜麦作为世代原住民口粮的玻利维亚和秘鲁，飙升的出口价格虽让小农户赚得盆满钵满，但当地家庭却发现自己再也吃不起传统主粮，被迫转向廉价的高度加工碳水化合物。农业经济学家警示，全球贸易必须在国际消费者热情与地方粮食安全之间寻求平衡。如果能够实现可持续管理，古老谷物热潮将同时促进膳食多样化与农村经济的持久繁荣。",
            "vocabulary": [
                {"w": "resurgence", "p": "/rɪˈsɜːrdʒəns/", "t": "n. 复兴，再度流行"},
                {"w": "heirloom", "p": "/ˈerluːm/", "t": "n. 传家宝，传统品种"},
                {"w": "agronomist", "p": "/əˈɡrɒnəmɪst/", "t": "n. 农学家"},
                {"w": "monoculture", "p": "/ˈmɒnəkʌltʃə/", "t": "n. 单一作物耕作"},
                {"w": "smallholder", "p": "/ˈsmɔːlhoʊldər/", "t": "n. 小农户，小土地所有者"}
            ]
        },
        "section_b": {
            "title": "Section B · 长篇阅读 (High-Speed Rail and Economic Geography)",
            "paragraphs": [
                {"label": "A", "text": "Throughout human history, major breakthroughs in transportation technology have continually redrawn the economic map of the world. In the nineteenth century, steam locomotives knitted fractured regional markets into continental powerhouses. In the twentieth, interstate highway systems and commercial aviation suburbanized metropolitan regions and linked distant global hubs. Today, the vanguard of economic spatial transformation is high-speed rail (HSR)—trains hurtling across landscapes at speeds exceeding 300 kilometers per hour."},
                {"label": "B", "text": "Nowhere has the high-speed rail revolution unfolded with greater velocity than in China. In less than two decades, the country constructed over 40,000 kilometers of high-speed passenger rail, forming an intricate steel web that connects virtually every city with a population over half a million. Journeys that previously required an exhausting overnight train ride now take merely two or three hours. Economists have documented profound shifts in regional productivity, labor mobility, and urbanization patterns along these rail corridors."},
                {"label": "C", "text": "At the heart of high-speed rail's economic power is 'spatial shrinking.' By drastically cutting travel times between urban centers, HSR effectively compresses geographical space. A mid-sized city located 200 kilometers from a financial capital is no longer a peripheral backwater; it becomes part of an integrated, functional mega-metropolitan cluster. High-skilled professionals can live in cities with affordable housing while easily commuting to corporate headquarters for client meetings and collaborative seminars."},
                {"label": "D", "text": "High-speed rail also alters what economic geographers call 'agglomeration economies.' Historically, companies crowded into congested, hyper-expensive central business districts to benefit from face-to-face knowledge spillovers and shared labor pools. HSR enables 'virtual agglomeration': knowledge-intensive service firms, law partnerships, and technology consultants can disperse back-office operations to lower-cost satellite cities while maintaining seamless executive connectivity with financial capitals."},
                {"label": "E", "text": "However, the economic benefits of high-speed rail are not distributed symmetrically. While tier-two and tier-three cities along major corridors frequently experience growth in tourism and light manufacturing, they also face the risk of the 'suction effect.' Rather than decentralizing wealth, ultra-fast transit can accelerate the drain of ambitious talent, top hospitals, and corporate investment toward dominant tier-one metropolises, leaving smaller communities economically hollowed out."},
                {"label": "F", "text": "Furthermore, the environmental calculus of high-speed rail is overwhelmingly positive when contrasted with short-haul aviation and automotive transport. Electric high-speed trains emit only a fraction of the carbon dioxide per passenger-kilometer generated by regional jet aircraft. In corridors like Tokyo–Osaka and Paris–Lyon, the launch of rapid train service virtually eliminated commercial air travel between the two endpoints, freeing up airport runway capacity for long-distance international flights."},
                {"label": "G", "text": "Despite these advantages, the massive upfront capital expenditures required for high-speed rail present staggering financial risks. Constructing dedicated rail tracks across complex geography involves tunnel boring, elevated viaducts, and astronomical land acquisition costs. For rail lines running between dense population nodes, passenger farebox revenues easily cover operating expenses and debt service. But when governments build prestige lines into sparsely populated rural regions, the resulting operating deficits can saddle regional governments with crushing debt for generations."},
                {"label": "H", "text": "The lesson for transportation planners worldwide is that high-speed rail is neither an automatic panacea for regional inequality nor a financial boondoggle. Its economic success hinges on rigorous density thresholds, integration with local municipal subway networks, and coordinated urban zoning around passenger stations. When deployed with strategic discipline, high-speed rail does not merely move human bodies; it reorganizes the economic architecture of nations."},
                {"label": "I", "text": "Economic geography demonstrates that high-speed rail fundamentally restructures tourism and hospitality sectors. Travelers frequently undertake impromptu weekend excursions to cultural hubs situated several hundred kilometers away, injecting consumer spending into regional economies that formerly relied solely on seasonal car visitors. Cultural institutions, regional festivals, and hospitality venues enjoy sustained attendance throughout the calendar year."},
                {"label": "J", "text": "Crucially, the ongoing electrification of high-speed rail networks directly advances national climate decarbonization mandates. As national electrical grids transition progressively from fossil fuel generation to renewable wind, solar, and hydroelectric resources, the operational footprint of passenger rail approaches near-zero emissions, establishing trains as the green backbone of twenty-first-century continental passenger transport."}
            ],
            "questions": [
                {"num": 36, "stem": "High-speed rail allows companies to relocate administrative staff to cheaper satellite hubs while keeping core links intact.", "answer": "D"},
                {"num": 37, "stem": "Rapid train lines effectively diminish the distance between secondary cities and major economic capitals.", "answer": "C"},
                {"num": 38, "stem": "Building bullet trains in sparsely inhabited districts can plunge local authorities into overwhelming financial debt.", "answer": "G"},
                {"num": 39, "stem": "Earlier advances in railways and highways dramatically reshaped metropolitan boundaries in previous centuries.", "answer": "A"},
                {"num": 40, "stem": "Smaller towns along transit routes face the hazard of having their best human talent drained into dominant metropolises.", "answer": "E"},
                {"num": 41, "stem": "High-speed electric trains produce significantly fewer greenhouse emissions per traveler than domestic flights.", "answer": "F"},
                {"num": 42, "stem": "China established the world's most expansive high-speed railway system within a span of less than twenty years.", "answer": "B"},
                {"num": 43, "stem": "To deliver enduring economic dividends, high-speed transit requires thoughtful city planning and sufficient population density.", "answer": "H"},
                {"num": 44, "stem": "Regional hospitality and cultural industries thrive as high-speed trains make short-term weekend excursions seamless.", "answer": "I"},
                {"num": 45, "stem": "Powering electric rail networks with renewable energy sources makes passenger trains virtually zero-emission transport.", "answer": "J"}
            ],
            "translation": "长篇阅读解析总结：文章探讨了高速铁路（HSR）对全球经济地理与区域发展的深远重塑。高铁通过“空间压缩”将中小城市纳入大都市功能圈，促进“虚拟集聚”并大幅降低碳排放。然而，高铁带来的发展并非均质，中小城市面临人才被一线城市虹吸的风险；高昂的基建成本若缺乏足够人口密度支撑，更可能造成沉重地方债务。高铁成功取决于人口密度门槛、市内交通接驳与站城一体化规划。"
        },
        "section_c1": {
            "title": "Section C · 仔细阅读 Passage 1 (Interactive Television Advertising)",
            "passage": "“It’s been the year of interactive television advertising for the last ten or twelve years,” says Colin Dixon of a digital-media consultancy. Interactive TV advertising, long hyped but never living up to expectations, met skepticism when American cable giant Cablevision rolled out its ambitious interactive advertising platform. For more than a decade, tech gurus had promised that viewers would soon click their television remote controls to instantly order pizza during football broadcasts, purchase designer dresses worn by sitcom actresses, or request detailed automobile brochures. Yet despite billions in venture capital, interactive TV remained a punchline of Silicon Valley overpromising.\nCablevision executives insisted their system was different because it required no cumbersome set-top box upgrades or clunky internet keyboards. Using existing digital remotes, viewers watching conventional 30-second commercials could press a button to open an on-screen menu, request product samples by mail, or download coupon codes directly to their smartphones. Early trial sponsors, including Unilever's Axe body spray and major auto manufacturers, reported viewer engagement rates several times higher than passive broadcast ads.\nHowever, industry analysts remain cautious about whether interactive TV can truly revolutionize advertising economics. The primary obstacle is the psychological nature of television viewing itself. Unlike internet browsing, which is an active, 'lean-forward' experience driven by intentional searching, television has traditionally been a passive, 'lean-back' medium. When exhausted workers slump onto their couches in the evening, they want to be entertained, not invited to engage in commercial transactions.\nFurthermore, the television landscape is undergoing violent fragmentation. Viewers are increasingly abandoning traditional scheduled cable broadcasts in favor of digital streaming platforms, ad-skipping digital video recorders (DVRs), and commercial-free subscription services. Even when traditional commercials air, viewers' attention is rarely focused on the television screen; instead, they glance down at their smartphones or tablets—a phenomenon known as 'second-screening.'\nIf interactive advertising is to achieve enduring commercial viability, media companies must integrate it seamlessly into modern streaming environments. Rather than interrupting entertainment with intrusive transactional prompts, forward-thinking advertisers are experimenting with non-intrusive QR codes, customized programmatic streaming ads, and shoppable content integrated into social video apps. The decade-long dream of interactive TV is finally arriving, but it looks far more like a smartphone app than an old-fashioned television commercial.",
            "questions": [
                {
                    "num": 46,
                    "stem": "What does Colin Dixon mean by saying 'It's been the year of interactive television advertising for the last ten or twelve years'?",
                    "options": [
                        {"label": "A", "text": "Interactive TV ads will become mainstream in 10-12 years."},
                        {"label": "B", "text": "The industry has fiercely debated the technology for a decade."},
                        {"label": "C", "text": "Interactive television has proven exceptionally effective in sitcoms."},
                        {"label": "D", "text": "Interactive TV advertising has repeatedly failed to meet expectations."}
                    ],
                    "answer": "D",
                    "question_zh": "科林·迪克森说“过去十到十二年每年都是互动电视广告年”是什么意思？",
                    "answer_zh": "互动电视广告屡屡未能达到预期的效果。",
                    "explanation": "首段第二句紧接着指出：'Interactive TV advertising, long hyped but never living up to expectations, met skepticism...'，说明该技术多年来一直被吹嘘却从未实现预期成果，对应D项。"
                },
                {
                    "num": 47,
                    "stem": "Why did Cablevision claim its interactive ad system had a competitive advantage?",
                    "options": [
                        {"label": "A", "text": "It was completely free of commercial advertising."},
                        {"label": "B", "text": "It offered lower advertising rates than internet websites."},
                        {"label": "C", "text": "It operated effortlessly on viewers' existing digital remote controls."},
                        {"label": "D", "text": "It exclusively broadcast commercials for luxury sports cars."}
                    ],
                    "answer": "C",
                    "question_zh": "为什么有线电视巨头Cablevision声称其互动广告系统具有竞争优势？",
                    "answer_zh": "它可以在观众现有的数字遥控器上轻松操作无需额外硬件。",
                    "explanation": "第二段指出'it required no cumbersome set-top box upgrades... Using existing digital remotes, viewers watching conventional commercials could press a button...'，对应C项。"
                },
                {
                    "num": 48,
                    "stem": "What inherent psychological barrier hinders interactive television advertising?",
                    "options": [
                        {"label": "A", "text": "Television is intrinsically a passive, relaxing entertainment medium."},
                        {"label": "B", "text": "Viewers are terrified of entering credit card information on screens."},
                        {"label": "C", "text": "Most consumers dislike all forms of corporate marketing."},
                        {"label": "D", "text": "Remote controls are too technologically complex for older adults."}
                    ],
                    "answer": "A",
                    "question_zh": "什么内在的心理障碍阻碍了互动电视广告？",
                    "answer_zh": "电视本质上是一种被动的、放松身心的娱乐媒介。",
                    "explanation": "第三段明确对比：'Unlike internet browsing, which is an active, lean-forward experience... television has traditionally been a passive, lean-back medium'，下班后人们只想放松娱乐而不愿进行交易，对应A项。"
                },
                {
                    "num": 49,
                    "stem": "What does the term 'second-screening' describe in modern viewing behavior?",
                    "options": [
                        {"label": "A", "text": "Purchasing a secondary television set for the home kitchen."},
                        {"label": "B", "text": "Looking down at smartphones while the television is playing."},
                        {"label": "C", "text": "Subscribing to multiple commercial-free streaming platforms."},
                        {"label": "D", "text": "Sharing television accounts among extended family members."}
                    ],
                    "answer": "B",
                    "question_zh": "现代收视行为中的“第二屏幕”现象指的是什么？",
                    "answer_zh": "在电视播放的同时低头看智能手机或平板。",
                    "explanation": "第四段指出：'viewers' attention is rarely focused on the television screen; instead, they glance down at their smartphones or tablets—a phenomenon known as second-screening'，对应B项。"
                },
                {
                    "num": 50,
                    "stem": "How is the long-delayed vision of interactive commercial engagement finally being realized?",
                    "options": [
                        {"label": "A", "text": "Through intrusive full-screen pop-ups on public billboards."},
                        {"label": "B", "text": "Through mandatory purchases required to unlock TV channels."},
                        {"label": "C", "text": "Through integrated mobile features and social streaming environments."},
                        {"label": "D", "text": "Through abandoning all mobile devices in favor of cable boxes."}
                    ],
                    "answer": "C",
                    "question_zh": "长久延迟的互动商业构想最终是如何实现的？",
                    "answer_zh": "通过整合移动端功能与社交流媒体生态。",
                    "explanation": "尾段总结指出互动体验正在通过无侵入二维码、流媒体程序化广告和社交视频APP中的一键购买功能实现，看起来更像手机APP而非传统电视，对应C项。"
                }
            ],
            "main_idea_zh": "本文评述了互动电视广告（Interactive TV Advertising）十几年来“年年被吹捧、年年难兑现”的尴尬现状。Cablevision虽试图利用遥控器简化交互，但电视本质上是“后仰式”被动娱乐媒介，与互联网“前倾式”主动搜索存在天壤之别。加之流媒体兴起与“第二屏幕（边看电视边玩手机）”现象，互动广告正加速向移动端与流媒体生态迁移重塑。",
            "main_idea_en": "The passage analyzes the long-hyped struggles of interactive television ads, examining lean-back psychological hurdles, second-screening habits, and their transformation within modern streaming platforms."
        },
        "section_c2": {
            "title": "Section C · 仔细阅读 Passage 2 (Paul Krugman on Mass Unemployment)",
            "passage": "Amid persistent mass unemployment following the Great Recession, a fashionable consensus hardened among economic commentators and policymakers: joblessness, they insisted, was 'structural.' Millions of workers, the narrative went, lacked the high-tech skills demanded by twenty-first-century employers; their occupations had been permanently displaced by globalization and software automation, leaving them stranded. Because there was supposedly no easy policy fix, politicians argued that the government could do nothing to quickly relieve suffering. The unemployed simply had to wait for decades of retraining programs.\nYet as Nobel laureate Paul Krugman fiercely argues, this bleak structural explanation is almost entirely baseless. When economists examine actual labor market data, the evidence for structural unemployment evaporates. If widespread joblessness were driven by a mismatch between workers' outdated skills and employers' unmet needs, one would expect to see soaring job openings and sharp wage increases in high-demand technical sectors. Instead, wages stagnated across virtually every industry, and employers reported surpluses of qualified applicants for almost every advertised position. High unemployment in America was not structural; it was the direct result of inadequate aggregate demand.\nKrugman points out that the structural excuse is a perennial historical myth. During the Great Depression of the 1930s, prominent economists similarly proclaimed that millions of unemployed coal miners and factory hands were permanently unadaptable to modern industry. A few years later, however, the massive fiscal stimulus of World War II mobilized the entire American economy, and suddenly private industry was desperate to hire and train those supposedly unemployable workers. When demand returned, the skills deficit vanished overnight.\nWhy, then, do claims of vast structural problems multiply so rapidly among elite circles? The answer, Krugman contends, is ideological. Acknowledging that mass unemployment stems from inadequate demand implies an immediate, commonsense remedy: aggressive government fiscal stimulus through investments in public infrastructure, schools, and green energy. But powerful political and corporate forces are ideologically opposed to the whole idea of large-scale public spending. Attributing unemployment to workers' personal skill deficits absolves leaders of responsibility and justifies inaction.\nPolicymakers must abandon the comfortable fiction of structural joblessness. Blaming the victim—telling hardworking men and women that their misery is their own fault for having obsolete skills—is not rigorous economic realism; it is an alibi for cowardice. America’s unemployment crisis could be substantially cured if leaders possessed the moral clarity and political will to act.",
            "questions": [
                {
                    "num": 51,
                    "stem": "What did mainstream economic commentators attribute mass unemployment to after the Great Recession?",
                    "options": [
                        {"label": "A", "text": "Excessive minimum wage laws enforced by labor unions."},
                        {"label": "B", "text": "Deep structural skill mismatches that government could not cure."},
                        {"label": "C", "text": "Sudden demographic declines in the domestic labor force."},
                        {"label": "D", "text": "Widespread worker refusal to relocate to industrial cities."}
                    ],
                    "answer": "B",
                    "question_zh": "大衰退后主流经济评论家将大规模失业归咎于什么？",
                    "answer_zh": "政府无法迅速解决的深层结构性技能错配。",
                    "explanation": "首段指出主流观点认定失业是结构性的（structural），工人们缺乏新技能，且'Because there was supposedly no easy policy fix, politicians argued that the government could do nothing...'，对应B项。"
                },
                {
                    "num": 52,
                    "stem": "What empirical evidence refutes the claim of widespread structural unemployment?",
                    "options": [
                        {"label": "A", "text": "College graduation rates dropped to historical lows."},
                        {"label": "B", "text": "Wages failed to rise even in high-demand technical fields."},
                        {"label": "C", "text": "American factories relocated their operations abroad."},
                        {"label": "D", "text": "Unemployment benefits were slashed by state governments."}
                    ],
                    "answer": "B",
                    "question_zh": "什么经验证据驳斥了广泛存在结构性失业的说法？",
                    "answer_zh": "即使在高需求的技术行业，工资也未能上涨。",
                    "explanation": "第二段指出若真是技能错配，应看到热门行业岗位激增和薪资暴涨，'Instead, wages stagnated across virtually every industry, and employers reported surpluses of qualified applicants...'，对应B项。"
                },
                {
                    "num": 53,
                    "stem": "What lesson does the author draw from the economic mobilization of World War II?",
                    "options": [
                        {"label": "A", "text": "Strong aggregate demand rapidly eliminates supposed skill deficits."},
                        {"label": "B", "text": "Military conflicts inevitably impoverish industrialized nations."},
                        {"label": "C", "text": "Private corporations cannot operate during national emergencies."},
                        {"label": "D", "text": "Vocational retraining requires at least twenty years to succeed."}
                    ],
                    "answer": "A",
                    "question_zh": "作者从二战的经济动员中总结出了什么经验教训？",
                    "answer_zh": "强劲的总需求能够迅速消除所谓的技能短缺问题。",
                    "explanation": "第三段指出二战期间巨大的财政刺激让曾经被认为'无法适应现代工业'的失业工人被企业争先抢后录用，'When demand returned, the skills deficit vanished overnight'，对应A项。"
                },
                {
                    "num": 54,
                    "stem": "Why do elite politicians cling so stubbornly to the structural unemployment narrative?",
                    "options": [
                        {"label": "A", "text": "They genuinely lack basic knowledge of economic statistics."},
                        {"label": "B", "text": "They are ideologically opposed to large-scale public investment."},
                        {"label": "C", "text": "They wish to eliminate all corporate income taxation."},
                        {"label": "D", "text": "They are mandated by the Constitution to prevent budget deficits."}
                    ],
                    "answer": "B",
                    "question_zh": "为什么精英政客如此顽固地坚持“结构性失业”的说法？",
                    "answer_zh": "他们在意识形态上强烈反对大规模公共投资与政府行动。",
                    "explanation": "第四段指出承认总需求不足就意味着要采取公共支出补救措施，但'powerful political and corporate forces are ideologically opposed to the whole idea of large-scale public spending'，对应B项。"
                },
                {
                    "num": 55,
                    "stem": "What is Paul Krugman's primary objective in writing this passage?",
                    "options": [
                        {"label": "A", "text": "To advise workers to seek employment overseas."},
                        {"label": "B", "text": "To encourage students to avoid technical engineering degrees."},
                        {"label": "C", "text": "To expose excuses for inaction and advocate decisive government policy."},
                        {"label": "D", "text": "To praise the resilience of unregulated free market capitalism."}
                    ],
                    "answer": "C",
                    "question_zh": "保罗·克鲁格曼写这篇文章的主要目的是什么？",
                    "answer_zh": "揭露不作为的借口，呼吁政府采取果断坚决的公共政策。",
                    "explanation": "尾段明确指出将失业归咎于工人的技能过时是不作为的借口（an alibi for cowardice），只要领导人拥有道德决断与政治意愿采取行动，失业危机完全可以得到实质性化解，对应C项。"
                }
            ],
            "main_idea_zh": "本文是诺贝尔经济学奖得主保罗·克鲁格曼对“结构性失业论”的有力批驳。经济界常将高失业率归咎于工人技能跟不上时代，然而数据显示各行业薪资普遍停滞、求职者过剩，证明真实根源是总需求不足。二战时期的财政扩张证明，只要需求复苏，所谓的技能短缺一夜之间便会烟消云散。政界之所以坚持“结构性”借口，源自反对政府公共支出的意识形态偏见。作者呼吁破除谎言，采取果断公共投资创造就业。",
            "main_idea_en": "Nobel laureate Paul Krugman dismantles the myth of structural unemployment, demonstrating that mass joblessness stems from deficient aggregate demand rather than worker skill deficits, while exposing ideological excuses for policy inaction."
        }
    })

    # ==========================================
    # 2017年12月 六级真题 (第1套)
    # ==========================================
    sets.append({
        "id": "2017_12_set1",
        "year": "2017",
        "month": "12",
        "set": "第1套",
        "title": "2017年12月 六级阅读真题 (第1套)",
        "theme": "可口可乐历史 / 农业机器人 / 开放科学",
        "section_a": {
            "title": "Section A · 选词填空 (Urban Heat Islands & Microclimates)",
            "passage": "As global urban populations swell toward unprecedented levels, city planners and meteorologists are grappling with the phenomenon of 'urban heat islands.' Because concrete sidewalks, asphalt roadways, and steel skyscrapers absorb and 26 solar radiation far more effectively than rural vegetation, urban centers experience temperatures substantially higher than their surrounding countryside. This temperature 27 is particularly pronounced at night, when dense buildings slowly release stored heat into the night air.\nThe consequences of urban heat islands extend far beyond thermal discomfort. Higher urban temperatures drastically accelerate the formation of ground-level ozone smog, 28 respiratory illnesses such as asthma and bronchitis. Peak summertime heat waves trigger massive spikes in residential electricity demand as millions of air conditioning units operate 29 , straining power transmission grids and increasing fossil fuel emissions from peaker power plants. Moreover, urban heat is not distributed 30 across a metropolis. Lower-income neighborhoods, characterized by fewer trees, sparse parks, and dense concrete, routinely record temperatures several degrees higher than affluent, leafy suburbs—a disparity environmental advocates call 'thermal 31 .'\nTo mitigate this urban furnace effect, pioneering municipalities are implementing innovative urban design 32 . Cities are mandating 'cool roofs' coated with reflective white pigments that bounce solar rays back into the atmosphere before heat can be absorbed. Other metropolises are expanding urban forestry programs, recognizing that tree canopies provide not only cooling shade but also natural evaporative cooling through 33 . Green rooftop gardens, permeable pavements that absorb rainwater, and vertical green walls are transforming drab concrete jungles into living, resilient ecosystems. By reimagining urban spaces with nature-based solutions, cities can protect public health, conserve energy, and build sustainable 34 against a rapidly warming 35 .",
            "word_bank": {
                "A": "retain",
                "B": "differential",
                "C": "exacerbating",
                "D": "continuously",
                "E": "equitably",
                "F": "inequality",
                "G": "strategies",
                "H": "transpiration",
                "I": "defenses",
                "J": "climate",
                "K": "suppress",
                "L": "abruptly",
                "M": "destabilize",
                "N": "fluctuate",
                "O": "reproduce"
            },
            "questions": [
                {"num": 26, "answer": "A", "word": "retain", "analysis": "动词原形与absorb并列，吸收并'留存/积蓄'太阳辐射。"},
                {"num": 27, "answer": "B", "word": "differential", "analysis": "名词作主语，'temperature differential'温差。"},
                {"num": 28, "answer": "C", "word": "exacerbating", "analysis": "现在分词作状语，'exacerbating respiratory illnesses'加剧呼吸道疾病。"},
                {"num": 29, "answer": "D", "word": "continuously", "analysis": "副词修饰operate，空调'持续不断'运行。"},
                {"num": 30, "answer": "E", "word": "equitably", "analysis": "副词修饰distributed，城市热量分布并不'公平/均等'。"},
                {"num": 31, "answer": "F", "word": "inequality", "analysis": "名词短语，'thermal inequality'热不平等。"},
                {"num": 32, "answer": "G", "word": "strategies", "analysis": "名词复数，创新的城市设计'策略'。"},
                {"num": 33, "answer": "H", "word": "transpiration", "analysis": "名词，树冠通过植物'蒸腾作用'实现降温。"},
                {"num": 34, "answer": "I", "word": "defenses", "analysis": "名词复数，建立抵御气候变暖的可持续'防线'。"},
                {"num": 35, "answer": "J", "word": "climate", "analysis": "名词，迅速变暖的'气候'。"}
            ],
            "translation": "随着全球城市人口膨胀至前所未有的规模，城市规划者与气象学者正致力于应对“城市热岛”现象。混凝土人行道、沥青路面和钢铁摩天大楼吸收和储存太阳辐射的效率远高于乡村植被，使得城市中心的气温显著高于周边乡村。这种温差在夜间尤为明显，密集建筑物将白天积蓄的热量缓慢释放到夜间空气中。\n城市热岛的危害远不止体感炎热。高温显著加速了近地面臭氧烟雾的生成，加剧了哮喘和支气管炎等呼吸系统疾病。夏季热浪还会引发住宅用电高峰，千家万户的空调持续运转，导致输电网络不堪重负并增加电厂的碳排放。不仅如此，城市内部的热量分布并不均衡。绿植稀少、水泥遍地的低收入街区温度往往比绿树成荫的富裕郊区高出数度，环保人士将此现象称为“热不平等”。\n为了缓解这种“城市火炉”效应，一些开创性城市正在推行创新的城市设计策略。许多城市强制推广涂有白色高反射涂层的“凉爽屋顶”，在热量被吸收前将其反射回大气中。另一些城市则大力拓展城市森林项目，依靠树冠提供荫凉并通过植物蒸腾作用实现降温。绿色屋顶花园、透水路面和垂直绿化墙正将单调的水泥丛林转变为充满生机与韧性的生态系统。通过因地制宜的自然方案重塑城市空间，城市方能捍卫公众健康、节约能源并构筑抵御气候变暖的坚实防线。",
            "vocabulary": [
                {"w": "differential", "p": "/ˌdɪfəˈrenʃl/", "t": "n. 差额，差异"},
                {"w": "exacerbate", "p": "/ɪɡˈzæsərbeɪt/", "t": "v. 加重，使恶化"},
                {"w": "transpiration", "p": "/ˌtrænspɪˈreɪʃn/", "t": "n. （植物的）蒸腾作用"},
                {"w": "permeable", "p": "/ˈpɜːrmiəbl/", "t": "adj. 可渗透的，透水的"},
                {"w": "equitably", "p": "/ˈekwɪtəbli/", "t": "adv. 公正地，合理平分地"}
            ]
        },
        "section_b": {
            "title": "Section B · 长篇阅读 (Data Sharing: An Open Mind on Open Data in Science)",
            "paragraphs": [
                {"label": "A", "text": "For centuries, scientific discovery has advanced through a curious mixture of fierce rivalry and communal sharing. Researchers toiled in private laboratories, jealously guarding laboratory notebooks until their findings were formally published in peer-reviewed journals. Once in print, findings became public property, allowing fellow scholars to replicate experiments, challenge flaws, and build upon foundations. Today, however, the digital revolution is transforming this ancient rhythm, giving birth to a global movement known as 'Open Science' and its contentious cornerstone: open data."},
                {"label": "B", "text": "In fields ranging from human genomics to particle physics, modern scientific inquiry generates mind-boggling torrents of raw digital data. Yet for decades, the vast majority of this data remained locked inside researchers' private hard drives or proprietary university servers. Studies evaluating published papers found that fewer than 20 percent of authors made their underlying raw datasets accessible to peers upon request. Without access to raw data, verifying whether statistical conclusions were sound or merely mathematical artifacts was nearly impossible."},
                {"label": "C", "text": "This lack of transparency contributed directly to what scientists call the 'reproducibility crisis.' In psychology, medicine, and oncology, independent researchers repeatedly failed to reproduce the results of landmark published studies. In one shocking investigation by biotechnology firm Amgen, scientists attempted to replicate 53 landmark cancer research papers published in top-tier journals; they were able to confirm the findings in only six cases. The revelation sent shockwaves through the scientific establishment, demonstrating that lack of data sharing was wasting billions in research funding."},
                {"label": "D", "text": "To address this crisis, major funding agencies, such as the US National Institutes of Health and Europe’s Wellcome Trust, began mandating that grant recipients deposit raw experimental data into open-access repositories. Leading academic journals like *Nature* and *Science* adopted strict policies requiring authors to provide open data access as a condition of publication. Enthusiasts proclaimed that universal data sharing would democratize discovery, curb academic fraud, and allow researchers around the globe to analyze existing datasets to find cures for disease."},
                {"label": "E", "text": "Yet despite widespread consensus on the theoretical merits of open data, frontline researchers frequently voice deep anxiety about its practical implementation. Collecting high-quality scientific data—such as tracking patients through decade-long clinical trials or conducting deep-sea submersible expeditions—demands years of exhausting labor and millions in grant funding. Junior faculty members and postdoctoral researchers worry that after spending years gathering unique data, predatory competitors with massive computational power will swoop in, analyze the dataset, and publish the glory papers before the original scientists have finished mining their own hard work."},
                {"label": "F", "text": "This dynamic has given rise to the controversial label of 'research parasites'—scholars who build careers analyzing other people’s openly shared datasets without contributing to the grueling physical labor of data collection. While proponents argue that secondary data analysis maximizes the social return on public investment, original data creators argue that existing academic tenure and promotion systems disproportionately reward final publications while providing zero professional credit for curating and sharing datasets."},
                {"label": "G", "text": "Furthermore, sharing raw data is technically complex and financially onerous. Data cannot merely be dumped into a public cloud folder; it must be cleaned, standardized, annotated with metadata, and formatted so that external software can parse it accurately. For underfunded academic labs lacking dedicated bioinformatics staff, preparing datasets for open access consumes hundreds of unpaid hours that would otherwise be dedicated to laboratory experimentation or mentoring graduate students."},
                {"label": "H", "text": "Overcoming these barriers requires reforming the cultural incentives of modern science. Academic institutions must establish formal mechanisms to cite datasets as independent scholarly achievements, granting data creators equal prestige and promotion credits as paper authors. Simultaneously, journals are adopting 'embargo periods' that grant original researchers exclusive rights to analyze their data for a reasonable window before public release. Open science will only flourish when sharing data is recognized not as an altruistic sacrifice, but as a celebrated academic triumph."},
                {"label": "I", "text": "Open data also accelerates machine-learning discoveries across computational biology and climate modeling. When thousands of independently gathered datasets are harmonized into open repositories, deep-learning models can uncover subtle predictive patterns that were invisible within smaller, siloed studies. This algorithmic cross-fertilization enables breakthrough discoveries in protein folding, drug discovery, and atmospheric forecasting."},
                {"label": "J", "text": "Ultimately, democratizing access to raw experimental data fosters public trust in the scientific enterprise. When controversial scientific claims can be independently scrutinized, analyzed, and verified by external citizen scientists and independent watchdog organizations, scientific inquiry defends itself against charges of elite bias or concealed corporate manipulation, reinforcing the empirical bedrock of enlightened society."}
            ],
            "questions": [
                {"num": 36, "stem": "Commercial biotechnology experiments revealed that an astonishingly small proportion of cancer studies could be verified.", "answer": "C"},
                {"num": 37, "stem": "Prominent funding bodies and scientific publications established compulsory rules requiring public deposition of research data.", "answer": "D"},
                {"num": 38, "stem": "Properly preparing and formatting datasets for public scrutiny requires immense time and financial commitments.", "answer": "G"},
                {"num": 39, "stem": "Traditionally, scientists kept their experimental data strictly confidential until findings were officially released in print.", "answer": "A"},
                {"num": 40, "stem": "Junior scholars fear that well-funded rivals might exploit openly accessible data to publish results ahead of them.", "answer": "E"},
                {"num": 41, "stem": "Academic promotion policies must be adjusted to award genuine professional credit to researchers who generate and curate datasets.", "answer": "H"},
                {"num": 42, "stem": "Prior to open data mandates, only a tiny fraction of academic authors voluntarily shared underlying raw data upon inquiry.", "answer": "B"},
                {"num": 43, "stem": "Critics labeled researchers who analyze existing public datasets without conducting fieldwork as parasitic scholars.", "answer": "F"},
                {"num": 44, "stem": "Aggregating publicly shared scientific datasets allows artificial intelligence systems to identify complex patterns.", "answer": "I"},
                {"num": 45, "stem": "Public availability of experimental data strengthens civic confidence in science against accusations of bias.", "answer": "J"}
            ],
            "translation": "长篇阅读解析总结：文章探讨了科学界近年来兴起的“开放数据”（Open Data）运动及其争议。由于传统数据封锁导致的“可重复性危机”（如安进公司重复53篇顶级癌症论文仅成功6篇），基金委与期刊开始强制开源数据。然而，年轻科研人员担忧自身辛苦数年采集的数据被拥有算力优势的“学术寄生虫”抢先发表。此外，清洗和标注元数据需要耗费大量无偿时间。文章呼吁建立数据集独立引用与职称认可机制，并设置合理的独占保护期，以实现开放科学的健康发展。"
        },
        "section_c1": {
            "title": "Section C · 仔细阅读 Passage 1 (The Historical Evolution of Coca-Cola)",
            "passage": "In May 1886, in a modest pharmacy in Atlanta, Georgia, an eccentric chemist named Dr. John Stith Pemberton concocted a sweet, fragrant amber syrup in a brass kettle over an open fire. Pemberton, a Confederate veteran who had developed an addiction to morphine after suffering battlefield injuries during the Civil War, was searching for an invigorating patent medicine that could relieve headaches, calm frazzled nerves, and cure depression without the lethargy of opiates. What he accidentally created became the world's most ubiquitous commercial beverage: Coca-Cola.\nPemberton’s recipe blended extracts from two exotic natural stimulants: the dried leaves of the South American coca plant and the caffeine-rich nuts of the West African kola tree. At the time, coca leaf extract mixed with wine was a fashionable and widely praised health tonic across Europe and North America. However, when the city of Atlanta enacted local temperance laws prohibiting the commercial sale of alcohol in 1885, Pemberton was forced to get around the ban by replacing wine with a sugary syrup base. When carbonated water was accidentally added at a soda fountain, Coca-Cola in its modern bubbly incarnation was born.\nIn its early marketing campaigns, Coca-Cola was promoted not as a recreational thirst-quencher, but as an intellectual health elixir. Advertisements proclaimed it 'The Great National Temperance Beverage' and an 'Ideal Brain Tonic' capable of reviving exhausted businessmen and tired housewives. However, by the late 1890s, medical attitudes toward cocaine had shifted from enthusiasm to alarm. Fearing racialized moral panics and regulatory crackdowns, the company quietly eliminated active cocaine from its extract in 1903, switching to 'spent' coca leaves with the psychoactive alkaloid chemically removed.\nSimilarly, while kola nuts were once shipped by the ton from West Africa to furnish natural caffeine and flavor, the modern drink has long abandoned fresh kola nut extracts, relying instead on commercial caffeine and synthetic flavor formulations to replicate its signature taste. Yet what is remarkable about Coca-Cola is how enduringly stable its flavor identity has remained. Through world wars, cultural revolutions, and corporate expansion across more than 200 nations, the consumer experience of drinking a Coke has remained nearly indistinguishable for over a century.\nCoca-Cola’s evolution from an improvised Victorian medicinal brew to a global cultural icon reveals the power of consumer myth-making. The drink succeeded not because of its original pharmacological promises, but because its stewards understood how to sell optimism, refreshment, and American modernity in a glass bottle.",
            "questions": [
                {
                    "num": 46,
                    "stem": "Why did chemist John Pemberton originally invent the formula that became Coca-Cola?",
                    "options": [
                        {"label": "A", "text": "To win an international culinary innovation prize in Atlanta."},
                        {"label": "B", "text": "To create a non-alcoholic tonic while seeking pain relief."},
                        {"label": "C", "text": "To manufacture a carbonated soda drink for neighborhood children."},
                        {"label": "D", "text": "To establish a national chain of commercial soda fountain shops."}
                    ],
                    "answer": "B",
                    "question_zh": "药剂师约翰·彭伯顿最初为何发明了成为可口可乐的配方？",
                    "answer_zh": "在寻求镇痛替代品的同时开发一种无酒精滋补药剂。",
                    "explanation": "首段提到彭伯顿战伤后寻找非鸦片镇痛提神配方，第二段指出亚特兰大实施禁酒令后他用糖浆替代酒精以绕过禁令，对应B项。"
                },
                {
                    "num": 47,
                    "stem": "What historical circumstance forced Pemberton to replace wine with sugary syrup?",
                    "options": [
                        {"label": "A", "text": "A severe grape blight that devastated local vineyards."},
                        {"label": "B", "text": "Local municipal laws prohibiting the commercial sale of alcohol."},
                        {"label": "C", "text": "Surging international taxes on imported French wine."},
                        {"label": "D", "text": "Customer complaints regarding the bitter flavor of fermented grapes."}
                    ],
                    "answer": "B",
                    "question_zh": "什么历史背景迫使彭伯顿用糖浆代替了葡萄酒？",
                    "answer_zh": "当地市政法规禁止商业销售酒精饮料。",
                    "explanation": "第二段明确指出：'when the city of Atlanta enacted local temperance laws prohibiting the commercial sale of alcohol in 1885, Pemberton was forced to get around the ban by replacing wine with a sugary syrup base'，对应B项。"
                },
                {
                    "num": 48,
                    "stem": "Why was active cocaine quietly removed from the Coca-Cola recipe in 1903?",
                    "options": [
                        {"label": "A", "text": "Shifting medical perceptions and growing alarm over cocaine's dangers."},
                        {"label": "B", "text": "The complete extinction of coca plants in South America."},
                        {"label": "C", "text": "A total decline in consumer demand for caffeinated drinks."},
                        {"label": "D", "text": "A decision to target kindergarten children with advertising."}
                    ],
                    "answer": "A",
                    "question_zh": "为什么1903年可口可乐配方中悄然去除了活性可卡因成分？",
                    "answer_zh": "医学观念的转变以及对可卡因危害的日益警惕。",
                    "explanation": "第三段指出'by the late 1890s, medical attitudes toward cocaine had shifted from enthusiasm to alarm. Fearing racialized moral panics and regulatory crackdowns, the company quietly eliminated active cocaine...'，对应A项。"
                },
                {
                    "num": 49,
                    "stem": "What is notable about the taste of modern Coca-Cola despite recipe changes?",
                    "options": [
                        {"label": "A", "text": "It changes flavor dramatically with every passing decade."},
                        {"label": "B", "text": "It is completely different from the historical nineteenth-century syrup."},
                        {"label": "C", "text": "It has maintained exceptional consistency for over a hundred years."},
                        {"label": "D", "text": "It is dictated exclusively by imported West African kola nuts."}
                    ],
                    "answer": "C",
                    "question_zh": "尽管配方经历演变，现代可口可乐的口味有什么显著特征？",
                    "answer_zh": "一百多年来它保持了非凡的一致性与稳定性。",
                    "explanation": "第四段指出：'what is remarkable about Coca-Cola is how enduringly stable its flavor identity has remained... nearly indistinguishable for over a century'，对应C项。"
                },
                {
                    "num": 50,
                    "stem": "What is the central theme of this passage?",
                    "options": [
                        {"label": "A", "text": "The chemical manufacturing processes of carbonated soda fountains."},
                        {"label": "B", "text": "The historical journey of Coca-Cola from patent medicine to global icon."},
                        {"label": "C", "text": "The agricultural harvesting techniques of kola nuts in Africa."},
                        {"label": "D", "text": "The legal controversies surrounding Atlanta's temperance legislation."}
                    ],
                    "answer": "B",
                    "question_zh": "本文的中心主旨是什么？",
                    "answer_zh": "可口可乐从维多利亚时代专利药剂蜕变为全球文化符号的历史轨迹。",
                    "explanation": "全文从彭伯顿煮制糖浆作为提神药剂起笔，历经去酒精、去可卡因、人工风味替代，最终成长为跨越百年的全球文化符号，对应B项。"
                }
            ],
            "main_idea_zh": "本文追溯了世界知名饮料可口可乐的传奇诞生与演变史。药剂师彭伯顿原本为了战后镇痛和抗抑郁研制含有古柯叶与可乐果成分的专利药水，后因亚特兰大禁酒令被迫将酒底改为糖浆，误打误撞配入苏打水成就经典气泡饮料。随着公众对毒品认知的改变，可卡因被剔除，可乐果亦被人工风味取代，但其经典口味跨越百年未曾改变，成为工业化现代性与消费主义神话的象征。",
            "main_idea_en": "The passage chronicles the fascinating evolution of Coca-Cola from a nineteenth-century patent medicine and temperance beverage into an iconic, globally ubiquitous cultural brand."
        },
        "section_c2": {
            "title": "Section C · 仔细阅读 Passage 2 (The Agricultural Robotics Revolution)",
            "passage": "Across the rolling fields of the industrialized world, agriculture is embarking on an unprecedented technological revolution. Beset by severe labor shortages, rising wages, and mounting pressures to feed a burgeoning global population while curbing environmental harm, farmers are turning to agricultural robotics. Autonomous tractors guided by satellite GPS plow fields through the dead of night, drone swarms survey soil moisture and crop health from the skies, and robotic harvesters gently pick delicate fruits without bruising their skin. What was once speculative science fiction has become a commercial reality.\nHistorically, agricultural mechanization was characterized by brute-force scale: colossal diesel combines and massive sprayers that treated entire square miles of crops identically. However, this indiscriminate approach required vast quantities of chemical herbicides and synthetic fertilizers, leading to severe soil degradation and pesticide runoff into aquatic ecosystems. By contrast, the hallmark of agricultural robotics is exquisite precision. Equipped with multispectral cameras and machine learning algorithms, modern robotic weeders can distinguish between cash crop seedlings and invasive weeds in milliseconds, delivering targeted micro-bursts of herbicide or incinerating weeds with laser beams. This precision reduces chemical use by up to 90 percent.\nFurthermore, robotic agriculture offers a critical lifeline in the face of an acute farm labor crisis. Across North America, Europe, and East Asia, agricultural workforces are aging rapidly, and younger generations show little inclination to endure the grueling, backbreaking physical labor of planting and harvesting in extreme weather. Immigration restrictions and border controls have exacerbated the seasonal harvest labor deficit, leaving millions of dollars in ripe produce to rot unpicked in fields. Robots do not suffer from fatigue, work in blistering heat or pitch darkness, and never demand overtime pay.\nNonetheless, the robotic revolution presents steep economic hurdles for smallholder farmers. Cutting-edge agricultural robots carry astronomical price tags, frequently exceeding several hundred thousand dollars. Large corporate agribusinesses with vast capital reserves can easily absorb these investments and amortize the costs across thousands of acres. For family farms operating on razor-thin profit margins, however, the inability to purchase high-tech automation threatens to widen the competitive divide, accelerating the consolidation of farmland into the hands of corporate agricultural monopolies.\nTo ensure that agricultural technology promotes rural equity rather than corporate concentration, innovative financial models are beginning to emerge. Tech startups are offering 'Robotics-as-a-Service' (RaaS), where farmers hire autonomous harvesting fleets on a per-acre or per-day basis without purchasing the underlying hardware. Agricultural cooperatives are also pooling community resources to purchase shared robotic equipment. The robotic transformation of farming is inevitable; the challenge ahead is ensuring that its abundance enriches rural farming communities rather than displacing them.",
            "questions": [
                {
                    "num": 51,
                    "stem": "What major factors have spurred modern farmers to adopt agricultural robotics?",
                    "options": [
                        {"label": "A", "text": "Severe labor shortages, rising wages, and environmental pressures."},
                        {"label": "B", "text": "Government mandates outlawing human participation in farm work."},
                        {"label": "C", "text": "Rapidly declining food prices across global retail supermarkets."},
                        {"label": "D", "text": "The total exhaustion of international satellite navigation networks."}
                    ],
                    "answer": "A",
                    "question_zh": "促使现代农场主采纳农业机器人的主要动因是什么？",
                    "answer_zh": "严重的劳动力短缺、工资上涨以及环保压力。",
                    "explanation": "首段第二句明确指出：'Beset by severe labor shortages, rising wages, and mounting pressures to feed a burgeoning global population while curbing environmental harm, farmers are turning to agricultural robotics'，对应A项。"
                },
                {
                    "num": 52,
                    "stem": "How do modern agricultural robots differ fundamentally from historical machinery?",
                    "options": [
                        {"label": "A", "text": "They consume vastly more chemical fertilizer per square acre."},
                        {"label": "B", "text": "They operate with exquisite precision rather than indiscriminate brute force."},
                        {"label": "C", "text": "They are exclusively powered by manual horse traction."},
                        {"label": "D", "text": "They require continuous direct human steering on every row."}
                    ],
                    "answer": "B",
                    "question_zh": "现代农业机器人与传统农业机械在本质上有何不同？",
                    "answer_zh": "它们以精细化的精准度运作，而非盲目的粗放力量。",
                    "explanation": "第二段指出传统农机以粗放规模为特征，而'the hallmark of agricultural robotics is exquisite precision... delivering targeted micro-bursts of herbicide or incinerating weeds with laser beams'，对应B项。"
                },
                {
                    "num": 53,
                    "stem": "Why has finding seasonal human farm labor become extraordinarily difficult?",
                    "options": [
                        {"label": "A", "text": "High school graduates are forbidden by law from visiting farms."},
                        {"label": "B", "text": "Aging populations and younger workers' aversion to grueling physical labor."},
                        {"label": "C", "text": "Robots have physically seized all farmland borders."},
                        {"label": "D", "text": "Farming yields have fallen to zero across North America."}
                    ],
                    "answer": "B",
                    "question_zh": "为什么雇佣季节性农业劳动力变得异常艰难？",
                    "answer_zh": "劳动力老龄化以及年轻一代厌恶繁重的农田体力劳动。",
                    "explanation": "第三段指出'agricultural workforces are aging rapidly, and younger generations show little inclination to endure the grueling, backbreaking physical labor...'，对应B项。"
                },
                {
                    "num": 54,
                    "stem": "What danger does the high cost of robotics pose to family farms?",
                    "options": [
                        {"label": "A", "text": "Family farmers will all be imprisoned for lack of technology."},
                        {"label": "B", "text": "It widens the competitive divide, favoring corporate agribusiness monopolies."},
                        {"label": "C", "text": "It forces family farmers to destroy their own crop seeds."},
                        {"label": "D", "text": "It causes robots to intentionally sabotage agricultural soil."}
                    ],
                    "answer": "B",
                    "question_zh": "高昂的机器人成本对家庭农场构成了什么威胁？",
                    "answer_zh": "拉大竞争鸿沟，使得企业化农业垄断巨头占据更大优势。",
                    "explanation": "第四段指出'the inability to purchase high-tech automation threatens to widen the competitive divide, accelerating the consolidation of farmland into the hands of corporate agricultural monopolies'，对应B项。"
                },
                {
                    "num": 55,
                    "stem": "How can the 'Robotics-as-a-Service' (RaaS) model help smaller agricultural operations?",
                    "options": [
                        {"label": "A", "text": "By allowing farmers to lease robotic fleets without paying massive upfront costs."},
                        {"label": "B", "text": "By providing farmers with free diesel fuel for twenty years."},
                        {"label": "C", "text": "By replacing agricultural crops with artificial plastic fruits."},
                        {"label": "D", "text": "By forcing big agribusiness corporations to donate their land."}
                    ],
                    "answer": "A",
                    "question_zh": "“机器人即服务”（RaaS）模式如何帮助中小型农场经营？",
                    "answer_zh": "允许农户按需租赁机器人车队，无需承受巨额前期购机成本。",
                    "explanation": "尾段明确提到：'Tech startups are offering Robotics-as-a-Service (RaaS), where farmers hire autonomous harvesting fleets on a per-acre or per-day basis without purchasing the underlying hardware'，对应A项。"
                }
            ],
            "main_idea_zh": "本文展望了农业机器人革命对全球现代农业的颠覆性重构。面对严峻的劳动力断层、工资暴涨与环保指标，自动驾驶拖拉机、巡检无人机与智能采摘机器人应运而生。相较于传统粗放机械，现代机器人凭借机器视觉与AI实现靶向精准施药除草，节约高达90%化学农药。然而，昂贵的初期购置成本令家庭小农望而却步，加剧土地向农业巨头集中的风险。“机器人即服务”（RaaS）与合作社共享等创新商业模式正在为中小农场开辟生机。",
            "main_idea_en": "The passage explores the agricultural robotics revolution, contrasting precision automation with legacy brute-force mechanization while addressing rural labor shortages, corporate consolidation risks, and innovative RaaS leasing models."
        }
    })

    # ==========================================
    # 2021年12月 六级真题 (第1套)
    # ==========================================
    sets.append({
        "id": "2021_12_set1",
        "year": "2021",
        "month": "12",
        "set": "第1套",
        "title": "2021年12月 六级阅读真题 (第1套)",
        "theme": "线上教育专注力 / 远程办公与城市经济 / 生态环保",
        "section_a": {
            "title": "Section A · 选词填空 (Urban Wildlife and Biodiversity)",
            "passage": "For decades, conventional urban planning viewed cities as the antithesis of the natural world—concrete environments designed to 26 wildlife and replace natural habitats with engineered infrastructure. Wild animals were seen as pests to be 27 or unwelcome intruders that posed health hazards to human inhabitants. However, a profound paradigm shift is sweeping urban ecology. Scientists and landscape architects now recognize that cities can serve as unexpected 28 of biodiversity, providing vital refuges for species facing habitat loss in rural agricultural landscapes.\nEcological field surveys demonstrate that cities often host surprisingly diverse animal populations. Peregrine falcons nest on high-rise skyscraper ledges, which 29 the steep cliff faces of their ancestral habitats, hunting urban pigeons with devastating speed. In suburban gardens and municipal parks, pollinator populations—such as wild bees and butterflies—frequently thrive in greater abundance and 30 than on surrounding industrial farmlands heavily sprayed with synthetic insecticides. Urban microclimates, characterized by warmer nighttime temperatures, also allow certain species to 31 their foraging seasons.\nTo deliberately nurture urban fauna, forward-thinking metropolises are adopting 'biophilic' design principles. Rather than manicured ornamental lawns that require chemical fertilizers and offer zero nutritional value to animals, cities are planting native wildflower meadows, installing bee hotels, and creating 'green corridors' that allow animals to 32 safely through dense urban districts without crossing treacherous multilane highways. Retrofitting buildings with bird-safe patterned glass prevents millions of fatal 33 each year. Cultivating urban nature does not merely protect wildlife; it also yields immense psychological 34 for human residents. Daily contact with bird song, green trees, and natural beauty lowers blood pressure, reduces anxiety, and fosters an enduring sense of community 35 .",
            "word_bank": {
                "A": "exclude",
                "B": "exterminated",
                "C": "sanctuaries",
                "D": "replicate",
                "E": "diversity",
                "F": "prolong",
                "G": "navigate",
                "H": "collisions",
                "I": "dividends",
                "J": "wellbeing",
                "K": "incur",
                "L": "recklessly",
                "M": "destabilize",
                "N": "fluctuate",
                "O": "reproduce"
            },
            "questions": [
                {"num": 26, "answer": "A", "word": "exclude", "analysis": "动词不定式，城市设计旨在'排除/排斥'野生动物。"},
                {"num": 27, "answer": "B", "word": "exterminated", "analysis": "被动语态，野生动物被视为应当被'消灭/清除'的害虫。"},
                {"num": 28, "answer": "C", "word": "sanctuaries", "analysis": "名词复数，城市可以成为意想不到的生物多样性'庇护所/避难所'。"},
                {"num": 29, "answer": "D", "word": "replicate", "analysis": "动词原形，摩天大楼壁立的边缘'模仿/复制'了自然悬崖峭壁。"},
                {"num": 30, "answer": "E", "word": "diversity", "analysis": "名词与abundance并列，授粉昆虫具有更高的丰富度与'多样性'。"},
                {"num": 31, "answer": "F", "word": "prolong", "analysis": "动词原形，温暖的微气候让动物得以'延长'觅食期。"},
                {"num": 32, "answer": "G", "word": "navigate", "analysis": "动词原形，允许动物在穿过密集街区时安全'通行/穿梭'。"},
                {"num": 33, "answer": "H", "word": "collisions", "analysis": "名词复数，防鸟撞玻璃预防了数以百万计的致命'碰撞'。"},
                {"num": 34, "answer": "I", "word": "dividends", "analysis": "名词复数，'psychological dividends'心理红利/益处。"},
                {"num": 35, "answer": "J", "word": "wellbeing", "analysis": "名词短语，'community wellbeing'社区福祉与幸福感。"}
            ],
            "translation": "数十年来，传统城市规划一直将城市视作自然界的对立面——纯粹由钢筋水泥构筑、旨在将野生生物排除在外并以人工设施取代自然栖息地的环境。野生动物常被当作应被彻底扑灭的害虫，或是对市民健康构成隐患的不受欢迎的不速之客。然而，一场深刻的范式变革正在席卷城市生态学领域。科学家与景观设计师如今深刻认识到，城市可以成为生物多样性意想不到的“庇护所”，为因周边农田开发而丧失家园的各种物种提供至关重要的避难空间。\n野外生态调查显示，现代城市中往往繁衍着令人惊叹的多样化动物种群。游隼在摩天大楼的屋檐壁立处筑巢——这完美复刻了其祖辈生活的天然悬崖，并以惊人极速捕猎城市鸽群。在郊区花园与市政公园中，野生蜜蜂与蝴蝶等授粉昆虫群落的丰度与多样性，甚至普遍超越了周边那些喷洒大量合成杀虫剂的工业化农田。城市热岛带来的温暖夜间微气候，还使某些动物得以延长其觅食与生长季节。\n为了有意识地呵护城市动物，前瞻性城市正积极采纳“亲自然”设计原则。相较于需要化肥且对生态无益的修剪草坪，城市开始广植本土野花草甸、搭建蜜蜂旅馆，并建设“生态绿色走廊”，使动物能够在不横穿危险多车道公路的前提下在密集街区间安全穿梭。为建筑物加装防鸟撞图案玻璃，每年可避免数以百万计的致命撞击事故。在城市中拥抱自然不仅庇护了野生动物，还给居民带来了巨大的心理红利。日常耳闻鸟语、目睹绿意与自然美景能够显著降低血压、舒缓焦虑，并培育持久的社区幸福感。",
            "vocabulary": [
                {"w": "sanctuary", "p": "/ˈsæŋktʃuəri/", "t": "n. 庇护所，避难地"},
                {"w": "replicate", "p": "/ˈreplɪkeɪt/", "t": "v. 复制，重现"},
                {"w": "pollinator", "p": "/ˈpɒləneɪtər/", "t": "n. 授粉媒介（如蜜蜂、蝴蝶）"},
                {"w": "biophilic", "p": "/ˌbaɪoʊˈfɪlɪk/", "t": "adj. 亲自然的，热爱生命的"},
                {"w": "wellbeing", "p": "/ˌwelˈbiːɪŋ/", "t": "n. 幸福，福祉，健康"}
            ]
        },
        "section_b": {
            "title": "Section B · 长篇阅读 (Remote Work and the Restructuring of Urban Geography)",
            "paragraphs": [
                {"label": "A", "text": "For more than two centuries, the physical reality of human economic life was anchored to a simple, unyielding commute: workers left their homes in the morning, traveled to centralized physical workplaces, and returned in the evening. Industrialization concentrated labor around steam engines and factory belts; the corporate white-collar revolution assembled millions into suburban commuter trains heading toward gleaming downtown skyscrapers. Yet the abrupt shock of global telecommuting shattered this spatial equilibrium overnight, initiating what urban economists call the greatest reordering of economic geography since the invention of the automobile."},
                {"label": "B", "text": "When emergency health measures forced millions of knowledge workers into home offices, corporate skeptics predicted a catastrophic collapse in employee productivity. Instead, enterprise after enterprise discovered that output remained steady or even surged. Liberated from grueling daily commutes that consumed hundreds of hours each year, professionals embraced the flexibility of remote arrangements. Even as offices fully reopened, workers adamantly resisted a full-time return to the five-day cubicle routine, compelling employers to negotiate hybrid compromises."},
                {"label": "C", "text": "This newfound spatial autonomy triggered what researchers term the 'Donut Effect.' While core business districts in superstar cities saw foot traffic plunge and office vacancies climb to historic highs, surrounding outer suburbs, satellite towns, and scenic rural regions experienced an unprecedented housing boom. Workers no longer needed to pay exorbitant urban rents to live within twenty minutes of an office; given the requirement to commute only once or twice a week, they eagerly traded downtown apartments for spacious suburban homes with dedicated home offices and backyards."},
                {"label": "D", "text": "The repercussions for traditional central business districts have been seismic. In metropolitan hubs like New York, San Francisco, and London, urban ecosystems were engineered around the daily influx of high-earning commuters. Sandwich delis, dry cleaners, fitness studios, and public transit agencies derived the bulk of their revenue from workday crowds. With office occupancy rates stubbornly hovering between 40 and 60 percent, retail establishments face bankruptcy, and municipal transit systems confront catastrophic 'fiscal cliffs.'"},
                {"label": "E", "text": "Furthermore, the devaluation of commercial real estate poses severe risks to municipal budgets. In major cities, commercial property taxes constitute a vital revenue pillar that finances essential public services, including public education, firefighting, policing, and sanitation. As institutional landlords renegotiate commercial leases at deep discounts or default on office building mortgages, declining property assessments threaten to starve city halls of operating revenues, sparking fears of a downward municipal spiral."},
                {"label": "F", "text": "Yet remote work is far from a universal luxury. Sociologists emphasize that the remote work revolution has widened existing class divides. Knowledge professionals—software engineers, lawyers, marketers, and financial analysts—enjoy substantial wage premiums alongside the privilege of geographic flexibility. Meanwhile, frontline service personnel, healthcare workers, hospitality staff, and factory laborers must continue to commute daily, bearing higher transportation costs and physical exposure risks without receiving remote flexibility."},
                {"label": "G", "text": "In response to office vacancies, forward-thinking cities are embarking on ambitious architectural transformations. Progressive urban planners are subsidizing the conversion of outdated commercial towers into residential apartment complexes, live-work lofts, and community arts hubs. Rather than mono-functional commercial monocultures that turn into ghost towns after 5:00 PM, downtowns are being reimagined as vibrant, mixed-use neighborhoods with 24-hour vitality, pedestrian plazas, and abundant green space."},
                {"label": "H", "text": "The ultimate legacy of the telecommuting revolution is not the demise of cities, but their liberation from the tyranny of the commute. By severing the mandatory tether between where people earn their livelihoods and where they sleep, remote and hybrid models grant individuals greater agency over their lives. Cities that successfully pivot from commercial commuter hubs to human-centric cultural capitals will thrive in this new landscape, proving once again that urban civilization endures by continually reinventing itself."},
                {"label": "I", "text": "Simultaneously, secondary and tertiary cities are enjoying unprecedented economic vitality. Formerly struggling rust-belt municipalities and scenic rural mountain towns have launched incentive programs offering cash grants and co-working subsidies to attract footloose telecommuters. These influxes of educated, well-paid professionals inject valuable purchasing power into local downtown businesses, revitalizing historic main streets across the countryside."},
                {"label": "J", "text": "Nevertheless, local municipal governments must deliberately manage the side effects of remote-worker migration. Rapid influxes of high-earning teleworkers into smaller rural communities often drive up residential real estate prices and displace long-term working-class locals. Equitable urban-regional development requires targeted investments in affordable housing and protective zoning ordinances alongside telework incentives."}
            ],
            "questions": [
                {"num": 36, "stem": "Commercial property valuation declines threaten to undermine tax revenues that fund crucial municipal public services.", "answer": "E"},
                {"num": 37, "stem": "Workers strongly opposed resuming a full-time office schedule, pushing corporate leaders toward hybrid arrangements.", "answer": "B"},
                {"num": 38, "stem": "Transforming empty office skyscrapers into residential complexes offers a viable path to revive central business districts.", "answer": "G"},
                {"num": 39, "stem": "The sudden transition to telecommuting dismantled an economic commute routine that had endured for over two hundred years.", "answer": "A"},
                {"num": 40, "stem": "Unequal access to telecommuting privileges has exacerbated economic divides between knowledge workers and frontline staff.", "answer": "F"},
                {"num": 41, "stem": "Commuter drops have inflicted severe financial distress on downtown service retailers and public transportation networks.", "answer": "D"},
                {"num": 42, "stem": "The 'Donut Effect' describes an exodus of residents from central business cores toward spacious suburban territories.", "answer": "C"},
                {"num": 43, "stem": "Rather than killing urban centers, remote flexibility gives people greater freedom and drives cities to reinvent themselves.", "answer": "H"},
                {"num": 44, "stem": "Smaller secondary cities and rural towns attract well-paid telecommuters through targeted financial subsidies.", "answer": "I"},
                {"num": 45, "stem": "Rapid migration of remote workers into small towns risks driving up local housing costs and displacing residents.", "answer": "J"}
            ],
            "translation": "长篇阅读解析总结：文章探讨了远程办公对城市经济地理的重构效应。两百年来以通勤为核心的职场模式被远程办公打破，企业发现居家办公效率未降反增，催生了“甜甜圈效应”——核心商务区写字楼空置率骤升，而外围郊区和卫星城因居住空间优势迎来房价繁荣。这直接重创了市中心依托通勤客流的餐饮零售业、公共交通系统及商业地产税收基石。此外，远程特权也拉大了知识阶层与一线服务工人的阶层鸿沟。城市必须通过“商改住”、步行化与功能复合化重塑活力。"
        },
        "section_c1": {
            "title": "Section C · 仔细阅读 Passage 1 (Online Learning & Cognitive Endurance)",
            "passage": "The rapid expansion of online higher education, accelerated by digital communication platforms, has undeniably democratized access to university instruction. Students residing thousands of miles from premier institutions can now enroll in specialized degree programs, balancing coursework with professional obligations. Yet as millions of undergraduates shifted to laptop-based learning environments, cognitive scientists and educational psychologists began uncovering a disconcerting reality: the digital medium fundamentally alters how human attention functions during the learning process.\nIn a traditional lecture theater or seminar room, physical architecture reinforces cognitive focus. The physical presence of a professor, the shared gaze of peers, and the absence of extraneous personal screens create an immersive social contract that discourages distraction. In contrast, online learning occurs on the very same digital interface that hosts email inboxes, social media feeds, streaming video games, and instant messaging apps. On a computer screen, serious academic inquiry must constantly compete against algorithms engineered specifically to hijack human dopamine pathways.\nLaboratory eye-tracking experiments conducted with university undergraduates reveal what researchers call 'shallow digital scanning.' When reading long academic texts on printed physical paper, students engage in deep, linear reading: their gaze moves methodically across paragraphs, pausing to reflect on complex arguments and integrating disparate concepts into working memory. When reading identical texts on digital screens, however, gaze patterns shift into an erratic 'F-shaped' pattern: students scan the first two sentences, skip rapidly down the left margin, and skim superficial keywords without digesting nuanced counterarguments.\nThis cognitive skimming takes a devastating toll on long-term retention and conceptual mastery. When students absorb course materials in an environment characterized by chronic digital interruptions, their working memory becomes overloaded with cognitive noise. Information is processed superficially, preventing the consolidation of knowledge into long-term memory structures in the brain's cortex. Consequently, while online learners frequently perform adequately on multiple-choice quizzes administered immediately after watching a lecture, their capacity to synthesize complex theories or apply principles to novel case studies several weeks later deteriorates dramatically.\nAddressing the cognitive deficits of online education requires redesigning digital pedagogies. Passive, pre-recorded sixty-minute video lectures must be abandoned in favor of modular, interactive learning blocks. Online instructors must embed frequent active-recall quizzes, facilitate small-group synchronous discussions, and explicitly train students in digital hygiene—teaching them to shut down superfluous browser tabs and silence notifications before studying. As higher education increasingly embraces hybrid models, the defining challenge will not be the technical delivery of content, but the deliberate cultivation of sustained cognitive endurance.",
            "questions": [
                {
                    "num": 46,
                    "stem": "What significant benefit has the growth of online higher education delivered?",
                    "options": [
                        {"label": "A", "text": "It completely abolished the requirement for academic testing."},
                        {"label": "B", "text": "It made university learning accessible regardless of geographic location."},
                        {"label": "C", "text": "It eliminated all operational expenditures for universities."},
                        {"label": "D", "text": "It guaranteed immediate high-paying employment for all graduates."}
                    ],
                    "answer": "B",
                    "question_zh": "线上高等教育的发展带来了什么显著益处？",
                    "answer_zh": "使大学学习不再受地理空间限制。",
                    "explanation": "首段前两句明确指出：'The rapid expansion of online higher education... has undeniably democratized access to university instruction. Students residing thousands of miles from premier institutions can now enroll...'，对应B项。"
                },
                {
                    "num": 47,
                    "stem": "Why does a physical classroom environment foster better cognitive focus than a laptop screen?",
                    "options": [
                        {"label": "A", "text": "Classroom air conditioning prevents students from falling asleep."},
                        {"label": "B", "text": "Social presence and architectural space naturally discourage distraction."},
                        {"label": "C", "text": "Professors in classrooms speak with louder and clearer voices."},
                        {"label": "D", "text": "University lecture halls forbid all paper notebooks and pens."}
                    ],
                    "answer": "B",
                    "question_zh": "为什么物理课堂环境比笔记本屏幕更能促进认知专注？",
                    "answer_zh": "人际共在的社交约束与空间环境自然抑制了分心行为。",
                    "explanation": "第二段指出传统课堂中'The physical presence of a professor, the shared gaze of peers, and the absence of extraneous personal screens create an immersive social contract that discourages distraction'，对应B项。"
                },
                {
                    "num": 48,
                    "stem": "What does eye-tracking research reveal about how students read on digital screens?",
                    "options": [
                        {"label": "A", "text": "They read significantly slower and memorize every comma."},
                        {"label": "B", "text": "They engage in superficial, erratic scanning rather than deep linear reading."},
                        {"label": "C", "text": "They refuse to read any sentences that contain numerals."},
                        {"label": "D", "text": "Their eye muscles suffer permanent physical paralysis."}
                    ],
                    "answer": "B",
                    "question_zh": "眼动追踪研究揭示了学生在电子屏幕上的什么阅读习惯？",
                    "answer_zh": "他们进行浅层且跳跃式的扫读，而非深度的线性精读。",
                    "explanation": "第三段指出屏幕阅读会呈现不规则的F型轨迹，'students scan the first two sentences, skip rapidly down the left margin, and skim superficial keywords without digesting nuanced counterarguments'，对应B项。"
                },
                {
                    "num": 49,
                    "stem": "What severe cognitive consequence results from chronic online study interruptions?",
                    "options": [
                        {"label": "A", "text": "Impaired long-term retention and diminished capacity to synthesize complex ideas."},
                        {"label": "B", "text": "Complete loss of auditory hearing across high-frequency ranges."},
                        {"label": "C", "text": "An irresistible compulsion to switch academic majors every term."},
                        {"label": "D", "text": "Immediate failure on simple multiple-choice quizzes."}
                    ],
                    "answer": "A",
                    "question_zh": "线上学习中的频繁干扰会导致什么严重的认知后果？",
                    "answer_zh": "长期记忆留存受损，综合理解复杂概念的能力急剧下降。",
                    "explanation": "第四段指出工作记忆超载使得信息无法固化至长时记忆，导致学生'capacity to synthesize complex theories or apply principles to novel case studies several weeks later deteriorates dramatically'，对应A项。"
                },
                {
                    "num": 50,
                    "stem": "What reform does the author advocate for online pedagogical instruction?",
                    "options": [
                        {"label": "A", "text": "Mandating twelve-hour live lectures without any breaks."},
                        {"label": "B", "text": "Replacing long passive videos with interactive, modular learning blocks."},
                        {"label": "C", "text": "Completely eliminating all internet technology from universities."},
                        {"label": "D", "text": "Abolishing all active-recall quizzes and class discussions."}
                    ],
                    "answer": "B",
                    "question_zh": "针对线上教学，作者主张采取什么教学改革？",
                    "answer_zh": "用交互式模块化学习模块取代长篇被动听课视频。",
                    "explanation": "尾段明确呼吁：'Passive, pre-recorded sixty-minute video lectures must be abandoned in favor of modular, interactive learning blocks'，对应B项。"
                }
            ],
            "main_idea_zh": "本文从认知科学与教育心理学角度剖析了线上高等教育的隐性挑战。虽然网络教学打破了地域限制，但在同一块诱惑遍布的数字屏幕上，算法严重争夺着学生的注意力。眼动实验表明，电子阅读常退化为浮躁的“F型浅层扫视”，阻碍信息向大脑长时记忆的固化沉淀，削弱理论整合与深层应用能力。作者呼吁用小颗粒度、模块化且富于即时互动的教学设计取代枯燥的长视频，主动培养数字专注力。",
            "main_idea_en": "The passage investigates the cognitive costs of online education, demonstrating how screen reading fosters shallow skimming and impairs long-term memory consolidation while recommending interactive modular redesigns."
        },
        "section_c2": {
            "title": "Section C · 仔细阅读 Passage 2 (Telecommuting and the Urban Economic Fabric)",
            "passage": "The global surge in telecommuting has sparked an intense debate among economists regarding the future of the modern metropolis. Throughout the industrial era, cities derived their economic supremacy from geographic concentration: agglomeration economies brought corporations, specialized talent, and support industries together, generating immense productivity gains and intellectual sparks. Today, as high-speed broadband and collaborative software prove that knowledge work can thrive beyond office towers, skeptics argue that the economic justification for the dense city has evaporated, heralding an era of urban decay.\nYet historical perspective suggests that predictions of the 'death of distance' and the demise of cities are wildly premature. Over the past century, technological innovations—from the telephone and facsimile machine to personal computers—were repeatedly expected to empty out cities by enabling remote collaboration. In each instance, however, technological connectivity paradoxically increased the value of face-to-face contact. When routine communication becomes cheap and frictionless, nuanced, trust-building human interactions—the kind that forge partnerships, spark creative breakthroughs, and negotiate delicate contracts—become all the more precious.\nRather than rendering cities obsolete, telecommuting is accelerating an overdue evolution in urban design and functionality. For decades, urban centers were distorted by the brutal demands of the 9-to-5 commuter economy. Downtown cores became sterile concrete canyons designed around high-capacity highways and parking garages, effectively dead zones after dark. High housing costs drove middle-class families out to far-flung suburbs, subjecting millions to grueling, soul-crushing daily commutes.\nThe decline of mandatory full-time in-person office work liberates cities to become what urbanists call 'consumption and connection centers.' Urban vitality in the twenty-first century is driven not by captive corporate workers trudging into cubicles, but by high concentrations of culture, gastronomy, performing arts, universities, and vibrant public spaces. People do not move to cities merely to sit in an office; they move to cities for the serendipity of meeting brilliant, diverse peers and immersing themselves in dynamic social environments.\nCities that cling to outdated twentieth-century models—attempting to force workers back into desks through political browbeating—will inevitably decline. Conversely, metropolises that embrace flexibility, converting redundant office space into affordable housing and investing aggressively in pedestrianized plazas and green transit, will flourish. The future city belongs not to the commuter, but to the community.",
            "questions": [
                {
                    "num": 51,
                    "stem": "What traditional economic concept gave historical cities their competitive preeminence?",
                    "options": [
                        {"label": "A", "text": "Agglomeration economies derived from dense physical concentration."},
                        {"label": "B", "text": "Mandatory isolation from international trade networks."},
                        {"label": "C", "text": "Abundant agricultural farmland inside urban boundaries."},
                        {"label": "D", "text": "Exclusive government subsidies for rural commuting."}
                    ],
                    "answer": "A",
                    "question_zh": "传统上赋予历史城市竞争优势的核心经济概念是什么？",
                    "answer_zh": "源自地理密集集聚的集聚经济效应。",
                    "explanation": "首段第二句指出：'Throughout the industrial era, cities derived their economic supremacy from geographic concentration: agglomeration economies brought corporations, specialized talent... together'，对应A项。"
                },
                {
                    "num": 52,
                    "stem": "What historical paradox occurred with previous communication innovations like the telephone?",
                    "options": [
                        {"label": "A", "text": "They caused the immediate bankruptcy of all national governments."},
                        {"label": "B", "text": "They actually magnified the value of nuanced in-person human contact."},
                        {"label": "C", "text": "They prevented people from talking to one another forever."},
                        {"label": "D", "text": "They forced universities to close their physical research libraries."}
                    ],
                    "answer": "B",
                    "question_zh": "电话等以往的通信技术革新带来了什么历史反讽现象？",
                    "answer_zh": "它们反而放大了面对面深度人际交往的独特价值。",
                    "explanation": "第二段指出'technological connectivity paradoxically increased the value of face-to-face contact. When routine communication becomes cheap... trust-building human interactions... become all the more precious'，对应B项。"
                },
                {
                    "num": 53,
                    "stem": "How did the 20th-century commuter economy distort urban downtown environments?",
                    "options": [
                        {"label": "A", "text": "By turning downtowns into sterile commercial dead zones after business hours."},
                        {"label": "B", "text": "By prohibiting cars and paving all avenues with cobblestones."},
                        {"label": "C", "text": "By tearing down all high-rise skyscrapers to plant orchards."},
                        {"label": "D", "text": "By forcing all corporations to operate inside subterranean tunnels."}
                    ],
                    "answer": "A",
                    "question_zh": "20世纪以通勤为导向的经济如何扭曲了城市市中心环境？",
                    "answer_zh": "使市中心在下班后变成了毫无生气的枯燥“死城”。",
                    "explanation": "第三段指出：'Downtown cores became sterile concrete canyons designed around high-capacity highways and parking garages, effectively dead zones after dark'，对应A项。"
                },
                {
                    "num": 54,
                    "stem": "What is the primary magnet drawing people to 21st-century cities?",
                    "options": [
                        {"label": "A", "text": "The mandatory requirement to sit inside an office cubicle."},
                        {"label": "B", "text": "Rich cultural vitality, gastronomy, and serendipitous human connections."},
                        {"label": "C", "text": "Cheaper gasoline prices at municipal fueling stations."},
                        {"label": "D", "text": "Strict legal bans on all digital computer technology."}
                    ],
                    "answer": "B",
                    "question_zh": "在21世纪，吸引人们进入城市的核心磁石是什么？",
                    "answer_zh": "丰富的文化活力、美食体验以及不期而遇的灵感与人际连接。",
                    "explanation": "第四段指出人们进城并非为了坐办公室，而是为了'high concentrations of culture, gastronomy, performing arts, universities, and vibrant public spaces... serendipity of meeting brilliant, diverse peers'，对应B项。"
                },
                {
                    "num": 55,
                    "stem": "What is the author's ultimate conclusion about the destiny of modern cities?",
                    "options": [
                        {"label": "A", "text": "Cities will inevitably be abandoned and reclaimed by forests."},
                        {"label": "B", "text": "Success belongs to flexible cities that prioritize human communities over commuters."},
                        {"label": "C", "text": "Politicians should legally criminalize all remote and hybrid employment."},
                        {"label": "D", "text": "All city residents should relocate to remote mountaintop cabins."}
                    ],
                    "answer": "B",
                    "question_zh": "作者关于现代城市命运的最终结论是什么？",
                    "answer_zh": "成功属于拥抱灵活性、将人本社区置于盲目通勤之上的城市。",
                    "explanation": "尾段末句总结指出：'The future city belongs not to the commuter, but to the community'，那些转换冗余办公楼为住宅并投资人本街区的城市将繁荣发展，对应B项。"
                }
            ],
            "main_idea_zh": "本文从经济地理与城市社会学高度反思了远程办公潮对大都市命运的深刻影响。面对“城市消亡论”，作者回顾历史指出电话等通信技术的普及反而提升了面对面深度交互的无价稀缺性。远程办公终结了朝九晚五的强制通勤枷锁，反而为城市从冰冷的水泥办公区蜕变为以文化、美食、多元灵感与社区人本为核心的“消费与连接中心”创造了契机。未来的城市属于宜居的社群，而非盲目的通勤者。",
            "main_idea_en": "The passage explores the economic transformation of cities in the telecommuting era, refuting urban decline narratives and arguing that cities are evolving from sterile commuter hubs into vibrant human-centric cultural capitals."
        }
    })

    return sets

print("Extra sets defined.")
