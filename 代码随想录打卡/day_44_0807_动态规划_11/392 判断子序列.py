class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n2 < n1:
            return False
        def recursive(idx1, idx2, n1, n2, s, t):
            if idx1 == n1:
                return True
            if idx2 == n2:
                return False
            for i in range(idx2, n2):
                if t[i] == s[idx1]:
                    return recursive(idx1 + 1, i + 1, n1, n2, s,t)
            return False
        return recursive(0, 0, n1, n2, s, t)

    def isSubsequencev1(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n2 < n1:
            return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n2 + 1):
            dp[n1][i] = True
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
        return dp[0][0]
    
    def isSubsequencev2(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n2 < n1:
            return False
        if n1 == 0:
            return True
        dp = [True] * (n2 + 1)
        dp[0] = False
        for i in range(1, n1 + 1):
            prev = True
            for j in range(1, n2 + 1):
                tmp = dp[j]
                if s[i - 1] == t[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = dp[j - 1]
                prev = tmp
        return dp[-1]




    

if __name__ == '__main__':
    solution = Solution()
    s = 'a'
    t = 'b'
    res = solution.isSubsequencev1(s, t)
    print(res)

