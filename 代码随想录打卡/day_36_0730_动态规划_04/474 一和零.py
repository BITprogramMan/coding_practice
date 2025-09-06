from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for i in range(k)]
        num_0, num_1 = sum([1 for char in list(strs[0]) if char == '0']), sum([1 for char in list(strs[0]) if char == '1'])
        if num_0 <= m and num_1 <= n:
            for i in range(num_0, m + 1):
                for j in range(num_1, n + 1):
                    dp[0][i][j] = 1
        for i1 in range(1, k):
            num_0, num_1 = sum([1 for char in list(strs[i1]) if char == '0']), sum([1 for char in list(strs[i1]) if char == '1'])
            for i2 in range(m + 1):
                for i3 in range(n + 1):
                    dp[i1][i2][i3] = dp[i1 - 1][i2][i3]
                    if num_0 <= i2 and num_1 <= i3:
                        dp[i1][i2][i3] = max(dp[i1 - 1][i2 - num_0][i3 - num_1] + 1, dp[i1][i2][i3])
        return dp[-1][-1][-1]
    
    def findMaxFormv1(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i1 in range(k):
            zero_num, one_num = 0, 0
            for char in strs[i1]:
                if char == '0':
                    zero_num += 1
                else:
                    one_num += 1
            for i2 in range(m, zero_num - 1, -1):
                for i3 in range(n, one_num - 1, -1):
                    dp[i2][i3] = max(dp[i2][i3], dp[i2 - zero_num][i3 - one_num] + 1)
        return dp[-1][-1]


    
if __name__ == '__main__':
    solution = Solution()
    strs = ["10","0001","111001","1","0"]
    m, n = 5, 3
    res = solution.findMaxForm(strs, m, n)
    print(res)