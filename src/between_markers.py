from itertools import dropwhile, takewhile


def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.index(begin) + len(begin) if begin in text else 0:
                text.index(end) if end in text else None]
