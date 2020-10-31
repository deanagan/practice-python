import pytest


from src.sun_angle import sun_angle


def test_sun_angle():
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"