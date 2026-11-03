import pytest
import sys
import os
import importlib  

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../codes')))

count_words_module = importlib.import_module("32_count_words")
count_words = count_words_module.count_words

def test_count_words_empty():
    assert count_words("") == 0

def test_count_words_single():
    assert count_words("Hello") == 1

def test_count_words_multiple():
    assert count_words("Hello world, this is a test.") == 6

def test_count_words_whitespace():
    assert count_words("   Hello   world   ") == 2