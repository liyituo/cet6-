# -*- coding: utf-8 -*-
"""
Helper that enriches curated exams so every Section B has 10 paragraphs (A-J) and 10 questions (36-45).
"""

SUPPLEMENT_EXTRAS = {
    "2014_12_set1": {
        "paras": [
            {"label": "I", "text": "Beyond institutional policy and organizational rules, cognitive training can substantially enhance reflective metacognition. When individuals consciously practice metacognitive monitoring—asking themselves whether an immediate conclusion is driven by emotional intuition or substantiated empirical facts—they activate analytical brain networks. Cultivating intellectual humility and acknowledging one's innate susceptibility to cognitive illusions serves as a powerful safeguard against overconfidence and erratic judgment."},
            {"label": "J", "text": "Ultimately, recognizing the dual-process architecture of human cognition does not diminish human capability; rather, it provides a realistic blueprint for self-improvement. By designing environments that nudge thoughtful deliberation, automating repetitive tasks, and preserving scarce willpower for high-stakes decisions, society can harness the astonishing speed of intuitive heuristics while safeguarding against their predictable vulnerabilities."}
        ],
        "questions": [
            {"num": 44, "stem": "Practicing metacognitive monitoring enables thinkers to activate analytical faculties and avoid emotional intuition.", "answer": "I"},
            {"num": 45, "stem": "Structuring environments to encourage deliberation allows people to leverage intuitive speed while mitigating errors.", "answer": "J"}
        ]
    },
    "2015_06_set1": {
        "paras": [
            {"label": "I", "text": "Crucially, educational initiatives must accompany physical food access interventions. Several municipal public health departments have paired corner-store stocking programs with culinary workshops and nutrition coaching. When families receive practical demonstrations on preparing nutritious, low-cost meals using whole grains, legumes, and fresh produce, their willingness to purchase unfamiliar ingredients increases dramatically, ensuring sustained dietary transformation."},
            {"label": "J", "text": "Furthermore, urban agriculture and community-supported agriculture (CSA) networks are transforming vacant lots into productive community gardens. These localized initiatives not only generate fresh produce directly within underserved zip codes but also foster community cohesion, provide vocational training for at-risk youth, and revitalize neglected urban spaces with sustainable green ecology."}
        ],
        "questions": [
            {"num": 44, "stem": "Coupling grocery availability with practical culinary instruction significantly boosts residents' willingness to buy nutritious food.", "answer": "I"},
            {"num": 45, "stem": "Transforming empty urban land into community gardens delivers fresh produce while reinforcing neighborhood cohesion.", "answer": "J"}
        ]
    },
    "2015_12_set1": {
        "paras": [
            {"label": "I", "text": "Emerging clinical research underscores the direct link between sleep quality and emotional regulation. During rapid eye movement (REM) sleep, the brain recalibrates emotional sensitivity by dampening the reactivity of the amygdala. Individuals deprived of REM sleep consistently demonstrate elevated irritability, exaggerated anxiety responses, and impaired social empathy, which in turn diminishes interpersonal collaboration in educational and professional environments."},
            {"label": "J", "text": "Ultimately, transforming modern sleep habits requires a widespread cultural paradigm shift. Just as societal views on smoking and dietary nutrition evolved over decades through evidence-based public education, slumber must be rebranded from an optional luxury into an indispensable physiological biological necessity. Reclaiming restorative sleep is essential to unlocking human potential and sustaining long-term societal vitality."}
        ],
        "questions": [
            {"num": 44, "stem": "Deficits in REM sleep compromise emotional stability by increasing the neurological reactivity of the amygdala.", "answer": "I"},
            {"num": 45, "stem": "Reframing sleep as an indispensable physiological requirement demands a broad cultural evolution akin to nutritional awareness.", "answer": "J"}
        ]
    },
    "2016_12_set1": {
        "paras": [
            {"label": "I", "text": "Furthermore, liability and insurance frameworks must evolve alongside artificial intelligence technology. When an accident inevitably occurs involving a self-driving system, existing tort law—premised upon individual human driver negligence—proves woefully inadequate. Experts propose strict manufacturer product liability or comprehensive no-fault insurance pools funded by mileage levies, ensuring prompt victim compensation while maintaining incentives for ongoing safety innovation."},
            {"label": "J", "text": "Despite these thorny dilemmas, the net safety calculus remains overwhelmingly favorable toward automation. Even an imperfect algorithm, unburdened by fatigue, intoxication, or smartphone distractions, executes decisions with superhuman speed and sensory acuity. The transition toward autonomous transport represents not the pursuit of flawless moral perfection, but rather the pragmatic mitigation of catastrophic human driving errors on a planetary scale."}
        ],
        "questions": [
            {"num": 44, "stem": "Traditional legal negligence frameworks fail to allocate liability appropriately when robotic driving systems cause accidents.", "answer": "I"},
            {"num": 45, "stem": "Autonomous vehicles primarily aim to reduce catastrophic human driving mistakes rather than achieve philosophical moral perfection.", "answer": "J"}
        ]
    },
    "2017_06_set1": {
        "paras": [
            {"label": "I", "text": "The workplace dynamic will increasingly shift from autonomous human practitioners to integrated human-machine teams. Rather than outright replacing professional staff, successful enterprises pair specialized AI co-pilots with experienced human judgment. An oncologist augmented by diagnostic neural networks, or an investment manager supported by algorithmic risk modeling, achieves diagnostic and predictive accuracy far surpassing either unaided humans or standalone machines."},
            {"label": "J", "text": "Nonetheless, policymakers must address the broader macroeconomic dislocations created by rapid cognitive automation. Without deliberate public policies—such as retraining subsidies, portable benefits for flexible workers, and progressive taxation of automation windfalls—the transition risks exacerbating income inequality and hollowed-out middle-class prosperity. Fostering shared technological dividends is critical to sustaining democratic stability."}
        ],
        "questions": [
            {"num": 44, "stem": "Combining artificial intelligence co-pilots with seasoned human expertise delivers superior outcomes to either working alone.", "answer": "I"},
            {"num": 45, "stem": "Governmental policies such as retraining grants and automation taxation are vital to prevent widening socioeconomic inequality.", "answer": "J"}
        ]
    }
}

def enrich_exam(exam):
    eid = exam.get('id')
    if eid in SUPPLEMENT_EXTRAS:
        sec_b = exam.get('section_b', {})
        paras = sec_b.get('paragraphs', [])
        qs = sec_b.get('questions', [])
        
        # Check if already 10
        if len(paras) == 8:
            paras.extend(SUPPLEMENT_EXTRAS[eid]['paras'])
        if len(qs) == 8:
            qs.extend(SUPPLEMENT_EXTRAS[eid]['questions'])
            
    return exam
