from typing import List

class Solution:
    def __init__(self):
        self.res = []
    def solveNQueens(self, n: int) -> List[List[str]]:

        def is_valid(path, curr):
            for i in range(curr):
                if path[curr] == path[i] or abs(path[curr] - path[i]) == abs(curr -i):
                    return False
            return True


        def process(path, curr_row, n):
            if curr_row == n:
                ans = []
                for i in range(n):
                    s = '.' * n
                    s = s[:path[i]] + 'Q'+s[path[i] + 1:]
                    ans.append(s)
                self.res.append(ans)
                return

            for i in range(n):
                path[curr_row] = i
                if is_valid(path, curr_row):
                    process(path, curr_row + 1, n)
                
        process([0] * n, 0, n)
        return self.res

    def solveNQueensv1(self, n: int) -> int:

        def is_valid(path, curr):
            for i in range(curr):
                if path[curr] == path[i] or abs(path[curr] - path[i]) == abs(curr -i):
                    return False
            return True

        def process(path, curr_row, n):
            if curr_row == n:
                return 1

            res = 0
            for i in range(n):
                path[curr_row] = i
                if is_valid(path, curr_row):
                    res += process(path, curr_row + 1, n)
            return res
        
        return process([0] * n, 0, n)
    

    def solveNQueensv2(self, n: int) -> int:
        if n < 1 or n > 32:
            return 0

        def is_valid(path, curr):
            for i in range(curr):
                if path[curr] == path[i] or abs(path[curr] - path[i]) == abs(curr -i):
                    return False
            return True

        def process(path, curr_row, n):
            if curr_row == n:
                return 1

            res = 0
            for i in range(n):
                path[curr_row] = i
                if is_valid(path, curr_row):
                    res += process(path, curr_row + 1, n)
            return res
        
        return process([0] * n, 0, n)

    def solveNQueensv3(self, n: int) -> int:
        if n < 1 or n > 32:
            return 0
        limit = (1 << n) - 1
        def process(limit, collimit, leftlimit, rightlimit):
            if collimit == limit:
                return 1
            pos = limit & (~(collimit | leftlimit | rightlimit))
            res = 0
            while pos != 0:
                mostRightOne = pos & ((~pos) + 1)
                res += process(limit, collimit | mostRightOne, (leftlimit | mostRightOne) << 1, (rightlimit | mostRightOne) >> 1)
                pos -= mostRightOne
            return res
        return process(n, 0, 0, 0)





if __name__ == '__main__':
    solution = Solution()
    for i in range(5):
        res = solution.solveNQueens(i)
        print(res)
        solution.res = []