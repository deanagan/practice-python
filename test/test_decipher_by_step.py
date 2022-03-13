import pytest
from src.decipher_by_step import decipher_by_step

@pytest.mark.parametrize(('word, step, expected'), [
    ("fboaor", 2, ["foo", "bar"]),
    ("fbboaaorz", 3, ["foo", "bar", "baz"]),
    ("sejpgoagkmse", 3, ["spam", "eggs", "joke"]),
])
def test_cut_sentence(word: str, step: int, expected: str):
    assert decipher_by_step(word, step) == expected
