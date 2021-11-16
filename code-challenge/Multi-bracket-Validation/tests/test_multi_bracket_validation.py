from multi_bracket_validation import __version__
import pytest
from multi_bracket_validation.multi_bracket_validation import validate_brackets


def test_version():
    assert __version__ == '0.1.0'

def test_null_string():
    assert validate_brackets('') == True

def test_easy_open_close():
    assert validate_brackets('()') == True

def test_fail_open_close():
    assert validate_brackets('(]') == False
    assert validate_brackets('(}') == False
    assert validate_brackets('{]') == False
    assert validate_brackets('{)') == False
    assert validate_brackets('[)') == False
    assert validate_brackets('[}') == False

def test_three_open_three_close():
    assert validate_brackets('({[]})') == True

def test_open_with_no_close():
    assert validate_brackets('({[]})(') == False

def test_all_open():
    assert validate_brackets('({[') == False

def test_first_open_no_closing():
    assert validate_brackets('(({[[()]]})') == False

def test_with_words():
    assert validate_brackets('(abc[123{lmnop[hello_world(3)[4]]}])') == True

def test_fail_in_middle():
    assert validate_brackets('({[(])})') == False

def test_big_string():
    assert validate_brackets('((((({{{{{[[[[[[(((((([[[[[[{{{((([[[{{{{(((([[[[({[((([[[]]])))]})]]]]))))}}}}]]])))}}}]]]]]]))))))]]]]]]}}}}})))))') == True