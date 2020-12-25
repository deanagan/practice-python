from typing import List, Generator


class Solution:

    @classmethod
    def paired(cls, height) -> Generator:
        left = 0
        right = len(height) - 1
        while left != right:
            left_height, right_height = height[left], height[right]
            smaller = min(left_height, right_height)
            yield abs(left - right) * smaller
            if left_height < right_height:
                left += 1
            else:
                right -= 1


    def max_area(self, height: List[int]) -> int:
        return max(self.paired(height))