import pytest
from src.word_order import words_order

@pytest.mark.parametrize(('text, words, expected'), [
    ('hi world im here', ['world', 'here'], True),
    ('hi world im here', ['here', 'world'], False),
    ('hi world im here', ['world'], True),
    ('hi world im here', ['world', 'here', 'hi'], False),
    ('hi world im here', ['world', 'im', 'here'], True),
    ('hi world im here', ['world', 'hi', 'here'], False),
    ('hi world im here', ['world', 'world'], False),
    ('hi world im here', ['country', 'world'], False),
    ('hi world im here', ['wo', 'rld'], False),
    ('', ['world', 'here'], False),
    ("hi world world im here", ["world","world"], False)
])
def test_word_order(text: str, words: list, expected: bool):
    assert words_order(text, words) == expected