from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0
        n = len(nums)
        ans = float('inf')
        subsum = 0
        while end < n :
            subsum += nums[end]
            while subsum >= target:
                  ans = min(ans , end - start + 1)
                  subsum -= nums[start]
                  start += 1
            end += 1
        return 0 if ans == float('inf') else ans

  

