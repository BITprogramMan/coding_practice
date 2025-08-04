from typing import List

class Solution:
    def twoSumv1(self, nums: List[int], target: int) -> List[int]:
        n =len(nums)
        for i in range(n-1):
            value = target - nums[i]
            for j in range(i+1, n):
                if nums[j] == value:
                    return [i, j]
        return [-1, -1]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict()
        for idx, num in enumerate(nums):
            if target - num in record:
                return [record[target -num], idx]
            else:
                record[num] = idx
        return [-1, -1]

