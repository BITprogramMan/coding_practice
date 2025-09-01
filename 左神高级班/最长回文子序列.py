class Solution:
    """
    给定一个字符串str，求最长的回文子序列。注意区分子序列和子串的不同。    
    """
    def PalindromeSubsequencev1(self, s):
        """
        可以将问题转换为原始字符串与其逆序串的最长公共子序列问题
        """
        return self.longestCommonSubsequence(s, s[::-1])


    def PalindromeSubsequence(self, s):
        """
        也可以直接使用动态规划，范围上的尝试模型，dp[i][j]表示s[i:j+1]上的最长回文子串
        """
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

