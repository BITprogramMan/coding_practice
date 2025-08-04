from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target > nums[-1] or target < nums[0]:
            return -1
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1








