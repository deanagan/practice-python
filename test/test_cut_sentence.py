import pytest
from src.cut_sentence import cut_sentence

@pytest.mark.parametrize(('line, length, expected'), [
    ("Hi my name is Alex", 4, "Hi..."),
    ("Hi my name is Alex", 8, "Hi my..."),
    ("Hi my name is Alex", 18, "Hi my name is Alex"),
    ("Hi my name is Alex", 20, "Hi my name is Alex"),
    ("Hi my name is Alex", 11, "Hi my name..."),
])
def test_cut_sentence(line: str, length: int, expected: str):
    assert cut_sentence(line, length) == expected
