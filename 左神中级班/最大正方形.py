class Solution:
    """
    给定一个N*N的矩阵matrix，只有0和1两种值，返回边框全是1的最大正方形的边
    长长度。
    例如:
    01111
    01001
    01001
    01111
    01011
    其中边框全是1的最大正方形的大小为4*4，所以返回4。
    """
    def process(self, matrix):
        n = len(matrix)
        ans = 0
        def is_valid(x, y, k, matrix):
            for i in range(x, x + k + 1):
                if matrix[i][y] == 0 or matrix[i][y + k] == 0:
                    return False
            for j in range(y, y + k + 1):
                if matrix[x][j] == 0 or matrix[x + k][j] == 0:
                    return False
            return True
        for x in range(n - 1):
            for y in range(n - 1):
                for k in range(1, min(n - x, n - y)):
                    if is_valid(x, y, k, matrix):
                        ans = max(ans, k)
        return ans
