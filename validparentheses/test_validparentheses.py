import pytest
from validparentheses import is_valid

def test_validparentheses():
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True
    assert is_valid("]") == False
    assert is_valid("(])") == False
    assert is_valid("){") == False
