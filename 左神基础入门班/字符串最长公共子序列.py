class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * n2 for _ in range(n1)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(1, n1):
            dp[i][0] = max(dp[i-1][0], 1 if text1[i] == text2[0] else 0)
        for i in range(1, n2):
            dp[0][i] = max(dp[0][i - 1], 1 if text1[0] == text2[i] else 0)
        for i in range(1, n1):
            for j in range(1, n2):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[n1 - 1][n2 - 1]