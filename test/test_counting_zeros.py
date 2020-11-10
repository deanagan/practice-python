import pytest

from src.counting_zeros import end_zeros, beginning_zeros

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


@pytest.mark.parametrize('input, count', [
    ('100',  0),
    ('001',  2),
    ('100100',  0),
    ('001001',  2),
    ('012345679',  1),
    ('0000',  4),
])
def test_beginning_zeroes(input: str, count: int):
    assert beginning_zeros(input) == count