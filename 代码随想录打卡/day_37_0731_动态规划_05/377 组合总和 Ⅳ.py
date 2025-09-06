from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def recursive(rest, nums):
            if rest == 0:
                return 1
            if rest < 0:
                return 0
            ans = 0
            for val in nums:
                ans += recursive(rest - val, nums)
            return ans
        return recursive(target, nums)


    def combinationSum4v1(self, nums: List[int], target: int) -> int:
        def recursive(rest, nums, dp):
            if rest == 0:
                return 1
            if rest < 0:
                return 0
            if rest in dp:
                return dp[rest]
            ans = 0
            for val in nums:
                ans += recursive(rest - val, nums, dp)
            dp[rest] = ans
            return ans
        dp = {}
        return recursive(target, nums, dp)


    def combinationSum4v2(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)  # : 凑成目标正整数为i的排列个数为dp[i]
        dp[0] = 1
        for i in range(1, target + 1):
            for val in nums:
                if val <= i:
                    dp[i] += dp[i - val]
        return dp[target]


