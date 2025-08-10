from typing import List
import math
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        limit = (1 << n) - 1
        res = []
        def dfs(path, colLimitimit, leftLimit, rightLimit, TotalLimit, n, res):
            if colLimitimit == TotalLimit:
                res.append(['.' * n for _ in range(n)])
                for row_idx, col_idx in enumerate(path):
                    res[-1][row_idx] = res[-1][row_idx][:col_idx] + 'Q' + res[-1][row_idx][col_idx + 1:]
                
                return
                    
            pos = TotalLimit & (~( colLimitimit | leftLimit | rightLimit))
            while pos != 0:
                mostRightOne = pos & ((~pos) + 1)
                pos -= mostRightOne
                path.append(int(math.log2(mostRightOne)))
                dfs(path, colLimitimit | mostRightOne, (leftLimit | mostRightOne) << 1, (rightLimit | mostRightOne) >> 1, TotalLimit, n, res)
                path.pop()
        dfs([], 0, 0, 0, limit, n, res)
        return res
    

if __name__ == '__main__':
    solution = Solution()
    res = solution.solveNQueens(5)
    print(res)
