class Solution:
    """
    给定一个括号字符串，求最长的的有效括号子串长度
    """
    def process(self, s):
        n = len(s)
        dp = [0] * n
        ans = 0
        for i in range(1, n):
            if s[i] == ')':
                pre = i - dp[i - 1] - 1
                if pre >= 0 and s[pre] == '(':
                    dp[i] = dp[i - 1] + 2 + (dp[pre - 1] if pre > 0 else 0)
            ans = max(ans, dp[i])
        return ans




