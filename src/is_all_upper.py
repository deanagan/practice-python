


def is_all_upper(text: str) -> bool:
    #return bool(filtered := [ch for ch in text if ch.isalpha()]) and all(ch.isupper() for ch in filtered)
    return False if text.lower() == text else text == text.upper()

def is_all_upper_or_empty(text: str) -> bool:
    return not text.strip() or is_all_upper(text)