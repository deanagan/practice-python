import pytest
from brackets import are_brackets_valid


def test_are_brackets_valid():
    assert are_brackets_valid("((5+3)*2+1)") == True, "Simple"
    assert are_brackets_valid("{[(3+1)+2]+}") == True, "Different types"
    assert are_brackets_valid("(3+{1-1)}") == False, ") is alone inside {}"
    assert are_brackets_valid("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert are_brackets_valid("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert are_brackets_valid("2+3") == True, "No brackets, no problem"
    assert are_brackets_valid("(3+{1-1)}") == False, "Mismatching brackets"
    assert are_brackets_valid("(((([[[{{{3}}}]]]]))))") == False, "Mismatching"
    assert are_brackets_valid("(((1+(1+1))))]") == False, "Extra closing at the end"
