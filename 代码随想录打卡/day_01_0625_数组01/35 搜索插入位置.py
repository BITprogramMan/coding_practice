from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        没有一次性通过，需要回顾
        '''
        l, r = 0, len(nums) - 1
        ans = r
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
            ans = mid
        return ans if nums[mid] > target else ans + 1