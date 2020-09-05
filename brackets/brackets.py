
def are_brackets_valid(expression) -> bool:
    bracket_open = ('{', '[', '(')
    bracket_close = ('}', ']', ')')
    stack = []
    for ch in expression:
        if ch in bracket_open:
            st.append(ch)
        elif ch in bracket_close:
            if len(st) > 0 and st[-1] == bracket_open[bracket_close.index(ch)]:
                st.pop()
            else:
                return False

    return len(st) == 0
