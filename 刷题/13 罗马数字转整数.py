class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        nums = [0] * n
        for i in range(n):
            if s[i] == 'I':
                nums[i] = 1
            elif s[i] == 'V':
                nums[i] = 5
            elif s[i] == 'X':
                nums[i] = 10
            elif s[i] == 'L':
                nums[i] = 50
            elif s[i] == 'C':
                nums[i] = 100
            elif s[i] == 'D':
                nums[i] = 500
            elif s[i] == 'M':
                nums[i] = 1000
        ans = 0
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                ans -= nums[i]
            else:
                ans += nums[i]
        ans += nums[n - 1]
        return ans

