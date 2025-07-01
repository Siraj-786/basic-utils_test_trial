# tests/test_core.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'basic_utils')))

from core import reverse_string, is_even, maximum, list_sum

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("") == ""
    assert reverse_string("") == ""

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False

def test_maximum():
    assert maximum(5, 9) == 9
    assert maximum(7, 7) == 7

def test_list_sum():
    assert list_sum([1, 2, 3]) == 6
    assert list_sum([]) == 0


