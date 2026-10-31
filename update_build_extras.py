# -*- coding: utf-8 -*-
"""
Update build_reading_platform.py to add paragraphs I & J and Q44 & Q45 to 2016_06_set1, 2017_12_set1, and 2021_12_set1.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('build_reading_platform.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. 2016_06_set1
target_16 = '''                {"label": "H", "text": "Ultimately, high-speed rail functions not as an isolated silver bullet, but as one integrated component of thoughtful territorial planning. Its enduring economic returns materialize when paired with pedestrian-oriented downtown terminal districts, seamless multimodal local transit connections, and land-use regulations that encourage compact mixed-use development. When cities align their spatial planning with high-speed mobility corridors, trains become powerful catalysts for sustainable, low-carbon regional prosperity."}
            ],
            "questions": [
                {"num": 36, "stem": "High-speed rail allows peripheral municipalities to attract talent and enterprise while mitigating real estate pressure on capitals.", "answer": "C"},
                {"num": 37, "stem": "High-speed electric rail emits dramatically fewer greenhouse gases per passenger-kilometer than commercial jetliner travel.", "answer": "E"},
                {"num": 38, "stem": "Constructing high-speed railway networks demands astronomical capital expenditures and prolonged development timelines.", "answer": "D"},
                {"num": 39, "stem": "Modern high-speed transit technology effectively shrinks geographic distance, making intercity daily commuting feasible.", "answer": "A"},
                {"num": 40, "stem": "Subordinate regional towns occasionally face talent drain when bullet trains link them closely to dominating mega-cities.", "answer": "G"},
                {"num": 41, "stem": "In sprawling automotive nations like the US, rail terminals often struggle due to poor last-mile local transit integration.", "answer": "F"},
                {"num": 42, "stem": "China established the world's most expansive high-speed railway system within a span of less than twenty years.", "answer": "B"},
                {"num": 43, "stem": "To deliver enduring economic dividends, high-speed transit requires thoughtful city planning and sufficient population density.", "answer": "H"}
            ]'''

new_16 = '''                {"label": "H", "text": "Ultimately, high-speed rail functions not as an isolated silver bullet, but as one integrated component of thoughtful territorial planning. Its enduring economic returns materialize when paired with pedestrian-oriented downtown terminal districts, seamless multimodal local transit connections, and land-use regulations that encourage compact mixed-use development. When cities align their spatial planning with high-speed mobility corridors, trains become powerful catalysts for sustainable, low-carbon regional prosperity."},
                {"label": "I", "text": "Economic geography demonstrates that high-speed rail fundamentally restructures tourism and hospitality sectors. Travelers frequently undertake impromptu weekend excursions to cultural hubs situated several hundred kilometers away, injecting consumer spending into regional economies that formerly relied solely on seasonal car visitors. Cultural institutions, regional festivals, and hospitality venues enjoy sustained attendance throughout the calendar year."},
                {"label": "J", "text": "Crucially, the ongoing electrification of high-speed rail networks directly advances national climate decarbonization mandates. As national electrical grids transition progressively from fossil fuel generation to renewable wind, solar, and hydroelectric resources, the operational footprint of passenger rail approaches near-zero emissions, establishing trains as the green backbone of twenty-first-century continental passenger transport."}
            ],
            "questions": [
                {"num": 36, "stem": "High-speed rail allows peripheral municipalities to attract talent and enterprise while mitigating real estate pressure on capitals.", "answer": "C"},
                {"num": 37, "stem": "High-speed electric rail emits dramatically fewer greenhouse gases per passenger-kilometer than commercial jetliner travel.", "answer": "E"},
                {"num": 38, "stem": "Constructing high-speed railway networks demands astronomical capital expenditures and prolonged development timelines.", "answer": "D"},
                {"num": 39, "stem": "Modern high-speed transit technology effectively shrinks geographic distance, making intercity daily commuting feasible.", "answer": "A"},
                {"num": 40, "stem": "Subordinate regional towns occasionally face talent drain when bullet trains link them closely to dominating mega-cities.", "answer": "G"},
                {"num": 41, "stem": "In sprawling automotive nations like the US, rail terminals often struggle due to poor last-mile local transit integration.", "answer": "F"},
                {"num": 42, "stem": "China established the world's most expansive high-speed railway system within a span of less than twenty years.", "answer": "B"},
                {"num": 43, "stem": "To deliver enduring economic dividends, high-speed transit requires thoughtful city planning and sufficient population density.", "answer": "H"},
                {"num": 44, "stem": "Regional hospitality and cultural industries thrive as high-speed trains make short-term weekend excursions seamless.", "answer": "I"},
                {"num": 45, "stem": "Powering electric rail networks with renewable energy sources makes passenger trains virtually zero-emission transport.", "answer": "J"}
            ]'''
text = text.replace(target_16, new_16)

# 2. 2017_12_set1
target_17 = '''                {"label": "H", "text": "Progress requires aligning academic career incentives with open scientific practices. Universities and tenure review boards are gradually beginning to evaluate data sharing, reproducible workflows, and collaborative tools alongside traditional citation counts. Digital repositories provide permanent Digital Object Identifiers (DOIs) for standalone datasets, allowing authors to receive formal academic citation credit when colleagues build upon their empirical groundwork. Science flourishes most rapidly when built upon shared, transparent foundations."}
            ],
            "questions": [
                {"num": 36, "stem": "A renowned medical journal editorial stirred controversy by warning against unscrupulous secondary data analysts.", "answer": "E"},
                {"num": 37, "stem": "A corporate biomedical venture failed to replicate the majority of landmark cancer research papers.", "answer": "A"},
                {"num": 38, "stem": "Rigorous data curation and standardized metadata documentation require significant investments of uncompensated scholarly time.", "answer": "D"},
                {"num": 39, "stem": "Academic hiring and tenure criteria must formally reward dataset curation alongside journal publication.", "answer": "H"},
                {"num": 40, "stem": "Mandatory data deposition policies introduced by prestigious publishers aim to restore empirical trust.", "answer": "C"},
                {"num": 41, "stem": "Scientists harbor legitimate fears that unvetted public access to raw data could enable competitive rivals to steal their ideas.", "answer": "G"},
                {"num": 42, "stem": "Prior to open data mandates, only a tiny fraction of academic authors voluntarily shared underlying raw data upon inquiry.", "answer": "B"},
                {"num": 43, "stem": "Critics labeled researchers who analyze existing public datasets without conducting fieldwork as parasitic scholars.", "answer": "F"}
            ]'''

new_17 = '''                {"label": "H", "text": "Progress requires aligning academic career incentives with open scientific practices. Universities and tenure review boards are gradually beginning to evaluate data sharing, reproducible workflows, and collaborative tools alongside traditional citation counts. Digital repositories provide permanent Digital Object Identifiers (DOIs) for standalone datasets, allowing authors to receive formal academic citation credit when colleagues build upon their empirical groundwork. Science flourishes most rapidly when built upon shared, transparent foundations."},
                {"label": "I", "text": "Open data also accelerates machine-learning discoveries across computational biology and climate modeling. When thousands of independently gathered datasets are harmonized into open repositories, deep-learning models can uncover subtle predictive patterns that were invisible within smaller, siloed studies. This algorithmic cross-fertilization enables breakthrough discoveries in protein folding, drug discovery, and atmospheric forecasting."},
                {"label": "J", "text": "Ultimately, democratizing access to raw experimental data fosters public trust in the scientific enterprise. When controversial scientific claims can be independently scrutinized, analyzed, and verified by external citizen scientists and independent watchdog organizations, scientific inquiry defends itself against charges of elite bias or concealed corporate manipulation, reinforcing the empirical bedrock of enlightened society."}
            ],
            "questions": [
                {"num": 36, "stem": "A renowned medical journal editorial stirred controversy by warning against unscrupulous secondary data analysts.", "answer": "E"},
                {"num": 37, "stem": "A corporate biomedical venture failed to replicate the majority of landmark cancer research papers.", "answer": "A"},
                {"num": 38, "stem": "Rigorous data curation and standardized metadata documentation require significant investments of uncompensated scholarly time.", "answer": "D"},
                {"num": 39, "stem": "Academic hiring and tenure criteria must formally reward dataset curation alongside journal publication.", "answer": "H"},
                {"num": 40, "stem": "Mandatory data deposition policies introduced by prestigious publishers aim to restore empirical trust.", "answer": "C"},
                {"num": 41, "stem": "Scientists harbor legitimate fears that unvetted public access to raw data could enable competitive rivals to steal their ideas.", "answer": "G"},
                {"num": 42, "stem": "Prior to open data mandates, only a tiny fraction of academic authors voluntarily shared underlying raw data upon inquiry.", "answer": "B"},
                {"num": 43, "stem": "Critics labeled researchers who analyze existing public datasets without conducting fieldwork as parasitic scholars.", "answer": "F"},
                {"num": 44, "stem": "Aggregating publicly shared scientific datasets allows artificial intelligence systems to identify complex patterns.", "answer": "I"},
                {"num": 45, "stem": "Public availability of experimental data strengthens civic confidence in science against accusations of bias.", "answer": "J"}
            ]'''
text = text.replace(target_17, new_17)

# 3. 2021_12_set1
target_21 = '''                {"label": "H", "text": "Far from spelling the death of the city, the shift toward flexible working represents an opportunity for urban revitalization. Freed from the sole identity of commuter dormitories and office hives, cities can transform into vibrant ecosystems centered around culture, recreation, green public spaces, and diverse housing. Urban resilience has weathered pandemics, wars, and industrial transitions for millennia; flexible work is merely the catalyst for the city's next creative evolution."}
            ],
            "questions": [
                {"num": 36, "stem": "Commuter rail systems and metropolitan transit agencies experienced catastrophic decreases in fare revenues.", "answer": "E"},
                {"num": 37, "stem": "The transition to hybrid telework proved that knowledge workers could remain exceptionally productive outside corporate towers.", "answer": "A"},
                {"num": 38, "stem": "Urban downtown districts face serious fiscal shortfalls as commercial real estate values and municipal tax receipts decline.", "answer": "D"},
                {"num": 39, "stem": "Downtown hospitality workers, cleaning staff, and baristas faced severe economic shocks when corporate commuters vanished.", "answer": "F"},
                {"num": 40, "stem": "Teleworking privileges created deep societal divisions between desk-bound professionals and on-site frontline service staff.", "answer": "G"},
                {"num": 41, "stem": "Commercial real estate owners scrambled to renovate older buildings with state-of-the-art air filtration and collaborative spaces.", "answer": "B"},
                {"num": 42, "stem": "The 'Donut Effect' describes an exodus of residents from central business cores toward spacious suburban territories.", "answer": "C"},
                {"num": 43, "stem": "Rather than killing urban centers, remote flexibility gives people greater freedom and drives cities to reinvent themselves.", "answer": "H"}
            ]'''

new_21 = '''                {"label": "H", "text": "Far from spelling the death of the city, the shift toward flexible working represents an opportunity for urban revitalization. Freed from the sole identity of commuter dormitories and office hives, cities can transform into vibrant ecosystems centered around culture, recreation, green public spaces, and diverse housing. Urban resilience has weathered pandemics, wars, and industrial transitions for millennia; flexible work is merely the catalyst for the city's next creative evolution."},
                {"label": "I", "text": "Simultaneously, secondary and tertiary cities are enjoying unprecedented economic vitality. Formerly struggling rust-belt municipalities and scenic rural mountain towns have launched incentive programs offering cash grants and co-working subsidies to attract footloose telecommuters. These influxes of educated, well-paid professionals inject valuable purchasing power into local downtown businesses, revitalizing historic main streets across the countryside."},
                {"label": "J", "text": "Nevertheless, local municipal governments must deliberately manage the side effects of remote-worker migration. Rapid influxes of high-earning teleworkers into smaller rural communities often drive up residential real estate prices and displace long-term working-class locals. Equitable urban-regional development requires targeted investments in affordable housing and protective zoning ordinances alongside telework incentives."}
            ],
            "questions": [
                {"num": 36, "stem": "Commuter rail systems and metropolitan transit agencies experienced catastrophic decreases in fare revenues.", "answer": "E"},
                {"num": 37, "stem": "The transition to hybrid telework proved that knowledge workers could remain exceptionally productive outside corporate towers.", "answer": "A"},
                {"num": 38, "stem": "Urban downtown districts face serious fiscal shortfalls as commercial real estate values and municipal tax receipts decline.", "answer": "D"},
                {"num": 39, "stem": "Downtown hospitality workers, cleaning staff, and baristas faced severe economic shocks when corporate commuters vanished.", "answer": "F"},
                {"num": 40, "stem": "Teleworking privileges created deep societal divisions between desk-bound professionals and on-site frontline service staff.", "answer": "G"},
                {"num": 41, "stem": "Commercial real estate owners scrambled to renovate older buildings with state-of-the-art air filtration and collaborative spaces.", "answer": "B"},
                {"num": 42, "stem": "The 'Donut Effect' describes an exodus of residents from central business cores toward spacious suburban territories.", "answer": "C"},
                {"num": 43, "stem": "Rather than killing urban centers, remote flexibility gives people greater freedom and drives cities to reinvent themselves.", "answer": "H"},
                {"num": 44, "stem": "Smaller secondary cities and rural towns attract well-paid telecommuters through targeted financial subsidies.", "answer": "I"},
                {"num": 45, "stem": "Rapid migration of remote workers into small towns risks driving up local housing costs and displacing residents.", "answer": "J"}
            ]'''
text = text.replace(target_21, new_21)

with open('build_reading_platform.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("build_reading_platform.py updated.")
