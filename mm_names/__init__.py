import json 

with open("data/en2mm.json") as f:
    en2mm_dict = json.load(f)

with open("data/mm2en.json") as f:
    mm2en_dict = json.load(f)