from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 1:
            return [[]]
        else:
            res = self.subsets(nums[1:])
            return res + [[nums[0]] + item for item in res]
        
    def subsetsv1(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, path, n, nums):
            if index == n:
                res.append(path[:])
                return
            else:
                backtrack(index + 1, path, n, nums)
                path.append(nums[index])
                backtrack(index + 1, path, n, nums)
                path.pop()
        backtrack(0, [], len(nums), nums)
        return res
    
    def subsetsv2(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, path, n, nums):  
            res.append(path[:])
            for i in range(index, n):
                path.append(nums[i])
                backtrack(i + 1, path, n, nums)
                path.pop()
        backtrack(0, [], len(nums), nums)
        return res





if __name__ == '__mnain__':
    solution = Solution()
    nums = [1, 2, 3]
    res = solution.subsets(nums)
    print(res)