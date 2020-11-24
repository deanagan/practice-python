import pytest

from src.determine_order import determine_order


@pytest.mark.parametrize(('input, expected'), [
    (["axton","bxton"], "abxton"),
])
def test_how_deep(input, expected: str):
    assert determine_order(input) == expected
