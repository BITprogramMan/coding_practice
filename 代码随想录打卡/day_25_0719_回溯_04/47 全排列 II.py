from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, path, used_index, n, nums):
            if index == n:
                res.append(path[:])
                return
            used_val = set()
            for i in range(n):
                if i in used_index:
                    continue
                elif nums[i] in used_val:
                    continue
                path.append(nums[i])
                used_index.add(i)
                used_val.add(nums[i])
                backtrack(index + 1, path, used_index, n, nums)
                path.pop()
                used_index.remove(i)
        backtrack(0, [], set(), len(nums), nums)
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2]
    res = solution.permuteUnique(nums)
    print(res)