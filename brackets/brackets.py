
def are_brackets_valid(expression) -> bool:
    bracket_open = ('{', '[', '(')
    bracket_close = ('}', ']', ')')
    stack = []
    for ch in expression:
        if ch in bracket_open:
            stack.append(ch)
        elif ch in bracket_close:
            if len(stack) > 0 and stack[-1] == bracket_open[bracket_close.index(ch)]:
                stack.pop()
            else:
                return False

    return len(stack) == 0
