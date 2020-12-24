from typing import List
from itertools import combinations

class Solution:
    def max_area(self, height: List[int]) -> int:
        return max(abs(x-y)* min(height[x], height[y]) for x,y in combinations(range(len(height)), r=2))