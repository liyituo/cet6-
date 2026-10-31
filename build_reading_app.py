# -*- coding: utf-8 -*-
"""
CET-6 Reading Comprehension Master Platform Builder (2014 - 2021)
Generates an all-in-one, ultra-polished, offline-first HTML application for CET-6 reading revision.
"""

import json
import os
import re
import sys

def clean_text(text):
    if not text:
        return ""
    text = text.replace('\xa0', ' ').replace('\u3000', ' ')
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def extract_word_bank(wb_text):
    raw_wb = re.findall(r'([A-O])[\)\.\s\uff09\u3001\uFF0E\-\:]+\s*([a-zA-Z\-\']+)', wb_text)
    clean_wb = {}
    for letter, word in raw_wb:
        w = word.strip().lower()
        if w and letter not in clean_wb:
            clean_wb[letter] = w
    return clean_wb

print("Builder initialized.")
