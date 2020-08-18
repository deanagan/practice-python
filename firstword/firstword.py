from string import ascii_letters
from itertools import takewhile, dropwhile

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """

    return ''.join(
        firstwordchar for firstwordchar in
        takewhile(
            lambda fwc: fwc in ascii_letters or fwc in "'",
            (char for char in dropwhile(lambda ch: not ch.isalpha(), text))
        )
    )

    # Alternatively, using regular expressions
    # import re
    # return re.search(r"[a-zA-z']+",text)[0]
