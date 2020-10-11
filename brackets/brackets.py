
def are_brackets_valid(expression) -> bool:

    stack = ['']
    brackets = { '{': '}', '[': ']', '(': ')'}
    for ch in expression:
        if ch in brackets:
            stack.append(brackets[ch])
        elif ch in brackets.values() and ch != stack.pop():
            return False

    return stack == ['']
