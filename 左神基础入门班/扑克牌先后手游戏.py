from typing import List
class Solution:
    """
    扑克牌先后手游戏
    """
    def CardsInLine(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        def f(nums, i, j):
            if i == j:
                return nums[i]
            return max(nums[i] + s(nums, i + 1, j), nums[j] + s(nums, i, j - 1))
        def s(nums, i, j):
            if i == j:
                return 0
            else:
                return min(f(nums, i + 1, j), f(nums, i, j - 1))
        return max(f(nums, 0, len(nums) - 1), s(nums, 0, len(nums) - 1))