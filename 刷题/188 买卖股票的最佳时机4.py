from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp_0 = [0] * (k + 1)
        dp_1 = [0] * (k + 1)
        for j in range(1, k + 1):
            dp_1[j] = -prices[0]
        for i in range(1, n):
            for j in range(1, k + 1):
                dp_0[j], dp_1[j] = max(dp_0[j], dp_1[j] + prices[i]), max(dp_1[j], dp_0[j - 1] - prices[i] if j > 1 else -prices[i])   # 规定买的时候算消耗了一次交易机会
        return dp_0[-1]


    def maxProfitv1(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for i in range(n)]
        for j in range(1, k + 1):
            dp[0][j][1] = -prices[0]
        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])   # 规定买的时候算消耗了一次交易机会
                dp[i][j][1] = max(dp[i -1][j][1], dp[i - 1][j - 1][0] - prices[i] if j > 1 else -prices[i])  
        return dp[-1][-1][0]  