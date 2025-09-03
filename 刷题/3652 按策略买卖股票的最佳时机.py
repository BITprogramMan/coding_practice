from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        from itertools import accumulate
        n = len(prices)
        price_sum = list(accumulate(prices, initial=0))
        sell_sum = list(accumulate([prices[i] * strategy[i] for i in range(n)], initial=0))
        ans = float('-inf')
        for i in range(k, n + 1):
            ans = max(ans, sell_sum[i - k] + price_sum[i] - price_sum[i - k // 2] + sell_sum[n] - sell_sum[i])
        return max(ans, sell_sum[n])
