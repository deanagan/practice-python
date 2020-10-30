import pytest

from src.backward_string_by_word import backward_string_by_word

def test_backward_string_by_word():
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'