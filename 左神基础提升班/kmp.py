class Solution:
    def getNextArray(self, s):
        n = len(s)
        res = [0] * n
        res[0] = -1
        i = 2
        cn = 0
        while i < n:
            if s[i - 1] == s[cn]:
                cn += 1
                res[i] = cn
                i += 1
            elif cn > 0:
                cn = res[cn]
            else:
                res[i] = 0
                i += 1
        return res
    
    def getIndexOf(self, s, t):
        n1, n2 = len(s), len(t)
        if n1 < n2 or n1 < 1 or n2 < 1:
            return -1
        nexts = self.getNextArray(t)
        i1, i2 = 0, 0
        while i1 < n1 and i2 < n2:
            if s[i1] == t[i2]:
                i1 += 1
                i2 += 1
            elif i2 > 0:
                i2 = nexts[i2]
            else:
                i1 += 1
        return i1 - i2 if i2 == n2 else -1