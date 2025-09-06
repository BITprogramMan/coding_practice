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
        target = abs(target)
        sum_val = sum(nums)
        if sum_val < target or ((sum_val & 1) ^ (target & 1) == 1):
            return 0
        new_target = (target + sum_val) // 2
        n = len(nums)
        dp = [[0] * (new_target + 1) for _ in range(n)]
        dp[0][0] = 1
        if nums[0] <= new_target:
            dp[0][nums[0]] += 1
        for i in range(1, n):
            for j in range(new_target + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i] <= j:
                    dp[i][j] += dp[i - 1][j - nums[i]] 
        return dp[-1][-1]
    
    def findTargetSumWaysv3(self, nums: List[int], target: int) -> int:
        target = abs(target)
        sum_val = sum(nums)
        if sum_val < target or ((sum_val & 1) ^ (target & 1) == 1):
            return 0
        new_target = (target + sum_val) // 2
        n = len(nums)
        dp = [0] * (new_target + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(new_target, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 1]
    res = solution.findTargetSumWaysv2(nums, 0)
    print(res)





