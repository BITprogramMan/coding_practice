from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = max(dp[i][j - 1],dp[i - 1][j])
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[-1][-1]
    
    def longestCommonSubsequencev1(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [0] * (n2 + 1)
        
        for i in range(1, n1 + 1):
            diag = 0  # dp[i-1][j-1]，初始为 dp[i-1][0] = 0
            for j in range(1, n2 + 1):
                tmp = dp[j]  # 保存当前 dp[j]（即上一轮的 dp[i-1][j]），用于下一轮的 diag
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = diag + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                diag = tmp  # 更新 diag 为上一轮的 dp[j]，用于下一个 j 的 dp[i-1][j-1]
        
        return dp[-1]
    


