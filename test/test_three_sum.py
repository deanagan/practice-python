import pytest
from src.three_sum import Solution
from typing import List

@pytest.mark.parametrize('input, expected', [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0], []),
    ([], []),
    ([0,0,0], [[0,0,0]])
])
def test_three_sum(input: List[int], expected: List[List[int]]):
    sut = Solution()
    assert sorted(sut.three_sum(input)) == sorted(expected)
