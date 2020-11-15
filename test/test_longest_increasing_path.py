import pytest

from src.longest_increasing_path import longest_increasing_path

@pytest.mark.parametrize(('input, expected'), [
    ([[9,9,4], [6,6,8], [2,1,1]], 4),
    ([[3,4,5], [3,2,6], [2,2,1]], 4),
    ([], 0),
])
def test_long_non_repeat(input, expected):
    assert longest_increasing_path(input) == expected
