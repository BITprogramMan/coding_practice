from typing import List
class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        start_row, start_col = 0, 0
        end_row, end_col = 0, 0
        reverse = False
        ans = []
        while end_col < n:
            curr_start_row, curr_start_col = start_row, start_col
            curr_end_row, curr_end_col = end_row, end_col
            if not reverse:
                while curr_start_row < curr_end_row + 1:
                    ans.append(matrix[curr_start_row][curr_start_col])
                    curr_start_row += 1
                    curr_start_col -= 1
            else:
                while curr_end_row > curr_start_row - 1:
                    ans.append(matrix[curr_end_row][curr_end_col])
                    curr_end_row -= 1
                    curr_end_col += 1   
            if end_row < m - 1:
                end_row += 1
            else:
                end_col += 1
            if start_col < n - 1:
                start_col += 1
            else:
                start_row += 1
            reverse = not reverse
        return ans
    

if __name__ == '__main__':
    solution = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

res = solution.spiralOrder(matrix)
print(res)




