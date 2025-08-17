from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp = [0] * (n + 1)
        step0 = 0
        step1 = cost[n - 1]
        # dp[n - 1] = cost[n - 1]
        for i in range(n - 2, -1, -1):
            # dp[i] = min(dp[i + 1] + cost[i], dp[i + 2] + cost[i])
            step0, step1 = step1, min(step1 + cost[i], step0 + cost[i])

        return min(step0, step1)
        
if __name__ == '__main__':
    solution = Solution()
    cost = [10, 15, 20]
    res = solution.minCostClimbingStairs(cost)
    print(res)

