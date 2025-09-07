class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1):
            dp[i][0] = 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[-1][-1]
    
    def numDistinctv1(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)
        dp = [0] * (n2 + 1)
        dp[0] = 1
        for i in range(1, n1 + 1):
            prev = 1
            for j in range(1, n2 + 1):
                tmp = dp[j]
                if s[i - 1] == t[j - 1]:
                    dp[j] += prev
                prev = tmp
        return dp[-1]

