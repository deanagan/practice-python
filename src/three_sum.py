from typing import List

class Solution:

    @staticmethod
    def index_negative_value_pairs(nums: List[int], offset: int = 0):
        """Generates index and number except consecutive pairs found at the middle of the list.
        This generator assumes a sorted list.
        Yields:
            (int, int): Tuple of index and number
        """
        yield from ((index,num) for index, num in enumerate(nums[offset:], start=offset)
                    if index == offset or num != nums[index - 1])

    def three_sum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()
        lookup = { k:v for v,k in enumerate(nums) }

        for ia, a in self.index_negative_value_pairs(nums):
            if a > 0:
                break

            for ib, b in self.index_negative_value_pairs(nums, ia+1):
                pair_sum = a + b
                if pair_sum > 0:
                    break

                cached_index = lookup[-pair_sum] if -pair_sum in lookup else None
                if cached_index and cached_index > ib:
                    result.append([a, b, nums[cached_index]])

        return result
