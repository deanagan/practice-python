import pytest

from src.iterable_depth import how_deep

@pytest.mark.parametrize('input, count',[
    ((1, 2, 3), 1),
    ((1, 2, (3,)), 2),
    ((1, 2, (3, (4,))), 3),
    ((), 1),
    (((),), 2),
    ((((),),), 3),
    ((1, (2,), (3,)), 2),
    ((1, ((),), (3,)), 3),
])
def test_end_zeroes(input: int, count: int):
    assert how_deep(input) == count
