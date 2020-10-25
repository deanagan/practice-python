def sum_numbers(text: str) -> int:

    return sum((int(t) for t in text.split() if t.isdigit()))
