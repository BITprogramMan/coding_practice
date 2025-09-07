from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for j in range(amount + 1):
            for i in range(n):
                if coins[i] <= j and dp[j - coins[i]] != float('inf'):
                    dp[j] = min(dp[j - coins[i]] + 1, dp[j])
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]

    def coinChangev1(self, coins: List[int], amount: int) -> int:
        def recursive(coins, amount, dp):
            if amount == 0:
                return 0
            if amount in coins:
                return 1
            if amount < 0:
                return -1
            if amount in dp:
                return dp[amount]
            ans = float('inf')
            for coin in coins:
                res = recursive(coins, amount - coin, dp)
                if res >= 0:
                    ans = min(ans, res + 1)
            dp[amount] = ans
            return ans
        dp = {}
        res = recursive(coins, amount, dp)
        return -1 if res == float('inf') else res
    
if __name__ == '__main__':
    solution = Solution()
    res = solution.coinChangev1([1, 2, 5], 11)
    print(res)
