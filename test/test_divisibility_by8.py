import pytest
from src.divisibility import divisible_by_8, divisible_by_8_oneliner

@pytest.mark.parametrize(('input, expected'), [
    ('75', False),
    ('61', True),
    ('12123123123123123123123008', True)

])
def test_divisibility_by_8(input: str, expected: bool):
    assert divisible_by_8(input) == expected
    assert divisible_by_8_oneliner(input) == expected
