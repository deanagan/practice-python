'''
The function should recognise if a subject line is stressful. A stressful subject line means
that all letters are in uppercase, and/or ends by at least 3 exclamation marks, and/or contains at
least one of the following “red” words:
    "help",
    "asap",
    "urgent".

Any of those "red" words can be
spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very
loooong way "HHHEEEEEEEEELLP," they just can't have any other letters interspersed between them.

Input: Subject line as a string.
Output: Boolean.

Precondition: Subject can be up to 100 letters
'''

import pytest
from stressful_subject import is_stressful

def test_stressful_subject():
    assert is_stressful("Hi") == False, "No stress found"
    assert is_stressful("I neeed HELP") == True, "asking for HELP in capital letters"
    assert is_stressful("asap help") == True, "has red words"
    assert is_stressful("UUUURGGGEEEEENT here") == True, "Has red word with repeating characters within"
    assert is_stressful("Hello!Please") == False, "No red words, capitalization or !!! at the end"
    assert is_stressful("Hello!!") == False, "Only 2 exclamation points"
