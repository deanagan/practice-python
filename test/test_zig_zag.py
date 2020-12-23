import pytest

from src.zig_zag import ZigZag


@pytest.mark.parametrize(("input, rows, expected"), [
    ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
    ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI')
])
def test_zig_zag(input, rows, expected):
    sut = ZigZag()
    assert sut.convert(input, rows) == expected