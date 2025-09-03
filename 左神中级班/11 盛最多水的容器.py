from typing import List

class Solution:
    """
    关键洞见：在每一步，我们都能确定某些组合不可能产生最大面积，因此可以安全地跳过它们，只关注那些可能推高最终结果的组合。这正是高效算法设计的精髓所在。
    """
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        ans = 0
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans
