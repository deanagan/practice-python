import pytest

from src.lru_cache import LRUCache
from collections.abc import Iterable
from collections import deque

@pytest.mark.parametrize('capacity, input, expected', [
    (2, [(1,1), (2,2), 1, (3,3), 2, (4,4), 1, 3, 4], [1,-1,-1, 3, 4]),
    (2,[(2,1),(2,2), 2, (1,1), (4,1), 2], [2, -1]),
    (2, [(2,1), (1,1), (2,3), (4,1), 1, 2], [-1, 3])
])
def test_lru_cache(capacity, input, expected):
    sut = LRUCache(capacity)
    get_expectations = deque(expected)
    for args in input:
        if isinstance(args, Iterable):
            sut.put(*args)
        else:
            assert sut.get(args) == get_expectations.popleft()

    assert len(get_expectations) == 0