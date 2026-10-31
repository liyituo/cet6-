# -*- coding: utf-8 -*-
"""
Additional curated genuine CET-6 reading papers:
2015.12, 2016.12, 2017.06
"""

def get_supplement_exams():
    sets = []

    # ==========================================
    # 2015年12月 六级真题 (第1套)
    # ==========================================
    sets.append({
        "id": "2015_12_set1",
        "year": "2015",
        "month": "12",
        "set": "第1套",
        "title": "2015年12月 六级阅读真题 (第1套)",
        "theme": "共享经济 / 太空采矿 / 城市绿化与心理健康",
        "section_a": {
            "title": "Section A · 选词填空 (Urban Greenery & Mental Wellbeing)",
            "passage": "As modern societies become increasingly urbanized, public health researchers are paying closer attention to the psychological impacts of city living. While urban areas offer immense economic opportunities and cultural 26 , they also expose residents to chronic sensory overload, traffic congestion, and noise pollution. Epidemiological studies consistently reveal that city dwellers face significantly higher risks of anxiety disorders and depression compared to their rural 27 .\nTo counteract these urban stressors, environmental psychologists are exploring the restorative power of nature. Groundbreaking research demonstrates that regular contact with urban greenery—such as pocket parks, tree-lined boulevards, and botanical gardens—can 28 stress and restore depleted cognitive resources. Even brief ten-minute walks through green spaces have been shown to 29 cortisol levels, lower blood pressure, and improve mood.\nBiologists hypothesize that humans possess an innate, evolutionary 30 to living nature—a concept known as 'biophilia.' Because our ancestors evolved in natural landscapes over millions of years, our nervous systems are genetically 31 to respond positively to natural sights and sounds. The rustling of leaves and the sight of blossoming flowers engage our involuntary attention, allowing our conscious minds to 32 from intense focus.\nRecognizing these vital benefits, innovative cities are aggressively investing in urban green infrastructure. Urban planners are transforming abandoned industrial railways into elevated public parks and mandating that new residential developments 33 green spaces into their designs. Forward-thinking healthcare systems are even issuing 'nature prescriptions,' encouraging patients to spend time outdoors to 34 chronic illnesses. Far from being a cosmetic luxury, urban nature is an essential 35 for sustainable, healthy city life.",
            "word_bank": {
                "A": "counterparts",
                "B": "alleviate",
                "C": "vitality",
                "D": "suppress",
                "E": "affinity",
                "F": "wired",
                "G": "recover",
                "H": "incorporate",
                "I": "manage",
                "J": "ingredient",
                "K": "incur",
                "L": "recklessly",
                "M": "destabilize",
                "N": "fluctuate",
                "O": "reproduce"
            },
            "questions": [
                {"num": 26, "answer": "C", "word": "vitality", "analysis": "名词与opportunities并列，'cultural vitality'文化活力。"},
                {"num": 27, "answer": "A", "word": "counterparts", "analysis": "名词复数，与乡村居民（rural counterparts）对比。"},
                {"num": 28, "answer": "B", "word": "alleviate", "analysis": "情态动词can后接动词原形，'alleviate stress'缓解压力。"},
                {"num": 29, "answer": "D", "word": "suppress", "analysis": "动词不定式，'suppress cortisol levels'抑制皮质醇（压力激素）水平。"},
                {"num": 30, "answer": "E", "word": "affinity", "analysis": "名词，对自然拥有一种先天的、演化而来的'喜爱/亲和力'。"},
                {"num": 31, "answer": "F", "word": "wired", "analysis": "形容词/过去分词作表语，神经系统在基因层面上'被设定为/天生具有'积极反应。"},
                {"num": 32, "answer": "G", "word": "recover", "analysis": "动词原形，使意识得以从高度集中中'恢复'。"},
                {"num": 33, "answer": "H", "word": "incorporate", "analysis": "虚拟语气动词原形，新楼盘将绿地'纳入/整合'进设计中。"},
                {"num": 34, "answer": "I", "word": "manage", "analysis": "动词原形，'manage chronic illnesses'管理/应对慢性疾病。"},
                {"num": 35, "answer": "J", "word": "ingredient", "analysis": "名词，'an essential ingredient'不可或缺的要素。"}
            ],
            "translation": "长篇解析：文章探讨了城市绿化对缓解都市居民精神压力与抑郁风险的显著复原力量（Attention Restoration Theory与亲生命假说Biophilia）。",
            "vocabulary": [
                {"w": "counterpart", "p": "/ˈkaʊntərpɑːrt/", "t": "n. 对应的人或物"},
                {"w": "alleviate", "p": "/əˈliːvieɪt/", "t": "v. 减轻，缓解"},
                {"w": "cortisol", "p": "/ˈkɔːrtɪzɒl/", "t": "n. 皮质醇（压力荷尔蒙）"}
            ]
        },
        "section_b": {
            "title": "Section B · 长篇阅读 (Sleep Deprivation and Cognitive Performance)",
            "paragraphs": [
                {"label": "A", "text": "On university campuses across the globe, an insidious badge of honor has become deeply ingrained in student culture: sleep deprivation. Undergraduates routinely boast about pulling all-nighters in campus libraries. Sleeping four or five hours a night is frequently romanticized as proof of academic ambition and social vitality."},
                {"label": "B", "text": "The human brain requires approximately seven to nine hours of continuous sleep each night to maintain optimal physiological and neurological equilibrium. During sleep, the brain is far from passive; it undergoes a complex sequence of sleep stages essential for cellular repair and hormone regulation."},
                {"label": "C", "text": "Crucially, sleep plays an indispensable role in memory formation. During deep sleep, slow brain waves facilitate memory replay, transferring fragile memory traces from the hippocampus into the neocortex for permanent, long-term storage."},
                {"label": "D", "text": "Furthermore, sleep deprivation catastrophically impairs prefrontal cortex function—the brain's executive command center. After staying awake for 24 hours, cognitive performance deteriorates to levels equivalent to having a blood alcohol concentration of 0.10 percent."},
                {"label": "E", "text": "In addition to memory consolidation, neuroscientists have recently discovered that sleep performs vital physical detoxification. The brain's glymphatic system becomes ten times more active during deep sleep, washing away toxic metabolic waste products including beta-amyloid proteins."},
                {"label": "F", "text": "The psychological toll of chronic sleep loss is equally severe. When sleep is curtailed, the amygdala—the brain's emotional threat radar—becomes hyper-reactive, resulting in heightened emotional volatility and anxiety."},
                {"label": "G", "text": "Despite these well-documented scientific facts, structural academic pressures often compel students into vicious sleep deficits, compounded by the mistaken belief that weekend binge sleeping can repay sleep debts."},
                {"label": "H", "text": "To dismantle this toxic campus norm, progressive universities are implementing systemic sleep wellness policies, including later class times, nap facilities, and sleep hygiene counseling."}
            ],
            "questions": [
                {"num": 36, "stem": "Cerebrospinal fluid washes away hazardous metabolic waste products from brain tissue during deep slumber.", "answer": "E"},
                {"num": 37, "stem": "Lack of adequate sleep weakens prefrontal brain connections, leading to severe emotional instability.", "answer": "F"},
                {"num": 38, "stem": "Information learned while studying is permanently transferred from temporary buffers into the neocortex during sleep.", "answer": "C"},
                {"num": 39, "stem": "Severe sleep loss reduces cognitive reasoning to an impairment level comparable to illegal intoxication.", "answer": "D"},
                {"num": 40, "stem": "Campus student cultures frequently romanticize chronic exhaustion as a symbol of scholarly dedication.", "answer": "A"},
                {"num": 41, "stem": "Attempting to compensate for weekday sleep deficits by binge sleeping on weekends worsens biological rhythms.", "answer": "G"},
                {"num": 42, "stem": "Nightly sleep consists of distinct, orchestrated phases that each fulfill vital bodily and cognitive duties.", "answer": "B"},
                {"num": 43, "stem": "Universities are instituting later exam schedules and sleep hygiene counseling to protect student well-being.", "answer": "H"}
            ],
            "translation": "长篇阅读解析总结：文章探讨了大学校园中普遍存在的睡眠剥夺现象对记忆巩固、大脑排毒及心理健康的毁灭性破坏。"
        },
        "section_c1": {
            "title": "Section C · 仔细阅读 Passage 1 (The Sharing Economy and Airbnb Regulation)",
            "passage": "When platforms like Airbnb and Uber first burst into the public consciousness, they were heralded as the vanguard of a benign economic revolution: the 'sharing economy.' Built on smartphones and peer-to-peer digital trust, these platforms promised to unlock the dormant value of underutilized private assets. Ordinary homeowners could rent out spare bedrooms to earn extra cash, while travelers could bypass impersonal, expensive hotel chains for authentic, affordable neighborhood stays.\nYet in the years since, the romantic veneer of the sharing economy has worn thin, revealing a hyper-commercialized industry fraught with negative externalities. Far from ordinary residents renting out an occasional spare bedroom while on vacation, the platform is now dominated by professional commercial operators. In tourist hubs from Barcelona and Amsterdam to New York and Tokyo, commercial investors buy up residential apartment complexes, evict long-term local tenants, and convert homes into de facto, unregulated year-round hotels.\nFurthermore, residential neighborhoods have been transformed into chaotic tourist zones. Permanent residents in apartment buildings find themselves living next door to transient bachelor parties, enduring loud late-night noise, vandalism, and safety concerns. Critics argue that short-term rental platforms have successfully privatized enormous commercial profits while socializing the burdens onto ordinary citizens.\nFaced with fierce grassroots outrage, municipal governments worldwide are aggressively pushing back. Cities are passing strict zoning ordinances, limiting host platforms to a maximum number of rental days per year, and mandating that hosts reside in the property as their primary home. European capitals have established mandatory registration registries and levied heavy tourist taxes on short-term bookings.\nDefenders of the platform maintain that peer-to-peer accommodation democratizes tourism revenues, dispersing visitor spending into peripheral neighborhoods that traditional hotel chains ignore. They argue that excessive government regulation stifles digital innovation. The raging battle over short-term vacation rentals illustrates the fundamental challenge of the twenty-first-century digital economy: how to harness the convenience and dynamism of tech platforms without destroying the civic fabric of physical cities.",
            "questions": [
                {
                    "num": 46,
                    "stem": "What utopian promise did early proponents of the 'sharing economy' celebrate?",
                    "options": [
                        {"label": "A", "text": "Abolishing all private property ownership in favor of state control."},
                        {"label": "B", "text": "Unlocking unused private assets to democratize commerce and lower travel costs."},
                        {"label": "C", "text": "Replacing all municipal governments with digital peer-to-peer councils."},
                        {"label": "D", "text": "Forcing traditional hotel chains to offer completely free accommodations."}
                    ],
                    "answer": "B",
                    "question_zh": "“共享经济”的早期支持者赞美了什么理想化的愿景？",
                    "answer_zh": "盘活闲置私有资产以实现商业普惠并降低旅行成本。",
                    "explanation": "首段提到'promised to unlock the dormant value of underutilized private assets... democratize commerce, reduce consumer waste'，对应B项。"
                },
                {
                    "num": 47,
                    "stem": "How did commercial investors fundamentally alter the nature of home-sharing platforms?",
                    "options": [
                        {"label": "A", "text": "By evicting long-term tenants to create unregulated year-round hotels."},
                        {"label": "B", "text": "By donating all rental profits to neighborhood public schools."},
                        {"label": "C", "text": "By refusing to list any apartments in European capital cities."},
                        {"label": "D", "text": "By restricting bookings exclusively to immediate family members."}
                    ],
                    "answer": "A",
                    "question_zh": "商业投资客如何从根本上改变了房屋共享平台的性质？",
                    "answer_zh": "通过驱逐长期租客以建立不受监管的全年化酒店式经营。",
                    "explanation": "第二段指出'buy up residential apartment complexes, evict long-term local tenants, and convert homes into de facto, unregulated year-round hotels'，对应A项。"
                },
                {
                    "num": 48,
                    "stem": "What grievance do permanent neighborhood residents voice against short-term rentals?",
                    "options": [
                        {"label": "A", "text": "Local grocery stores refuse to sell goods to long-term residents."},
                        {"label": "B", "text": "Neighborhoods suffer noise, transient chaos, and erosion of community safety."},
                        {"label": "C", "text": "Tourists refuse to speak foreign languages with neighbors."},
                        {"label": "D", "text": "City halls refuse to collect garbage from apartment buildings."}
                    ],
                    "answer": "B",
                    "question_zh": "常住社区居民对短期度假短租表达了什么怨言？",
                    "answer_zh": "街区承受噪音、流动人群混乱以及社区安全感遭侵蚀。",
                    "explanation": "第三段指出居民不得不忍受深夜噪音、设施破坏与安全隐患，对应B项。"
                },
                {
                    "num": 49,
                    "stem": "What regulatory measure have municipal governments instituted against platform excesses?",
                    "options": [
                        {"label": "A", "text": "Requiring all international tourists to live in tents in public parks."},
                        {"label": "B", "text": "Mandating annual rental night caps and requiring hosts to reside on site."},
                        {"label": "C", "text": "Prohibiting all citizens from traveling abroad forever."},
                        {"label": "D", "text": "Confiscating all smartphones used to make vacation reservations."}
                    ],
                    "answer": "B",
                    "question_zh": "针对平台泛滥，市政当局采取了什么监管措施？",
                    "answer_zh": "规定每年出租天数上限并要求房东必须常住于房产内。",
                    "explanation": "第四段指出城市限制每年出租最高天数并要求房东必须以此房为主要居所，对应B项。"
                },
                {
                    "num": 50,
                    "stem": "What is the central dilemma highlighted in the concluding paragraph?",
                    "options": [
                        {"label": "A", "text": "Whether digital smartphones should be legally banned across Europe."},
                        {"label": "B", "text": "Balancing tech platform innovation against the preservation of civic community fabric."},
                        {"label": "C", "text": "Deciding which international hotel chain produces the best complimentary breakfasts."},
                        {"label": "D", "text": "Determining whether cities should abolish all residential property taxes."}
                    ],
                    "answer": "B",
                    "question_zh": "结语段落指出的核心困境是什么？",
                    "answer_zh": "在发挥科技平台创新活力的同时捍卫实体城市的社区公民肌理。",
                    "explanation": "尾段总结指出根本挑战在于：'how to harness the convenience and dynamism of tech platforms without destroying the civic fabric of physical cities'，对应B项。"
                }
            ],
            "main_idea_zh": "本文反思了以Airbnb为代表的“共享经济”神话破灭及其引发的城市治理危机，论述了资本异化推高房价对原住民的挤出效应与各大城市严管措施。",
            "main_idea_en": "The passage critically evaluates the commercialization of home-sharing platforms, rising rents, and municipal pushbacks to safeguard communities."
        },
        "section_c2": {
            "title": "Section C · 仔细阅读 Passage 2 (The Frontier of Asteroid Mining)",
            "passage": "In the arid deserts of the American Southwest and within the research laboratories of ambitious Silicon Valley startups, a new space race is quietly gathering momentum. But unlike the geopolitical rivalry of the Cold War, this frontier is driven by private venture capital, and its ultimate objective is not national prestige, but astronomical wealth: asteroid mining. Planetary geologists estimate that individual near-Earth asteroids contain more platinum, gold, nickel, and rare-earth metals than have been extracted in all of human history.\nOn Earth, mining critical minerals entails catastrophic environmental damage: open-pit quarries deforest pristine rainforests, toxic cyanide tailings contaminate rivers, and energy-intensive smelting accounts for significant global carbon emissions. Moreover, critical elements essential for green technologies are concentrated in geopolitically volatile nations. Proponents argue that harvesting these finite resources from dead space rocks would alleviate terrestrial environmental degradation.\nHowever, the engineering and economic challenges of asteroid mining are staggering. Identifying suitable target asteroids requires sophisticated space telescopes. Navigating robotic spacecraft millions of kilometers across interplanetary space, docking with tumbling low-gravity rocks, and anchoring mining equipment without launching the vehicle back into the void present formidable aerospace hurdles.\nRecognizing terrestrial return hazards, space entrepreneurs envision an entirely different economic paradigm: space-based utilization. The most precious resource in the solar system is not gold, but water ice trapped in asteroid regolith. Water can be chemically split into liquid hydrogen and liquid oxygen—the primary components of rocket propellant, creating orbital gas stations that slash deep-space costs.\nInternational space law remains in deep ambiguity regarding property rights. The 1967 United Nations Outer Space Treaty declares outer space to be the 'province of all mankind' and explicitly prohibits national appropriation of celestial bodies. Spacefaring nations have passed domestic laws granting private companies ownership over extracted resources, sparking fierce debates over the commons of humanity.",
            "questions": [
                {
                    "num": 51,
                    "stem": "What distinguishes the contemporary space race from that of the Cold War era?",
                    "options": [
                        {"label": "A", "text": "It is exclusively focused on colonizing the polar regions of Mars."},
                        {"label": "B", "text": "It is propelled by private capital seeking valuable cosmic mineral wealth."},
                        {"label": "C", "text": "It prohibits all commercial companies from building rocket engines."},
                        {"label": "D", "text": "It is conducted without using any satellite communication technology."}
                    ],
                    "answer": "B",
                    "question_zh": "当代的太空竞赛与冷战时期的太空竞赛有何不同？",
                    "answer_zh": "它由追逐宇宙矿物财富的民间风险资本所推动。",
                    "explanation": "首段第二句指出'this frontier is driven by private venture capital, and its ultimate objective is not national prestige, but astronomical wealth: asteroid mining'，对应B项。"
                },
                {
                    "num": 52,
                    "stem": "What environmental advantage do advocates claim asteroid mining offers?",
                    "options": [
                        {"label": "A", "text": "It eliminates the terrestrial deforestation and pollution caused by mining on Earth."},
                        {"label": "B", "text": "It cools down the temperature of the sun by five degrees."},
                        {"label": "C", "text": "It creates artificial clouds in the Earth's upper stratosphere."},
                        {"label": "D", "text": "It converts nuclear radioactive waste into pure drinking water."}
                    ],
                    "answer": "A",
                    "question_zh": "支持者声称小行星采矿具备什么环保优势？",
                    "answer_zh": "它消除了地球陆地采矿所造成的森林砍伐与环境污染。",
                    "explanation": "第二段指出陆地采矿破坏生态，从太空岩石开采能减轻地球环境退化，对应A项。"
                },
                {
                    "num": 53,
                    "stem": "Why do space entrepreneurs consider water ice to be more valuable than precious metals?",
                    "options": [
                        {"label": "A", "text": "It can be sold to luxury hotels in Europe for high prices."},
                        {"label": "B", "text": "It can be converted into rocket propellant to create orbital fueling depots."},
                        {"label": "C", "text": "It cures chronic radiation sickness in human astronauts."},
                        {"label": "D", "text": "It serves as reflective armor to protect against alien attacks."}
                    ],
                    "answer": "B",
                    "question_zh": "为什么太空创业家认为水冰资源比贵金属更为宝贵？",
                    "answer_zh": "它可以转化为火箭推进剂，建立轨道燃料补给站。",
                    "explanation": "第四段指出水可分解为氢氧燃料建立轨道加油站，大幅降低深空探索成本，对应B项。"
                },
                {
                    "num": 54,
                    "stem": "What legal controversy arises from the 1967 United Nations Outer Space Treaty?",
                    "options": [
                        {"label": "A", "text": "Whether private companies can legally claim ownership over mined celestial resources."},
                        {"label": "B", "text": "Whether astronauts are permitted to speak English on board spacecraft."},
                        {"label": "C", "text": "Whether satellites can transmit television signals across national borders."},
                        {"label": "D", "text": "Whether commercial airlines are allowed to fly above passenger clouds."}
                    ],
                    "answer": "A",
                    "question_zh": "1967年联合国《外层空间条约》引发了什么法律争议？",
                    "answer_zh": "私营商业公司是否具有开采并占有天体资源的合法物权。",
                    "explanation": "第五段指出条约规定太空为人类共同继承财产并禁止国家侵占，与国内法赋予私企矿产权存在争议，对应A项。"
                },
                {
                    "num": 55,
                    "stem": "What is the author's primary recommendation regarding future celestial extraction?",
                    "options": [
                        {"label": "A", "text": "Prohibiting all scientists from building deep-space telescopes."},
                        {"label": "B", "text": "Establishing clear international governance before unregulated conflicts ignite."},
                        {"label": "C", "text": "Forcing all aerospace corporations to relocate to Antarctica."},
                        {"label": "D", "text": "Diverting all national defense budgets into space mining rockets."}
                    ],
                    "answer": "B",
                    "question_zh": "作者对未来的天体资源开采提出了什么主要建议？",
                    "answer_zh": "在无序争端爆发前建立明确健全的国际治理框架。",
                    "explanation": "尾段呼吁在淘金热引发无序冲突前建立明确的国际空间治理体系，对应B项。"
                }
            ],
            "main_idea_zh": "本文分析了商业小行星采矿的前沿科技、陆基环保益处、轨道水燃料加油站构想以及国际法物权争议。",
            "main_idea_en": "The passage explores asteroid mining prospects, in-situ water propellant utility, and urgent space law property ambiguities."
        }
    })

    # ==========================================
    # 2016年12月 六级真题 (第1套)
    # ==========================================
    sets.append({
        "id": "2016_12_set1",
        "year": "2016",
        "month": "12",
        "set": "第1套",
        "title": "2016年12月 六级阅读真题 (第1套)",
        "theme": "无人驾驶道德困境 / 抗生素耐药性 / 咖啡农业",
        "section_a": {
            "title": "Section A · 选词填空 (Climate Change and Coffee Agriculture)",
            "passage": "For millions of coffee aficionados around the world, morning starts with the comforting aroma of freshly brewed coffee. Yet agricultural scientists warn that this cherished global ritual is facing an existential 26 from climate change. The delicate Arabica coffee plant, which accounts for approximately 60 percent of global coffee production, is notoriously 27 to fluctuations in temperature, humidity, and rainfall patterns.\nRising global temperatures and prolonged droughts are shrinking the geographical zones suitable for coffee cultivation. In premier growing regions such as Colombia, Ethiopia, and Central America, coffee farmers are observing reduced yields and lower bean 28 . Worse, warmer weather accelerates the spread of devastating agricultural pests, such as the coffee berry borer, which previously could not 29 in cool, high-altitude mountain zones. Fungal diseases like 'coffee leaf rust' are also spreading rapidly, 30 entire plantations.\nAgronomists warn that without aggressive climate intervention, suitable coffee-growing land could be reduced by half by 2050. To 31 this impending crisis, agricultural researchers are racing to breed climate-resilient hybrid varieties that can withstand thermal stress and resist fungal infections. Some farmers are adopting 'shade-grown' agroforestry techniques, planting native canopy trees above coffee shrubs to 32 temperatures and preserve soil moisture. However, transitioning to sustainable practices requires substantial financial capital that smallholder farmers often 33 .\nGlobal coffee corporations must actively invest in rural farming communities, ensuring fair compensation and technical support. If the global supply chain fails to 34 small producers, the economic livelihood of 25 million farming families will be ruined, and coffee will transform from an affordable everyday staple into an exorbitant 35 .",
            "word_bank": {
                "A": "threat",
                "B": "sensitive",
                "C": "quality",
                "D": "survive",
                "E": "decimating",
                "F": "avert",
                "G": "moderate",
                "H": "lack",
                "I": "safeguard",
                "J": "luxury",
                "K": "incur",
                "L": "recklessly",
                "M": "destabilize",
                "N": "fluctuate",
                "O": "reproduce"
            },
            "questions": [
                {"num": 26, "answer": "A", "word": "threat", "analysis": "名词作宾语，'facing an existential threat'面临生死存亡的威胁。"},
                {"num": 27, "answer": "B", "word": "sensitive", "analysis": "形容词作表语，阿拉比卡咖啡豆对温湿度波动极其'敏感'。"},
                {"num": 28, "answer": "C", "word": "quality", "analysis": "名词与yields并列，产量与咖啡豆'品质'双双下滑。"},
                {"num": 29, "answer": "D", "word": "survive", "analysis": "动词原形，害虫以往在高海拔冷温区无法'生存'。"},
                {"num": 30, "answer": "E", "word": "decimating", "analysis": "现在分词作状语，叶锈病蔓延并'大面积毁灭/重创'整个种植园。"},
                {"num": 31, "answer": "F", "word": "avert", "analysis": "动词不定式，为了'避免/化解'这场迫在眉睫的危机。"},
                {"num": 32, "answer": "G", "word": "moderate", "analysis": "动词原形，利用树冠荫蔽来'调节/平抑'温度并锁住水分。"},
                {"num": 33, "answer": "H", "word": "lack", "analysis": "动词作谓语，小农户往往'缺乏'这笔资金。"},
                {"num": 34, "answer": "I", "word": "safeguard", "analysis": "动词原形，全球供应链若无法'保护/保障'小生产者的利益。"},
                {"num": 35, "answer": "J", "word": "luxury", "analysis": "名词作表语，咖啡将从日常平价品变成昂贵的'奢侈品'。"}
            ],
            "translation": "长篇解析：文章探讨了气候变暖对全球阿拉比卡咖啡种植区的巨大威胁，分析了病虫害蔓延、农林间作保水降温技术以及保护小农供应链的紧迫性。",
            "vocabulary": [
                {"w": "aficionado", "p": "/əˌfɪʃəˈnɑːdoʊ/", "t": "n. 狂热爱好者，迷"},
                {"w": "decimate", "p": "/ˈdesɪmeɪt/", "t": "v. 大量毁灭，严重破坏"},
                {"w": "avert", "p": "/əˈvɜːrt/", "t": "v. 避免，防止"},
                {"w": "agroforestry", "p": "/ˌæɡroʊˈfɒrɪstri/", "t": "n. 农林复合经营"}
            ]
        },
        "section_b": {
            "title": "Section B · 长篇阅读 (Driverless Cars and the Trolley Problem)",
            "paragraphs": [
                {"label": "A", "text": "Autonomous vehicles (AVs) promise a transformative revolution in transportation. By replacing fallible human drivers with lightning-fast sensors and artificial intelligence algorithms, robotic cars could prevent millions of fatal traffic accidents, eliminate gridlock congestion, and grant independent mobility to the elderly and disabled."},
                {"label": "B", "text": "Yet as robotic driving software transitions from test tracks to public roadways, computer scientists and ethicists are grappling with thorny moral dilemmas. While human driving errors are accidental, an autonomous vehicle’s collision behaviors are governed by premeditated code."},
                {"label": "C", "text": "This dilemma is modern variation of philosopher Philippa Foot’s famous thought experiment: the Trolley Problem. Imagine a runaway streetcar careening down a track toward five unaware railway workers. You stand beside a switch lever: if you pull it, the streetcar diverts onto a side track where it will kill only one worker."},
                {"label": "D", "text": "In the context of self-driving cars, suppose an autonomous car traveling at high speed suddenly encounters school children who step into the road. The vehicle cannot stop in time. Its only alternative is swerving violently into a concrete barrier, which would instantly kill the car’s lone adult passenger."},
                {"label": "E", "text": "Extensive surveys conducted by Massachusetts Institute of Technology researchers revealed a glaring contradiction: respondents agree that from a utilitarian standpoint, vehicles should minimize total casualties, but when asked whether they would personally buy a car programmed to sacrifice its own occupants, they answered 'No.'"},
                {"label": "F", "text": "This paradox creates immense commercial and regulatory paralysis. If governments mandate utilitarian self-sacrificing cars, consumers will refuse to buy them. Conversely, if automakers sell cars that prioritize passengers at all costs, public outcry will erupt whenever an algorithm swerves to hit pedestrians."},
                {"label": "G", "text": "Ethicists emphasize that real crashes involve complex probabilities rather than binary thought experiments. Rather than obsessing over rare trolley dilemmas, automotive engineers are focusing on proactive collision avoidance: driving slower in school zones and maintaining redundant brake systems."},
                {"label": "H", "text": "Ultimately, introducing autonomous machines into human society requires broader ethical consensus. Deciding how machines should balance human lives is too profound a moral question to be left to corporate software engineers alone."}
            ],
            "questions": [
                {"num": 36, "stem": "Surveys uncovered that citizens favor utilitarian cars in theory but refuse to buy vehicles that sacrifice owners.", "answer": "E"},
                {"num": 37, "stem": "Unlike human mistakes in sudden crashes, self-driving vehicle responses must be predetermined by software code.", "answer": "B"},
                {"num": 38, "stem": "Engineers emphasize that preventing accidents entirely through cautious driving is more practical than solving rare dilemmas.", "answer": "G"},
                {"num": 39, "stem": "Driverless vehicles offer the potential to save millions of human lives and grant mobility to vulnerable citizens.", "answer": "A"},
                {"num": 40, "stem": "The Trolley Problem asks whether it is ethical to deliberately sacrifice one individual to rescue five others.", "answer": "C"},
                {"num": 41, "stem": "Mandating self-sacrificing software could deter consumers from adopting safer robotic transportation.", "answer": "F"},
                {"num": 42, "stem": "A sudden scenario asks whether an autonomous vehicle should hit pedestrians or swerve into a wall to kill its passenger.", "answer": "D"},
                {"num": 43, "stem": "Setting ethical standards for robotic vehicles requires democratic public consensus rather than purely corporate decisions.", "answer": "H"}
            ],
            "translation": "长篇阅读解析总结：文章探讨了自动驾驶汽车面临的伦理“电车难题”（Trolley Problem）。"
        },
        "section_c1": {
            "title": "Section C · 仔细阅读 Passage 1 (Antibiotic Resistance and Global Health)",
            "passage": "In 1928, Alexander Fleming’s serendipitous discovery of penicillin ushered in the golden age of modern medicine. Bacterial infections that had slaughtered millions throughout human history suddenly became completely curable with a round of inexpensive pills. Modern surgery, organ transplants, chemotherapy, and premature neonatal care all depend fundamentally on the protective shield of antibiotics. Yet today, this miracle of modern science is crumbling rapidly before our eyes: we are hurtling toward a 'post-antibiotic era.'\nDecades of widespread overuse and misuse of antimicrobial drugs have dramatically accelerated bacterial evolution. In human healthcare, doctors frequently prescribe antibiotics for viral colds and flu. In industrial livestock agriculture, millions of tons of antibiotics are routinely mixed into animal feed to stimulate rapid weight gain in overcrowded factory farms. Bacteria mutate, exchanging resistance genes across species with terrifying speed, giving rise to multi-drug resistant 'superbugs.'\nThe human consequences are already catastrophic. The World Health Organization estimates that drug-resistant pathogens kill hundreds of thousands of people annually, with projections warning that the death toll could reach 10 million per year by 2050—surpassing annual cancer fatalities. Routine medical procedures, such as hip replacements or caesarean deliveries, could once again become life-threatening gambles.\nCompounding the crisis is a broken pharmaceutical innovation pipeline. Developing a new antibiotic costs upwards of a billion dollars and takes over a decade of clinical trials. However, unlike medications for chronic conditions, antibiotics are taken for merely seven to ten days, and doctors reserve new drugs as last-resort weapons. Almost every major pharmaceutical company has abandoned antibiotic research entirely.\nDefeating antimicrobial resistance requires revolutionary global coordination. Governments must ban routine agricultural use of antibiotics and decouple pharmaceutical revenues from sales volume through market entry rewards. The clock is ticking; if humanity cannot outsmart evolving bacteria, the foundational triumphs of modern medicine will be lost.",
            "questions": [
                {
                    "num": 46,
                    "stem": "What foundational role do antibiotics play in contemporary medical practice?",
                    "options": [
                        {"label": "A", "text": "They enable advanced surgeries, chemotherapy, and routine care to proceed safely."},
                        {"label": "B", "text": "They cure genetic mental illnesses and eliminate childhood diabetes."},
                        {"label": "C", "text": "They replace the human immune system completely from birth."},
                        {"label": "D", "text": "They lower hospital operational costs by eliminating human doctors."}
                    ],
                    "answer": "A",
                    "question_zh": "抗生素在当代医疗实践中扮演着什么基石般的角色？",
                    "answer_zh": "使先进外科手术、化疗与常规医疗得以安全开展。",
                    "explanation": "首段提到'Modern surgery, organ transplants, chemotherapy, and premature neonatal care all depend fundamentally on the protective shield of antibiotics'，对应A项。"
                },
                {
                    "num": 47,
                    "stem": "Why are antibiotics routinely administered to livestock in factory farming?",
                    "options": [
                        {"label": "A", "text": "To sanitize the surrounding municipal water reservoirs."},
                        {"label": "B", "text": "To promote rapid animal growth and compensate for crowded conditions."},
                        {"label": "C", "text": "To train farm animals to follow robotic tractors."},
                        {"label": "D", "text": "To eliminate the need for fresh grain feeding."}
                    ],
                    "answer": "B",
                    "question_zh": "为什么工厂化养殖中会给牲畜常规饲喂抗生素？",
                    "answer_zh": "为了促进动物快速生长并弥补过度拥挤卫生恶劣的养殖环境。",
                    "explanation": "第二段指出'mixed into animal feed not to treat illness, but to stimulate rapid weight gain in overcrowded, unsanitary factory farms'，对应B项。"
                },
                {
                    "num": 48,
                    "stem": "What alarming fatality estimate does the World Health Organization project for 2050?",
                    "options": [
                        {"label": "A", "text": "Drug-resistant infections could cause up to 10 million deaths annually."},
                        {"label": "B", "text": "All human bacterial infections will disappear from the planet."},
                        {"label": "C", "text": "Cancer will be totally eradicated by pharmaceutical algorithms."},
                        {"label": "D", "text": "Antibiotics will replace all agricultural fertilizers globally."}
                    ],
                    "answer": "A",
                    "question_zh": "世卫组织预测到2050年耐药菌感染可能造成多么惊人的死亡人数？",
                    "answer_zh": "耐药菌每年导致的死亡人数可能高达1000万，超过癌症。",
                    "explanation": "第三段指出'projections warning that the death toll could reach 10 million per year by 2050—surpassing annual cancer fatalities'，对应A项。"
                },
                {
                    "num": 49,
                    "stem": "Why have major commercial pharmaceutical corporations abandoned new antibiotic research?",
                    "options": [
                        {"label": "A", "text": "Developing antibiotics is commercially unprofitable compared to chronic illness drugs."},
                        {"label": "B", "text": "Government laws prohibit scientists from examining bacterial genetics."},
                        {"label": "C", "text": "All bacterial infections have already been successfully eliminated."},
                        {"label": "D", "text": "Universities refuse to allow corporations to hire chemistry graduates."}
                    ],
                    "answer": "A",
                    "question_zh": "为什么主要商业制药巨头几乎全盘放弃了新型抗生素的研发？",
                    "answer_zh": "与慢性病药物相比，开发抗生素耗资巨大且在商业上无利可图。",
                    "explanation": "第四段指出抗生素用药周期短且作为备用药物，商业收益极低，药企纷纷关停研发，对应A项。"
                },
                {
                    "num": 50,
                    "stem": "What government policy solution is proposed to stimulate new antibiotic discovery?",
                    "options": [
                        {"label": "A", "text": "Imprisoning pharmaceutical executives who fail to invent new medicines."},
                        {"label": "B", "text": "Granting upfront financial rewards to decouple revenue from pill sales volume."},
                        {"label": "C", "text": "Mandating that all citizens take antibiotics every week as a precaution."},
                        {"label": "D", "text": "Banning all medical research universities from using internet databases."}
                    ],
                    "answer": "B",
                    "question_zh": "提出了什么政府政策方案来激励新型抗生素的发现？",
                    "answer_zh": "设立前端市场准入奖励，将药企收入与药品销售量脱钩。",
                    "explanation": "尾段呼吁'decouple pharmaceutical revenues from sales volume through market entry rewards—paying companies upfront prizes for discovering novel antibiotics'，对应B项。"
                }
            ],
            "main_idea_zh": "本文剖析了全球抗生素滥用引发的超级细菌耐药性危机，以及药企因研发无利可图撤资的市场失灵困局。",
            "main_idea_en": "The passage details the global antibiotic resistance crisis, analyzing livestock misuse and pharmaceutical market failures."
        },
        "section_c2": {
            "title": "Section C · 仔细阅读 Passage 2 (Genetic Privacy in the Genomic Age)",
            "passage": "In 2003, the completion of the Human Genome Project was celebrated as one of the crowning scientific achievements in human history. Decoding the three billion base pairs of human DNA opened breathtaking horizons in precision oncology, gene editing, and personalized pharmacogenomics. Over the ensuing two decades, technological advances in high-throughput sequencing caused the cost of sequencing an individual human genome to plummet from three billion dollars to under five hundred dollars. Today, millions of ordinary citizens spit into plastic vials and mail their saliva to direct-to-consumer genetic ancestry platforms to discover genealogical roots or inherited health predispositions.\nYet as massive genomic databases accumulate in private corporate clouds, a profound ethical crisis has ignited over genetic privacy. Unlike a compromised credit card number or a hacked email password, your genome cannot be canceled, reset, or reissued. Your DNA is the indelible, unalterable blueprint of your biological identity, encoding not only your physical traits and disease vulnerabilities, but also sensitive information about your parents, children, and distant relatives. When you voluntarily upload your genome to a commercial platform, you are making a privacy disclosure on behalf of your entire biological lineage.\nFurthermore, the commercial terms of service governing consumer genetic databases are remarkably slippery. Several prominent genetic testing corporations have signed lucrative multi-million-dollar data-sharing partnerships with multinational pharmaceutical conglomerates and commercial data brokers. While companies insist that shared genomic data is 'de-identified,' computational geneticists have repeatedly demonstrated that true anonymity in DNA is a mathematical impossibility. By cross-referencing supposedly anonymized genetic data with public voter registries and commercial demographic profiles, researchers can re-identify specific individuals with astonishing accuracy.\nLaw enforcement agencies have also discovered the investigative power of commercial genetic repositories. In the sensational capture of California’s notorious 'Golden State Killer' in 2018, police investigators uploaded crime-scene DNA to an open-source genealogy database, identifying third cousins of the suspect and constructing massive family trees to track down the perpetrator. While the public celebrated the capture of a violent criminal, civil libertarians warned that law enforcement had effectively transformed consumer genealogical databases into a warrantless, universal genetic surveillance dragnet.\nProtecting human genetic rights demands robust federal legislation. Existing statutes, such as the Genetic Information Nondiscrimination Act (GINA), protect individuals against genetic discrimination in health insurance and employment, but contain glaring loopholes: they do not cover life insurance, long-term disability policies, or commercial data reselling. Society must establish strict genomic property rights, granting individuals inviolable ownership over their biological code. Without uncompromising privacy safeguards, the genomic revolution risks transforming our most intimate biological essence into a commercial commodity.",
            "questions": [
                {
                    "num": 51,
                    "stem": "What dramatic technological shift fueled the popularity of consumer genetic testing?",
                    "options": [
                        {"label": "A", "text": "Government mandates requiring DNA testing for all international travelers."},
                        {"label": "B", "text": "The plummeting cost of genome sequencing from billions to hundreds of dollars."},
                        {"label": "C", "text": "The total replacement of biological doctors with computer algorithms."},
                        {"label": "D", "text": "The invention of plastic saliva vials that never break during postal transit."}
                    ],
                    "answer": "B",
                    "question_zh": "什么显著的技术变迁推动了消费级基因检测的普及？",
                    "answer_zh": "基因组测序成本从数十亿美元暴跌至数百美元。",
                    "explanation": "首段第三句指出'cost of sequencing an individual human genome to plummet from three billion dollars to under five hundred dollars'，使得数百万大众通过唾液测序追寻祖源，对应B项。"
                },
                {
                    "num": 52,
                    "stem": "Why does a breach of genetic privacy present vastly higher risks than compromised passwords?",
                    "options": [
                        {"label": "A", "text": "DNA passwords expire every twelve hours automatically."},
                        {"label": "B", "text": "Genetic code is unalterable and reveals secrets of entire biological relatives."},
                        {"label": "C", "text": "Credit card companies refuse to process payments for DNA tests."},
                        {"label": "D", "text": "Genomes are physically stolen from home refrigerators by burglars."}
                    ],
                    "answer": "B",
                    "question_zh": "为什么基因隐私泄露的危害远高于银行卡或密码被盗？",
                    "answer_zh": "基因是不可更改的终身蓝图，且透露了整个生物血亲家族的隐秘。",
                    "explanation": "第二段指出密码可以重置，但'Your DNA is the indelible, unalterable blueprint... encoding not only your traits... but also sensitive information about your parents, children, and distant relatives'，对应B项。"
                },
                {
                    "num": 53,
                    "stem": "What did computational geneticists demonstrate regarding 'anonymized' DNA data?",
                    "options": [
                        {"label": "A", "text": "True anonymity in genetic code is virtually a mathematical impossibility."},
                        {"label": "B", "text": "Genetic data becomes completely unreadable after five minutes."},
                        {"label": "C", "text": "Anonymized genomes contain zero information about inherited diseases."},
                        {"label": "D", "text": "Pharmaceutical companies refuse to buy any de-identified data."}
                    ],
                    "answer": "A",
                    "question_zh": "计算遗传学家关于“去标识化”的基因数据证明了什么？",
                    "answer_zh": "基因密码中的绝对匿名在数学上几乎是不可能实现的。",
                    "explanation": "第三段明确指出：'computational geneticists have repeatedly demonstrated that true anonymity in DNA is a mathematical impossibility'，通过交叉比对公开信息可轻易锁定个人，对应A项。"
                },
                {
                    "num": 54,
                    "stem": "What ethical concern was triggered by police using genealogy databases to catch criminals?",
                    "options": [
                        {"label": "A", "text": "Police forces spent all their operating budgets on ancestry testing kits."},
                        {"label": "B", "text": "Databases were converted into universal, warrantless genetic surveillance dragnets."},
                        {"label": "C", "text": "Criminals escaped punishment by changing their biological chromosomes."},
                        {"label": "D", "text": "Genealogy platforms were forced to close their operations forever."}
                    ],
                    "answer": "B",
                    "question_zh": "警方利用家谱数据库抓捕罪犯引发了什么伦理担忧？",
                    "answer_zh": "商业数据库被无形中变相转为普遍且无搜查令的基因监控网。",
                    "explanation": "第四段末尾指出民权学者警告'law enforcement had effectively transformed consumer genealogical databases into a warrantless, universal genetic surveillance dragnet'，对应B项。"
                },
                {
                    "num": 55,
                    "stem": "What major loophole exists in current genetic anti-discrimination legislation?",
                    "options": [
                        {"label": "A", "text": "It fails to protect citizens against discrimination in life and disability insurance."},
                        {"label": "B", "text": "It prohibits doctors from prescribing antibiotics to sick patients."},
                        {"label": "C", "text": "It permits employers to physically examine employees' chromosomes at work."},
                        {"label": "D", "text": "It forces universities to disclose all student genetic records publicly."}
                    ],
                    "answer": "A",
                    "question_zh": "现行的基因反歧视法案存在什么重大漏洞？",
                    "answer_zh": "它未能将寿险与长期伤残保险纳入保护范围。",
                    "explanation": "尾段明确指出《反基因歧视法》存在漏洞：'they do not cover life insurance, long-term disability policies, or commercial data reselling'，对应A项。"
                }
            ],
            "main_idea_zh": "本文深入揭示了基因组学时代个人基因隐私面临的严峻危机。DNA无法重置且关联全血亲家族，去标识化难防交叉比对，警方家谱库天网破案引发无令监控争议。呼吁完善立法堵住寿险歧视漏洞。",
            "main_idea_en": "The passage analyzes genetic privacy vulnerabilities, consumer direct-to-consumer data brokers, and statutory insurance discrimination gaps."
        }
    })

    # ==========================================
    # 2017年6月 六级真题 (第1套)
    # ==========================================
    sets.append({
        "id": "2017_06_set1",
        "year": "2017",
        "month": "06",
        "set": "第1套",
        "title": "2017年6月 六级阅读真题 (第1套)",
        "theme": "习惯心理学 / 白领自动化 / 海洋微塑料污染",
        "section_a": {
            "title": "Section A · 选词填空 (The Science of Habit Formation)",
            "passage": "From the moment we wake up to the time we fall asleep, nearly forty percent of our daily actions are governed not by conscious deliberation, but by habit. Cognitive neuroscientists define a habit as an automated neurological 26 that unfolds in three distinct stages: the cue, the routine, and the reward. The cue acts as a mental trigger that prompts the brain to enter an automatic pilot mode; the routine is the physical or mental behavior executed; and the reward is the neurochemical payoff—frequently a surge of dopamine—that reinforces the loop in the brain's basal 27 .\nOver evolutionary history, habit formation developed as an indispensable energy-saving mechanism. By relegating routine behaviors—such as brushing teeth, tying shoes, or driving a familiar route—to subconscious neural circuits, the brain frees up precious working memory and prefrontal cortex capacity for complex problem-solving and environmental 28 . However, this very efficiency can become a double-edged sword when maladaptive routines take root. Because the brain cannot readily 29 between beneficial and destructive habits, unhealthy behaviors like mindless snacking or compulsive smartphone checking become deeply 30 in our neural pathways.\nPsychologists emphasize that bad habits cannot simply be eradicated through sheer willpower. When individuals attempt to suppress a habit through brute self-control, they frequently experience cognitive exhaustion and relapse under stress. Instead, behavioral scientists advocate the Golden Rule of Habit Change: rather than fighting the craving, keep the cue and the reward intact while 31 a healthier routine. For instance, if an afternoon slump prompts a desire for a sugary snack, replacing the candy with a brief walk or green tea can deliver a similar energy boost without the 32 health penalties.\nFurthermore, social environments exert an enormous 33 on habit longevity. When individuals join groups where the desired habit is the communal norm, adopting new routines becomes significantly easier. Over time, consistent small changes trigger what researchers call 'keystone habits'—foundational routines like daily exercise that create positive cascading 34 across diet, productivity, and sleep. By mastering the hidden mechanics of human habit, we can deliberately 35 our daily behaviors and unlock lasting personal transformation.",
            "word_bank": {
                "A": "loop",
                "B": "ganglia",
                "C": "threats",
                "D": "distinguish",
                "E": "entrenched",
                "F": "substituting",
                "G": "adverse",
                "H": "leverage",
                "I": "effects",
                "J": "sculpt",
                "K": "incur",
                "L": "recklessly",
                "M": "destabilize",
                "N": "fluctuate",
                "O": "reproduce"
            },
            "questions": [
                {"num": 26, "answer": "A", "word": "loop", "analysis": "名词短语，'automated neurological loop'自动化神经回路/习惯回路。"},
                {"num": 27, "answer": "B", "word": "ganglia", "analysis": "解剖学专有名词，'basal ganglia'基底节/基底核。"},
                {"num": 28, "answer": "C", "word": "threats", "analysis": "名词与problem-solving并列，感知环境中的'威胁/风险'。"},
                {"num": 29, "answer": "D", "word": "distinguish", "analysis": "动词原形，'distinguish between beneficial and destructive'区分有益与破坏性习惯。"},
                {"num": 30, "answer": "E", "word": "entrenched", "analysis": "形容词/过去分词作表语，不良行为在神经通路中深深'根深蒂固/固化'。"},
                {"num": 31, "answer": "F", "word": "substituting", "analysis": "现在分词作介词宾语，'substituting a healthier routine'替换为更健康的惯常行为。"},
                {"num": 32, "answer": "G", "word": "adverse", "analysis": "形容词修饰penalties，没有'负面的/不利的'健康代价。"},
                {"num": 33, "answer": "H", "word": "leverage", "analysis": "名词作宾语，社交环境对习惯维持发挥巨大的'杠杆作用/影响力'。"},
                {"num": 34, "answer": "I", "word": "effects", "analysis": "名词复数，'cascading effects'级联效应/连锁反应。"},
                {"num": 35, "answer": "J", "word": "sculpt", "analysis": "动词原形，刻意'雕琢/塑造'我们的日常行为。"}
            ],
            "translation": "长篇解析：文章探讨了习惯形成的神经机制（提示、惯常行为、奖赏回路与基底核作用），指出了单纯靠意志力戒除恶习的局限性，提出了保留提示与奖赏并替换新行为的“习惯黄金法则”。",
            "vocabulary": [
                {"w": "entrench", "p": "/ɪnˈtrentʃ/", "t": "v. 使处于牢固地位，使盘根错节"},
                {"w": "ganglia", "p": "/ˈɡæŋɡliə/", "t": "n. （神经）节，基底核"},
                {"w": "maladaptive", "p": "/ˌmæləˈdæptɪv/", "t": "adj. 适应不良的，不适应环境的"}
            ]
        },
        "section_b": {
            "title": "Section B · 长篇阅读 (The Impact of Automation on White-Collar Employment)",
            "paragraphs": [
                {"label": "A", "text": "For decades, the narrative surrounding technological unemployment focused almost exclusively on blue-collar manufacturing workers. Robotics on assembly lines, automated checkout kiosks, and computerized warehouse forklifts replaced repetitive physical labor. Educated professionals comforted themselves with the belief that intellectual, cognitive, and analytical tasks were uniquely human prerogatives that machines could never replicate."},
                {"label": "B", "text": "Today, however, the vanguard of machine learning and generative artificial intelligence has shattered that complacency. Cognitive automation is moving upstream into lucrative white-collar sectors: law, finance, medical diagnostics, software programming, and journalism. Tasks once reserved for graduates of elite universities are now performed by software algorithms with greater speed, lower error rates, and zero compensation."},
                {"label": "C", "text": "In the legal profession, corporate law firms traditionally hired legions of junior associates to spend months manually reviewing discovery documents in commercial litigation. Today, machine learning algorithms can analyze millions of emails, contracts, and filings in minutes, flagging relevant evidence and predicting judicial outcomes with superhuman accuracy, decimating entry-level legal employment."},
                {"label": "D", "text": "In financial analysis, algorithmic trading and automated financial advisors execute investment strategies, rebalance portfolios, and generate personalized retirement plans without human financial planners. Automated systems synthesize quarterly corporate earnings reports into coherent news articles in fractions of a second, eliminating the need for human financial beat reporters."},
                {"label": "E", "text": "Economists emphasize that automation rarely eliminates entire occupations outright; rather, it unbundles occupations into discrete constituent tasks. When software automates the routine informational components of a profession, the remaining non-automatable human skills—empathy, complex negotiation, ethical judgment, and multidisciplinary synthesis—become dramatically more valuable."},
                {"label": "F", "text": "However, this unbundling threatens to hollow out the traditional apprenticeship model of white-collar professions. Historically, junior professionals mastered their craft by performing mundane, routine tasks under the mentorship of senior partners. If algorithms perform all entry-level analysis, how will young graduates acquire the tacit knowledge and clinical intuition needed to become senior leaders?"},
                {"label": "G", "text": "Furthermore, the cognitive automation revolution risks exacerbating income inequality. The immense financial gains generated by artificial intelligence accrue overwhelmingly to tech capital owners and a tiny elite of top superstars, while mid-tier professional salaries face stagnation or downward pressure."},
                {"label": "H", "text": "Navigating this transition requires reimagining higher education and lifelong learning. Universities must shift away from rote memorization and formulaic problem-solving, teaching students meta-learning, ethical reasoning, and creative collaboration with machine algorithms. In an automated world, human worth will be defined not by competing against algorithms in calculating speed, but by cultivating our uniquely human virtues."}
            ],
            "questions": [
                {"num": 36, "stem": "Software algorithms can review millions of legal litigation records in minutes, slashing entry-level associate roles.", "answer": "C"},
                {"num": 37, "stem": "Advanced artificial intelligence is now expanding into prestigious intellectual fields historically deemed immune to machines.", "answer": "B"},
                {"num": 38, "stem": "Automation typically divides professions into discrete duties rather than abolishing entire jobs immediately.", "answer": "E"},
                {"num": 39, "stem": "Automated algorithms generate investment strategies and draft corporate financial news without human intervention.", "answer": "D"},
                {"num": 40, "stem": "Historically, technological job displacement was presumed to threaten only factory manual labor.", "answer": "A"},
                {"num": 41, "stem": "If computers handle all basic tasks, young graduates may struggle to develop the intuition needed for leadership.", "answer": "F"},
                {"num": 42, "stem": "The financial windfalls of cognitive automation flow disproportionately to technology corporate owners.", "answer": "G"},
                {"num": 43, "stem": "Educational institutions must prepare students to excel at creative collaboration rather than rote memorization.", "answer": "H"}
            ],
            "translation": "长篇阅读解析总结：文章探讨了人工智能与自动化向白领高薪认知阶层（法律、金融、医疗诊断）的强势渗透及其对传统师徒学徒制、就业结构与收入差距的深刻冲击。"
        },
        "section_c1": {
            "title": "Section C · 仔细阅读 Passage 1 (The Pervasive Menace of Ocean Microplastics)",
            "passage": "In recent years, environmental awareness of marine plastic pollution has surged, catalyzed by harrowing images of sea turtles entangled in six-pack rings and colossal floating gyres of consumer garbage like the Great Pacific Garbage Patch. Yet marine biologists warn that the most insidious and perilous dimension of plastic pollution is invisible to the naked eye: microplastics. Defined as synthetic plastic fragments measuring less than five millimeters across, these microscopic particles now permeate every ocean basin, marine trench, and polar ice sheet on Earth.\nMicroplastics originate from two primary pathways. Primary microplastics are intentionally manufactured at microscopic scales for commercial purposes, including abrasive microbeads in facial cleansers and industrial blasting agents. Secondary microplastics, by contrast, result from the physical fragmentation, solar ultraviolet degradation, and wave erosion of larger discarded plastic items—water bottles, plastic bags, synthetic clothing fibers, and automotive tire wear. Every time a polyester fleece jacket is laundered in a washing machine, hundreds of thousands of microscopic plastic fibers are discharged into municipal sewage systems and ultimately washed into the sea.\nBecause plastics are virtually non-biodegradable, they persist in marine environments for centuries, fragmenting into increasingly minute nano-particles. The ecological consequences for marine fauna are devastating. Zooplankton, shellfish, small fish, and seabirds routinely mistake floating microplastics for fish eggs or natural food particles. Ingesting indigestible plastic fills the stomachs of marine organisms with zero-calorie synthetic debris, leading to chronic malnutrition, intestinal punctures, and starvation.\nFurthermore, microplastics act as chemical sponges in marine ecosystems. Due to their hydrophobic chemical properties, microplastics attract and concentrate toxic persistent organic pollutants (POPs)—including pesticides like DDT and industrial polychlorinated biphenyls (PCBs)—present in surrounding seawater at concentrations millions of times higher than baseline levels. When marine organisms ingest these plastic sponges, chemical toxins leach into their fatty tissues, bioaccumulating up the marine food chain and ultimately reaching the dinner plates of human consumers.\nHalting the microplastic deluge requires a coordinated systemic response. Banning cosmetic microbeads is a symbolic first step, but real progress demands redesigning synthetic textile manufacturing, mandating micro-fiber filters on domestic washing machines, and establishing rigorous global treaties to curtail single-use packaging. The oceans are not an infinite sink for indestructible human waste; safeguarding marine life requires turning off the plastic tap at its source.",
            "questions": [
                {
                    "num": 46,
                    "stem": "Why do marine biologists consider microplastics more dangerous than visible plastic trash?",
                    "options": [
                        {"label": "A", "text": "They are invisible to the naked eye and permeate every marine ecosystem on Earth."},
                        {"label": "B", "text": "They are heavier than iron and cause ships to sink in harbors."},
                        {"label": "C", "text": "They exclusively target endangered blue whales in polar waters."},
                        {"label": "D", "text": "They dissolve instantly into clean drinking water."}
                    ],
                    "answer": "A",
                    "question_zh": "为什么海洋生物学家认为微塑料比肉眼可见的塑料垃圾更具威胁？",
                    "answer_zh": "它们肉眼不可见且渗透进了地球上的每一个海洋生态系统。",
                    "explanation": "首段末尾明确指出：'invisible to the naked eye: microplastics... now permeate every ocean basin, marine trench, and polar ice sheet on Earth'，对应A项。"
                },
                {
                    "num": 47,
                    "stem": "How do secondary microplastics primarily originate in the environment?",
                    "options": [
                        {"label": "A", "text": "Through intentional chemical synthesis in pharmaceutical laboratories."},
                        {"label": "B", "text": "Through the weathering and physical fragmentation of larger discarded plastic items."},
                        {"label": "C", "text": "Through natural volcanic eruptions along oceanic trenches."},
                        {"label": "D", "text": "Through the digestive secretions of marine dolphins."}
                    ],
                    "answer": "B",
                    "question_zh": "次生微塑料在环境中主要因何产生？",
                    "answer_zh": "由于被丢弃的大件塑料垃圾经风化和物理碎片化分解所致。",
                    "explanation": "第二段指出：'Secondary microplastics, by contrast, result from the physical fragmentation, solar ultraviolet degradation, and wave erosion of larger discarded plastic items...'，对应B项。"
                },
                {
                    "num": 48,
                    "stem": "What physical harm occurs when marine organisms ingest microplastics?",
                    "options": [
                        {"label": "A", "text": "Their stomachs are filled with non-nutritive debris leading to malnutrition."},
                        {"label": "B", "text": "They grow ten times larger than their normal biological size."},
                        {"label": "C", "text": "They immediately develop resistance to all bacterial diseases."},
                        {"label": "D", "text": "Their scales turn into solid gold."}
                    ],
                    "answer": "A",
                    "question_zh": "海洋生物误食微塑料会产生什么生理伤害？",
                    "answer_zh": "胃部被毫无营养的合成碎片填满，导致慢性营养不良与饥饿。",
                    "explanation": "第三段指出'Ingesting indigestible plastic fills the stomachs of marine organisms with zero-calorie synthetic debris, leading to chronic malnutrition, intestinal punctures, and starvation'，对应A项。"
                },
                {
                    "num": 49,
                    "stem": "Why are microplastics described as 'chemical sponges' in ocean waters?",
                    "options": [
                        {"label": "A", "text": "They absorb seawater and cause oceans to dry up."},
                        {"label": "B", "text": "They attract and concentrate toxic organic pollutants at high concentrations."},
                        {"label": "C", "text": "They clean the ocean by transforming chemicals into harmless oxygen."},
                        {"label": "D", "text": "They provide soft beds for coral larvae to sleep upon."}
                    ],
                    "answer": "B",
                    "question_zh": "为什么在海水中微塑料被比作“化学海绵”？",
                    "answer_zh": "它们吸附并高浓度富集了海水中的有毒持久性有机污染物。",
                    "explanation": "第四段指出'Due to their hydrophobic chemical properties, microplastics attract and concentrate toxic persistent organic pollutants (POPs)... at concentrations millions of times higher than baseline levels'，对应B项。"
                },
                {
                    "num": 50,
                    "stem": "What is the author's primary conclusion regarding solutions to microplastic pollution?",
                    "options": [
                        {"label": "A", "text": "Filtering all ocean water through giant mechanical nets across the Pacific."},
                        {"label": "B", "text": "Intervening at the manufacturing source to curtail single-use plastics and fibers."},
                        {"label": "C", "text": "Encouraging citizens to throw more plastic bottles into rivers."},
                        {"label": "D", "text": "Waiting for marine fish to develop genetic mutations that digest plastic."}
                    ],
                    "answer": "B",
                    "question_zh": "关于解决微塑料污染，作者得出的主要结论是什么？",
                    "answer_zh": "从制造源头进行系统干预，遏制一次性塑料与合成纤维的产生。",
                    "explanation": "尾段末句明确指出：'safeguarding marine life requires turning off the plastic tap at its source'，通过源头减塑与合成织物重塑化解危机，对应B项。"
                }
            ],
            "main_idea_zh": "本文揭示了海洋微塑料污染对全球生态系统和人类食物链的致命威胁。微塑料无处不在，不仅让海洋生物因假饱而活活饿死，更像海绵一般富集农药与工业剧毒物，通过食物链层层富集到人类餐桌。作者呼吁从洗衣机滤网到条约限塑从源头关紧塑料龙头。",
            "main_idea_en": "The passage details the ecological crisis of ocean microplastics, examining their origins, the ingestion starvation cycle, toxic bioaccumulation up the food web, and the urgent imperative for source reduction."
        },
        "section_c2": {
            "title": "Section C · 仔细阅读 Passage 2 (Artificial Intelligence in Medical Diagnosis)",
            "passage": "In the sterile halls of modern academic medicine, artificial intelligence is challenging the most venerable prerogative of human physicians: clinical diagnosis. Powered by deep neural networks and trained on millions of digital radiological scans, algorithmic diagnostic tools are achieving superhuman accuracy. In identifying malignant melanomas from dermatological photographs, detecting early-stage diabetic retinopathy from retinal images, and spotting subtle micro-nodules on lung CT scans, deep learning algorithms routinely match or exceed the diagnostic accuracy of board-certified human specialists.\nProponents argue that AI diagnostics will democratize world-class healthcare. In rural clinics and developing nations facing severe shortages of certified radiologists and pathologists, automated cloud diagnostics can analyze scans in seconds for pennies, flagging urgent abnormalities for immediate clinical intervention. In overburdened urban emergency departments, triage algorithms can scan chest X-rays to prioritize critical patients with collapsed lungs or internal hemorrhages, dramatically shortening life-or-death waiting times.\nYet integrating algorithmic diagnosis into clinical practice raises profound technical and epistemological dilemmas. Deep neural networks are notoriously opaque 'black boxes.' An algorithm may correctly identify a cancerous tumor, but it cannot explain the clinical rationale behind its conclusion. When a human physician makes a diagnosis, they synthesize patient medical history, physical exams, and biological mechanisms into an explainable causal narrative. If an algorithm makes a catastrophic diagnostic error, tracing the underlying failure is mathematically intractable, creating severe legal liability dilemmas: is the hospital, the attending doctor, or the software developer legally responsible?\nFurthermore, medical algorithms frequently reflect and amplify racial and demographic biases embedded in their training data. If an algorithmic tool for detecting skin cancer is trained overwhelmingly on images of fair-skinned Caucasian patients, its accuracy drops precipitously when evaluating lesions on darker-skinned individuals. In clinical trials, algorithms have repeatedly latched onto spurious statistical artifacts—such as the specific model of X-ray machine or hospital clerical markings—rather than genuine pathological signals.\nRather than replacing human doctors, the future of healthcare lies in symbiotic collaboration. The most effective diagnostic paradigm is not machine versus human, but human plus machine. AI excels at rapid pattern recognition across terabytes of pixels, while human clinicians excel at holistic empathy, ethical judgment, and contextual patient communication. By delegating cognitive grunt work to intelligent machines, physicians can step back from computer screens and return to the bedside, reviving the human art of healing.",
            "questions": [
                {
                    "num": 51,
                    "stem": "In what medical domain has deep learning artificial intelligence demonstrated superhuman capability?",
                    "options": [
                        {"label": "A", "text": "Performing heart-lung transplants without human oversight."},
                        {"label": "B", "text": "Analyzing radiological scans and photographic diagnostic images."},
                        {"label": "C", "text": "Comforting grieving family members in hospital waiting rooms."},
                        {"label": "D", "text": "Eliminating all legal liability insurance in medical malpractice."}
                    ],
                    "answer": "B",
                    "question_zh": "深度学习人工智能在哪个医疗领域展现了超越常人的准确率？",
                    "answer_zh": "分析放射影像与医学图片诊断。",
                    "explanation": "首段提到'trained on millions of digital radiological scans... In identifying malignant melanomas... detecting diabetic retinopathy... algorithms routinely match or exceed the diagnostic accuracy of human specialists'，对应B项。"
                },
                {
                    "num": 52,
                    "stem": "How can automated diagnostic algorithms help underserved healthcare systems?",
                    "options": [
                        {"label": "A", "text": "By providing instant, low-cost scan evaluations where human specialists are scarce."},
                        {"label": "B", "text": "By manufacturing free prescription pharmaceuticals on home printers."},
                        {"label": "C", "text": "By forcing all patients to relocate to large research universities."},
                        {"label": "D", "text": "By eliminating the requirement for clean surgical rooms."}
                    ],
                    "answer": "A",
                    "question_zh": "自动化诊断算法如何赋能医疗资源匮乏的地区？",
                    "answer_zh": "在专家匮乏的地区以极低成本提供即时的影像评估与筛选。",
                    "explanation": "第二段指出'In rural clinics and developing nations facing severe shortages of certified radiologists... automated cloud diagnostics can analyze scans in seconds for pennies'，对应A项。"
                },
                {
                    "num": 53,
                    "stem": "What major obstacle is posed by the 'black box' nature of deep learning algorithms?",
                    "options": [
                        {"label": "A", "text": "Algorithms cannot explain the clinical causal reasoning behind their diagnoses."},
                        {"label": "B", "text": "Computer monitors emit toxic radiation inside hospital rooms."},
                        {"label": "C", "text": "Algorithms delete medical records every twenty minutes."},
                        {"label": "D", "text": "Doctors are forbidden by law from viewing computer screens."}
                    ],
                    "answer": "A",
                    "question_zh": "深度学习算法的“黑箱”特性带来了什么主要障碍？",
                    "answer_zh": "算法无法解释其诊断结论背后的临床因果逻辑。",
                    "explanation": "第三段指出'Deep neural networks are notoriously opaque black boxes. An algorithm may correctly identify a cancerous tumor, but it cannot explain the clinical rationale behind its conclusion'，对应A项。"
                },
                {
                    "num": 54,
                    "stem": "Why did skin cancer detection algorithms fail when evaluating patients with darker skin?",
                    "options": [
                        {"label": "A", "text": "The algorithms were trained predominantly on images of fair-skinned individuals."},
                        {"label": "B", "text": "Darker skin completely blocks all hospital optical camera lenses."},
                        {"label": "C", "text": "Algorithms refuse to diagnose patients who do not speak English."},
                        {"label": "D", "text": "Skin cancer never affects people with darker pigmentation."}
                    ],
                    "answer": "A",
                    "question_zh": "为什么皮肤癌筛查算法在评估深肤色人群时准确率急剧下降？",
                    "answer_zh": "因为算法的训练数据集绝大多数取自浅肤色患者的图像。",
                    "explanation": "第四段第二句指出'If an algorithmic tool for detecting skin cancer is trained overwhelmingly on images of fair-skinned Caucasian patients, its accuracy drops precipitously when evaluating lesions on darker-skinned individuals'，对应A项。"
                },
                {
                    "num": 55,
                    "stem": "What optimal model does the author envision for the future of clinical medicine?",
                    "options": [
                        {"label": "A", "text": "Total replacement of human clinicians with autonomous software robots."},
                        {"label": "B", "text": "A symbiotic partnership where machines assist humans while doctors provide holistic care."},
                        {"label": "C", "text": "Banning all artificial intelligence tools from public hospitals forever."},
                        {"label": "D", "text": "Forcing medical students to study only computer programming instead of anatomy."}
                    ],
                    "answer": "B",
                    "question_zh": "作者对临床医学的未来构想了什么理想模式？",
                    "answer_zh": "机器辅助图像模式识别，医生专注人本关怀与综合因果决策的共生合作。",
                    "explanation": "尾段明确指出：'The most effective diagnostic paradigm is not machine versus human, but human plus machine... AI excels at rapid pattern recognition... while human clinicians excel at holistic empathy'，对应B项。"
                }
            ],
            "main_idea_zh": "本文客观辩证探讨了人工智能在医学诊断领域的革命性应用与现实局限。虽然深度学习在放射影像与眼底阅片上达到甚至超越人类专科医生水平，并有望填补基层医疗鸿沟，但其“黑箱”不可解释性、医疗纠纷归责难题与训练集种族偏差依然棘手。文章总结指出未来的医疗模式绝非机器取代医生，而是人机共生的互补协作，使医生从屏幕前解放出来重归床边关怀。",
            "main_idea_en": "The passage evaluates artificial intelligence in medical diagnosis, exploring superhuman imaging accuracy, black-box explainability hurdles, data bias risks, and the imperative for human-machine clinical symbiosis."
        }
    })

    return sets

print("Supplements extended successfully.")
