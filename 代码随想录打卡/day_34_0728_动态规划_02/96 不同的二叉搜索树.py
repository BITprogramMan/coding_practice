class Solution:
    def numTreesv1(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
    
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        ans = 0
        for root in range(1, n + 1):
            ans += self.numTrees(root - 1) * self.numTrees(n - root)
        return ans


    
if __name__ == '__main__':
    solution = Solution()
    res = solution.numTrees(3)
    print(res)         

