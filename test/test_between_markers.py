import pytest
from src.between_markers import between_markers

def test_between_markers():
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
