import pytest

from src.sort_except_zeros import sort_except_zeros


@pytest.mark.parametrize('input, expected', [
    ([5, 3, 0, 0, 4, 1, 4, 0, 7],  [1, 3, 0, 0, 4, 4, 5, 0, 7]),
    ([0, 2, 3, 1, 0, 4, 5],  [0, 1, 2, 3, 0, 4, 5]),
    ([0, 0, 0, 1, 0],  [0, 0, 0, 1, 0]),
    ([4, 5, 3, 1, 1],  [1, 1, 3, 4, 5]),
    ([0, 0],  [0, 0]),
])
def test_sort_except_zeros(input, expected):
    assert list(sort_except_zeros(input)) == expected