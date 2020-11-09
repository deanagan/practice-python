import numpy as np
from typing import Iterable
from collections import deque

def replace_first_np(items: list) -> Iterable:
    return list(i for i in np.roll(items, -1))


def replace_first(items: list) -> Iterable:
    return items[1:] + items[0:1]