class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i < n - 1:
                dp[i][i + 1] = 1 if s[i] == s[i + 1] else 0
        for i in range(2, n):
            for j in range(n - i):
                if dp[j + 1][j + i - 1] == 1 and s[j] == s[j + i]:
                    dp[j][j + i] = 1
        return sum([sum(dp[i]) for i in range(n)])
    

if __name__ == '__main__':
    solution = Solution()
    s = 'aaaaa'
    res = solution.countSubstrings(s)
    print(res)    