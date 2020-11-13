from collections.abc import Iterable


def how_deep(structure):
    stack, depth_count = [structure], 1
    while stack:
        s = stack.pop()
        current_stack_size = len(stack)
        stack.extend(e for e in s if isinstance(e, Iterable))
        depth_count += current_stack_size != len(stack)

    return depth_count
