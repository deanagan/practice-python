import pytest

from src.morse_code import morse_decoder



@pytest.mark.parametrize('input, expected',
    [("... --- -- .   - . -..- -", "Some text"),
    ("..--- ----- .---- ---..", "2018"),
    (".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--", "It was a good day")])
def test_morse_decoder(input, expected):
    assert morse_decoder(input) == expected
