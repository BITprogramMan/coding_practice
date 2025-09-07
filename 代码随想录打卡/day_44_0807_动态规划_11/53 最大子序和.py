from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_sum = nums[0]
        for val in nums[1:]:
            if curr_sum <= 0:
                curr_sum = val
            else:
                curr_sum += val
            ans = max(ans, curr_sum)
        return ans


