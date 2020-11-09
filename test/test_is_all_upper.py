import pytest

from src.is_all_upper import is_all_upper, is_all_upper_or_empty


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


@pytest.mark.parametrize('input,expected', [
    ('ALL UPPER', True),
    ('all lower', False),
    ('mixed UPPER and lower', False),
    ('', True),
    ('     ', True),
    ('123', True) # all upper or empty of upper case characters
])
def test_is_all_upper_or_empty(input, expected):
    assert expected == is_all_upper_or_empty(input)