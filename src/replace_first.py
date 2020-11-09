import numpy as np
from typing import Iterable

def replace_first_np(items: list) -> Iterable:
    return list(i for i in np.roll(items, -1))