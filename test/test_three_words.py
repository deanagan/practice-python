import pytest

from src.three_words import has_3digitless_consecutive

def test_three_words():

    assert has_3digitless_consecutive("Hello World hello") == True, "Hello"
    assert has_3digitless_consecutive("He is 123 man") == False, "123 man"
    assert has_3digitless_consecutive("1 2 3 4") == False, "Digits"
    assert has_3digitless_consecutive("bla bla bla bla") == True, "Bla Bla"
    assert has_3digitless_consecutive("Hi") == False, "Hi"
