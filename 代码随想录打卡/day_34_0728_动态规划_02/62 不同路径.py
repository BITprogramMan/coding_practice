class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[0] * n for _ in range(m)]
        for col in range(n - 1):
            dp[m - 1][col] = 1
        for row in range(m - 1):
            dp[row][n - 1] = 1
        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                dp[row][col] = dp[row][col + 1] + dp[row + 1][col]
        return dp[0][0]
    
    def uniquePathsv1(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

