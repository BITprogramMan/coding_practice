from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(val, i, j, board):
            if val in board[i]:
                return False
            if val in list(zip(* board))[j]:
                return False
            row, col = i // 3, j // 3
            for row_idx in range(row * 3, (row + 1) * 3):
                if val in board[row_idx][col * 3: (col + 1) * 3]:
                    return False
            return True
        def backtrack(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        continue
                    for val in range(1, 10):
                        if isValid(str(val), i, j, board):
                            board[i][j] = str(val)
                            if backtrack(board):
                                return True
                            board[i][j] = '.'
                    return False
            return True
        backtrack(board)

if __name__ == '__main__':
    solution = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solution.solveSudoku(board)
    print(board)

                        
            