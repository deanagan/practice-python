from typing import Iterable
from itertools import zip_longest

def split_pairs(items: list) -> Iterable:
    return (''.join(i) for i in zip_longest(*[iter(items)] * 2, fillvalue='_'))

def chunking_by(items: list, size: int) -> Iterable:
    return [[e for e in i if e] for i in zip_longest(*[iter(items)] * size)]

def split_list(items: list) -> Iterable:
    return [items[:(len(items) + 1) // 2], items[(len(items) + 1) // 2:]]
