import pytest

from src.replace_first import replace_first_np


@pytest.mark.parametrize('input, expected', [
    ([1, 2, 3, 4] , [2, 3, 4, 1]),
    ([1] , [1]),
    ([] , []),
])
def test_replace_first(input, expected):
    assert expected == replace_first_np(input)