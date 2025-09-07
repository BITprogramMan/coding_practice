from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]
    def maxProfitv1(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp_0, dp_1 = 0, -prices[0]
        for i in range(1, n):
            dp_0, dp_1 = max(dp_0, dp_1 + prices[i] - fee), max(dp_1, dp_0 - prices[i])
        return dp_0