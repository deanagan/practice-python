
VOWELS = list("AEIOUY")
CONSONANTS = list("BCDFGHJKLMNPQRSTVWXZ")

from itertools import islice
import re

def count_stripes(text):

    # split text using regular expression, and splitting according to punctuation.
    # we could have used split but this method only takes 1 delimeter, so we'll use re.
    words = re.findall(r"[\w']{2,}", text)
    consonants = lambda s: set(s).issubset(CONSONANTS)
    vowels = lambda s: set(s).issubset(VOWELS)
    stripeit = lambda word: [[item.upper() for item in islice(word, s , None, 2)] for s in range(2)]
    alternator = lambda word: zip(stripeit(word), reversed(stripeit(word)))

    return [any(vowels(b) and consonants(w) for b,w in alternator(word)) for word in words].count(True)
