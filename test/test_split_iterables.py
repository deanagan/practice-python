import pytest
from typing import Iterable
ResultType = Iterable[str]

from src.split_string import split_pairs, chunking_by, split_list

@pytest.mark.parametrize('input, expected', [
    ('abcd', ['ab', 'cd']),
    ('abc', ['ab', 'c_']),
    ('abcdf', ['ab', 'cd', 'f_']),
    ('a', ['a_']),
    ('', []),
])
def test_split_string_by_pairs(input: str, expected: ResultType):
    assert list(split_pairs(input)) == expected

@pytest.mark.parametrize('input, expected', [
    ([1, 2, 3, 4, 5, 6], [[1, 2, 3], [4, 5, 6]]),
    ([1, 2, 3], [[1, 2], [3]]),
    ([1, 2, 3, 4, 5], [[1, 2, 3], [4, 5]]),
    ([1], [[1], []]),
    ([], [[], []]),
])
def test_split_list(input, expected):
    assert split_list(input) == expected

@pytest.mark.parametrize('items, size, expected', [
    ([5, 4, 7, 3, 4, 5, 4], 3, [[5, 4, 7], [3, 4, 5], [4]])

])
def test_chunking_by(items, size, expected):
    assert chunking_by(items, size) == expected
