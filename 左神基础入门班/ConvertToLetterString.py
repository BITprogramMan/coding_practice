class Solution:
    def ConvertToLetterString(self, s):
        if len(s) < 1:
            return 0
        def process(i, n, s):
            if i == n :
                return 1
            if s[i] == '0':
                return 0
            res = process(i + 1, n, s)
            if s[i] == '1':
                if i + 1 < n:
                    res += process(i + 2, n, s)
                return res
            if s[i] == '2':
                if i + 1 < n and s[i + 1] < '7':
                    res += process(i + 2, n, s)
                return res
            return res
