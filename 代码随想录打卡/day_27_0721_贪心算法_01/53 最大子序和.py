from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        ans = nums[0]
        prev = nums[0]
        for d in nums[1:]:
            prev = max(prev + d, d)
            ans = max(ans, prev)
        return ans


            

