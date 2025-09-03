class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1, n2 = len(s), len(t)
        if n1 < n2:
            return ''
        l, r = 0, 0
        need = dict()
        window = dict()
        valid = 0
        length = float('inf')
        start = -1
        for i in range(n2):
            need[t[i]] = need.get(t[i], 0) + 1
        while r < n1:
            if s[r] in need:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == need[s[r]]:
                    valid += 1
            r += 1
            while valid == len(need):
                if r - l < length:
                    start = l
                    length = r - l
                if s[l] in need:
                    if window[s[l]] == need[s[l]]:
                        valid -= 1
                    window[s[l]] -= 1
                l += 1
        return '' if start == -1 else s[start: start + length]



