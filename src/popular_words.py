

def popular_words(text: str, words: list) -> dict:
    split_text = text.lower().split()
    return {word: split_text.count(word) for word in words}
