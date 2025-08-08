from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(curr, path):
            if len(path) == k:
                res.append(path[:])
                return
            # for i in range(curr, n + 1):
            for i in range(curr, n + 2 - (k - len(path))):  # 剪枝
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(1, [])
        return res
    
if __name__ == '__main__':
    solution = Solution()
    res = solution.combine(4, 2)
    print(res)
