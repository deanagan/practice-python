
VOWELS = list("AEIOUY")
CONSONANTS = list("BCDFGHJKLMNPQRSTVWXZ")

from itertools import islice
import re

def checkio(text):

    #split text using regular expression, and splitting according to punctuation.
    #we could have used split but this method only takes 1 delimeter, so we'll use re.
    words = re.findall(r"[\w']{2,}", text)
    count = 0
    for word in words:
        stripes = [[item.upper() for item in islice(word, s , None, 2)] for s in range(2)]
        count += 1 if any(set(s).issubset(VOWELS) and set(i).issubset(CONSONANTS) for s,i in zip(stripes, reversed(stripes))) else 0
        
    return count



if __name__ == "__main__":
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

