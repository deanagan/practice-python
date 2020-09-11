
#max (range(10), key = lambda values_in_range: values_in_range -1 if values_in_range % 2 == 1 else values_in_range)

from string import ascii_lowercase

def most_wanted(text):

        text = text.lower()
        g = 0
        letter = ''
        for i in filter(lambda t: t in ascii_lowercase, text):
                if g < text.count(i):
                        g, letter = text.count(i), i
                elif g == text.count(i) and i < letter:
                        letter = i

        return letter
