from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i] if i > 1 else - prices[i])
        return dp[-1][0]
    
    def maxProfitv1(self, prices: List[int]) -> int:
        n = len(prices)
        dp_0_pre, dp_0, dp_1 = 0, 0, -prices[0]
        for i in range(1, n):
            dp_1 = max(dp_1, dp_0_pre - prices[i])
            dp_0_pre = dp_0
            dp_0 = max(dp_0, dp_1 + prices[i])
        return dp_0


if __name__ == '__main__':
    solution = Solution