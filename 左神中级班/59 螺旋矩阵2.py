from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        start = 0
        length = n
        curr_num = 1
        while start < (n + 1) // 2:
            if length == 1:
                ans[start][start] = curr_num
                curr_num += 1
            else:
                for col in range(start, start + length - 1):
                    ans[start][col] = curr_num
                    curr_num += 1
                for row in range(start, start + length - 1):
                    ans[row][start + length - 1] = curr_num
                    curr_num += 1
                for col in range(start + length - 1, start, -1):
                    ans[start + length - 1][col] = curr_num
                    curr_num += 1
                for row in range(start + length - 1, start, -1):
                    ans[row][start] = curr_num
                    curr_num += 1
            start += 1
            length -= 2
        return ans
