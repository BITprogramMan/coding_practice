from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, path, n, nums):
            if len(path) > 1:
                res.append(path[:])
            used = set()
            for i in range(index, n):
                if (len(path) < 1 or path[-1] <= nums[i]) and nums[i] not in used:
                    path.append(nums[i])
                    used.add(nums[i])
                    backtrack(i + 1, path, n, nums)
                    path.pop()
        
        backtrack(0, [], len(nums), nums)        
        return res
if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]
    res = solution.findSubsequences(nums)
    print(res)
