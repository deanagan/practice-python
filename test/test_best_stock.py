import pytest

from src.best_stock import best_stock

@pytest.mark.parametrize('input, expected', [
    ({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}, "ATX"),
    ({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}, "TASI")
])
def test_best_stock(input: dict, expected: str):
    assert best_stock(input) == expected
