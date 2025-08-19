class Solution:
    def process(self, values, weights, bag):
        n = len(values)
        dp = [[0] * (bag + 1) for _ in range(n)]
        for i in range(weights[0], bag + 1):
            dp[0][i] = values[0]
        for i in range(1, n):
            for j in range(bag + 1):
                if weights[i] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - weights[i]] + values[i])
        return dp[n - 1][bag]


    
