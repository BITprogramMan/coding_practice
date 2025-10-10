class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(1, m):
            dp[i][0] = 1 if dp[i - 1][0] == 1 or text1[i] == text2[0] else 0
        for j in range(1, n):
            dp[0][j] = 1 if dp[0][j - 1] == 1 or text1[0] == text2[j] else 0
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[-1][-1]