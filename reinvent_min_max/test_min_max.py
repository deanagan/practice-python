import pytest
from min_max import mymin, mymax


def test_min_max():

    assert mymax(3, 2) == 3
    assert mymin(3, 2) == 2
    assert mymax([1, 2, 0, 3, 4]) == 4
    assert mymin("hello") == "e"
    assert mymax(2.2, 5.6, 5.9, key=int) == 5.6
    assert mymin([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
