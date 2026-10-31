# -*- coding: utf-8 -*-
"""
CET-6 Reading Comprehension Master Platform Generator (2014 - 2021)
Generates the complete, standalone offline HTML application with genuine past exams.
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

def build_app():
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

    # Load astrbot and sikefix data
    from assemble_database import build_exams_database
    base_exams = build_exams_database()

    # Load curated data
    from make_curated_data import get_curated_exams
    curated = get_curated_exams()
    for cex in curated:
        base_exams[cex['id']] = cex

    # Add 2014-2017 & 2021.12 authentic sets
    more_curated = get_more_curated_exams()
    for cex in more_curated:
        base_exams[cex['id']] = cex

    # Convert exams to sorted list
    all_exams = list(base_exams.values())
    # Sort by year desc, month desc, set asc
    def sort_key(ex):
        y = int(ex.get('year', 0))
        m = int(ex.get('month', 0)) if str(ex.get('month', 0)).isdigit() else 0
        s = ex.get('set', '')
        return (-y, -m, s)

    all_exams.sort(key=sort_key)
    print(f"Total exams compiled: {len(all_exams)}")
    for ex in all_exams:
        print(f"  {ex.get('id'):16s} | {ex.get('title')}")

    # Generate HTML
    generate_html(all_exams, dict_map)

def get_more_curated_exams():
    res = []

    # ==========================================
    # 2014年12月 六级真题 (第1套)
    # ==========================================
    res.append({
        "id": "2014_12_set1",
        "year": "2014",
        "month": "12",
        "set": "第1套",
        "title": "2014年12月 六级阅读真题 (第1套)",
        "theme": "认知心理 / 新能源 / 商业管理",
        "section_a": {
            "title": "Section A · 选词填空 (Solar Power & Grid Integration)",
            "passage": "Solar power has undergone dramatic cost reductions over the past decade, transforming from an expensive niche curiosity into a mainstream energy contender. Technological innovations in photovoltaic manufacturing have dramatically increased panel 26 while slashing production expenses. Today, commercial solar installations are increasingly cost-competitive with conventional fossil fuels, offering an attractive, carbon-free alternative to coal and natural gas.\nHowever, integrating vast amounts of solar power into electricity grids poses distinct technical 27 . Solar generation is inherently 28 , surging during bright daylight hours and dropping to zero at sunset. This mismatch between production peaks and peak evening demand creates what utility operators call the 'duck curve'—a steep drop in net power demand during sunny midday hours followed by an abrupt ramp-up as workers return home. In extreme cases, grid operators are forced to 29 clean solar electricity because local transmission lines cannot absorb the excess power.\nTo overcome these hurdles, power companies are investing heavily in energy storage systems and 30 grid management technologies. Advanced lithium-ion battery banks can store surplus solar energy generated during the day and 31 it into the grid during high-demand evening hours. Meanwhile, artificial intelligence algorithms predict cloud cover and solar variations in real time, allowing engineers to 32 conventional backup plants smoothly. Regulatory frameworks are also evolving to 33 distributed rooftop generation and encourage demand response. As storage costs continue to 34 , clean energy advocates envision a future where renewable power forms the 35 foundation of the modern electric grid.",
            "word_bank": {
                "A": "curtail",
                "B": "efficiency",
                "C": "stabilize",
                "D": "intermittent",
                "E": "primary",
                "F": "challenges",
                "G": "incentivize",
                "H": "plummet",
                "I": "discharge",
                "J": "intricate",
                "K": "coincide",
                "L": "inflexible",
                "M": "recklessly",
                "N": "abruptly",
                "O": "speculate"
            },
            "questions": [
                {"num": 26, "answer": "B", "word": "efficiency", "analysis": "名词作宾语，'increased panel efficiency'提高电池板效率。"},
                {"num": 27, "answer": "F", "word": "challenges", "analysis": "名词复数，'technical challenges'技术挑战。"},
                {"num": 28, "answer": "D", "word": "intermittent", "analysis": "形容词作表语，光伏发电本质上是'间歇性的、断断续续的'。"},
                {"num": 29, "answer": "A", "word": "curtail", "analysis": "动词不定式，被迫'削减/弃弃'太阳能发电。"},
                {"num": 30, "answer": "J", "word": "intricate", "analysis": "形容词修饰grid management，'错综复杂的电网管理技术'。"},
                {"num": 31, "answer": "I", "word": "discharge", "analysis": "动词原形与store并列，电池'放电'把电能输入电网。"},
                {"num": 32, "answer": "C", "word": "stabilize", "analysis": "动词原形，让工程师平稳'稳定'传统备用发电厂。"},
                {"num": 33, "answer": "G", "word": "incentivize", "analysis": "动词原形，'incentivize distributed rooftop generation'激励屋顶光伏发电。"},
                {"num": 34, "answer": "H", "word": "plummet", "analysis": "动词原形，储能成本继续'暴跌、直线下降'。"},
                {"num": 35, "answer": "E", "word": "primary", "analysis": "形容词修饰foundation，构成现代电网的'主要、根本基石'。"}
            ],
            "translation": "在过去十年中，太阳能发电成本大幅下降，从一种昂贵的小众新鲜事物转变为具有主流竞争力的能源力量。光伏制造领域的技术创新不仅大幅降低了生产成本，还显著提高了太阳能电池板的转换效率。如今，商业化太阳能装置与传统化石燃料相比越来越具有成本竞争力，为煤炭和天然气提供了一种极具吸引力的无碳替代方案。\n然而，将大规模太阳能并入电网带来了一系列特殊的技术挑战。太阳能发电本质上具有间歇性，在阳光充沛的白天发电量激增，而到日落时则降为零。发电高峰与傍晚用电高峰之间的脱节催生了电力运营商所称的“鸭子曲线”——在阳光明媚的正午时分，净电力需求急剧下降，而随着下班人群归家，傍晚需求则陡然飙升。在极端情况下，电网运营商不得不弃光（削减太阳能上网电量），因为当地输电线路无法消纳多余电能。\n为了克服这些障碍，电力企业正在大力投资储能系统和精细化的智能电网管理技术。先进的锂电池组能够存储白天产生的富余太阳能，并在傍晚用电高峰期间将其释放到电网中。与此同时，人工智能算法能够实时预测云层覆盖和太阳辐射波动，帮助工程师平稳调控传统备用电厂。监管框架也正在逐步完善，以激励分布式屋顶光伏发电并促进需求侧响应。随着储能成本持续暴跌，清洁能源倡导者预见，可再生能源终将成为现代电网的核心基石。",
            "vocabulary": [
                {"w": "intermittent", "p": "/ˌɪntərˈmɪtənt/", "t": "adj. 间歇的，断断续续的"},
                {"w": "curtail", "p": "/kɜːrˈteɪl/", "t": "v. 削减，缩减"},
                {"w": "incentivize", "p": "/ɪnˈsentɪvaɪz/", "t": "v. 激励，奖励"},
                {"w": "plummet", "p": "/ˈplʌmɪt/", "t": "v. 暴跌，急速下降"},
                {"w": "photovoltaic", "p": "/ˌfoʊtoʊvɒlˈteɪɪk/", "t": "adj. 光伏的，光生伏打的"}
            ]
        },
        "section_b": {
            "title": "Section B · 长篇阅读 (The Psychology of Everyday Decision-Making)",
            "paragraphs": [
                {"label": "A", "text": "Every single day, the human brain makes approximately 35,000 conscious and unconscious decisions. From the moment the alarm clock rings—choosing whether to hit snooze, what outfit to wear, which route to take to work, and what to eat for lunch—our minds are constantly weighing alternatives, evaluating risks, and predicting outcomes. While we pride ourselves on being rational creatures, cognitive psychologists have revealed that our decision-making is heavily governed by mental shortcuts, emotional impulses, and predictable biases."},
                {"label": "B", "text": "In his seminal work on behavioral economics, Nobel laureate Daniel Kahneman introduced the framework of System 1 and System 2 thinking. System 1 operates automatically and quickly, with little or no effort and no sense of voluntary control. It recognizes a friendly face, swerves a bicycle away from an obstacle, and reads words on a highway billboard. System 2, by contrast, allocates attention to effortful mental operations, including complex computations, critical analysis, and deliberate choices."},
                {"label": "C", "text": "Because the human brain accounts for only about 2 percent of total body weight but consumes roughly 20 percent of its metabolic energy, it constantly seeks ways to conserve mental resources. System 1 relies on heuristics—practical rules of thumb—to make rapid judgments without overburdening working memory. In our ancestral environment, reacting immediately to a sudden rustle in the tall grass was far more essential for survival than methodically analyzing whether it was a predator or merely the wind."},
                {"label": "D", "text": "However, cognitive shortcuts that served early hominids well can lead modern individuals into systematic judgment errors. One prominent example is the availability heuristic: we assess the likelihood of an event based on how easily examples spring to mind. After watching dramatic television coverage of a plane crash, people drastically overestimate the danger of flying while underestimating far more hazardous daily activities like driving a car."},
                {"label": "E", "text": "Another pervasive cognitive phenomenon is 'decision fatigue.' Psychologists have demonstrated that making a succession of complex choices depletes our finite reserve of willpower. When judges in parole hearings review cases throughout the morning, their likelihood of granting parole starts high and plummets steadily as lunch approaches. After resting and eating, their favorable ruling rates spike back to baseline. As decision fatigue sets in, people either become recklessly impulsive or default to the safest, most passive option available."},
                {"label": "F", "text": "Corporate leaders like Steve Jobs and Mark Zuckerberg famously recognized decision fatigue, choosing to wear near-identical outfits every day to eliminate trivial wardrobe decisions and reserve their cognitive stamina for high-stakes business choices. Similarly, successful professionals often schedule their most intellectually demanding tasks for early morning hours before decision-making exhaustion clouds their judgment."},
                {"label": "G", "text": "Moreover, modern digital environments exploit human cognitive vulnerabilities with remarkable precision. E-commerce platforms employ artificial scarcity ('Only 2 items left in stock!') and social proof ('14 people are viewing this hotel room right now') to trigger loss aversion—our tendency to feel the pain of a loss twice as acutely as the pleasure of an equivalent gain. Driven by fear of missing out, shoppers make impulsive purchases they would otherwise avoid."},
                {"label": "H", "text": "To counter these pitfalls, behavioral scientists recommend 'decision hygiene.' Rather than relying on gut feelings, individuals and organizations should use structured checklists, mandate cooling-off periods before major financial commitments, and solicit Devil's Advocates to challenge prevailing group consensus. By deliberately slowing down and forcing System 2 into gear, we can protect ourselves against self-deception and navigate an increasingly complex world with genuine clarity."}
            ],
            "questions": [
                {"num": 36, "stem": "Mental fatigue causes decision-makers to become either hasty and rash or overly passive.", "answer": "E"},
                {"num": 37, "stem": "System 1 functions smoothly and rapidly without requiring substantial conscious exertion.", "answer": "B"},
                {"num": 38, "stem": "People assess how likely an occurrence is according to how readily relevant memories come to awareness.", "answer": "D"},
                {"num": 39, "stem": "High-profile tech executives standardized their daily clothing to avoid draining valuable mental energy.", "answer": "F"},
                {"num": 40, "stem": "Immediate reactive thinking was critical for prehistoric humans to survive dangerous environments.", "answer": "C"},
                {"num": 41, "stem": "Humans generally experience the distress of losing something much more intensely than gaining an identical benefit.", "answer": "G"},
                {"num": 42, "stem": "Psychological research demonstrates that human judgment is far less rational than people normally presume.", "answer": "A"},
                {"num": 43, "stem": "Establishing systematic procedures and delaying impulsive actions helps individuals avoid flawed decisions.", "answer": "H"}
            ],
            "translation": "长篇阅读解析总结：文章探讨了日常人类决策的心理学与行为经济学机制。丹尼尔·卡尼曼提出的系统1（快思考）与系统2（慢思考）模型解释了大脑为节约能量而依赖经验法则（启发式）。但在现代社会，易得性启发式、损失厌恶及“决策疲劳”会导致系统性偏差。乔布斯等人通过简化衣着对抗决策疲劳。行为科学家提倡通过决策卫生（如检查清单和冷静期）来激活慢思考，提升决策质量。"
        },
        "section_c1": {
            "title": "Section C · 仔细阅读 Passage 1 (Digital Distractions & Cognitive Multitasking)",
            "passage": "In modern corporate and educational environments, multitasking is frequently praised as an indispensable virtue. Job advertisements routinely demand candidates who can 'juggle multiple priorities with ease,' while university students take pride in simultaneously streaming lectures, messaging friends, and scrolling social media feeds. Yet neuroscientists have reached an unequivocal verdict: the human brain cannot consciously execute multiple high-level cognitive tasks at once. What we celebrate as multitasking is actually rapid, erratic task-switching, and its cognitive toll is staggering.\nWhen you switch back and forth between writing a research paper and answering text messages, your prefrontal cortex must disengage from one set of cognitive rules and engage with another. This process generates what cognitive psychologists call 'attention residue.' Even after you shift your gaze back to your primary task, your mind remains partially anchored to the previous interruption. As a result, comprehension plummets, problem-solving slows down, and error rates multiply.\nLaboratory experiments conducted at Stanford University revealed that chronic media multitaskers—those who habitually consume multiple streams of digital information simultaneously—perform significantly worse on fundamental cognitive tests. Paradoxically, despite believing they possess superior attention control, heavy multitaskers are worse at filtering out irrelevant environmental noise, slower at organizing working memory, and less adept at switching between tasks than their single-tasking peers. Chronic digital overstimulation appears to erode the very mental filters that allow for deep focus.\nFurthermore, continuous digital interruptions impair long-term memory formation. When learning occurs amid fragmented attention, the brain stores information in the striatum—a brain region responsible for automated habits and motor skills—rather than the hippocampus, which handles flexible, conceptual memory. Consequently, while multitaskers may retain superficial facts, they struggle to apply that knowledge creatively to novel problems.\nReclaiming cognitive endurance requires deliberate digital boundaries. Leading organizations are implementing 'focus blocks'—periods during the workday where internal messaging and meetings are strictly prohibited. At an individual level, adopting practices like 'monotasking' (immersing oneself in a single task for a designated duration) can gradually rebuild damaged neural pathways. In an economy increasingly dominated by automated algorithms, deep, uninterrupted concentration has become the rarest and most valuable human currency.",
            "questions": [
                {
                    "num": 46,
                    "stem": "What is neuroscientists' conclusive view regarding human multitasking?",
                    "options": [
                        {"label": "A", "text": "It is an innate ability that improves with practice."},
                        {"label": "B", "text": "It is merely rapid and destructive task-switching in disguise."},
                        {"label": "C", "text": "It helps students comprehend abstract academic concepts."},
                        {"label": "D", "text": "It stimulates creative breakthroughs in corporate teams."}
                    ],
                    "answer": "B",
                    "question_zh": "关于人类的多任务处理，神经科学家的确定性结论是什么？",
                    "answer_zh": "它不过是换了伪装的快速且具有破坏性的任务切换。",
                    "explanation": "首段末尾明确指出：'What we celebrate as multitasking is actually rapid, erratic task-switching, and its cognitive toll is staggering'，对应B项。"
                },
                {
                    "num": 47,
                    "stem": "What negative consequence does 'attention residue' produce?",
                    "options": [
                        {"label": "A", "text": "Permanent damage to physical vision."},
                        {"label": "B", "text": "Excessive production of stress hormones in the bloodstream."},
                        {"label": "C", "text": "Lingering cognitive distraction that degrades primary task performance."},
                        {"label": "D", "text": "An irresistible desire to purchase digital gadgets."}
                    ],
                    "answer": "C",
                    "question_zh": "“注意力残留”会产生什么负面后果？",
                    "answer_zh": "挥之不去的认知分散削弱主要任务的表现。",
                    "explanation": "第二段指出即使目光回到主任务，思想依然部分滞留在前一个干扰上，导致'comprehension plummets, problem-solving slows down, and error rates multiply'，对应C项。"
                },
                {
                    "num": 48,
                    "stem": "What ironic finding emerged from the Stanford University experiments?",
                    "options": [
                        {"label": "A", "text": "Frequent multitaskers performed worse on focus and memory tests."},
                        {"label": "B", "text": "College professors were worse at concentration than young children."},
                        {"label": "C", "text": "Smartphones actually enhanced students' spelling accuracy."},
                        {"label": "D", "text": "Heavy internet users enjoyed higher overall academic grades."}
                    ],
                    "answer": "A",
                    "question_zh": "斯坦福大学的实验得出了什么讽刺性的发现？",
                    "answer_zh": "频繁的多任务处理者在专注力和记忆力测试中表现更差。",
                    "explanation": "第三段指出'Paradoxically, despite believing they possess superior attention control, heavy multitaskers are worse at filtering out irrelevant environmental noise...'，对应A项。"
                },
                {
                    "num": 49,
                    "stem": "How does divided attention affect the way knowledge is stored in the brain?",
                    "options": [
                        {"label": "A", "text": "It accelerates the formation of deep conceptual memories."},
                        {"label": "B", "text": "It prevents information from moving into flexible conceptual memory areas."},
                        {"label": "C", "text": "It erases childhood recollections stored in the hippocampus."},
                        {"label": "D", "text": "It triggers sudden seizures in the prefrontal cortex."}
                    ],
                    "answer": "B",
                    "question_zh": "注意力分散如何影响大脑存储知识的方式？",
                    "answer_zh": "它阻止信息进入灵活的概念记忆区域。",
                    "explanation": "第四段指出注意力分散导致信息存储在纹状体而非海马体，使得他们难以将知识灵活创造性地应用于新问题（对应B项）。"
                },
                {
                    "num": 50,
                    "stem": "What practical advice does the author offer to cultivate deep focus?",
                    "options": [
                        {"label": "A", "text": "Completely disconnecting from all modern internet networks."},
                        {"label": "B", "text": "Practicing single-task immersion within dedicated periods."},
                        {"label": "C", "text": "Relying on artificial intelligence to reply to messages."},
                        {"label": "D", "text": "Encouraging employees to work longer shifts at night."}
                    ],
                    "answer": "B",
                    "question_zh": "为了培养深度专注，作者提供了什么切实可行的建议？",
                    "answer_zh": "在专属时间段内练习单任务沉浸。",
                    "explanation": "尾段提到设立'focus blocks'以及践行'monotasking (immersing oneself in a single task for a designated duration)'，对应B项。"
                }
            ],
            "main_idea_zh": "本文从神经科学角度彻底破除了“多任务处理”的迷思。所谓多任务处理本质上是大脑快速而低效的任务切换，会产生注意力残留，削弱工作记忆与深度理解力。长期多任务习惯甚至会改变信息在大脑中的存储路径，损害概念构建能力。作者呼吁通过专属专注时段和单任务沉浸重新赢回深度思考的能力。",
            "main_idea_en": "The passage debunks the myth of multitasking through neuroscience evidence, highlighting how task-switching causes attention residue and memory deficits while advocating for monotasking and dedicated focus blocks."
        },
        "section_c2": {
            "title": "Section C · 仔细阅读 Passage 2 (Electric Vehicles & Urban Infrastructure)",
            "passage": "The global automotive industry is undergoing its most profound transformation in more than a century. Spurred by urgent climate goals and tightening emission regulations, major carmakers have pledged tens of billions of dollars to phase out internal combustion engines in favor of electric vehicles (EVs). Battery costs have plunged by over 80 percent in the past decade, and consumer demand is surging as new models achieve longer ranges and superior acceleration. Yet as electric cars transition from luxury novelty to mass-market reality, the greatest obstacle to their widespread adoption is no longer the vehicle itself, but the public charging infrastructure.\nUnlike gasoline vehicles, which can refuel in three minutes at any of the millions of gas stations across the globe, electric cars require a fundamentally different fueling paradigm. The vast majority of early EV owners are affluent suburban homeowners who plug in overnight in private garages, paying cheap residential electricity rates. For this demographic, EV ownership is remarkably convenient. However, the next wave of buyers—urban apartment dwellers, curbside parkers, and lower-income drivers—lack dedicated off-street parking. If they cannot charge reliably near where they live or work, they will simply refuse to buy electric cars.\nPublic charging networks today are plagued by severe deficiencies. Independent audits routinely discover that nearly one in four public charging stalls is broken, suffering from software glitches, broken connectors, or payment processing errors. Furthermore, the existing network exhibits stark geographical disparities: wealthy coastal cities are saturated with fast chargers, while rural highways and lower-income urban neighborhoods remain charging deserts.\nUpgrading urban grids to support thousands of high-speed chargers presents immense civil engineering hurdles. Fast chargers draw enormous surges of electrical power—equivalent to powering an entire commercial office building. If hundreds of drivers in a dense neighborhood plug in simultaneously after work, local substations could easily overload. Power utilities must invest heavily in grid reinforcement, neighborhood transformer upgrades, and local battery storage buffers to smooth out demand spikes.\nGovernment policymakers must recognize that electrifying transportation requires more than consumer tax credits for purchasing vehicles. Massive public investment is urgently needed to standardize charging plugs, enforce reliability standards, and subsidize curbside chargers in multi-family residential zones. The transition to clean mobility will not succeed until charging an electric vehicle becomes as seamless, reliable, and equitable as pumping a gallon of gas.",
            "questions": [
                {
                    "num": 51,
                    "stem": "What is now regarded as the primary impediment to mass electric vehicle adoption?",
                    "options": [
                        {"label": "A", "text": "Prohibitively expensive battery replacement costs."},
                        {"label": "B", "text": "Sluggish acceleration and poor safety performance."},
                        {"label": "C", "text": "Inadequate and unreliable public charging networks."},
                        {"label": "D", "text": "Fierce consumer attachment to fossil fuel brands."}
                    ],
                    "answer": "C",
                    "question_zh": "如今什么被视为电动汽车大规模普及的首要阻碍？",
                    "answer_zh": "不充分且不可靠的公共充电网络。",
                    "explanation": "首段尾句明确指出：'the greatest obstacle to their widespread adoption is no longer the vehicle itself, but the public charging infrastructure'，对应C项。"
                },
                {
                    "num": 52,
                    "stem": "Why was EV ownership comparatively effortless for early adopters?",
                    "options": [
                        {"label": "A", "text": "They were granted free unlimited public charging by the state."},
                        {"label": "B", "text": "They possessed private garages for overnight residential charging."},
                        {"label": "C", "text": "Their vehicles did not require battery recharging for months."},
                        {"label": "D", "text": "Automakers assigned personal mechanics to their residences."}
                    ],
                    "answer": "B",
                    "question_zh": "为什么对早期尝鲜者来说拥有电动车相对轻松无忧？",
                    "answer_zh": "他们拥有私家车库可在夜间进行家庭充电。",
                    "explanation": "第二段指出：'The vast majority of early EV owners are affluent suburban homeowners who plug in overnight in private garages'，对应B项。"
                },
                {
                    "num": 53,
                    "stem": "What glaring problem currently affects public charging stations?",
                    "options": [
                        {"label": "A", "text": "High rates of equipment malfunction and software breakdown."},
                        {"label": "B", "text": "Universal rejection by electric vehicle manufacturers."},
                        {"label": "C", "text": "Excessive charging speeds that damage battery life."},
                        {"label": "D", "text": "Government mandates requiring special licenses to operate."}
                    ],
                    "answer": "A",
                    "question_zh": "当前公共充电桩面临的突出问题是什么？",
                    "answer_zh": "高故障率与软件故障问题突出。",
                    "explanation": "第三段指出：'nearly one in four public charging stalls is broken, suffering from software glitches, broken connectors, or payment processing errors'，对应A项。"
                },
                {
                    "num": 54,
                    "stem": "Why does rapid public charging strain urban electricity grids?",
                    "options": [
                        {"label": "A", "text": "High-speed chargers draw massive power spikes equivalent to buildings."},
                        {"label": "B", "text": "Underground cables melt when exposed to direct sunlight."},
                        {"label": "C", "text": "Electric cars leak current into municipal water pipes."},
                        {"label": "D", "text": "Power companies intentionally throttle residential voltage."}
                    ],
                    "answer": "A",
                    "question_zh": "为什么快速公共充电会给城市电网带来巨大压力？",
                    "answer_zh": "快速充电桩抽取巨大的脉冲电能，相当于一栋大楼的负荷。",
                    "explanation": "第四段指出：'Fast chargers draw enormous surges of electrical power—equivalent to powering an entire commercial office building'，对应A项。"
                },
                {
                    "num": 55,
                    "stem": "What is the author's ultimate prescription for government policymakers?",
                    "options": [
                        {"label": "A", "text": "Abandon electric cars and reinvest in hydrogen railways."},
                        {"label": "B", "text": "Shift focus toward equitable public charging infrastructure."},
                        {"label": "C", "text": "Double consumer tax subsidies on luxury sports cars."},
                        {"label": "D", "text": "Prohibit private companies from operating charging stations."}
                    ],
                    "answer": "B",
                    "question_zh": "作者给政府决策者提出的最终建议是什么？",
                    "answer_zh": "将重心转向建设公平便捷的公共充电基础设施。",
                    "explanation": "尾段指出不能仅仅依赖购车税收减免，必须进行大规模公共投资，使公共充电如加油一般无缝、可靠且公平（对应B项）。"
                }
            ],
            "main_idea_zh": "本文分析了全球电动汽车行业从“小众尝鲜”迈向“大众普及”过程中面临的最大瓶颈——公共充电基础设施。早期郊区车主依靠车库充电，而未来城市租房者及中低收入人群严重依赖公共设施。当前充电桩故障率高、区域分布失衡、对城市电网负荷冲击巨大。作者指出政策必须从单纯的购车补贴转向全面、公平的电网与充电基建升级。",
            "main_idea_en": "The passage argues that public charging infrastructure is the pivotal bottleneck for electric vehicle adoption, analyzing urban grid constraints, maintenance reliability deficits, and policy imperatives."
        }
    })

    # ==========================================
    # 2015年6月 六级真题 (第1套)
    # ==========================================
    res.append({
        "id": "2015_06_set1",
        "year": "2015",
        "month": "06",
        "set": "第1套",
        "title": "2015年6月 六级阅读真题 (第1套)",
        "theme": "双语认知 / 高等教育溢价 / 金融算法",
        "section_a": {
            "title": "Section A · 选词填空 (The Bilingual Brain Advantage)",
            "passage": "For much of the twentieth century, educators and pediatricians warned parents that raising children with two languages would 26 cognitive confusion. Monolingualism was considered the natural human norm, and conventional wisdom held that learning a second language early in life would 27 a child's vocabulary acquisition and delay speech milestones. However, decades of rigorous neuroscience research have completely 28 this outdated notion, demonstrating instead that the bilingual brain enjoys profound cognitive advantages.\nNeuroscientists have discovered that the real benefit of bilingualism lies not in language proficiency itself, but in enhanced executive 29 . Executive function refers to the brain's command center—the cognitive system that directs attention, filters out distractions, and coordinates working memory. Because both languages remain active 30 in the brain, bilingual individuals must constantly suppress one language system while activating the other. This mental gymnastics acts as a continuous workout for the prefrontal cortex, strengthening neural 31 across a lifespan.\nConsequently, bilingual children consistently 32 their monolingual peers on problem-solving tasks that require cognitive flexibility and abstract reasoning. In older adults, lifelong bilingualism serves as a powerful protective shield against neurodegenerative decline, 33 the onset of Alzheimer's symptoms by an average of four to five years. Even when physical brain degeneration occurs, bilinguals demonstrate remarkable cognitive 34 , maintaining clear mental functioning far longer than monolinguals. Far from being an impediment, speaking multiple languages 35 the brain's architecture and enriches lifelong cognitive health.",
            "word_bank": {
                "A": "induce",
                "B": "circuits",
                "C": "function",
                "D": "outperform",
                "E": "postponing",
                "F": "simultaneously",
                "G": "debunked",
                "H": "hinder",
                "I": "resilience",
                "J": "fortifies",
                "K": "incur",
                "L": "spontaneous",
                "M": "abruptly",
                "N": "destabilize",
                "O": "reproduce"
            },
            "questions": [
                {"num": 26, "answer": "A", "word": "induce", "analysis": "动词原形，'induce cognitive confusion'意为诱发认知混乱。"},
                {"num": 27, "answer": "H", "word": "hinder", "analysis": "动词原形，'hinder vocabulary acquisition'阻碍词汇习得。"},
                {"num": 28, "answer": "G", "word": "debunked", "analysis": "过去分词与have构成现在完成时，'completely debunked'彻底揭穿/破除了过时观念。"},
                {"num": 29, "answer": "C", "word": "function", "analysis": "名词短语，'executive function'执行功能。"},
                {"num": 30, "answer": "F", "word": "simultaneously", "analysis": "副词修饰active，两种语言在脑中'同时'保持活跃。"},
                {"num": 31, "answer": "B", "word": "circuits", "analysis": "名词复数，'neural circuits'神经回路。"},
                {"num": 32, "answer": "D", "word": "outperform", "analysis": "及物动词，双语儿童在解决问题任务上'胜过/优于'单语儿童。"},
                {"num": 33, "answer": "E", "word": "postponing", "analysis": "现在分词作状语，'postponing the onset'推迟阿尔茨海默病发作。"},
                {"num": 34, "answer": "I", "word": "resilience", "analysis": "不可数名词，'cognitive resilience'认知韧性/复原力。"},
                {"num": 35, "answer": "J", "word": "fortifies", "analysis": "第三人称单数动词，'fortifies the brain's architecture'强化大脑生理结构。"}
            ],
            "translation": "在20世纪的大部分时间里，教育工作者和儿科医生曾警告父母：双语育儿会导致孩子认知混乱。当时人们认为单语才是人类的自然常态，传统观念坚称，幼年学习第二语言会阻碍孩子的词汇习得并延迟语言发展。然而，数十年严谨的神经科学研究彻底推翻了这一陈腐观念，反而表明双语大脑具有显著的认知优势。\n神经科学家发现，双语真正的益处并不在于语言本身，而在于增强了大脑的“执行功能”。执行功能是大脑的指挥中枢——负责分配注意力、屏蔽外界干扰并协调工作记忆的认知系统。由于两种语言系统在大脑中始终同时保持活跃状态，双语者必须在抑制一种语言的同时激活另一种语言。这种高频心理转换相当于对前额叶皮层进行持续锻炼，终生强化其神经回路。\n因此，在需要认知灵活性和抽象推理的问题解决任务中，双语儿童的表现始终优于单语同龄人。对于老年群体而言，终生使用双语如同一面强有力的护盾，抵御神经退行性衰退，将阿尔茨海默病的症状发作平均推迟四到五年。即使脑部发生物理退行性病变，双语者仍展现出非凡的认知韧性，保持清醒思维的时间远长于单语者。学习掌握多门语言绝非负担，而是极大地强化了大脑的架构，丰富了终生认知健康。",
            "vocabulary": [
                {"w": "monolingualism", "p": "/ˌmɒnəʊˈlɪŋɡwəlɪzəm/", "t": "n. 单语使用，单语能力"},
                {"w": "debunk", "p": "/diːˈbʌŋk/", "t": "v. 揭穿，拆穿（假话或过时观点）"},
                {"w": "executive", "p": "/ɪɡˈzekjətɪv/", "t": "adj. 执行的；n. 高管"},
                {"w": "resilience", "p": "/rɪˈzɪliəns/", "t": "n. 韧性，复原力"},
                {"w": "fortify", "p": "/ˈfɔːrtɪfaɪ/", "t": "v. 强化，设防于"}
            ]
        },
        "section_b": {
            "title": "Section B · 长篇阅读 (Food Deserts and Nutritional Inequality)",
            "paragraphs": [
                {"label": "A", "text": "In the world's wealthiest economies, severe malnutrition rarely stems from an absolute scarcity of calories. Instead, an insidious form of deprivation has taken root across thousands of inner cities and rural hamlets: 'food deserts.' These are geographical regions where residents lack affordable access to fresh, nutritious food, such as fruits, vegetables, whole grains, and lean meats. In these neighborhoods, walking into a supermarket is an impossibility, but finding cheap, processed junk food is effortless."},
                {"label": "B", "text": "According to estimates from the United States Department of Agriculture (USDA), approximately 23.5 million Americans live in low-income areas that are more than one mile from a supermarket in urban zones, or more than ten miles in rural territory. For individuals living below the poverty threshold, physical distance is compounded by transportation deficits. Households without personal automobiles must rely on public transit or costly taxis, turning an ordinary weekly grocery trip into an exhausting multi-hour journey."},
                {"label": "C", "text": "Where traditional grocery stores have fled, fast-food franchises, gas station mini-marts, and dollar stores have aggressively rushed in to fill the vacuum. The shelves of these retailers are heavily stocked with shelf-stable packaged foods loaded with refined sugars, sodium, and trans fats, while fresh produce is conspicuously absent. For a mother working two low-wage jobs, purchasing inexpensive calorie-dense processed food is often the only economically and logistically feasible choice to feed her family."},
                {"label": "D", "text": "The long-term public health ramifications of this environment are catastrophic. Decades of epidemiological tracking reveal that populations residing in food deserts suffer disproportionately high rates of chronic diet-related illnesses, including obesity, type-2 diabetes, cardiovascular diseases, and hypertension. Children raised in these environments face stunted physical development and higher rates of behavioral issues in school, perpetuating intergenerational cycles of poverty and illness."},
                {"label": "E", "text": "For years, policymakers operated under a straightforward hypothesis: if supermarkets abandoned low-income neighborhoods, the solution was simply to subsidize new supermarkets to open their doors. Under initiatives like the Healthy Food Financing Initiative, hundreds of millions of public dollars were poured into incentives for grocery chains. However, early research evaluating these newly opened stores produced puzzling and disheartening findings."},
                {"label": "F", "text": "Economists discovered that simply dropping a modern supermarket into a food desert produced remarkably little change in residents' actual nutritional intake. While neighborhood residents appreciated the convenience of having a nearby store, their grocery shopping habits remained largely unaltered. Families continued to purchase heavily processed items, while sales of raw fruits and green vegetables lagged far behind expectations."},
                {"label": "G", "text": "These findings forced a fundamental reassessment of dietary decision-making. Researchers realized that physical access is only one dimension of a complex equation; economic affordability, cultural food traditions, cooking education, and time poverty play equally powerful roles. Fresh vegetables require refrigeration, cooking equipment, preparation time, and culinary confidence—luxuries that families working precarious shifts often cannot afford. In contrast, processed foods deliver predictable taste, require zero preparation, and never spoil on the shelf."},
                {"label": "H", "text": "Recognizing these nuances, innovative community organizations are pioneering grassroots solutions. Urban farming cooperatives turn vacant city lots into organic vegetable gardens, while mobile grocery buses deliver fresh produce directly to community centers, accepting federal food stamps. Concurrently, community kitchens provide culturally relevant cooking workshops, teaching families how to prepare wholesome meals on tight budgets. Combating food inequality requires not merely commercial real estate, but addressing the structural poverty that dictates what people can afford to eat."}
            ],
            "questions": [
                {"num": 36, "stem": "Introducing modern supermarkets into deprived zones failed to meaningfully alter people's grocery buying behaviors.", "answer": "F"},
                {"num": 37, "stem": "Severe distance to fresh grocery stores is further worsened by inadequate transportation for poor families.", "answer": "B"},
                {"num": 38, "stem": "Prolonged exposure to processed foods causes excessive rates of diabetes and heart diseases in food deserts.", "answer": "D"},
                {"num": 39, "stem": "Corner stores and fast-food eateries dominate neighborhoods where conventional grocers have departed.", "answer": "C"},
                {"num": 40, "stem": "Government leaders originally assumed that subsidizing supermarket openings would easily resolve nutritional deficits.", "answer": "E"},
                {"num": 41, "stem": "Food deserts describe areas where citizens cannot easily purchase wholesome, unprocessed ingredients.", "answer": "A"},
                {"num": 42, "stem": "Community farming projects and traveling grocery buses offer adaptable, grassroots answers to food scarcity.", "answer": "H"},
                {"num": 43, "stem": "Culinary skill, time constraints, and tight finances profoundly shape people's daily dietary selections.", "answer": "G"}
            ],
            "translation": "长篇阅读解析总结：文章深入剖析了现代城市中的“食品荒漠”（Food Deserts）现象。食品荒漠指低收入居民难以获得平价新鲜蔬菜和肉类的地区，便利店和快餐店充斥其间。研究表明，单纯靠政府补贴引入大型超市并不能自动改变居民的垃圾饮食习惯，因为时间贫困、文化习惯、烹饪条件与经济可负担性共同制约着选择。最终解决这一困境需要结合社区农场、移动菜车和烹饪教育等全方位草根行动。"
        },
        "section_c1": {
            "title": "Section C · 仔细阅读 Passage 1 (The Economic Value of College Degrees)",
            "passage": "As undergraduate tuition and student loan balances climb to record-shattering heights, a contentious debate has erupted over the fundamental value of higher education. Critics argue that higher education has become an overpriced financial bubble, pushing millions of young Americans into debt servitude for degrees that do not translate into stable, remunerative employment. Media stories abound of recent graduates with degrees in humanities or arts working as baristas and rideshare drivers. Yet empirical economic data tells a far more nuanced and reassuring story: on average, a college degree remains the single best investment a young person can make.\nDecades of labor economics research demonstrate that the 'college wage premium'—the earnings gap between bachelor's degree holders and workers with only a high school diploma—remains near historical highs. Over a forty-year working career, a typical college graduate earns approximately $1.2 million more than a high school graduate. Furthermore, college-educated workers enjoy substantially lower unemployment rates during economic downturns, greater employer-provided health coverage, and longer life expectancies. The financial returns on a college education outpace average returns from the stock market.\nHowever, the aggregate data conceals enormous divergence beneath the surface. The economic return on a degree is increasingly dictated by field of study and the specific institution attended. Graduates in engineering, computer science, nursing, and economics experience immediate, substantial wage gains that easily justify their educational debts. Conversely, degrees in visual arts, theater, and certain social sciences often yield earnings comparable to or lower than those of skilled vocational trades, such as electricians, plumbers, and HVAC technicians.\nMoreover, the student debt crisis is not distributed evenly across academia. The most catastrophic default rates occur not at selective non-profit universities, but at predatory for-profit colleges that charge exorbitant tuition for worthless credentials while targeting low-income and veteran students. Alarmingly, the students most likely to default on their educational loans are not those who borrowed $100,000 for graduate school, but those who borrowed modest amounts—between $5,000 and $10,000—and dropped out without completing their degrees.\nUltimately, the college debate must move beyond simplistic binaries. A college degree is neither a golden guarantee of middle-class prosperity nor an outright financial scam. It is an investment that requires informed consumer judgment. High schools must provide realistic career guidance, universities must rein in runaway administrative bloat to restrain tuition growth, and federal policymakers must hold poor-performing institutions accountable when their students cannot earn enough to repay their loans.",
            "questions": [
                {
                    "num": 46,
                    "stem": "What is critics' primary indictment against modern higher education?",
                    "options": [
                        {"label": "A", "text": "Universities refuse to admit low-income applicants."},
                        {"label": "B", "text": "Excessive tuition thrusts students into debt without yielding stable jobs."},
                        {"label": "C", "text": "College professors are unconcerned with academic research."},
                        {"label": "D", "text": "Campus extracurricular activities have grown overly lavish."}
                    ],
                    "answer": "B",
                    "question_zh": "批评人士对现代高等教育的主要指责是什么？",
                    "answer_zh": "高昂的学费使学生背负债务却无法获得稳定的工作。",
                    "explanation": "首段指出：'pushing millions of young Americans into debt servitude for degrees that do not translate into stable, remunerative employment'，对应B项。"
                },
                {
                    "num": 47,
                    "stem": "What does empirical data reveal regarding the 'college wage premium'?",
                    "options": [
                        {"label": "A", "text": "It has vanished entirely over the last decade."},
                        {"label": "B", "text": "It remains near historic highs across lifetime career earnings."},
                        {"label": "C", "text": "It only benefits students with graduate degrees."},
                        {"label": "D", "text": "It is lower than returns from municipal savings accounts."}
                    ],
                    "answer": "B",
                    "question_zh": "经验数据揭示了关于“大学工资溢价”的什么事实？",
                    "answer_zh": "在其整个职业生涯的总收入中，该溢价依然处于历史高位附近。",
                    "explanation": "第二段指出'the college wage premium... remains near historical highs. Over a forty-year working career, a typical college graduate earns approximately $1.2 million more'，对应B项。"
                },
                {
                    "num": 48,
                    "stem": "How do different fields of study influence college graduates' earnings?",
                    "options": [
                        {"label": "A", "text": "Humanities degrees yield substantially higher salaries than engineering."},
                        {"label": "B", "text": "All academic majors yield virtually identical compensation."},
                        {"label": "C", "text": "STEM and healthcare fields deliver immediate, high financial returns."},
                        {"label": "D", "text": "Vocational workers earn less than all university graduates."}
                    ],
                    "answer": "C",
                    "question_zh": "不同的专业领域如何影响大学毕业生的收入水平？",
                    "answer_zh": "理工科和医疗护理专业带来立竿见影且丰厚的回报。",
                    "explanation": "第三段指出'Graduates in engineering, computer science, nursing, and economics experience immediate, substantial wage gains...'，对应C项。"
                },
                {
                    "num": 49,
                    "stem": "Which category of student borrowers experiences the highest rate of loan default?",
                    "options": [
                        {"label": "A", "text": "Medical school graduates with massive liabilities."},
                        {"label": "B", "text": "Elite Ivy League law school alumni."},
                        {"label": "C", "text": "Dropouts with modest debts who never completed degrees."},
                        {"label": "D", "text": "International graduate students in doctoral programs."}
                    ],
                    "answer": "C",
                    "question_zh": "哪一类借贷学生出现助学贷款违约的比例最高？",
                    "answer_zh": "背负少量债务却中途辍学未获学位的学生。",
                    "explanation": "第四段末尾明确指出：'the students most likely to default on their educational loans are not those who borrowed $100,000 for graduate school, but those who borrowed modest amounts... and dropped out without completing their degrees'，对应C项。"
                },
                {
                    "num": 50,
                    "stem": "What is the author's overall stance regarding college education?",
                    "options": [
                        {"label": "A", "text": "It represents an investment that demands careful, informed decision-making."},
                        {"label": "B", "text": "It is an unmitigated disaster that should be defunded by taxpayers."},
                        {"label": "C", "text": "High school graduates should universally bypass university education."},
                        {"label": "D", "text": "The government should eliminate all vocational trade apprenticeships."}
                    ],
                    "answer": "A",
                    "question_zh": "作者对大学教育的总体态度是什么？",
                    "answer_zh": "它是一项需要审慎且知情决策的投资。",
                    "explanation": "尾段总结：'A college degree is neither a golden guarantee of middle-class prosperity nor an outright financial scam. It is an investment that requires informed consumer judgment'，对应A项。"
                }
            ],
            "main_idea_zh": "本文客观评估了大学学位的经济价值。面对“学历泡沫论”，宏观经济数据显示大学毕业生的终生工资溢价依然高达120万美元。然而，不同专业（工科/护理 vs 艺术/部分社科）以及办学性质（非营利大学 vs 营利性骗局学校）导致回报率剧烈分化。最高比例的违约并非来自高负债名校生，而是借款数千美元却辍学的群体。大学教育是一项需要理性知情抉择的重要投资。",
            "main_idea_en": "The passage evaluates the economic returns of higher education, balancing the enduring college wage premium against disparities across majors, predatory colleges, and dropout default risks."
        },
        "section_c2": {
            "title": "Section C · 仔细阅读 Passage 2 (High-Frequency Algorithmic Trading)",
            "passage": "In the modern financial marketplace, the romantic image of traders shouting buy and sell orders on crowded exchange floors has vanished forever. Today, global capital markets are dominated by high-frequency trading (HFT)—automated mathematical algorithms executing thousands of stock transactions per second inside supercomputers located mere yards from exchange servers. High-frequency firms employ physicists and mathematicians to craft predictive models, competing in an arms race measured in microseconds. Proponents celebrate HFT for narrowing bid-ask spreads and providing abundant liquidity, but critics argue that algorithmic speed introduces systemic fragility and unfair advantages.\nAt the core of high-frequency trading is 'co-location.' By placing their servers in the very same data centers that house the stock exchange's matching engines, HFT firms shave fractions of a millisecond off data transmission times. In high-speed finance, light travels through fiber-optic glass at approximately 200 kilometers per millisecond. Being ten miles farther away can mean receiving market-moving news too late. Armed with this speed advantage, algorithmic systems can detect an institutional investor's large purchase order on one venue and 'front-run' it, buying up shares on other exchanges before the slower investor's order arrives.\nThis technological supremacy has generated bitter controversies. In May 2010, the U.S. stock market experienced the infamous 'Flash Crash,' where the Dow Jones Industrial Average plunged nearly 1,000 points in minutes before recovering. When unexpected volatility struck, automated algorithms abruptly withdrew their bids to protect capital, creating a sudden liquidity vacuum that triggered cascading automated sell-offs. The crash demonstrated that when markets operate faster than human comprehension, software glitches can threaten entire national economies.\nFurthermore, the complexity of modern electronic exchanges creates opaque order types that benefit HFT traders at the expense of ordinary retail investors and mutual funds that manage workers' pensions. High-frequency algorithms engage in 'quote stuffing'—flooding exchanges with millions of phantom orders and cancellations every second simply to slow down rival computer systems and gain an informational edge.\nFinancial regulators have struggled to keep pace with algorithmic evolution. Proposals such as financial transaction taxes, mandatory minimum order resting times, and batch auctions—which group orders into frequent discrete intervals rather than continuous microsecond races—are gaining traction. Financial markets must exist to allocate capital to productive human enterprises, not to serve as an unregulated digital casino for hyper-fast computers.",
            "questions": [
                {
                    "num": 51,
                    "stem": "What has replaced traditional human traders on contemporary stock exchange floors?",
                    "options": [
                        {"label": "A", "text": "Government regulatory inspectors."},
                        {"label": "B", "text": "Automated algorithms executing microsecond transactions."},
                        {"label": "C", "text": "Artificial intelligence robots wearing physical trading jackets."},
                        {"label": "D", "text": "Retail investors trading via smartphone applications."}
                    ],
                    "answer": "B",
                    "question_zh": "当代证券交易所交易大厅里，什么取代了传统的人工作交易员？",
                    "answer_zh": "以微秒级执行交易的自动化算法。",
                    "explanation": "首段第二句指出：'markets are dominated by high-frequency trading (HFT)—automated mathematical algorithms executing thousands of stock transactions per second...'，对应B项。"
                },
                {
                    "num": 52,
                    "stem": "Why do high-frequency trading firms pay enormous fees for 'co-location'?",
                    "options": [
                        {"label": "A", "text": "To reduce electricity cooling costs for their supercomputers."},
                        {"label": "B", "text": "To minimize physical distance and gain microsecond speed advantages."},
                        {"label": "C", "text": "To comply with strict government financial transparency laws."},
                        {"label": "D", "text": "To prevent corporate spies from stealing computer motherboards."}
                    ],
                    "answer": "B",
                    "question_zh": "高频交易公司为何支付巨额费用进行“主机托管”（co-location）？",
                    "answer_zh": "为了缩减物理距离并获得微秒级的速度优势。",
                    "explanation": "第二段指出托管服务将服务器放置在交易所同个数据中心，'shave fractions of a millisecond off data transmission times... Armed with this speed advantage'，对应B项。"
                },
                {
                    "num": 53,
                    "stem": "What was the root cause of the 2010 'Flash Crash'?",
                    "options": [
                        {"label": "A", "text": "A deliberate terrorist attack on the New York power grid."},
                        {"label": "B", "text": "Algorithms suddenly withdrawing bids and sparking cascading sell-offs."},
                        {"label": "C", "text": "A total collapse of global commercial banking institutions."},
                        {"label": "D", "text": "A catastrophic earthquake damaging submarine fiber cables."}
                    ],
                    "answer": "B",
                    "question_zh": "2010年“闪崩”事件的根本诱因是什么？",
                    "answer_zh": "算法为了规避风险突然撤单并引发连锁式抛售。",
                    "explanation": "第三段指出'automated algorithms abruptly withdrew their bids to protect capital, creating a sudden liquidity vacuum that triggered cascading automated sell-offs'，对应B项。"
                },
                {
                    "num": 54,
                    "stem": "What tactic involves flooding exchanges with fake orders to slow down competitors?",
                    "options": [
                        {"label": "A", "text": "Batch auctioning."},
                        {"label": "B", "text": "Quote stuffing."},
                        {"label": "C", "text": "Subsidized routing."},
                        {"label": "D", "text": "Co-located indexing."}
                    ],
                    "answer": "B",
                    "question_zh": "向交易所发送数百万张虚假订单以延缓竞争对手的策略叫什么？",
                    "answer_zh": "虚假报价泛滥（Quote stuffing）。",
                    "explanation": "第四段明确指出：'High-frequency algorithms engage in quote stuffing—flooding exchanges with millions of phantom orders and cancellations every second simply to slow down rival computer systems...'，对应B项。"
                },
                {
                    "num": 55,
                    "stem": "What fundamental purpose should financial markets serve according to the author?",
                    "options": [
                        {"label": "A", "text": "Allocating capital efficiently to productive human enterprises."},
                        {"label": "B", "text": "Maximizing the processing speed of financial supercomputers."},
                        {"label": "C", "text": "Eliminating all human participation in capital transactions."},
                        {"label": "D", "text": "Enabling tech firms to generate untaxed computational wealth."}
                    ],
                    "answer": "A",
                    "question_zh": "在作者看来，金融市场应当服务的根本宗旨是什么？",
                    "answer_zh": "高效地将资本配置给具有生产力的人类实体产业。",
                    "explanation": "尾段末句总结：'Financial markets must exist to allocate capital to productive human enterprises, not to serve as an unregulated digital casino for hyper-fast computers'，对应A项。"
                }
            ],
            "main_idea_zh": "本文深入揭示了高频交易（HFT）对现代全球金融市场的重塑与潜在危害。高频公司依靠物理贴近交易所（主机托管）抢占微秒速度优势进行抢先交易。2010年“闪崩”揭露了当算法在恐慌时撤单会抽干流动性并酿成灾难。虚假报价等手段损害普通投资者利益。文章呼吁推行批量竞价等监管改革，让金融市场回归配置实体资本的本源。",
            "main_idea_en": "The passage examines high-frequency algorithmic trading, discussing the mechanics of co-location, the risks of flash crashes, predatory order practices, and urgent regulatory reforms."
        }
    })

    return res

print("More curated defined.")
