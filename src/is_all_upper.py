


def is_all_upper(text: str) -> bool:
    return False if text.lower() == text else text == text.upper()

def is_all_upper_or_empty(text: str) -> bool:
    return all(fch.isupper() for fch in filter(lambda ch: ch.isalpha(), text))