from itertools import dropwhile, takewhile


def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.index(begin) + 1: text.index(end)]


if __name__ == '__main__':
    between_markers('What is >apple<', '>', '<')# == "apple", "One sym"
