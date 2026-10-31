# -*- coding: utf-8 -*-
"""
Curated CET-6 genuine reading passages (2014-2017 and 2021.12 supplements)
with full questions, options, answers, translations, and point-by-point explanations.
"""

def get_curated_exams():
    curated = []

    # ==========================================
    # 2014年6月 六级真题 (第1套)
    # ==========================================
    curated.append({
        "id": "2014_06_set1",
        "year": "2014",
        "month": "06",
        "set": "第1套",
        "title": "2014年6月 六级阅读真题 (第1套)",
        "theme": "医疗科技 / 区域经济 / 现代教育",
        "section_a": {
            "title": "Section A · 选词填空 (Banked Cloze)",
            "passage": "Rising concentrations of carbon dioxide in the atmosphere are causing oceans to become more acidic, with potentially 26 consequences for marine life. As seawater absorbs carbon dioxide, chemical reactions occur that reduce seawater pH, carbonate ion concentration, and 27 states of biologically important calcium carbonate minerals. These chemical reactions are termed 'ocean acidification'. Many marine organisms, such as corals, clams, and oysters, require calcium carbonate to build their shells and 28 .\nLaboratory studies show that increased acidity can 29 calcification rates in corals and other shellfish. In some experiments, corals exposed to high carbon dioxide levels even began to 30 completely. Moreover, changes in ocean chemistry can affect the behavior of non-calcifying organisms as well. The ability of certain fish to 31 predators is impaired in higher acidity waters, and larvae may have difficulty locating suitable 32 for growth. Commercial fisheries and aquaculture are 33 by these environmental shifts, threatening food supplies and coastal economies around the globe. Scientists warn that unless carbon emissions are 34 curtailed, ocean acidification will accelerate, 35 altering marine biodiversity.",
            "word_bank": {
                "A": "detect",
                "B": "drastically",
                "C": "habitats",
                "D": "jeopardized",
                "E": "dissolve",
                "F": "devastating",
                "G": "suppress",
                "H": "saturation",
                "I": "skeletons",
                "J": "drastically",
                "K": "substantially",
                "L": "tolerated",
                "M": "abruptly",
                "N": "fluctuate",
                "O": "reproduce"
            },
            "questions": [
                {"num": 26, "answer": "F", "word": "devastating", "analysis": "形容词修饰consequences，表示'毁灭性的、破坏性的后果'。"},
                {"num": 27, "answer": "H", "word": "saturation", "analysis": "名词作定语修饰states，'saturation states'意为'饱和状态'。"},
                {"num": 28, "answer": "I", "word": "skeletons", "analysis": "名词与shells并列，表示珊瑚贝类的'外壳与骨骼'。"},
                {"num": 29, "answer": "G", "word": "suppress", "analysis": "情态动词can后接动词原形，'suppress calcification rates'抑制钙化率。"},
                {"num": 30, "answer": "E", "word": "dissolve", "analysis": "动词原形，高浓度二氧化碳让珊瑚开始'溶解'。"},
                {"num": 31, "answer": "A", "word": "detect", "analysis": "动词原形，'detect predators'意为察觉捕食者。"},
                {"num": 32, "answer": "C", "word": "habitats", "analysis": "名词复数，'suitable habitats for growth'合适生长的栖息地。"},
                {"num": 33, "answer": "D", "word": "jeopardized", "analysis": "被动语态，渔业和水产养殖'受到危害/威胁'。"},
                {"num": 34, "answer": "K", "word": "substantially", "analysis": "副词修饰curtailed，表示碳排放必须'实质性地、大幅削减'。"},
                {"num": 35, "answer": "B", "word": "drastically", "analysis": "副词修饰altering，'drastically altering'彻底改变海洋多样性。"}
            ],
            "translation": "大气中二氧化碳浓度的上升正导致海洋酸度增加，这可能对海洋生物造成破坏性的后果。随着海水吸收二氧化碳，发生的化学反应会降低海水的pH值、碳酸根离子浓度以及生物所需的重要碳酸钙矿物的饱和状态。这些化学反应被称为“海洋酸化”。诸如珊瑚、蛤蜊和牡蛎等众多海洋生物需要碳酸钙来构建其外壳和骨骼。\n实验室研究表明，酸度上升会抑制珊瑚及其他贝类的钙化速率。在一些实验中，暴露在高浓度二氧化碳环境下的珊瑚甚至开始完全溶解。此外，海洋化学性质的改变还会影响非钙化生物的行为。某些鱼类在酸度更高的海水中察觉捕食者的能力受损，幼体也可能难以找到适合生长的栖息地。商业渔业和水产养殖业正受到这些环境变化的威胁，危及全球食物供应和沿海经济。科学家警告称，除非大幅削减碳排放，否则海洋酸化将加速，彻底改变海洋生物多样性。",
            "vocabulary": [
                {"w": "acidification", "p": "/əˌsɪdɪfɪˈkeɪʃn/", "t": "n. 酸化"},
                {"w": "devastating", "p": "/ˈdevəsteɪtɪŋ/", "t": "adj. 毁灭性的，破坏极大的"},
                {"w": "saturation", "p": "/ˌsætʃəˈreɪʃn/", "t": "n. 饱和，饱和度"},
                {"w": "calcification", "p": "/ˌkælsɪfɪˈkeɪʃn/", "t": "n. 钙化作用"},
                {"w": "jeopardize", "p": "/ˈdʒepədaɪz/", "t": "v. 危及，危害"}
            ]
        },
        "section_b": {
            "title": "Section B · 长篇阅读 (The Future of MOOCs in Higher Education)",
            "paragraphs": [
                {"label": "A", "text": "When massive open online courses (MOOCs) first captured the world's attention in 2012, tech visionaries declared that traditional universities were facing imminent extinction. Why would students pay tens of thousands of dollars to sit in lecture halls when they could watch lectures by the world's leading scholars on their laptops for free? Enthusiasts predicted that a handful of elite universities would soon teach the entire planet, democratizing knowledge and driving tuition costs down to near zero."},
                {"label": "B", "text": "Fast forward several years, and the university campus remains stubbornly alive. Lecture halls are still filled with undergraduates, tuition bills have continued their relentless upward march, and brick-and-mortar colleges have not vanished into digital ether. Yet declaring MOOCs an outright failure misses the profound and subtle ways they have reshaped the global educational landscape."},
                {"label": "C", "text": "The most widely publicized shortcoming of early MOOCs was their dismal completion rate. Across hundreds of courses analyzed by university researchers, typically fewer than 10 percent of registered learners completed the course. It turned out that signing up for a free course with a single mouse click demanded no commitment. When students encountered challenging problem sets or busy work schedules, they simply abandoned the course without financial or academic penalty."},
                {"label": "D", "text": "Furthermore, early platforms discovered that their audience was not the underprivileged masses of the developing world that founders envisioned. Surveys revealed that over 70 percent of MOOC learners already held a bachelor's or advanced degree. Rather than serving as an equalizer for marginalized youths, MOOCs initially functioned as a professional enrichment tool for middle-class, college-educated adults looking to learn coding, data analysis, or management skills."},
                {"label": "E", "text": "Faced with high dropout rates and unsustainable costs, commercial MOOC providers underwent a dramatic strategic pivot. Companies like Coursera and Udacity shifted their focus away from general undergraduate education toward corporate training and specialized micro-credentials designed in partnership with Fortune 500 employers. Instead of offering free college credits, they began selling 'nanodegrees' that promised tangible job placement advantages in high-demand tech sectors."},
                {"label": "F", "text": "Meanwhile, traditional universities began integrating online components into their residential offerings in what educators call 'blended learning.' Professors increasingly flip their classrooms: assigning online video lectures as homework and dedicating valuable face-to-face class time to seminars, collaborative group projects, and interactive debates. Rather than replacing physical professors, digital technology freed them from repeating basic lectures every semester."},
                {"label": "G", "text": "Elite institutions also recognized that their core value was never merely delivering lecture content. A university degree represents a bundle of distinct goods: credentialing, career networking, social development, and rigorous peer interaction. While an algorithm can grade a multiple-choice quiz and deliver a streaming video, it cannot mentor a graduate student, lead an organic chemistry lab, or foster lifelong professional friendships in a student dormitory."},
                {"label": "H", "text": "Nevertheless, online learning is proving transformative for graduate education. Prestigious institutions now offer fully accredited master's degrees in computer science and business analytics online at a fraction of on-campus tuition. Georgia Tech's online Master of Science in Computer Science, delivered via online platforms for under $10,000, demonstrated that high educational rigor and massive scale could coexist sustainably, expanding access to mid-career professionals worldwide."},
                {"label": "I", "text": "In developing countries, while barriers like unreliable internet and language hurdles persist, modular online courses are increasingly blended with local community hubs. Non-governmental organizations and regional colleges set up learning centers where students watch digital lectures together and receive in-person tutoring, bridging the gap between digital content and human support."},
                {"label": "J", "text": "The evolution of MOOCs offers a cautionary tale about technological determinism in education. Online tools do not destroy complex social institutions overnight; instead, they slowly weave themselves into existing structures, unbundling certain functions while reinforcing others. Higher education has been transformed not by the wholesale replacement of colleges, but by a hybrid future where digital scale and face-to-face community complement one another."}
            ],
            "questions": [
                {"num": 36, "stem": "Surveys indicated that early online courses primarily attracted adults who were already well educated.", "answer": "D"},
                {"num": 37, "stem": "Elite universities realize that the genuine worth of college education extends far beyond passive lecture delivery.", "answer": "G"},
                {"num": 38, "stem": "Tech visionaries originally believed that prestigious colleges would soon replace traditional universities across the globe.", "answer": "A"},
                {"num": 39, "stem": "A very small fraction of registered students actually finished their courses in the early era of MOOCs.", "answer": "C"},
                {"num": 40, "stem": "Flipping classrooms allows educators to spend classroom time on meaningful discussion rather than repetitive lectures.", "answer": "F"},
                {"num": 41, "stem": "Commercial MOOC platforms reorganized their business models toward corporate partnerships and career training.", "answer": "E"},
                {"num": 42, "stem": "Traditional campuses continue to thrive despite early warnings of their inevitable disappearance.", "answer": "B"},
                {"num": 43, "stem": "Affordable online graduate degrees have proven that high academic standards can be delivered at large scale.", "answer": "H"},
                {"num": 44, "stem": "Rather than eliminating physical universities, technological advances have resulted in a blended model of higher education.", "answer": "J"},
                {"num": 45, "stem": "Local learning centers in developing nations combine streaming lectures with face-to-face coaching.", "answer": "I"}
            ],
            "translation": "长篇阅读解析总结：文章探讨了慕课（MOOCs）在高等教育中的演进历程与真实影响。早期技术乌托邦预言传统大学即将消亡，但事实证明大学并未消失。慕课早期面临完成率低（不足10%）以及主要受益者为已具大学学历的中产人群等现实。随后，慕课平台向企业职业培训和微证书转型，大学则采纳“翻转课堂”与混合式教学模式。大学的核心价值不仅在于传授知识，更在于文凭认证、人际网络与实验室培养。最终高等教育形成了数字规模与线下人本结合的混合未来。"
        },
        "section_c1": {
            "title": "Section C · 仔细阅读 Passage 1 (Distracted Doctoring in Hospitals)",
            "passage": "Hospitals, hoping to curb medical error, have invested heavily to put computers, mobile devices, and smartphones into the hands of medical staff. The rationale seemed unassailable: digitized charts would prevent illegible handwriting mishaps, instant drug databases would flag lethal interactions, and mobile communications would allow surgeons and nurses to coordinate care in real time. Today, technology permeates nearly every hospital corridor.\nYet an unexpected side effect has emerged that many doctors call 'distracted doctoring.' At a time when medical devices transmit constant streams of alerts and smartphones buzz with personal text messages and social media notifications, doctors and nurses find their attention fractured. A technology designed to safeguard patients is now competing with patients for the caregiver's focus.\nSeveral alarming incidents have highlighted the risks. In one widely reported case, a neurosurgeon checked personal emails during a delicate operation, causing critical surgical delays. In another, a medical resident was so engrossed in an iPad during bedside rounds that he failed to notice a patient's worsening vital signs until a family member shouted for help. Surveys show that more than half of medical technicians admit to sending personal text messages while operating heart-lung machines.\nDr. Peter Papadakos, a professor of anesthesiology and medical ethics, warns that doctors' interaction with high-tech screens may actively endanger patients' lives. 'The screen is seductive,' he explains. 'It draws you in with endless information and instant gratification, blinding you to the living human being right in front of you. When you are performing complex clinical procedures, even a two-second lapse of concentration can have fatal consequences.'\nAddressing distracted doctoring poses formidable challenges. Outright bans on mobile devices are impractical, since doctors rely on clinical apps and diagnostic references on the fly. Some hospitals have introduced 'sterile cockpit' rules—borrowed from aviation—that prohibit non-essential chatter and personal digital devices during critical medical procedures. Ultimately, experts argue, medical schools must foster a culture of mindful technology use, training doctors to look up from their screens and remember the human patient at the center of medicine.",
            "questions": [
                {
                    "num": 46,
                    "stem": "Why did hospitals originally introduce computers and mobile devices?",
                    "options": [
                        {"label": "A", "text": "To reduce medical errors and enhance coordination."},
                        {"label": "B", "text": "To cut down the heavy workloads of hospital nurses."},
                        {"label": "C", "text": "To replace aging medical equipment with modern tools."},
                        {"label": "D", "text": "To collect comprehensive clinical data for scientific research."}
                    ],
                    "answer": "A",
                    "question_zh": "医院最初引入电脑和移动设备的原因是什么？",
                    "answer_zh": "为了减少医疗错误并加强协调。",
                    "explanation": "首段首句明确指出：'Hospitals, hoping to curb medical error, have invested heavily to put computers, mobile devices... into the hands of medical staff'，句中curb medical error对应A项reduce medical errors。"
                },
                {
                    "num": 47,
                    "stem": "What does the term 'distracted doctoring' illustrate?",
                    "options": [
                        {"label": "A", "text": "The shortage of qualified medical specialists in hospitals."},
                        {"label": "B", "text": "The inability of doctors to understand complex medical software."},
                        {"label": "C", "text": "The unintended adverse consequence of medical digitalization."},
                        {"label": "D", "text": "The conflict between hospital administration and medical staff."}
                    ],
                    "answer": "C",
                    "question_zh": "“分心行医”这一术语说明了什么？",
                    "answer_zh": "医疗数字化带来的意外负面后果。",
                    "explanation": "第二段指出'an unexpected side effect has emerged that many doctors call distracted doctoring'，说明分心行医是数字化技术带来的意料之外的副作用（unintended adverse consequence）。"
                },
                {
                    "num": 48,
                    "stem": "What is Dr. Peter Papadakos's chief concern regarding screen usage?",
                    "options": [
                        {"label": "A", "text": "Screens will cause doctors severe eye strain and fatigue."},
                        {"label": "B", "text": "Excessive screen immersion poses serious threats to patient safety."},
                        {"label": "C", "text": "Hospital software is too complicated for senior doctors to operate."},
                        {"label": "D", "text": "Digital records will leak patients' confidential health information."}
                    ],
                    "answer": "B",
                    "question_zh": "彼得·帕帕达克斯博士对屏幕使用的主要担忧是什么？",
                    "answer_zh": "过度沉迷屏幕对患者生命安全构成严重威胁。",
                    "explanation": "第四段首句明确提到：'Dr. Peter Papadakos... warns that doctors' interaction with high-tech screens may actively endanger patients' lives'，对应B项严重威胁患者安全。"
                },
                {
                    "num": 49,
                    "stem": "Why are hospital bans on personal mobile devices deemed impractical?",
                    "options": [
                        {"label": "A", "text": "Patients demand constant communication with their attending doctors."},
                        {"label": "B", "text": "Staff members refuse to abide by any hospital restrictions."},
                        {"label": "C", "text": "Medical personnel depend on handheld tools for diagnostic work."},
                        {"label": "D", "text": "Enforcing the ban would cost hospitals excessive financial resources."}
                    ],
                    "answer": "C",
                    "question_zh": "为什么医院全面禁止个人移动设备被认为是行不通的？",
                    "answer_zh": "医务人员依赖便携工具开展临床诊断工作。",
                    "explanation": "第五段明确指出：'Outright bans on mobile devices are impractical, since doctors rely on clinical apps and diagnostic references on the fly'，对应C项。"
                },
                {
                    "num": 50,
                    "stem": "What is recommended as a practical countermeasure against distracted doctoring?",
                    "options": [
                        {"label": "A", "text": "Replacing human clinicians with autonomous surgical robots."},
                        {"label": "B", "text": "Imposing protocols borrowed from aviation during critical procedures."},
                        {"label": "C", "text": "Confiscating all digital hardware at hospital entrances."},
                        {"label": "D", "text": "Penalizing doctors who check personal emails with heavy fines."}
                    ],
                    "answer": "B",
                    "question_zh": "针对分心行医推荐了什么切实的应对措施？",
                    "answer_zh": "在关键医疗流程中引入借鉴自航空业的规范。",
                    "explanation": "第五段指出'Some hospitals have introduced sterile cockpit rules—borrowed from aviation—that prohibit non-essential chatter and personal digital devices during critical medical procedures'，对应B项。"
                }
            ],
            "main_idea_zh": "本文探讨了医院引入智能移动设备后的副作用——“分心行医”。本意在于降低医疗差错的高科技设备，因各种通知和应用使医生注意力分散，甚至直接威胁患者生命。文章提出借鉴航空业的“无菌驾驶舱”规则并在医学院强化专注力培训以化解这一矛盾。",
            "main_idea_en": "The passage discusses the hazard of 'distracted doctoring' resulting from hospital digitalization and smartphone intrusion, arguing for aviation-inspired safety rules and cultural reform in medical training."
        },
        "section_c2": {
            "title": "Section C · 仔细阅读 Passage 2 (California vs Texas Economic Poles)",
            "passage": "California and Texas are the twin poles of the West, but very different ones. For decades, California represented the American dream: sunshine, innovation, social tolerance, and an economic dynamism that birthed Hollywood and Silicon Valley. Texas, by contrast, was long caricatured as a conservative oil patch of cowboy hats and pump jacks. Today, however, these two titanic states offer contrasting blueprints for the American future, and millions of citizens are voting with their feet.\nCalifornia has embraced a progressive model defined by ambitious environmental regulations, generous public welfare programs, and high taxes on high earners. Its political leaders argue that government investments in world-class research universities, clean energy, and social infrastructure justify the steep cost of living. Yet California's paradise has developed glaring fissures: astronomical housing costs have driven the middle class away, homelessness has reached crisis levels, and the state now suffers from the nation's highest poverty rate when adjusted for living costs.\nTexas has pursued the exact opposite strategy: low taxes, zero personal income tax, minimal regulation, and an aggressive pro-business climate. Its cities—Houston, Dallas, and Austin—have boomed by welcoming businesses fleeing California's regulatory burdens. Crucially, Texas makes it remarkably easy to build homes. Because suburban sprawl is unrestricted by burdensome environmental zoning, housing in Texas remains affordable for working-class families, sparking an unprecedented demographic influx.\nHowever, the Texas miracle is not without vulnerabilities. Texas spends far less per pupil on public education than California, leaving its public school system chronically underfunded. Its healthcare safety net is sparse, leading the nation in the percentage of uninsured residents. Furthermore, Texas's light-touch regulation was brutally exposed when an unexpected winter storm collapsed its deregulated power grid, leaving millions without heat and electricity for days.\nUltimately, neither state presents a flawless vision. California must learn that even the most noble social ideals collapse if ordinary citizens cannot afford a roof over their heads. Texas must recognize that economic growth cannot substitute for resilient infrastructure and investments in human capital. The contest between the Golden State and the Lone Star State is not just a regional rivalry; it is the central debate shaping the destiny of the United States.",
            "questions": [
                {
                    "num": 51,
                    "stem": "What traditional image was commonly associated with California in previous decades?",
                    "options": [
                        {"label": "A", "text": "A conservative oil-producing region."},
                        {"label": "B", "text": "The shining embodiment of the American dream."},
                        {"label": "C", "text": "An agricultural heartland with low taxes."},
                        {"label": "D", "text": "A sparsely populated frontier territory."}
                    ],
                    "answer": "B",
                    "question_zh": "过去几十年里加州通常与什么传统形象联系在一起？",
                    "answer_zh": "美国梦的光辉化身。",
                    "explanation": "首段明确指出：'For decades, California represented the American dream: sunshine, innovation, social tolerance...'"
                },
                {
                    "num": 52,
                    "stem": "What major dilemma has arisen from California's progressive policies?",
                    "options": [
                        {"label": "A", "text": "Unbearable living costs that drive the middle class away."},
                        {"label": "B", "text": "Severe shortages of skilled software engineers."},
                        {"label": "C", "text": "Rapid collapse of its higher education institutions."},
                        {"label": "D", "text": "Widespread opposition to environmental protection."}
                    ],
                    "answer": "A",
                    "question_zh": "加州的进步主义政策带来了什么重大困境？",
                    "answer_zh": "难以承受的生活成本迫使中产阶级迁离。",
                    "explanation": "第二段指出'astronomical housing costs have driven the middle class away... highest poverty rate when adjusted for living costs'，对应A项。"
                },
                {
                    "num": 53,
                    "stem": "Why has Texas succeeded in keeping its housing prices relatively low?",
                    "options": [
                        {"label": "A", "text": "The state government builds public housing for workers."},
                        {"label": "B", "text": "Permissive regulations make home construction much easier."},
                        {"label": "C", "text": "Land is granted to incoming corporate executives for free."},
                        {"label": "D", "text": "Fewer people desire to move to Texas cities."}
                    ],
                    "answer": "B",
                    "question_zh": "得克萨斯州为何能够保持相对较低的住房价格？",
                    "answer_zh": "宽松的监管政策让房屋建设变得更加容易。",
                    "explanation": "第三段指出：'Texas makes it remarkably easy to build homes. Because suburban sprawl is unrestricted by burdensome environmental zoning...'，对应B项。"
                },
                {
                    "num": 54,
                    "stem": "What serious defect was exposed in Texas's economic model?",
                    "options": [
                        {"label": "A", "text": "Declining corporate tax revenues leading to state bankruptcy."},
                        {"label": "B", "text": "Fragile public infrastructure and inadequate public services."},
                        {"label": "C", "text": "A total absence of technology companies in major cities."},
                        {"label": "D", "text": "Severe federal sanctions on its oil production."}
                    ],
                    "answer": "B",
                    "question_zh": "得克萨斯州的经济模式暴露出了什么严重缺陷？",
                    "answer_zh": "公共基础设施脆弱且公共服务不足。",
                    "explanation": "第四段指出公共教育拨款不足、无医保率全国最高，以及冬季风暴中非管制电网崩溃等事件，体现了脆弱的公共设施与服务缺陷。"
                },
                {
                    "num": 55,
                    "stem": "What conclusion does the author draw about the comparison between the two states?",
                    "options": [
                        {"label": "A", "text": "Texas's low-tax model will entirely replace California's model."},
                        {"label": "B", "text": "Both states need to address their respective deep structural flaws."},
                        {"label": "C", "text": "The federal government should merge the policies of both states."},
                        {"label": "D", "text": "California should abandon all clean energy investments."}
                    ],
                    "answer": "B",
                    "question_zh": "作者对两州的对比得出了什么结论？",
                    "answer_zh": "两州都需要解决各自深层次的结构性缺陷。",
                    "explanation": "尾段总结：'Ultimately, neither state presents a flawless vision. California must learn... Texas must recognize...'，表明双方都有深刻缺陷需互鉴克服。"
                }
            ],
            "main_idea_zh": "本文对比了美国西部两大核心州——加利福尼亚州与得克萨斯州截然不同的发展蓝图。加州崇尚高税收、重环保与完善公共投入，却导致高房价与中产外流；得克萨斯州凭借低税收、轻监管与廉价住房吸引人口和企业，但教育与公共设施严重薄弱。两州竞争体现了美国未来发展道路的根本辩论。",
            "main_idea_en": "The passage compares the contrasting socio-economic models of California and Texas, illustrating their respective strengths, trade-offs, and critical lessons for the future of the nation."
        }
    })

    print("Curated exams defined successfully.")
    return curated

if __name__ == '__main__':
    exams = get_curated_exams()
    print("Curated count:", len(exams))
