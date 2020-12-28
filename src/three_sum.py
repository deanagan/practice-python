from typing import List

class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        lookup = { k:v for v,k in enumerate(nums) }

        for ia, a in enumerate(nums):
            if a > 0:
                break

            if ia > 0 and a == nums[ia - 1]:
                continue

            for ib,b in enumerate(nums[ia + 1:], start = ia + 1):
                if b == nums[ib-1] and ib - ia > 1:
                    continue
                pair_sum = a + b

                if pair_sum > 0:
                    break

                if -pair_sum in lookup and lookup[-pair_sum] > ib:
                    result.append([a, b,  nums[lookup[-pair_sum]]])

        return result

if __name__ == '__main__':
    sut = Solution()
    print(sut.three_sum([-1,0,1,2,-1,-4]))