from itertools import takewhile as tw


def cut_sentence(line: str, length: int) -> str:
    cut = ' '.join(tw(lambda word: word in line.split(), line[:length].split()))
    return cut + '...' if len(line) > length else cut



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
    assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
    assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
    assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
    assert cut_sentence("Hi my name is Alex", 11) == "Hi my name...", "Fifth"