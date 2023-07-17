## This syllable segmentation code is from sayar ye kyaw thu's github
## I changed a little bit

"""
Module Name: syl Module
Description: This module segments a string in Burmese into syllables.
"""

import re


class SylBreak:
    # pylint: disable=too-few-public-methods
    """
    A class for segmentation of a string in burmese into syllables
    """

    def __init__(self):
        self.my_consonant = r"က-အ"
        self.en_char = r"a-zA-Z0-9"
        self.other_char = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
        self.ss_symbol = r"္"
        self.a_thet = r"်"
        self.break_pattern = re.compile(
            rf"((?<!{self.ss_symbol})[{self.my_consonant}](?![{self.a_thet}{self.ss_symbol}])|"
            "[{self.en_char}{self.other_char}])",
            re.UNICODE,
        )

    def syllable(self, line: str, delimiter: str = " ") -> str:
        """
        Segment a string in Burmese into syllables
        Args:
            line (str): a string in Burmese
            delimiter (str, optional): string to join different syllables. Defaults to " ".

        Returns:
            str: a string in Burmese in syllable segmentation
        """
        return self.break_pattern.sub(delimiter + r"\1", line).strip()
