from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) 
        if target & 1 == 1:
            return False
        target = target // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
            if dp[target] > 0:
                return True
        return False
        