import pytest

from src.iterable_depth import how_deep, how_deep_forgiveness, how_deep_permission

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
def test_how_deep(input: int, count: int):
    assert how_deep(input) == count
    assert how_deep_forgiveness(input) == count
    assert how_deep_permission(input) == count
