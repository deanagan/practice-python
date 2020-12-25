import pytest
from typing import List
from src.container_with_most_water import Solution


@pytest.mark.parametrize('height, result',[
    ([1, 1], 1),
    ([4,3,2,1,4], 16),
    ([1,2,1], 2),
    ([2,3,4,5,18,17,6], 17)
])
def test_container_with_most_water(height: List[int], result: int):
    sut = Solution()
    assert sut.max_area(height) == result