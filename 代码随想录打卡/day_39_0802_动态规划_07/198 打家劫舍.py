from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = nums[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[-1][1], dp[-1][0])
    
    def robv1(self, nums: List[int]) -> int:
        n = len(nums)
        dp_0, dp_1 = 0, nums[0]
        for i in range(1, n):
            dp_0, dp_1 = max(dp_1, dp_0), dp_0 + nums[i]
        return max(dp_0, dp_1)
    
    def robv2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[size - 1]

    def robv3(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(first + nums[i], second)
        return second