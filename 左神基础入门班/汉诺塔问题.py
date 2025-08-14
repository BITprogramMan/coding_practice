from typing import List

class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        def dfs(index, n, A, B, C):
            if index == n - 1:
                C.append(A.pop())
            else:
                dfs(index + 1, n, A, C, B)
                C.append(A.pop())
                dfs(index + 1, n, B, A, C)

        dfs(0, len(A), A, B, C)


if __name__ == '__main__':
    solution = Solution()
    A = [4, 3, 2, 1, 0]
    B = []
    C = []
    solution.hanota(A, B, C)
    print(C)