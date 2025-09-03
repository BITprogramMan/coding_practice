from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[[0] * 3 for _ in range(k + 1)] for i in range(n)]
        for j in range(1, k + 1):
            dp[0][j][1] = -prices[0]
            dp[0][j][2] = prices[0]
        dp[0][0][2] = prices[0]
        for i in range(1, n):
            dp[i][0][2] = max(dp[i - 1][0][2], prices[i])
            for j in range(1, k + 1):
                dp[i][j][0] = max([dp[i - 1][j][0], dp[i - 1][j][1] + prices[i], dp[i - 1][j - 1][2] - prices[i]])   # 规定买的时候算消耗了一次交易机会
                dp[i][j][1] = max(dp[i -1][j][1], dp[i - 1][j - 1][0] - prices[i] if j > 1 else - prices[i])  
                dp[i][j][2] = max(dp[i - 1][j][2], dp[i - 1][j][0] + prices[i])
        return dp[-1][-1][0]  
    
if __name__ == '__main__':
    solution = Solution()
    prices = [14, 6]
    res = solution.maximumProfit(prices, 1)
    print(res)