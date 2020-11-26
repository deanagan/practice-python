import pytest

from src.three_words import has_3digitless_consecutive


@pytest.mark.parametrize(('input, expected, note'), [
    ("Hello World hello", True, "Hello"),
    ("He is 123 man", False, "123 man"),
    ("1 2 3 4", False, "Digits"),
    ("bla bla bla bla", True, "Bla Bla"),
    ("Hi", False, "Hi"),
])
def test_three_words(input, expected, note):
    assert has_3digitless_consecutive(input) == expected, note
