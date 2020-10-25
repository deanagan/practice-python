import pytest

from src.striped_words import count_stripes

def test_striped_words():
    assert count_stripes("My name is ...") == 3, "All words are striped"
    assert count_stripes("Hello world") == 0, "No one"
    assert count_stripes("A quantity of striped words.") == 1, "Only of"
    assert count_stripes("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"