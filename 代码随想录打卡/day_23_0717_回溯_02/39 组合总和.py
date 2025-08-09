from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(currSum, path, index, n, candidates, target):
            if currSum > target:
                return
            if currSum == target:
                res.append(path[:])
                return
            else:
                for i in range(index, n):
                    path.append(candidates[i])
                    currSum += candidates[i]
                    backtrack(currSum, path, i, n, candidates, target)
                    currSum -= candidates[i]
                    path.pop()
        backtrack(0, [], 0, len(candidates), candidates, target)
        return res


    def combinationSumv1(self, candidates: List[int], target: int) -> List[List[int]]:
        '''剪枝'''
        res = []
        def backtrack(currSum, path, index, n, candidates, target):
            if currSum == target:
                res.append(path[:])
                return
            else:
                for i in range(index, n):
                    if currSum + candidates[i] > target:
                        break
                    path.append(candidates[i])
                    currSum += candidates[i]
                    backtrack(currSum, path, i, n, candidates, target)
                    currSum -= candidates[i]
                    path.pop()
        candidates.sort()
        backtrack(0, [], 0, len(candidates), candidates, target)
        return res