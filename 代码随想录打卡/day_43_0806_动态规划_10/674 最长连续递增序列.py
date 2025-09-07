from typing import List
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        curr = 1
        ans = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                ans = max(ans, curr)
                curr = 1
        ans = max(ans, curr)
        return ans