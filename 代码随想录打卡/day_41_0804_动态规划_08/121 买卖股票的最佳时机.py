from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minPrice = prices[0]
        for price in prices[1:]:
            minPrice = min(minPrice, price)
            ans = max(ans, price - minPrice)
        return ans