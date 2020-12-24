import pytest

from src.my_atoi import Solution


@pytest.mark.parametrize('input, expected', [
    ('42', 42),
    ('   -42', -42), # The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.
    ('4193 with words', 4193), # The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.
    ('words and 987', 0), #  The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.
    ('-91283472332', -2147483648),
    ('', 0),
    ('  -0012a42', -12),
    ('-5-', -5),
])
def test_my_atoi(input: str, expected: int):
    sln = Solution()
    assert sln.my_atoi(input) == expected