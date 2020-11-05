import pytest

from src.is_all_upper import is_all_upper


@pytest.mark.parametrize('input,expected', [
    ('ALL UPPER', True),
    ('all lower', False),
    ('mixed UPPER and lower', False),
    ('', False),
    ('   ', False),
    ('123', False)
])
def test_is_all_upper(input, expected):
    assert expected == is_all_upper(input)