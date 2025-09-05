from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def recursive(index, rest, nums, n):
            if index == n:
                return 1 if rest == 0 else 0
            return recursive(index + 1, rest - nums[index], nums, n) + recursive(index + 1, rest + nums[index], nums, n)
        return recursive(0, target, nums, len(nums))
            

    def findTargetSumWaysv1(self, nums: List[int], target: int) -> int:
        def recursive(index, rest, nums, n, dp):
            if index == n:
                return 1 if rest == 0 else 0
            if index in dp and rest in dp[index]:
                return dp[index][rest]
            else:
                res = recursive(index + 1, rest - nums[index], nums, n, dp) + recursive(index + 1, rest + nums[index], nums, n, dp)
                if index not in dp:
                    dp[index] = {}
                dp[index][rest] = res
            return dp[index][rest]
        dp = {}
        return recursive(0, target, nums, len(nums), dp)
        
    def findTargetSumWaysv2(self, nums: List[int], target: int) -> int:
        sum_val = sum(nums)
        if sum_val < target or ((sum_val & 1) ^ (target & 1) == 1):
            return 0
        new_target = (target + sum_val) // 2
        n = len(nums)
        dp = [[0] * (new_target + 1) for _ in range(n)]
        if nums[0] < target:
            dp[0][nums[0]] = 1
        for i in range(1, n):

            





