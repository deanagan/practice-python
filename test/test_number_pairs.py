import pytest

from src.number_pairs import NumberPairs

def test_number_pairs():
    np = NumberPairs([5, 25, 45, 15])
    assert np.count_divisibility_pairs(30) == 2

    np = NumberPairs([30,30,30])
    assert np.count_divisibility_pairs(30) == 3