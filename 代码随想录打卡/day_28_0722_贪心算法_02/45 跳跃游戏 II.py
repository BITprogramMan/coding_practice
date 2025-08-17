from typing import List

class Solution:
    def jumpv0(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n + 1] * n
        dp[0] = 0
        for i in range(n):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[n - 1]

    def jump(self, nums: List[int]) -> int:
        step = 0
        curr = 0
        nextPos = 0
        n = len(nums)
        for i in range(n):
            if i > curr:
                step += 1
                curr = nextPos
            nextPos = max(nextPos, i + nums[i])
        return step  






if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2]
    res = solution.jump(nums)
    print(res)
