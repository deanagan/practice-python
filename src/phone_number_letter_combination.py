from itertools import product
from typing import List

class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        lookup = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7':'pqrs', '8': 'tuv', '9':'wxyz'}
        return [''.join(a) for a in product(*(lookup[ch] for ch in list(digits)))]