from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n =len(nums)
        if n < 3:
            return max(nums)
        def process(nums, n):
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[-1]
        return max(process(nums[1:], n - 1), process(nums[:-1], n - 1))