from typing import List

class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        # Algorithm:
        # we traverse with 2 pointers to the left and 1 to the right.
        # we keep left first item on hold while second item traverses toward
        # the direction of the right pointer. We keep going until they hit the same index,
        # gathering triplets along the way. When we hit the same index, we move
        # the first item next.
        if len(nums) < 3:
            return []
        snums = sorted(nums)

        result = set()

        for i, a in enumerate(snums):
            b_index = i + 1
            c_index = len(snums) - 1
            while b_index < c_index:
                b,c = snums[b_index], snums[c_index]
                total = a + b + c
                if total == 0:
                    result.add((a,b,c))
                    b_index += 1
                    c_index -= 1
                elif total > 0:
                    c_index -= 1
                else: # total < 0:
                    b_index += 1

        return [list(l) for l in result]

if __name__ == '__main__':
    sut = Solution()
    print(sut.three_sum([-1,0,1,2,-1,-4]))