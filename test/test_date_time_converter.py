import pytest
from src.date_time_converter import date_time, time_converter

@pytest.mark.parametrize("input, expected, note",
    [("01.01.2000 00:00", "1 January 2000 year 0 hours 0 minutes", "Somebody was born") ,
     ("09.05.1945 06:30", "9 May 1945 year 6 hours 30 minutes", "Victory"),
     ("20.11.1990 03:55", "20 November 1990 year 3 hours 55 minutes", "Somebody was born"),
     ("11.04.1812 01:01", "11 April 1812 year 1 hour 1 minute", "Not plural")])
def test_date_time_converter(input, expected, note):
    assert date_time(input) == expected, note



@pytest.mark.parametrize("input, expected",
    [
        ('12:30 p.m.', '12:30'),
        ('9:00 a.m.', '09:00'),
        ('11:15 p.m.', '23:15'),
     ])
def test_date_time_converter(input, expected):
    assert time_converter(input) == expected
