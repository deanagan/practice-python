
def is_valid(s: str) -> bool:
    brackets = { '{': '}', '(': ')', '[': ']'}
    entries = []
    if len(s) % 2:
        return False

    for ch in s:
        if ch in brackets:
            entries.append(ch)
        elif entries and brackets[entries[-1]] == ch:
            entries.pop()

    return not entries
