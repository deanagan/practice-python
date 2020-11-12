from typing import Iterable
from collections import deque

def sort_except_zeros(items: list) -> Iterable:
    d = deque(sorted(fi for fi in items if fi != 0))
    return (i if i == 0 else d.popleft() for i in items)
