from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        max_l, max_r = height[0], height[n - 1]
        l, r = 1, n - 2
        ans = 0
        while l <= r:
            if max_l <= max_r:
                ans += max(0, max_l - height[l])
                max_l = max(max_l, height[l])
                l += 1
            else:
                ans += max(0, max_r - height[r])
                max_r = max(max_r, height[r])
                r -= 1
        return ans




