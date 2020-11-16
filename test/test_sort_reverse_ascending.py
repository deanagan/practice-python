import pytest

from src.sort_reverse_ascending import reverse_ascending


@pytest.mark.parametrize('input, expected', [
    ([1, 2, 3, 4, 5],  [5, 4, 3, 2, 1]),
    ([5, 7, 10, 4, 2, 7, 8, 1, 3],  [10, 7, 5, 4, 8, 7, 2, 3, 1]),
    ([5, 4, 3, 2, 1],  [5, 4, 3, 2, 1]),
    ([],  []),
    ([1],  [1]),
    ([1, 1],  [1, 1]),
    ([1, 1, 2],  [1, 2, 1]),
    ([1, 2, 2, 3],  [2, 1, 3, 2]),
])
def test_sort_except_zeros(input, expected):
    assert reverse_ascending(input) == expected