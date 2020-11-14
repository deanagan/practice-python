from collections.abc import Iterable


def how_deep(structure):
    stack, depth_count = [structure], 1
    while stack:
        s = stack.pop()
        current_stack_size = len(stack)
        stack.extend(e for e in s if isinstance(e, Iterable))
        depth_count += current_stack_size != len(stack)

    return depth_count

# Easier to ask forgiveness than permission
def how_deep_forgiveness(structure):
    try: return 1 + max(map(how_deep_forgiveness, structure), default=0)
    except TypeError: return 0


def how_deep_permission(structure):
    if not isinstance(structure, Iterable):
        return 0
    return 1 + max((how_deep_permission(e) for e in structure), default = 0)
