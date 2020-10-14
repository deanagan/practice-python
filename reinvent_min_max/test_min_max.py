import pytest
from min_max import mymin, mymax


def test_min_max():

    assert mymax(3, 2) == 3
    # mymin(3, 2) == 2
    # mymax([1, 2, 0, 3, 4]) == 4
    # mymin("hello") == "e"
    # mymax(2.2, 5.6, 5.9, key=int) == 5.6
    # mymin([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
