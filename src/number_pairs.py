

from collections import Counter

class NumberPairs:
    def __init__(self, numbers: int):
        self.numbers = numbers

    def count_divisibility_pairs(self, denominator: int) -> int:
        '''Count pairs that add up to be divisible by denominator'''
        numbers_counted = Counter()
        total_pairs =  0
        for number in self.numbers:
            total_pairs += numbers_counted[-number % denominator]
            numbers_counted[number % denominator] += 1
        return total_pairs
