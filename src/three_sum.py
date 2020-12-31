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

    def three_sum_closest(self, nums: List[int], target: int) -> int:

        difference = float('inf')
        nums.sort()

        for ia, a in enumerate(nums):
            ib, ic = ia + 1, len(nums) - 1
            while ic > ib:
                total = a + nums[ib] + nums[ic]
                if abs(target - total) < abs(difference):
                    difference = target - total
                # we adjust ic or ib based on whether our total is bigger or smaller
                # vs the target. If it is smaller, we increment ib, otherwise, we reduce ic.
                if total < target:
                    ib += 1
                else:
                    ic -= 1

                # if we already match total, we break
                if total == target:
                    break


        return target - difference
