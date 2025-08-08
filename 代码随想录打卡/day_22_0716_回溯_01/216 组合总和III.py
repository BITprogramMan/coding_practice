from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(index, currSum, path, k, n):
            if currSum > n:
                return 
            elif len(path) == k:
                if sum(path) == n:
                    res.append(path[:])
                return
            else:
                for i in range(index, 10):
                    path.append(i)
                    currSum += i
                    backtrack(i + 1, currSum, path, k, n)
                    currSum -= i
                    path.pop()
        backtrack(1, 0, [], k, n)
        return res
            
if __name__ == '__main__':
    solution = Solution()
    res = solution.combinationSum3(3, 7)
    print(res)

