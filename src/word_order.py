from itertools import zip_longest
from operator import contains, eq

def words_order(text: str, words: list) -> bool:
    def all_unique(w: list) -> bool:
        return len(set(w)) == len(w)

    def in_words(word: str) -> bool:
        return contains(words, word)

    return all_unique(words) and all(eq(a, b) for a, b in
            zip_longest(filter(in_words, text.split()), words, fillvalue=None))
