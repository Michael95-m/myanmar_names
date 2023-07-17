"""
Module Name: test_convert Module
Description: This module tests the methods inside Converter Class from convert module 
             from mm_names
"""

from mm_names.convert import Converter


def test_mm2en():
    """
    Test the mm2en() method of the Converter class.

    This test case ensures that the mm2en() method correctly converts Burmese names
    to English names using the Converter class.
    """
    converter = Converter()
    assert converter.mm2en("မင်းခန့်မောင်မောင်") == "min khant maung maung"


def test_en2mm():
    """
    Test the en2mm() method of the Converter class.

    This test case ensures that the en2mm() method correctly converts English names
    to Burmese names using the Converter class.
    """
    converter = Converter()
    assert converter.en2mm("Min Khant Maung Maung") == "မင်း ခန့် မောင် မောင်"
    assert converter.en2mm("min khant maung maung") == "မင်း ခန့် မောင် မောင်"
