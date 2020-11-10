from typing import Iterable
from itertools import zip_longest

def split_pairs(a, grp_size = 2):
    return (''.join(i) for i in zip_longest(*[iter(a)] * grp_size, fillvalue='_'))

def chunking_by(items: list, size: int) -> Iterable:
    return [[5, 4, 7], [3, 4, 5], [4]]

def split_list(items: list) -> Iterable:
    return [items[:(len(items) + 1) // 2], items[(len(items) + 1) // 2:]]
