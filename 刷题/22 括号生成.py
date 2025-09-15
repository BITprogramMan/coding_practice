from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recursive(path, remain_left, remain_right):
            if remain_right == 0:
                res.append(''.join(path))
            if remain_left > 0:
                path.append('(')
                recursive(path, remain_left - 1, remain_right)
                path.pop()
            if remain_right > remain_left:
                path.append(')')
                recursive(path, remain_left, remain_right - 1)
                path.pop()
        recursive([], n, n)
        return res
    
if __name__ == '__main__':
    solution = Solution()
    res = solution.generateParenthesis(3)
    print(res)