from itertools import groupby

def backward_string_by_word(text: str) -> str:
    #return ''.join(''.join(v)[::-1] for _,v in groupby(text, lambda w: w.isspace())) # Keeping this solution here for reference
    return ' '.join([word[::-1] for word in text.split(' ')])
