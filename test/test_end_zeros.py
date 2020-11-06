import pytest

from src.end_zeros import end_zeros

@pytest.mark.parametrize('input, count',[
    (0, 1),
    (1, 0),
    (10, 1),
    (101, 0),
    (245, 0),
    (100100, 2),
])
def test_end_zeroes(input: int, count: int):
    assert end_zeros(input) == count