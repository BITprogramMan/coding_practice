class Solution:
    """
    给定一个字符串str，返回把str全部切成回文子串的最小分割数。
    【举例】
    str="ABA"。
    不需要切割，str本身就是回文串，所以返回0。
    str="ACDCDCDAD"。
    最少需要切2次变成3个回文子串，比如"A"、"CDCDC"和"DAD"，所以返回2。
    """
    def PalindromeMinCut(self, s):
        pass
        if len(s) < 2:
            return 0
        def isValid(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        def process(s, i, length):
            if i >= length - 1 :
                return 0
            ans = length - i
            for end in range(i, length):
                if isValid(s, i, end):
                    ans = min(ans, process(s, end + 1, length))
            return ans
        return process(s, 0, len(s))
    

    def PalindromeMinCutv1(self, s):
        n = len(s)
        record = [[False] * n for _ in range(n)]
        for i in range(n):
            record[i][i] = True
            if i + 1 < n:
                record[i][i + 1] = True if s[i] == s[i + 1] else False
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                record[i][j] = True if s[i] == s[j] and record[i + 1][j - 1] else False

        dp = [0] * (n + 1)
        dp[n] = -1
        for i in range(n - 2, -1, -1):
            dp[i] = n - i
            for j in range(i, n):
                if record[i][j]:
                    dp[i] = min(dp[i], dp[j + 1] + 1)
        return dp[0]
    

if __name__ == '__main__':
    solution = Solution()
    s = "ACDCDCDAD"
    res = solution.PalindromeMinCutv1(s)
    print(res)