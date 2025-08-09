from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(currSum, index, path, candidates, n,  target):
            if currSum == target:
                res.append(path[:])
                return
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                elif currSum + candidates[i] > target:
                    break
                else:
                    path.append(candidates[i])
                    currSum += candidates[i]
                    backtrack(currSum, i + 1, path, candidates, n, target)
                    path.pop()
                    currSum -= candidates[i]
        candidates.sort()
        backtrack(0, 0, [], candidates, len(candidates), target)
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.combinationSum2([10,1,2,7,6,1,5], 8)
    print(res)
       