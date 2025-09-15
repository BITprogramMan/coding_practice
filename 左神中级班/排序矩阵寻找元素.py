class Solution:
    """
    给定一个元素为非负整数的二维数组matrix，每行和每列都是从小到大有序的。
    再给定一个非负整数aim，请判断aim是否在matrix中。
    """
    def process(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m and col > -1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

