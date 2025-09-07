from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i] - prices[i - 1])
        return ans
    
    def maxProfitv1(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n-1][0]
    
    def maxProfitv2(self, prices: List[int]) -> int:
        n = len(prices)
        dp_0 = 0
        dp_1 = -prices[0]
        for i in range(1, n):
            dp_0, dp_1 = max(dp_0, dp_1 + prices[i]), max(dp_1, dp_0 - prices[i])
        return dp_0
