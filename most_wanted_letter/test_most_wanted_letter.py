# You are given a text, which contains different english
# letters and punctuation symbols. You should find the most
# frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter,
# so for the purpose of your search, "A" == "a". Make sure you do
# not count punctuation symbols, digits and whitespaces, only letters.
# If you have two or more letters with the same frequency,
# then return the letter which comes first in the latin alphabet.
# For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
# Input: A text for analysis as a string (unicode for py2.7).
# Output: The most frequent letter in lower case as a string.

# Bryukh's solution
# import string

# def checkio(text):
    # return max(string.ascii_lowercase, key=lambda ch: text.lower().count(ch))

# Veky's solution
# map applies chr to range 97-123, which is basically the lower case characters in ASCII.
# max can have a second parameter which allows you to sort the values in the first param.
# checkio=lambda t:max(map(chr,range(97,123)),key=t.lower().count)

# key in a max/min allows you to pick out values.
# as an example, if you want to get the max even number from a range
# subtract 1 to make it even
import pytest

from most_wanted_letter import most_wanted

def tests():
    assert most_wanted("Hello World!") == "l", "Hello test"
    assert most_wanted("How do you do?") == "o", "O is most wanted"
    assert most_wanted("One") == "e", "All letter only once."