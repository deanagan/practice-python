from itertools import groupby

def backward_string_by_word(text: str) -> str:
    return ' '.join([word[::-1] for word in text.split(' ')])
