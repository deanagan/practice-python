import pytest
from typing import Iterable
ResultType = Iterable[str]

from src.split_string import split_pairs

@pytest.mark.parametrize('input, expected', [
    ('abcd', ['ab', 'cd']),
    ('abc', ['ab', 'c_']),
    ('abcdf', ['ab', 'cd', 'f_']),
    ('a', ['a_']),
    ('', []),
])
def test_split_string_by_pairs(input: str, expected: ResultType):
    assert list(split_pairs(input)) == expected
