import json, re

raw_wb_text = """
A)chronicles I）perfect
B)complete J) precision
C) established K) puzzled
D) fascinates L）remnants
E)hypothesis M）removed
F)maximum N) revelations
G) momentum O）slightly
H) mysteriously
"""

matches = re.findall(r'([A-O])[\)\.\s\uff09\u3001\uFF0E\-\:]+\s*([a-zA-Z\-\']+)', raw_wb_text)
wb = {k: v.strip() for k, v in matches}
print(f"Total words: {len(wb)}")
print(wb)
