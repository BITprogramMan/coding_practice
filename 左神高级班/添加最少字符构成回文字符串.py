class Solution:
    """
    给定一个字符串str，如果可以在str的任意位置添加字符，请返回在添加字符最少
    的情况下，让str整体都是回文字符串的一种结果。
    【举例】
    str="ABA"。str本身就是回文串，不需要添加字符，所以返回"ABA"。
    str="AB"。可以在'A'之前添加'B'，使str整体都是回文串，故可以返回"BAB"。也
    可以在'B'之后添加'A'，使str整体都是回文串，故也可以返回"ABA"。总之，只要
    添加的字符数最少，返回其中一种结果即可。
    """
    def PalindromeMinAdd(self, s):
        if len(s) < 2:
            return 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1):
            dp[i][i + 1] = 1 if s[i] != s[i + 1] else 0
        for i in range(n - 3, -1 , -1):
            for j in range(i + 1, n):
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
                if s[i] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j - 1])
        return dp[0][n - 1]
