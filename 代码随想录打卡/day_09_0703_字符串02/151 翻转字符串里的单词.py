class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) < 2:
            return s.strip()
        n = len(s)
        i = n - 1
        res = ''
        while i >= 0:
            if i == n - 1:
                if s[i] != ' ':
                    r = i
                else:
                    pass
            elif s[i] != ' ' and s[i + 1] == ' ':
                r = i
            elif s[i] == ' ' and s[i + 1] != ' ':
                l = i + 1
                if not res:
                    res = s[l : r + 1]
                else:
                    res = res + ' ' + s[l : r + 1]
            i -= 1
        if s[0] != ' ':
            res = res + ' ' + s[:r + 1] if res else s[:r + 1]
        return res

            
if __name__ == '__main__':
    solution = Solution()
    s = "the sky is blue"
    res = solution.reverseWords(s)
    print(res)
        








