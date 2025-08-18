class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(max(j * dp[i -j], j * (i -j)), dp[i])
        return dp[n]
    
    def integerBreakv1(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = max(2 * (i - 2), 2 * dp[i - 2], 3 * (i - 3), 3 * dp[i - 3])
        
        return dp[n]




if __name__ == '__main__':
    solution = Solution()
    n = 10
    res = solution.integerBreak(n)
    print(res)

