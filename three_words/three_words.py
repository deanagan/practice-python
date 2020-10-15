from itertools import groupby


def has_3digitless_consecutive(words: str) -> bool:
    groups = groupby(words.split(), key = lambda word: word.isalpha())
    return max(len(list(cwords)) if g else 0 for g,cwords in groups) > 2