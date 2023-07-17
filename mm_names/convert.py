"""
Module Name: convert
Description: This module provides function to convert Myanmar names to English and vice versa.
"""

from mm_names import en2mm_dict, mm2en_dict
from mm_names.syl import SylBreak


class Converter:
    """
    A class for converting names between Burmese and English using pre-built dictionaries.
    """

    def __init__(self):
        self.syl_break = SylBreak()

    def mm2en(self, mm_names: str) -> str:
        """
        Convert Burmese names to English presentation by using a pre-built json file.

        Args:
            mm_names (str): a string in Burmese (should be Burmese name)

        Returns:
            str: a string in English
        """
        eng_words = []
        syllables = self.syl_break.syllable(mm_names).split()

        for syl in syllables:
            eng_word = mm2en_dict.get(syl, syl)
            eng_words.append(eng_word)

        eng_name = " ".join(eng_words)

        return eng_name

    def en2mm(self, eng_names: str) -> str:
        """
        Convert Burmese name in English to Burmese by using a pre-built json file.
        Args:
            eng_names (str): a string in English (should be Burmese name in English)

        Returns:
            str: a string in Burmese
        """
        mm_syls = []

        for eng in eng_names.split():
            mm_syl = en2mm_dict.get(eng.lower(), eng)
            mm_syls.append(mm_syl)

        return " ".join(mm_syls)
