"""
Module Name: test_syl Module
Description: This module tests the methods inside SylBreak Class from syl module
             from mm_names
"""

from mm_names.syl import SylBreak


def test_syllable():
    """
    Test the syllable() method of the SylBreak class.

    This test case ensures that the syllable() method correctly segments a string in
    Burmese into syllables.
    """
    syl_break = SylBreak()

    assert syl_break.syllable("မင်းခန့်မောင်မောင်") == "မင်း ခန့် မောင် မောင်"
