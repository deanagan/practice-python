import pytest

from src.determine_order import determine_order


@pytest.mark.parametrize(('input, expected'), [
    (["jhgedba","jihcba","jigfdca"], "jihgefdcba"),
    (["ghi","abc","def"], "abcdefghi"),
    (["b", "d", "a"], "abd"),
    (["axton","bxton"], "abxton"),
    (["acb", "bd", "zwa"], "zwacbd"),
    (["klm", "kadl", "lsm"], "kadlsm"),
    (["a", "b", "c"], "abc"),
    (["aazzss"], "azs"),
    (["dfg", "frt", "tyg"], "dfrtyg"),
    (["xxxyyz", "yyww", "wwtt", "ttzz"], "xywtz"),
    (["jhgfdba","jihcba","jigedca"], "jihgefdcba"),
])
def test_how_deep(input, expected: str):
    assert determine_order(input) == expected
