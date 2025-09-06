from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]
        dp[0][0] = 1
        for i in range(coins[0], amount + 1):
            dp[0][i] = dp[0][i - coins[0]]
        for i in range(1, n):
            for j in range(amount + 1):
                if j < coins[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
        return dp[-1][-1]


    def changev1(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(coins[0], amount + 1):
            dp[i] = dp[i - coins[0]]
        for i in range(1, n):
            for j in range(amount + 1):
                if j >= coins[i]:
                    dp[j] = dp[j] + dp[j - coins[i]]
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    coins = [1, 2, 5]
    res = solution.change(5, coins)
    print(res)

