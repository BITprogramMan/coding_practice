from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        prev_price = prices[0]
        for i in range(1, n):
            if prices[i] > prev_price:
                ans += (prices[i] -prev_price)
            prev_price = prices[i]
        return ans