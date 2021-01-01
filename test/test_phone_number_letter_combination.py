import pytest
from src.phone_number_letter_combination import Solution
from typing import List

@pytest.mark.parametrize('input, expected',[
    ('23', ['ad','ae','af','bd','be','bf','cd','ce','cf']),
    ('', []),
    ('2', ['a', 'b', 'c'])
])
def test_ph_number_letter_combo(input: str, expected: List[str]):
    sut = Solution()
    assert sorted(sut.letter_combinations(input)) == sorted(expected)