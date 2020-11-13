# Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times
# they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
# Input: Iterable
# Output: Iterable
import pytest
from src.sort_array_by_element_frequency import frequency_sort, asc_frequency_sort

@pytest.mark.parametrize(('input, expected'), [
    ([4, 6, 2, 2, 6, 4, 4, 4],  [4, 4, 4, 4, 6, 6, 2, 2]),
    (['bob', 'bob', 'carl', 'alex', 'bob'],  ['bob', 'bob', 'bob', 'carl', 'alex']),
    ([17, 99, 42],  [17, 99, 42]),
    ([],  []),
    ([1],  [1]),
])
def test_frequency_sort(input, expected):
    assert list(frequency_sort(input)) == expected


@pytest.mark.parametrize(('input, expected, note'), [
    ([1, 2, 3, 4, 5],  [1, 2, 3, 4, 5], "Already sorted"),
    ([3, 4, 11, 13, 11, 4, 4, 7, 3],  [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"),
    ([99, 99, 55, 55, 21, 21, 10, 10],  [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"),
])
def test_asc_frequency_sort(input, expected, note):
    assert asc_frequency_sort(input) == expected, note