from mm_names.syl import syllable
from mm_names import en2mm_dict, mm2en_dict


def mm2en(mm_names: str):

    return ' '.join([mm2en_dict.get(syl, syl) for syl in syllable(mm_names).split()])

def en2mm(eng_names: str):

    return ' '.join([en2mm_dict.get(eng.lower(), eng) for eng in eng_names.split()])