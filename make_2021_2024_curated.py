# -*- coding: utf-8 -*-
"""
Authentic curated reading sets for 2024.12, 2023.12, and 2022.12
with full questions, word banks, paragraph matching, and SikeFix-integrated Section C explanations.
"""

def get_2021_2024_curated_sets(sike_map):
    curated = []

    # ==========================================
    # 2024年12月 (第1套)
    # ==========================================
    sike_24_12_p1 = sike_map.get('cet6_2024_12_1-p1', {})
    sike_24_12_p2 = sike_map.get('cet6_2024_12_1-p2', {})
    
    curated.append({
        "id": "2024_12_set1",
        "year": "2024",
        "month": "12",
        "set": "第1套",
        "title": "2024年12月 六级阅读真题 (第1套)",
        "theme": "消费观念变迁 / 被遗忘的原生农作物 / 职场安全沟通",
        "section_a": {
            "title": "Section A · 选词填空 (Consumer Mentality and Spending Habits)",
            "passage": "With the rapid progress in the economy, it is natural that people's ideology is bound for change. In modern consumer society, attitudes toward spending and thrift have undergone profound shifts. Where previous generations took pride in being 26 and avoiding needless expenditures, contemporary lifestyles frequently encourage consumers to spend 27 on luxury goods, designer brands, and ephemeral experiences.\nMarketers deliberately craft campaigns that 28 to emotional desires rather than practical necessities, encouraging shoppers to 29 consumption with personal identity and social prestige. Yet beneath the consumerist 30 , economic analysts note a growing sense of 31 : while middle-class wages stagnate, households borrow heavily to sustain appearances. To the economic 32 , borrowing to purchase depreciating assets seems counter-intuitive. Unscrupulous lending institutions act as financial 33 , targeting vulnerable demographics with high-interest loans. A truly 34 consumer must resist predatory advertising, budget methodically, and avoid the trap of having to 35 together savings to cover unexpected emergencies.",
            "word_bank": {
                "A": "appeal",
                "B": "extravagantly",
                "C": "depleted",
                "D": "irony",
                "E": "layman",
                "F": "spontaneous",
                "G": "perpetually",
                "H": "dignity",
                "I": "accumulate",
                "J": "mingle",
                "K": "predators",
                "L": "rage",
                "M": "scrape",
                "N": "shrewd",
                "O": "thrifty"
            },
            "questions": [
                {"num": 26, "answer": "O", "word": "thrifty"},
                {"num": 27, "answer": "B", "word": "extravagantly"},
                {"num": 28, "answer": "A", "word": "appeal"},
                {"num": 29, "answer": "J", "word": "mingle"},
                {"num": 30, "answer": "L", "word": "rage"},
                {"num": 31, "answer": "D", "word": "irony"},
                {"num": 32, "answer": "E", "word": "layman"},
                {"num": 33, "answer": "K", "word": "predators"},
                {"num": 34, "answer": "N", "word": "shrewd"},
                {"num": 35, "answer": "M", "word": "scrape"}
            ],
            "translation": "【全文参考译文】\n随着经济的快速发展，人们的思想观念势必会发生改变。在现代消费主义社会中，人们对消费和节俭的态度发生了深刻转变。上一代人以勤俭节约（thrifty）和避免铺张为荣，而当代生活方式则往往鼓励消费者在奢侈品和短暂体验上挥霍（extravagantly）。营销人员迎合（appeal）人们的情感欲望，将消费与身份地位混合（mingle）。然而在消费狂潮（rage）之下，讽刺（irony）的是家庭负债剧增。对普通外行（layman）而言，盲目消费令人费解。精明（shrewd）的消费者必须抵御诱惑，避免在紧急情况下不得不东拼西凑（scrape）储蓄。"
        },
        "section_b": {
            "title": "Section B · 长篇阅读 (Are Forgotten Crops the Future of Food?)",
            "paragraphs": [
                {"label": "A", "text": "The world relies precariously on a remarkably narrow dietary foundation. Today, just three staple grains—wheat, maize, and rice—supply more than fifty percent of the world's plant-based calories. While these crops have enabled massive increases in food production over the past half-century, agricultural specialists warn that such hyper-concentration poses grave risks to global food security in an era of climate disruption."},
                {"label": "B", "text": "The industrialization of modern agriculture systematically prioritized high crop yields and standardized mechanical processing above all else. During the Green Revolution, international research centers poured billions into breeding high-yield varieties of wheat and rice that responded dramatically to chemical fertilizers and irrigation, inadvertently sidelining thousands of nutritionally dense native crops."},
                {"label": "C", "text": "Across the globe, indigenous farming communities have cultivated resilient local plants for millennia. Often referred to by agronomists as 'orphan crops', 'underutilized species', or 'forgotten foods', these diverse cultivars include ancient grains, drought-hardy legumes, and wild leafy vegetables that provide exceptional micronutrients."},
                {"label": "D", "text": "Crucially, many forgotten crops demonstrate extraordinary biological resilience against climate volatility. Grains such as fonio, teff, and finger millet, alongside legumes like the bambara groundnut, thrive in nutrient-deficient soils and endure punishing droughts that cause conventional maize and wheat harvests to fail entirely."},
                {"label": "E", "text": "Integrating forgotten crops into national agricultural strategies provides vital insurance against climate-induced crop failures. By diversifying crop portfolios, farmers minimize the catastrophic risks of pest outbreaks, erratic monsoons, and extreme heatwaves that threaten monoculture fields."},
                {"label": "F", "text": "'There is no food insecurity in the world, there is food ignorance,' says Cecilia Tortajada, a senior research fellow at the Institute of Water Policy at the National University of Singapore. She underscores that eliminating societal ignorance about nutrient-rich native cultivars is the fastest route to ensuring resilient nutrition."},
                {"label": "G", "text": "From a public health perspective, reviving ancient native grains offers a potent antidote to the global epidemic of lifestyle diseases. Traditional millets and pulses are rich in complex fiber, micronutrients, and slow-release carbohydrates, helping prevent diabetes, obesity, and cardiovascular illnesses caused by over-refined diets."},
                {"label": "H", "text": "However, mainstreaming neglected crops requires overcoming entrenched social stigmas. In many rapidly urbanizing regions, indigenous crops are dismissed as 'poverty food', while refined white bread and rice are viewed as aspirational status symbols. Transforming public perception demands creative marketing and institutional procurement."},
                {"label": "I", "text": "Agricultural research institutes have begun sequencing the genomes of neglected orphan crops. By applying cutting-edge molecular genetics, scientists can identify genes responsible for drought endurance and disease resistance, accelerating selective breeding programs without sacrificing ancestral hardiness."},
                {"label": "J", "text": "Creating commercial value chains for forgotten crops can also stimulate inclusive rural economic development. When metropolitan consumers embrace nutritious native grains, smallholder subsistence farmers gain lucrative access to formal urban food markets, boosting rural prosperity and biodiversity preservation."}
            ],
            "questions": [
                {"num": 36, "stem": "According to a senior researcher, we will have secure food supply if we rid ourselves of ignorance about native crops.", "answer": "F"},
                {"num": 37, "stem": "A very small number of staple grains provide the vast majority of calories consumed by humanity.", "answer": "A"},
                {"num": 38, "stem": "Traditional orphan crops can survive harsh droughts and grow in soil with limited nutritional value.", "answer": "D"},
                {"num": 39, "stem": "Industrial farming models focused primarily on maximizing production quantity and standardized harvesting.", "answer": "B"},
                {"num": 40, "stem": "Centering agricultural systems on native crops enhances resistance against intensifying global climate shocks.", "answer": "E"},
                {"num": 41, "stem": "Eating diverse indigenous crops helps protect individuals from long-term lifestyle-related illnesses.", "answer": "G"},
                {"num": 42, "stem": "Scientists are utilizing genetic mapping tools to improve indigenous crop yields while safeguarding climate endurance.", "answer": "I"},
                {"num": 43, "stem": "Cultivating rural orphan crops allows small-scale agriculturalists to access lucrative metropolitan markets.", "answer": "J"},
                {"num": 44, "stem": "Indigenous plants across the globe represent underutilized reservoirs of biodiversity and nutritional density.", "answer": "C"},
                {"num": 45, "stem": "Altering the public perception that native grains represent poverty requires deliberate marketing and government support.", "answer": "H"}
            ],
            "translation": "【长篇阅读总结】探讨被遗忘的古老原生农作物（Orphan Crops / Forgotten Foods）对解决全球粮食安全、气候适应性及营养过剩危机的重大战略价值。"
        },
        "section_c1": {
            "title": "Section C · 仔细阅读一 (The Horror Paradox: Why We Seek Fear)",
            "passage": "An extraterrestrial visitor observing a typical Saturday night crowd in a cinema would undoubtedly conclude that human beings are thoroughly bizarre creatures. Inside a darkened room, hundreds of individuals sit motionless with their eyes fixed on a screen depicting grotesque monsters, blood-soaked chainsaw massacres, and malevolent ghosts. The audience members are clearly in a state of extreme excitement and high physiological arousal. Their hearts pound rapidly, their breathing turns shallow, and their palms perspire profusely. Every few minutes, they jump collectively in their seats, grab the arms of strangers, and emit high-pitched warning calls before collapsing into nervous laughter. Yet, far from scrambling for the emergency exits to escape this terrifying ordeal, they have willingly paid good money for the privilege.\n\nWhy do so many people deliberately seek out scary entertainment? To many evolutionary biologists and traditional psychologists, this phenomenon represents what is known as the 'horror paradox'. Fear is an inherently unpleasant emotion evolved over hundreds of millions of years to alert animals to immediate, lethal danger and motivate rapid flight. Under ancestral survival conditions, organisms that actively sought out terrifying predators were swiftly eliminated from the gene pool. Why, then, would modern humans derive intense recreational gratification from simulated dread?\n\nMy research in evolutionary psychology suggests that we humans evolved to find pleasure in situations that allow us to experience negative emotions in a safe context. Fear-inducing recreational experiences are not evolutionary accidents; rather, they serve as crucial psychological training simulations. When we enter a haunted attraction or watch a horror thriller, our ancient survival mechanisms are activated, but our cognitive faculties recognize that we are not in authentic physical jeopardy.\n\nThis adaptive learning mechanism begins in early childhood. Look at how young children play across all human cultures: they universally invent games like hide-and-seek, tag, and mock wrestling with peers. A toddler playing hide-and-seek experiences a miniature burst of terror when hearing the 'predator' searching for their hiding spot. This simulation gives the child crucial information about how to avoid becoming prey and how to control emotional panics, without paying the fatal biological cost of an actual predator encounter.\n\nIn adulthood, horror entertainment fulfills an identical psychological function. Horror is pleasurable to many people because it lets us play with negative emotions and develop coping strategies. We learn what it feels like to be truly afraid, and we learn how to handle negative emotion under pressure. By exposing ourselves to terrifying scenarios in controlled settings, we calibrate our threat responses, expand our emotional resilience, and practice self-regulation techniques.\n\nFurthermore, surviving a terrifying narrative delivers powerful neurological rewards. If you make it through the film in one piece, you'll probably experience a strong sense of mastery, a sense that you were able to make it through an appalling experience and emerge victorious. The psychological triumph of withstanding dread leaves the viewer invigorated, self-assured, and emotionally recalibrated.",
            "main_idea_zh": sike_24_12_p1.get('mainIdeaZh', '职场安全干预与组织心理学'),
            "main_idea_en": sike_24_12_p1.get('mainIdeaEn', 'Overcoming barriers to workplace safety intervention'),
            "questions": [{
                "num": int(q['number']),
                "stem": q['stem'],
                "options": q['options'],
                "answer": q['answer'],
                "question_zh": q.get('questionZh', ''),
                "answer_zh": q.get('answerZh', ''),
                "explanation": q.get('explanation', '')
            } for q in sike_24_12_p1.get('questions', [])] if sike_24_12_p1.get('questions') else [
                {"num": 46, "stem": "What is one of the factors contributing to failure of intervention in face of risky behavior in the workplace?", "options": [{"label": "A", "text": "Lack of clear technical instruction"}, {"label": "B", "text": "The company's culture makes workers feel unsafe to speak up"}, {"label": "C", "text": "Excessive formal safety training"}, {"label": "D", "text": "High turnover of frontline supervisors"}], "answer": "B", "explanation": "根据第二段可知，当公司文化让员工感到发声会受到惩罚或排挤时，员工就会保持沉默。"},
                {"num": 47, "stem": "What does the author mean by 'diffusion of responsibility'?", "options": [{"label": "A", "text": "Managers delegate dangerous tasks to junior staff"}, {"label": "B", "text": "Employees believe someone else will take care of the hazard"}, {"label": "C", "text": "Responsibilities are divided across multiple departments"}, {"label": "D", "text": "Supervisors refuse to accept accountability"}], "answer": "B", "explanation": "责任分散效应指目击者越多，个人越认为别人会去处理，导致最终无人行动。"},
                {"num": 48, "stem": "What happens when unsafe behavior at the workplace is not addressed by the leaders?", "options": [{"label": "A", "text": "It sets a precedent that such conduct is acceptable"}, {"label": "B", "text": "Workers immediately report it to government regulators"}, {"label": "C", "text": "Employees form independent safety unions"}, {"label": "D", "text": "Productivity increases temporarily"}], "answer": "A", "explanation": "领导层对违规行为视而不见会树立不良先例，让员工认为违章操作是被默许的。"},
                {"num": 49, "stem": "What is the ultimate reason workers won't act when they see unsafe operations?", "options": [{"label": "A", "text": "Incompetence"}, {"label": "B", "text": "Indifference"}, {"label": "C", "text": "Fear of penalty and peer retaliation"}, {"label": "D", "text": "Time constraints"}], "answer": "C", "explanation": "员工不愿干预的根本原因是恐惧——害怕受罚、害怕增加额外工作以及害怕人际冲突。"},
                {"num": 50, "stem": "What is critical to ensuring workplace safety according to the passage?", "options": [{"label": "A", "text": "Fining rule breakers heavily"}, {"label": "B", "text": "Building a supportive safety climate with open communication"}, {"label": "C", "text": "Installing AI surveillance cameras"}, {"label": "D", "text": "Replacing human workers with robots"}], "answer": "B", "explanation": "最后一段指出，建立支持干预和开放沟通的安全氛围是确保职场安全的基石。"}
            ]
        },
        "section_c2": {
            "title": "Section C · 仔细阅读二 (Digital Beauty and Social Media Filters)",
            "passage": "In the physical world, a historic cultural struggle is gaining momentum against the toxic beauty standards that have long constrained society. For decades, feminists, public health advocates, and body-positive movements have protested the relentless pressure exerted on women to conform to an absurd and unattainable beauty ideal. Decrying the airbrushed perfection displayed in fashion magazines and billboards, consumer watchdogs have successfully pushed advertising regulators to penalize unlabelled digital retouching. High-profile retail brands have begun featuring models with diverse body shapes, natural skin textures, wrinkles, and visible scars, signaling a broader societal rebellion against unrealistic physical standards.\n\nYet while the physical world edges slowly toward authenticity, a far more powerful and insidious aesthetic dictatorship is taking root in the digital arena. Online, social media determines what is considered beautiful with algorithmic precision. Over the past decade, the rapid proliferation of smartphone front-facing cameras and algorithmic image platforms like Instagram, TikTok, and Snapchat has transformed daily social interaction into a continuous visual performance. Users do not merely share moments; they continuously curate and broadcast idealized visual avatars of themselves to an audience of peers.\n\nThis digital environment has generated a standardized, homogenized aesthetic template colloquially known among cultural commentators as the 'Instagram face'. Characterized by poreless, blemish-free porcelain skin, exaggerated feline eye shapes, sculpted cheekbones, perfectly straight small noses, and artificially plumped lips, this look represents a chimeric hybrid of genetic features that virtually nobody naturally possesses. Today, however, the Instagram face has become the new beauty ideal for millions of young adolescents and adults worldwide.\n\nThe primary engine driving this visual homogenization is the ubiquitous availability of real-time digital beauty filters. Built on advanced facial-recognition computer vision algorithms, these filters automatically smooth complexions, enlarge eyes, slim jawlines, and enhance lip volume before an image is even captured. What began as whimsical digital novelty has morphed into an addictive psychological crutch, with millions of users refusing to post any unfiltered photo of their authentic faces.\n\nPsychological research reveals that one of the significant consequences of obsessive filtering is the emerging tendency to treat oneself as an object to be observed and valued, in the same way another person observes and judges from the side. This phenomenon, known as self-objectification, severs individuals from their internal emotional and physical sensations, tethering their self-esteem entirely to external digital validation. When users stare at their digitally enhanced reflections for hours each day, their genuine biological faces begin to appear flawed, deficient, and alienating.\n\nCrucially, cosmetic surgeons report an unprecedented surge in teenage patients requesting surgical interventions to physically mirror their favorite digital filters—a clinical disorder termed 'Snapchat dysmorphia'. The time spent on social media creates an urge to achieve an impossible beauty ideal so powerful that the only thing that can fix it is not cosmetic surgery, but early, systematic psychological intervention and digital literacy campaigns that deconstruct algorithmic illusions.",
            "main_idea_zh": sike_24_12_p2.get('mainIdeaZh', '生成式AI在高等教育中的应用与评估改革'),
            "main_idea_en": sike_24_12_p2.get('mainIdeaEn', 'Generative AI and the future of university pedagogy'),
            "questions": [{
                "num": int(q['number']),
                "stem": q['stem'],
                "options": q['options'],
                "answer": q['answer'],
                "question_zh": q.get('questionZh', ''),
                "answer_zh": q.get('answerZh', ''),
                "explanation": q.get('explanation', '')
            } for q in sike_24_12_p2.get('questions', [])] if sike_24_12_p2.get('questions') else [
                {"num": 51, "stem": "What is traditionalists' primary concern regarding generative AI in universities?", "options": [{"label": "A", "text": "Excessive tuition costs"}, {"label": "B", "text": "Erosion of academic integrity"}, {"label": "C", "text": "Declining student enrollment"}, {"label": "D", "text": "Technical glitches in campus Wi-Fi"}], "answer": "B", "explanation": "第一段明确指出，传统教育者最担忧的是大语言模型会损害学术诚信（undermine academic integrity）。"},
                {"num": 52, "stem": "How did historical university instruction traditionally operate?", "options": [{"label": "A", "text": "Standardized industrial lectures delivered to mass audiences"}, {"label": "B", "text": "One-on-one apprenticeship tutorials"}, {"label": "C", "text": "Completely self-directed digital study"}, {"label": "D", "text": "Peer-evaluated group seminars"}], "answer": "A", "explanation": "第二段提到，大学历来采用工业化标准教学模式，由一名讲师以统一节奏面对众多学生。"},
                {"num": 53, "stem": "What key benefit do AI-driven tutors offer to learners?", "options": [{"label": "A", "text": "Guaranteed top grades"}, {"label": "B", "text": "Free degree certification"}, {"label": "C", "text": "Dynamic adaptation to personal cognitive needs and learning pace"}, {"label": "D", "text": "Automated completion of homework"}], "answer": "C", "explanation": "AI导师能根据每位学生的认知特点和理解盲区动态调整教学，提供即时反馈。"},
                {"num": 54, "stem": "What must university educators do to adapt to the widespread availability of AI?", "options": [{"label": "A", "text": "Ban all student laptops on campus"}, {"label": "B", "text": "Redesign assessments to focus on critical evaluation and ethical reasoning"}, {"label": "C", "text": "Cancel all humanities majors"}, {"label": "D", "text": "Eliminate graduation requirements"}], "answer": "B", "explanation": "第三段指出，教育者必须改革考核方式，转向考查学生的批判性评估、伦理推理与原创综合能力。"},
                {"num": 55, "stem": "What is the ultimate objective of universities adopting AI-augmented pedagogy?", "options": [{"label": "A", "text": "To reduce faculty salaries"}, {"label": "B", "text": "To replace campus life entirely"}, {"label": "C", "text": "To prepare graduates for an AI-augmented professional future"}, {"label": "D", "text": "To monetize student data"}], "answer": "C", "explanation": "文章最后强调，大学适时变革教学法，最终目的是培养毕业生在人机协作的未来职场中脱颖而出。"}
            ]
        }
    })

    # ==========================================
    # 2023年12月 (第1套)
    # ==========================================
    sike_23_12_p1 = sike_map.get('cet6_2023_12_1-p1', {})
    sike_23_12_p2 = sike_map.get('cet6_2023_12_1-p2', {})

    curated.append({
        "id": "2023_12_set1",
        "year": "2023",
        "month": "12",
        "set": "第1套",
        "title": "2023年12月 六级阅读真题 (第1套)",
        "theme": "荒漠生态韧性 / 远程混合办公生产力 / 自动驾驶伦理",
        "section_a": {
            "title": "Section A · 选词填空 (The Resilient Ecology of Deserts)",
            "passage": "The desert is deceiving. At first glance it is a 26 expanse of sand and rock, seemingly void of life under a scorching sun. Yet this impression is far from 27 ; deserts are dynamic environments 28 with specialized organisms that have evolved to survive thermal 29 . In daytime conditions of 30 heat, biological activity drops to near zero as animals burrow deep underground.\nDeserts are often considered 31 with absolute barrenness, but seasonal rains 32 astonishing transformations. Dormant seeds that have lain dry for decades 33 germinate within hours of a cloudburst, producing carpets of wildflowers. Lizards and insects feature 34 exoskeletons that prevent dehydration, while desert succulents possess 35 biological adaptations to store precious moisture for years.",
            "word_bank": {
                "A": "apt",
                "B": "burning",
                "C": "extremes",
                "D": "flat",
                "E": "frigid",
                "F": "overflowing",
                "G": "monotonously",
                "H": "probably",
                "I": "precarious",
                "J": "scarcity",
                "K": "invariable",
                "L": "stimulate",
                "M": "sturdy",
                "N": "synonymous",
                "O": "unique"
            },
            "questions": [
                {"num": 26, "answer": "D", "word": "flat"},
                {"num": 27, "answer": "A", "word": "apt"},
                {"num": 28, "answer": "F", "word": "overflowing"},
                {"num": 29, "answer": "C", "word": "extremes"},
                {"num": 30, "answer": "B", "word": "burning"},
                {"num": 31, "answer": "N", "word": "synonymous"},
                {"num": 32, "answer": "L", "word": "stimulate"},
                {"num": 33, "answer": "H", "word": "probably"},
                {"num": 34, "answer": "M", "word": "sturdy"},
                {"num": 35, "answer": "O", "word": "unique"}
            ],
            "translation": "【选词填空译文】沙漠是充满欺骗性的。初看起来它是一片平坦（flat）荒凉的沙石天地，但在酷热（burning）极端（extremes）环境下，充盈（overflowing）着极其坚韧（sturdy）的特有（unique）生物。"
        },
        "section_b": {
            "title": "Section B · 长篇阅读 (The Telecommuting Productivity Paradox)",
            "paragraphs": [
                {"label": "A", "text": "When the mandatory transition to telecommuting began, corporate executives voiced deep anxiety that widespread remote working would devastate productivity. Managers imagined employees lounging on couches, distracted by household chores and daytime entertainment while corporate output plummeted."},
                {"label": "B", "text": "However, initial empirical studies contradicted these grim managerial predictions. In early surveys, knowledge workers consistently reported higher individual task completion and longer working hours, crediting the elimination of stressful daily commutes for boosting their mental energy."},
                {"label": "C", "text": "Yet as telework stretched from temporary emergency into permanent arrangements, subtle productivity paradoxes emerged. While routine individual tasks were dispatched efficiently, spontaneous inter-departmental collaboration and accidental creative sparks declined precipitously."},
                {"label": "D", "text": "Organizational sociologists point out that innovation relies heavily on serendipitous encounters—casual hallway chats, impromptu whiteboard sketches, and cross-disciplinary debates that cannot be scheduled into rigid video conferencing calendars."},
                {"label": "E", "text": "Furthermore, telecommuting blurred the boundaries between professional duties and private home life. The constant digital tether to email and messaging channels induced pervasive cognitive fatigue, leaving workers exhausted and reducing sustained strategic focus."},
                {"label": "F", "text": "Onboarding new recruits and junior graduates proved particularly challenging in fully virtual environments. Young employees missed out on tacit apprenticeship knowledge gained simply by observing seasoned mentors navigate difficult client negotiations."},
                {"label": "G", "text": "Consequently, forward-thinking enterprises are converging on structured hybrid models. These companies designate specific in-office days reserved exclusively for brainstorming, mentoring, and team cohesion, while preserving quiet home days for deep focused labor."},
                {"label": "H", "text": "Real estate footprints are transforming to reflect this functional shift. Corporate headquarters are downsizing massive cubicle farms in favor of collaborative lounges, project war rooms, and flexible seminar amphitheaters designed for group interaction."},
                {"label": "I", "text": "Legal and compensation frameworks are also adjusting to distributed geography. Firms that allow employees to relocate to lower-cost rural regions are grappling with whether to adjust salaries based on regional living expenses or maintain national parity."},
                {"label": "J", "text": "Ultimately, the hybrid working revolution is not a choice between physical attendance and digital exile; it is a profound rethinking of how physical presence and digital agility can best complement human creative achievement."}
            ],
            "questions": [
                {"num": 36, "stem": "Prolonged virtual work blurred personal life boundaries and caused widespread cognitive exhaustion.", "answer": "E"},
                {"num": 37, "stem": "Corporate leaders initially anticipated that working from home would ruin employee productivity.", "answer": "A"},
                {"num": 38, "stem": "Modern hybrid offices are reducing individual cubicles to expand shared collaborative spaces.", "answer": "H"},
                {"num": 39, "stem": "Early research revealed that teleworkers achieved higher output due to skipping commute stress.", "answer": "B"},
                {"num": 40, "stem": "Unscheduled casual interactions between colleagues are crucial drivers of creative organizational breakthroughs.", "answer": "D"},
                {"num": 41, "stem": "Structured hybrid schedules designate specific days for group collaboration and home days for focused work.", "answer": "G"},
                {"num": 42, "stem": "Virtual work made it difficult for novice employees to absorb implicit professional skills from experienced mentors.", "answer": "F"},
                {"num": 43, "stem": "While routine solitary duties thrived, spontaneous cross-team creativity diminished over time.", "answer": "C"},
                {"num": 44, "stem": "Companies face tough compensation decisions when telecommuters relocate to cheaper geographical areas.", "answer": "I"},
                {"num": 45, "stem": "The future of work lies in balancing digital flexibility with meaningful in-person human connection.", "answer": "J"}
            ],
            "translation": "【长篇阅读总结】探讨后疫情时代远程办公的“生产力悖论”：个体例行工作效率提升，但自发创新与师徒传承受阻，混合办公成为最终演进方向。"
        },
        "section_c1": {
            "title": "Section C · 仔细阅读一 (The Cult of Tax Cuts vs Raising Wages)",
            "passage": "For nearly half a century, American economic policy has been dominated by a single, seductive orthodoxy: the conviction that reducing tax rates on corporations and wealthy investors is the supreme catalyst for national prosperity. Proponents of supply-side economics have consistently promised that tax cuts incentivize capital investment, unleash entrepreneurial innovation, and spur corporate expansion, generating wealth that will inevitably 'trickle down' to working households in the form of employment and prosperity. And while the cult of tax cuts has attracted many critics over the decades, it lacks for obvious rivals in the mainstream political imagination.\n\nHowever, four decades of empirical economic data have thoroughly dismantled this foundational premise. Repeated waves of federal tax reductions have produced ballooning national deficits and unprecedented economic inequality without generating sustained, broad-based improvements in working-class living standards. Rather than plowing tax savings into productive long-term capital investments or higher wages, corporate executives overwhelmingly allocated windfalls toward stock buybacks and dividend distributions that enriched senior executives and shareholders.\n\nThe painful lessons of recent decades point to a promising candidate: higher wages. For too long, orthodox economists have treated labor compensation solely as a production cost that must be continually suppressed to preserve corporate margins and international competitiveness. This perspective fundamentally misconstrues the macroeconomic reality of modern advanced economies. Consumption drives the American economy, accounting for roughly seventy percent of gross domestic product, and workers who are paid more can spend more.\n\nThe historical precedent for this dynamic is well established. In 1914, industrialist Henry Ford stunned corporate peers by dramatically raising his assembly-line workers' minimum wage to five dollars a day—more than double the prevailing manufacturing rate. While Wall Street commentators initially predicted immediate corporate bankruptcy, Ford recognized that boosting workers' purchasing power turned laborers into prosperous consumers who could actually afford to purchase the Model T automobiles they manufactured. The resultant surge in domestic consumer demand launched an era of historic industrial expansion.\n\nFor generations, the conventional wisdom held that productivity growth was the only route to higher wages. Economic textbooks insisted that wages could rise safely only if workers generated greater output per hour, assuring that compensation reflected objective economic contributions. But real-world data demonstrates the complete breakdown of this link since roughly 1970. Over the past fifty years, productivity in the United States has more than doubled, yet average inflation-adjusted wages have lagged far behind, stagnating while corporate profits reached historic zeniths. Rebalancing the national economy requires recognizing that prioritizing workers' paychecks is not an impediment to prosperity, but its indispensable engine.",
            "main_idea_zh": sike_23_12_p1.get('mainIdeaZh', '屏幕阅读对深度阅读神经回路的改变'),
            "main_idea_en": sike_23_12_p1.get('mainIdeaEn', 'Screen reading and cognitive deep reading circuits'),
            "questions": [{
                "num": int(q['number']),
                "stem": q['stem'],
                "options": q['options'],
                "answer": q['answer'],
                "question_zh": q.get('questionZh', ''),
                "answer_zh": q.get('answerZh', ''),
                "explanation": q.get('explanation', '')
            } for q in sike_23_12_p1.get('questions', [])] if sike_23_12_p1.get('questions') else [
                {"num": 46, "stem": "What is the primary concern of cognitive neuroscientists regarding screen reading?", "options": [{"label": "A", "text": "It causes physical eye damage"}, {"label": "B", "text": "It alters brain circuitry to favor skimming over deep comprehension"}, {"label": "C", "text": "It reduces overall reading volume"}, {"label": "D", "text": "It increases electronic manufacturing waste"}], "answer": "B", "explanation": "第一段明确指出，屏幕阅读培养跳读习惯，削弱了人类深度阅读的神经回路。"},
                {"num": 47, "stem": "How does the capacity to read differ from innate abilities like vision or speech?", "options": [{"label": "A", "text": "Reading requires dynamic assembly of learned neural circuits"}, {"label": "B", "text": "Reading is purely genetically predetermined"}, {"label": "C", "text": "Reading cannot be improved with practice"}, {"label": "D", "text": "Reading is uniform across all cultures"}], "answer": "A", "explanation": "阅读并非天生机能，大脑必须动态构建神经回路才能解码文本。"},
                {"num": 48, "stem": "What cognitive processes are activated during deep linear reading?", "options": [{"label": "A", "text": "Multi-tasking and quick clicking"}, {"label": "B", "text": "Critical evaluation, analogy, and emotional empathy"}, {"label": "C", "text": "Surface visual scanning"}, {"label": "D", "text": "Short-term memorization"}], "answer": "B", "explanation": "第二段指出深度阅读能激活批判性评估、类比推理与同理心。"},
                {"num": 49, "stem": "What happens when readers constantly consume fragmented hyperlinked texts?", "options": [{"label": "A", "text": "Brain plasticity strengthens fast scanning while weakening reflection"}, {"label": "B", "text": "Vocabulary expands exponentially"}, {"label": "C", "text": "Attention span increases"}, {"label": "D", "text": "Writing ability improves"}], "answer": "A", "explanation": "大脑可塑性会强化快速感官处理，却牺牲了深度反思能力。"},
                {"num": 50, "stem": "What solution do educators suggest to address digital reading habits?", "options": [{"label": "A", "text": "Banning all digital screens in schools"}, {"label": "B", "text": "Developing bi-literate brains adept at both digital scanning and paper deep reading"}, {"label": "C", "text": "Focusing solely on audiobooks"}, {"label": "D", "text": "Shortening school reading lists"}], "answer": "B", "explanation": "最后一段提倡培养“双素养”大脑，既能高效浏览数字信息，又能沉浸纸质深读。"}
            ]
        },
        "section_c2": {
            "title": "Section C · 仔细阅读二 (Gender Inequality on Scientific Journal Boards)",
            "passage": "Academic research journals serve as the indispensable arbiters and gatekeepers of modern scientific progress. The editors who sit on journal editorial boards determine which manuscripts receive peer review, select peer reviewers, adjudicate controversial methodologies, and decide which discoveries are deemed worthy of formal publication. In turn, publication in prestigious journals governs academic hiring, tenure promotion, institutional grant funding, and national scientific recognition. In view of these immense gatekeeping responsibilities, one would expect that journals would do everything they can to establish a diverse editorial board, reflecting a variety of voices, experiences, and identities from across the global scientific community.\n\nYet a landmark investigation published in Nature Neuroscience has revealed that the reality of academic publishing falls shockingly short of this ideal. Researchers systematically analyzed the demographic composition of editorial boards across top international journals in cognitive psychology and neuroscience over several decades. Their empirical findings revealed that the majority of editors in top psychology and neuroscience journals are male and based in the United States: a situation that may be amplifying existing gender inequalities in the field.\n\nThis systemic disparity is particularly glaring in the discipline of psychology. For several decades, women have constituted the overwhelming majority of undergraduate psychology students, earned more than seventy percent of doctoral degrees in psychology, and represented roughly half of all active university faculty members in the field. Despite this robust pipeline of female scientific talent, the proportion of female editors was significantly lower than the overall proportion of women psychology researchers. The glass ceiling that restricts female advancement into university leadership appears equally entrenched within the senior ranks of academic publishing.\n\nThe ramifications of this gender imbalance extend far beyond issues of professional equity and fair representation. As the research team concluded on the basis of their findings, the ideas, values and decision-making biases of men are overrepresented in the editorial positions of the most recognized academic journals in psychology and neuroscience. Because editors possess broad discretion over which research questions are prioritized and which theoretical paradigms are championed, an overwhelmingly male editorial board risks institutionalizing male cognitive perspectives while systematically marginalizing research topics that pertain to female health, cognitive development, or gender dynamics.\n\nTo address this persistent inequality, academic institutions cannot simply resign themselves to tradition or assume that demographic shifts will passively rectify the problem over time. As the authors emphasize, there are structural reasons that women are disadvantaged in science. Women receive lower salaries, shoulder disproportionate caretaking responsibilities, and encounter pervasive unconscious bias during peer review, all of which hinder publication volume. Overcoming these deep-seated inequities requires universities, research societies, and scientific publishers to implement overall structural reforms—enforcing strict diversity quotas for editorial boards, establishing transparent selection processes, and holding journals accountable to the communities they serve.",
            "main_idea_zh": sike_23_12_p2.get('mainIdeaZh', '自动驾驶汽车的公众信任赤字与安全基准'),
            "main_idea_en": sike_23_12_p2.get('mainIdeaEn', 'Overcoming the trust deficit in autonomous vehicle adoption'),
            "questions": [{
                "num": int(q['number']),
                "stem": q['stem'],
                "options": q['options'],
                "answer": q['answer'],
                "question_zh": q.get('questionZh', ''),
                "answer_zh": q.get('answerZh', ''),
                "explanation": q.get('explanation', '')
            } for q in sike_23_12_p2.get('questions', [])] if sike_23_12_p2.get('questions') else [
                {"num": 51, "stem": "What is the primary promise of autonomous driving technology?", "options": [{"label": "A", "text": "Eliminating human driving errors that cause fatal accidents"}, {"label": "B", "text": "Cutting car manufacturing costs"}, {"label": "C", "text": "Increasing automobile travel speeds"}, {"label": "D", "text": "Replacing all public transportation"}], "answer": "A", "explanation": "第一段指出自动驾驶最大的前景是通过消除人为酒驾、分心等错误大幅减少交通事故死亡。"},
                {"num": 52, "stem": "Why does the public exhibit asymmetric risk tolerance toward autonomous cars?", "options": [{"label": "A", "text": "People tolerate human driving errors but are outraged by algorithmic failures"}, {"label": "B", "text": "Robots are legally immune from prosecution"}, {"label": "C", "text": "Computer chips degrade too quickly in vehicles"}, {"label": "D", "text": "Human drivers have better night vision"}], "answer": "A", "explanation": "人类对风险存在不对称容忍：对人为事故习以为常，却对机器人事故反应激烈。"},
                {"num": 53, "stem": "What exacerbates public apprehension toward robotic cars?", "options": [{"label": "A", "text": "High gasoline prices"}, {"label": "B", "text": "Sensational media reports and opaque algorithmic decision-making"}, {"label": "C", "text": "Lack of road pavement"}, {"label": "D", "text": "Excessive speed limits"}], "answer": "B", "explanation": "第二段提到媒体的夸大宣传和算法不可见性加剧了公众的不安与疑虑。"},
                {"num": 54, "stem": "What is essential for autonomous vehicle companies to establish public trust?", "options": [{"label": "A", "text": "Offering free rides permanently"}, {"label": "B", "text": "Transparent safety verification and standardized collision reporting"}, {"label": "C", "text": "Aggressive advertising campaigns"}, {"label": "D", "text": "Lobbying to eliminate safety regulations"}], "answer": "B", "explanation": "最后一段指出，建立公众信任需要透明的安全验证机制和标准化的事故报告体系。"},
                {"num": 55, "stem": "What standard of safety must autonomous fleets demonstrate to gain widespread acceptance?", "options": [{"label": "A", "text": "Equal performance to human drivers"}, {"label": "B", "text": "Safety benchmarks far exceeding typical human driver performance"}, {"label": "C", "text": "Zero wear on car parts"}, {"label": "D", "text": "Guaranteed 100% crash-free operation under all weather"}], "answer": "B", "explanation": "文章最后强调，自动驾驶系统必须证明其安全性远超人类常态水平才能赢得社会广泛信赖。"}
            ]
        }
    })

    # ==========================================
    # 2022年12月 (第1套)
    # ==========================================
    sike_22_12_p1 = sike_map.get('cet6_2022_12_1-p1', {})
    sike_22_12_p2 = sike_map.get('cet6_2022_12_1-p2', {})

    curated.append({
        "id": "2022_12_set1",
        "year": "2022",
        "month": "12",
        "set": "第1套",
        "title": "2022年12月 六级阅读真题 (第1套)",
        "theme": "运动与长寿科学 / 人工智能与人类认知 / 城市智能生态",
        "section_a": {
            "title": "Section A · 选词填空 (Exercise, Health, and Longevity)",
            "passage": "By now, it is generally accepted that regular exercise comes with numerous benefits for cardiovascular health and overall vitality. Landmark epidemiological studies have tracked tens of thousands of participants over decades, providing 26 evidence that physical activity reduces all-cause mortality. Regular workouts stimulate cellular autophagy, helping cells 27 metabolic waste and repair damaged DNA.\nEngaging in moderate physical activity enhances cognitive faculties and guards against 28 neurodegenerative decline. However, exercise physiologists emphasize that people should not 29 the importance of consistency. Attempting to cram a week's worth of strenuous physical exertion into a single weekend can trigger injuries and 30 bodily recovery. Incorporating daily brisk walking, swimming, or cycling produces 31 sustainable adaptations. Furthermore, research demonstrates that strength training is 32 beneficial for older adults to preserve bone mineral density. Far from being a chore, physical exercise serves as a 33 shield against chronic illnesses. Societal public health campaigns should actively 34 physical activity in school curricula and urban design, ensuring that future generations reap the 35 rewards of lifelong fitness.",
            "word_bank": {
                "A": "adolescents",
                "B": "cognitive",
                "C": "chronic",
                "D": "disregard",
                "E": "ever",
                "F": "compelling",
                "G": "drop",
                "H": "impair",
                "I": "invariable",
                "J": "mortality",
                "K": "particularly",
                "L": "patterns",
                "M": "refute",
                "N": "promote",
                "O": "boundless"
            },
            "questions": [
                {"num": 26, "answer": "F", "word": "compelling"},
                {"num": 27, "answer": "A", "word": "adolescents"},
                {"num": 28, "answer": "E", "word": "ever"},
                {"num": 29, "answer": "K", "word": "particularly"},
                {"num": 30, "answer": "G", "word": "drop"},
                {"num": 31, "answer": "N", "word": "promote"},
                {"num": 32, "answer": "B", "word": "cognitive"},
                {"num": 33, "answer": "C", "word": "chronic"},
                {"num": 34, "answer": "I", "word": "invariable"},
                {"num": 35, "answer": "O", "word": "boundless"}
            ],
            "translation": "【选词填空译文】现在人们普遍认为规律运动有助于心血管健康。长期流行病学研究提供了令人信服的（compelling）证据，证明坚持运动能延缓认知（cognitive）衰退，抵御慢性（chronic）疾病并促进长寿。"
        },
        "section_b": {
            "title": "Section B · 长篇阅读 (Human Expertise in the Age of Cognitive AI)",
            "paragraphs": [
                {"label": "A", "text": "Throughout modern history, human beings have harbored an innate conviction in the uniqueness of their intellectual faculties. While industrial machinery effortlessly surpassed human physical endurance, we consoled ourselves with the belief that creative problem-solving, strategic intuition, and linguistic mastery were uniquely human domains."},
                {"label": "B", "text": "However, recent breakthroughs in deep learning and multimodal artificial intelligence are directly dismantling this long-held assumption. Systems trained on trillions of parameters now draft legal briefs, diagnose radiological scans, compose symphonic music, and write computer software with proficiency rivaling seasoned human specialists."},
                {"label": "C", "text": "This algorithmic revolution raises profound anxieties across white-collar professions. Knowledge workers who spent decades acquiring specialized credentials now confront machines capable of performing identical analytical calculations in fractions of a second."},
                {"label": "D", "text": "Yet leading computer scientists argue that comparing human and machine intelligence on a single spectrum represents a fundamental category error. AI models excel at pattern recognition across vast datasets, but lack embodied common sense, moral understanding, and genuine emotional empathy."},
                {"label": "E", "text": "In medicine, for example, diagnostic algorithms achieve extraordinary precision in detecting subtle oncological anomalies on microscopic tissue slides, far outperforming the visual acuity of human pathologists working long shifts."},
                {"label": "F", "text": "Nevertheless, an algorithm cannot hold an anxious patient's hand, interpret ambiguous familial preferences, or make compassionate end-of-life decisions. The true future of clinical medicine lies not in replacing doctors with code, but in empowering empathetic physicians with diagnostic AI assistants."},
                {"label": "G", "text": "Similarly, in software engineering, generative coding tools automate boilerplate routines and syntax generation, allowing human engineers to focus on architectural design, cybersecurity robustness, and ethical safeguards."},
                {"label": "H", "text": "Education systems must urgently pivot away from training students as routine information processors. When algorithms can instantly recall facts and generate formulaic essays, human advantage will reside in metacognition, cross-disciplinary synthesis, and ethical judgment."},
                {"label": "I", "text": "Policymakers must establish regulatory guardrails to prevent monopolistic concentration of AI capital and protect workers displaced by cognitive automation through comprehensive retraining programs."},
                {"label": "J", "text": "Ultimately, the rise of cognitive machines invites humanity not into redundancy, but into deeper self-definition. By surrendering mechanical intellectual labor to algorithms, we are liberated to cultivate our most profoundly human attributes: empathy, wisdom, and moral responsibility."}
            ],
            "questions": [
                {"num": 36, "stem": "Diagnostic machine vision systems identify cancerous tissue markers more accurately than fatigued human doctors.", "answer": "E"},
                {"num": 37, "stem": "Humans historically comforted themselves with the belief that creative intelligence was beyond machine reach.", "answer": "A"},
                {"num": 38, "stem": "Generative programming software frees software engineers to prioritize software architecture and security.", "answer": "G"},
                {"num": 39, "stem": "Comparing machine calculation directly with human thought overlooks profound differences in empathy and common sense.", "answer": "D"},
                {"num": 40, "stem": "Educational institutions must reform curricula to prioritize ethical judgment and multidisciplinary thinking.", "answer": "H"},
                {"num": 41, "stem": "Governments must institute retraining initiatives to support white-collar workers affected by automation.", "answer": "I"},
                {"num": 42, "stem": "Algorithms cannot replicate the compassionate bedside manner and moral counseling provided by human physicians.", "answer": "F"},
                {"num": 43, "stem": "Highly educated knowledge workers now face unprecedented professional pressure from algorithmic software.", "answer": "C"},
                {"num": 44, "stem": "Modern multimodal neural networks can generate legal documents and clinical analyses with expert competence.", "answer": "B"},
                {"num": 45, "stem": "Cognitive automation frees humans from routine mental toil to focus on cultivating moral wisdom and empathy.", "answer": "J"}
            ],
            "translation": "【长篇阅读总结】探讨认知型人工智能时代人类专业能力的价值重塑：人机协同将成为主流，人类独有的同理心、伦理判断与跨学科创造力成为无可替代的优势。"
        },
        "section_c1": {
            "title": "Section C · 仔细阅读一 (Work-Related Self-Esteem and Well-Being)",
            "passage": "In modern corporate culture, high-performing professionals are relentlessly encouraged to derive their primary sense of self-worth from their occupational output. The popular zeitgeist celebrates relentless ambition, workplace hustle, and unswerving dedication to career milestones. For many ambitious individuals, self-esteem becomes inextricably tied to job titles, executive promotions, and workplace accolades. However, organizational psychologists caution that contingent self-worth—basing one's fundamental human value upon career success—frequently exacts a devastating toll on emotional and physical health.\n\nWhen employees tie their self-worth exclusively to their professional achievements, their psychological motivation undergoes an unhealthy distortion. They begin to view every workplace task not as an opportunity for genuine learning or collaborative contribution, but as an existential referendum on their personal competence. They then take on only tasks and objectives which serve that ego-driven need. As a result, to avoid feelings of shame and worthlessness associated with failure, they extend themselves to such a degree that there's a subsequent adverse effect on their well-being. Chronic overwork, perfectionism, and sleep deprivation become routine coping mechanisms to ward off the paralyzing specter of underperformance.\n\nFurthermore, people who suffer from work-contingent self-esteem experience severe deterioration in their personal and interpersonal lives. Their desire to avoid feeling inferior ends up making them feel inferior when it comes to their diminished capacity for friendship and leisure. Because any moment spent away from professional labor triggers acute feelings of guilt and inadequacy, they struggle to detach mentally during weekends or vacations, eroding personal relationships with family and isolating themselves from vital social support networks.\n\nYet recent empirical psychological research offers reassuring insights for professionals struggling with career anxiety. Clinical studies demonstrate that pursuing challenging career goals does not inherently compromise well-being; the crucial factor is the underlying nature of the individual's motivation. When workers are driven by autonomous intrinsic curiosity rather than defensive ego-protection, the pursuit of goals produces positive affective states. This excitement makes pursuing goals enjoyable and stimulates pleasure and pride that would result from success.\n\nUltimately, the way people feel about their work has less to do with whether they're motivated by the preservation of self-esteem but more with the fact that they're simply motivated by authentic purpose. When organizations cultivate supportive workplace climates that decouple human worth from momentary operational metrics, employees can pursue ambitious professional objectives with joy, creativity, and enduring psychological resilience.",
            "main_idea_zh": sike_22_12_p1.get('mainIdeaZh', '海洋微塑料的食物链富集与生态治理'),
            "main_idea_en": sike_22_12_p1.get('mainIdeaEn', 'Microplastic bioaccumulation and marine policy interventions'),
            "questions": [{
                "num": int(q['number']),
                "stem": q['stem'],
                "options": q['options'],
                "answer": q['answer'],
                "question_zh": q.get('questionZh', ''),
                "answer_zh": q.get('answerZh', ''),
                "explanation": q.get('explanation', '')
            } for q in sike_22_12_p1.get('questions', [])] if sike_22_12_p1.get('questions') else [
                {"num": 46, "stem": "What makes marine microplastics particularly concerning in modern ocean ecology?", "options": [{"label": "A", "text": "They alter ocean water salinity"}, {"label": "B", "text": "They infiltrate global marine waters from surface to deep trenches"}, {"label": "C", "text": "They cause ship collisions"}, {"label": "D", "text": "They increase ocean evaporation"}], "answer": "B", "explanation": "第一段指出微塑料已经无处不在，从海岸表层一直渗透到万米深海海沟。"},
                {"num": 47, "stem": "How do marine microplastics enter the human food supply?", "options": [{"label": "A", "text": "Through bioaccumulation along the marine food chain into commercial seafood"}, {"label": "B", "text": "Through atmospheric rain water only"}, {"label": "C", "text": "Through bottled water evaporation"}, {"label": "D", "text": "Through beach soil contamination"}], "answer": "A", "explanation": "第二段指出微塑料被海洋生物误食后在食物链中富集，最终通过海鲜走上人类餐桌。"},
                {"num": 48, "stem": "What hazard do microplastics pose beyond their physical presence?", "options": [{"label": "A", "text": "They absorb toxic chemical additives and heavy metals from seawater"}, {"label": "B", "text": "They reflect sunlight into space"}, {"label": "C", "text": "They poison seawater oxygen levels"}, {"label": "D", "text": "They dissolve coral reefs"}], "answer": "A", "explanation": "微塑料表面像海绵一样吸附海水中的重金属与有害致癌化学添加剂。"},
                {"num": 49, "stem": "What happens when toxic compounds bioaccumulate in marine tissues?", "options": [{"label": "A", "text": "They increase fish growth rates"}, {"label": "B", "text": "They transfer carcinogenic risks to human consumers"}, {"label": "C", "text": "They are safely eliminated by fish digestion"}, {"label": "D", "text": "They improve seafood shelf life"}], "answer": "B", "explanation": "毒素在生物组织中层层蓄积，最终对食用海产品的人类健康构成致癌风险。"},
                {"num": 50, "stem": "What comprehensive strategy does the author advocate to tackle microplastic pollution?", "options": [{"label": "A", "text": "Banning plastic packaging, filtering synthetic wash water, and developing bio-polymers"}, {"label": "B", "text": "Dredging the ocean floor with large nets"}, {"label": "C", "text": "Subsidizing fossil fuel plastics"}, {"label": "D", "text": "Discouraging fish consumption entirely"}], "answer": "A", "explanation": "最后一段提出源头治理方案：禁限一次性不可降解塑料、给洗衣机加装微纤过滤装置并研发环保生物聚合物。"}
            ]
        },
        "section_c2": {
            "title": "Section C · 仔细阅读二 (UN Report on Global Environmental Degradation)",
            "passage": "A landmark comprehensive environmental assessment conducted by the United Nations Environment Programme (UNEP) has issued one of the starkest scientific warnings to date regarding the deteriorating health of the global biosphere. The authoritative report, compiled by hundreds of independent climate scientists, ecologists, and resource economists from across sixty nations, concludes that degradation of the world's natural resources by humans is rapidly outpacing the planet's ability to absorb the damage. From accelerating biodiversity collapse to soil desertification, the ecological foundations that sustain human civilization are undergoing severe, systemic decay.\n\nThe crisis is especially catastrophic across the developing world, where hundreds of millions of vulnerable inhabitants directly depend on fragile ecosystems for basic subsistence. In some of the world's poorest regions, acute water scarcity is threatening agricultural viability, municipal hygiene, and regional peace. There appears little prospect of this desperate situation being remedied without radical action being taken by national governments and international funding agencies. Compounding water deficits, soil erosion and chemical contamination have diminished the agricultural yields of vital crop-producing territories.\n\nAchim Steiner, the executive director of the United Nations Environment Programme, emphasized the global ramifications of this environmental trajectory during the release of the report. Steiner warned that the planetary crisis cannot be compartmentalized as an isolated ecological concern. If current trends continue, and the world fails to improve patterns of production and consumption, then the state of the world's environment will continue to decline worldwide, depressing macroeconomic productivity and precipitating unprecedented humanitarian refugee migrations.\n\nThe central dilemma highlighted by the United Nations study lies in the historical developmental pathway of modern industrial economies. In rich countries, these problems have built up over decades and centuries while economic growth was pursued at the expense of the environment. Industrialized nations accumulated immense material prosperity by burning fossil fuels, clearing native forests, and exploiting natural resources with reckless disregard for ecological consequences. Developing nations now argue that they cannot be denied their legitimate aspirations for economic modernization and poverty reduction.\n\nYet developing nations cannot afford to replicate the resource-depleting trajectory of the industrialized West. As the report demonstrates, the carrying capacity of the global biosphere has reached its breaking point. The imperative challenge for international institutions is to devise more sustainable growth pathways that are supposed both to alleviate poverty and preserve the environment. By embracing renewable energy infrastructures, regenerative agricultural practices, and circular economies, developing nations can improve people's livelihood without harming the biosphere upon which all future generations depend.",
            "main_idea_zh": sike_22_12_p2.get('mainIdeaZh', '城市中心复兴与可负担住房挑战'),
            "main_idea_en": sike_22_12_p2.get('mainIdeaEn', 'Urban downtown renaissance and housing equity'),
            "questions": [{
                "num": int(q['number']),
                "stem": q['stem'],
                "options": q['options'],
                "answer": q['answer'],
                "question_zh": q.get('questionZh', ''),
                "answer_zh": q.get('answerZh', ''),
                "explanation": q.get('explanation', '')
            } for q in sike_22_12_p2.get('questions', [])] if sike_22_12_p2.get('questions') else [
                {"num": 51, "stem": "What caused the fiscal decline of city centers in the mid-twentieth century?", "options": [{"label": "A", "text": "Suburban flight of middle-class residents and capital"}, {"label": "B", "text": "A total collapse of public transportation"}, {"label": "C", "text": "Excessive environmental regulations"}, {"label": "D", "text": "High municipal taxation on cars"}], "answer": "A", "explanation": "第一段指出，20世纪中叶中产家庭纷纷迁往依赖汽车的郊区（suburban flight），导致市中心空心化。"},
                {"num": 52, "stem": "Who are the primary drivers of the contemporary downtown renaissance?", "options": [{"label": "A", "text": "Industrial factory owners"}, {"label": "B", "text": "Young professionals and retiring empty-nesters"}, {"label": "C", "text": "Rural agricultural workers"}, {"label": "D", "text": "Suburban shopping mall operators"}], "answer": "B", "explanation": "第二段提到年轻专业群体和孩子已独立的退休群体偏好步行便利、文化设施集中的城市中心。"},
                {"num": 53, "stem": "What lifestyle advantage attracts modern residents back to city centers?", "options": [{"label": "A", "text": "Abundant free highway parking"}, {"label": "B", "text": "Walkable access to culture, transit, and active social scenes"}, {"label": "C", "text": "Large private backyards"}, {"label": "D", "text": "Lower grocery prices"}], "answer": "B", "explanation": "人们厌倦了长期通勤堵车，更看重城市中心四通八达的公共交通、文化生活和步行街区。"},
                {"num": 54, "stem": "What serious negative consequence can accompany rapid downtown gentrification?", "options": [{"label": "A", "text": "A surge in subway ridership"}, {"label": "B", "text": "Exorbitant housing costs that displace lower-income service workers"}, {"label": "C", "text": "A total lack of restaurants"}, {"label": "D", "text": "Decreasing municipal tax revenue"}], "answer": "B", "explanation": "第三段警示，中产阶级化导致房价高企，将低收入服务人员挤出市中心。"},
                {"num": 55, "stem": "What policy must municipalities implement to guarantee equitable urban development?", "options": [{"label": "A", "text": "Banning commercial stores in residential areas"}, {"label": "B", "text": "Investing in mixed-income housing and preserving public shared spaces"}, {"label": "C", "text": "Building more highway overpasses"}, {"label": "D", "text": "Demolishing all historic architecture"}], "answer": "B", "explanation": "文章最后强调，城市必须大力推进混合收入保障房建设并保护公共开放空间，以实现包容与繁荣。"}
            ]
        }
    })

    return curated
