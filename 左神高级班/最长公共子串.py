class Solution:
    """
    请注意区分子串和子序列的不同，给定两个字符串str1和str2，求两个字符串的最长公共子串。
    """
    def lcst(self, s1, s2):
        if len(s1) < 1 or len(s2) < 1:
            return ''
        
        def getdp(s1, s2):
            m ,n = len(s1), len(s2)
            dp = [[0] * n for _ in range(m)]
            for i in range(m):
                dp[i][0] = 1 if s1[i] == s2[0] else 0
            for j in range(n):
                dp[0][j] = 1 if s1[0] == s2[j] else 0
            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] = dp[i - 1][j - 1] + 1 if s1[i] == s2[j] else 0
            return dp
        dp = getdp(s1,s2)
        end, max_ = 0, 0
        for i in range(len(s1)):
            for j in range(len(s2)):
                if dp[i][j] > max_:
                    end = i
                    max_ = dp[i][j]
        return s1[end - max_ + 1: end + 1]
    

    def lcstv1(self, s1, s2):
        '''
        空间压缩的动态规划
        '''
        if len(s1) < 1 or len(s2) < 1:
            return ''
        m, n = len(s1), len(s2)
        row, col = 0, n - 1  # 起始位置的行与列
        end, max_len = 0, 0
        while row < m:
            i, j = row, col
            length = 0
            while i < m and j < n:
                if s1[i] == s2[j]:
                    length += 1
                else:
                    length = 0
                if length > max_len:
                    max_len = length
                    end = i
                i += 1
                j += 1
            if col > 0:
                col -= 1
            else:
                row += 1
        return s1[end - max_len + 1: end + 1]








