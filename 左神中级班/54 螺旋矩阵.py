from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        start_row, start_col = 0, 0
        len_row, len_col = m, n
        ans = []
        while start_row < (m + 1) // 2 and start_col < (n + 1) // 2:
            if len_row == 1:
                for i in range(start_col, start_col + len_col):
                    ans.append(matrix[start_row][i])
                break
            if len_col == 1:
                for i in range(start_row, start_row + len_row):
                    ans.append(matrix[i][start_col])
                break
            for i in range(start_col, start_col + len_col - 1):
                ans.append(matrix[start_row][i])

            for i in range(start_row, start_row + len_row - 1):
                ans.append(matrix[i][start_col + len_col - 1])

            for i in range(start_col + len_col - 1, start_col, -1):
                ans.append(matrix[start_row + len_row - 1][i])

            for i in range(start_row + len_row - 1, start_row, -1):
                ans.append(matrix[i][start_col])
            start_row += 1
            start_col += 1
            len_col -= 2
            len_row -= 2
        return ans
    
if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    res = solution.spiralOrder(matrix)
    print(res)
   
