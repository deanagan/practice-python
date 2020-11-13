import pytest

from src.long_non_repeat import non_repeat, non_repeat_single_pass

@pytest.mark.parametrize(('input, expected'), [
    ('aaaaa', 'a'),
    ('abdjwawk', 'abdjw'),
    ('abcabcffab', 'abcf'),
    ('', '')
])
def test_long_non_repeat(input, expected):
    assert non_repeat(input) == expected


@pytest.mark.parametrize(('input, expected'), [
    ('aaaaa', 'a'),
    ('abdjwawk', 'abdjw'),
    ('abcabcffab', 'abcf'),
    ('', '')
])
def test_long_non_repeat_single_pass(input, expected):
    assert non_repeat_single_pass(input) == expected
