class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        l = 0
        ans = 0
        window = set()
        for r in range(n):

            while s[r] in window:
                window.discard(s[l])
                l += 1
            window.add(s[r])
            ans = max(ans, r - l + 1)
        return ans

  