import pytest

from src.roman_numerals import Solution


@pytest.mark.parametrize('input, expected', [
    (3, 'III'),
    (4, 'IV'),
    (9, 'IX'),
    (58, 'LVIII'),
    (1994, 'MCMXCIV')
])
def test_roman_numerals(input: int, expected: str):
    sut = Solution()
    assert sut.int_to_roman(input) == expected