from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, path, n, nums):
            res.append(path[:])
            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path, n, nums)
                path.pop()  
        nums.sort()
        backtrack(0, [], len(nums), nums)
        return res