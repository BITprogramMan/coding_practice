class Solution:
    """
    给定一个非负整数n，代表二叉树的节点个数。返回能形成多少种不同的二叉树结构
    """
    def process(self, n):
        if n == 0:
            return 1
        elif n < 3:
            return n
        ans = 0
        for i in range(n):
            ans += self.process(n - 1 - i) * self.process(i)
        return ans
    
    def processv1(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n):
            for j in range(i):
                dp[i] += dp[i - 1 -j] * dp[j]
        return dp[n]

    