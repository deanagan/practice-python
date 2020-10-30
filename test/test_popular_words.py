import pytest

from src.popular_words import popular_words

def test_popular_words():
    assert popular_words('''
            When I was One
            I had just begun
            When I was Two
            I was nearly new
            ''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }