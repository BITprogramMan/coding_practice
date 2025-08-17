from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        mostRightPos = 0
        for i in range(n):
            if i > mostRightPos:
                return False
            mostRightPos = max(mostRightPos, i + nums[i])
        return True

    def canJumpv1(self, nums: List[int]) -> bool:
        n = len(nums)
        mostRightPos = 0
        i = 0
        while i <= mostRightPos:
            mostRightPos = max(mostRightPos, i + nums[i])
            if mostRightPos >= n - 1:
                return True
            i += 1
        return False