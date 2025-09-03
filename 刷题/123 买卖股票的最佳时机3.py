from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 2 for _ in range(3)] for i in range(n)]
        dp[0][1][1], dp[0][2][1] = -prices[0], -prices[0]

        for i in range(1, n):
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])   # 规定买的时候算消耗了一次交易机会
            dp[i][1][1] = max(dp[i -1][1][1], - prices[i]) 
            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])   # 规定买的时候算消耗了一次交易机会
            dp[i][2][1] = max(dp[i -1][2][1], dp[i - 1][1][0] - prices[i]) 

        return dp[-1][-1][0]
        

    def maxProfitv1(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 2 for _ in range(3)] for i in range(n)]
        dp_10, dp_20, dp_11, dp_21 = 0, 0, -prices[0], -prices[0]
        for i in range(1, n):
            dp_10, dp_20, dp_11, dp_21 = max(dp_10, dp_11 + prices[i]), max(dp_20, dp_21 + prices[i]), max(dp_11, -prices[i]), max(dp_21, dp_10 - prices[i]) # 规定买的时候算消耗了一次交易机会
        return dp_20