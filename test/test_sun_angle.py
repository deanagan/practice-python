import pytest


from src.sun_angle import sun_angle


def test_sun_angle():
    assert sun_angle("07:00") == 15