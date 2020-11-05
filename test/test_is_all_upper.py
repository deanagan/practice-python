import pytest

from src.is_all_upper import is_all_upper


@pytest.mark.parametrize('input,expected', [
    ('ALL UPPER', True),
])
def test_is_all_upper(input, expected):
    assert is_all_upper(input) == expected