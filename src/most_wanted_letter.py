
from string import ascii_lowercase

def most_wanted(text):
        return max(list(ascii_lowercase), key = text.lower().count)
