class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            dp[i][i + 1] = 2 if s[i] == s[i + 1] else 1
        for row in range(n - 2, -1, -1):
            for col in range(row + 2, n):
                dp[row][col] = max(dp[row + 1][col], dp[row][col - 1])
                if s[row] == s[col]:
                    dp[row][col] = max(dp[row][col], dp[row + 1][col - 1] + 2)
                 
        return dp[0][n - 1]