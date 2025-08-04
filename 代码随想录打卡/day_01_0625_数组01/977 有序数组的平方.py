from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i1, i2 = 0, len(nums) - 1
        res = []
        while i1 != i2:
            v1 = nums[i1] ** 2
            v2 = nums[i2] ** 2
            if v1 >= v2:
                res.append(v1)
                i1 += 1
            else:
                res.append(v2)
                i2 -= 1
        res.append(nums[i1]**2)
        return res[::-1]
        


