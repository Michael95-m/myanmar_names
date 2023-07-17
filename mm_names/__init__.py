"""
Module Name: mm_names Module
Description: This module loads JSON dictionaries from files.
"""

import json

with open("data/en2mm.json", encoding="utf-8") as f:
    en2mm_dict = json.load(f)

with open("data/mm2en.json", encoding="utf-8") as f:
    mm2en_dict = json.load(f)
