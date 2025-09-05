from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def process(nums):
            if len(nums) < 1:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            first, second = nums[0], max(nums[0], nums[1])
            n = len(nums)
            for i in range(2, n):
                first, second = second, max(first + nums[i], second)
            return second
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(process(nums[:-1]), process(nums[1:]))