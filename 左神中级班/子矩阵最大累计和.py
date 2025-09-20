class Solution:
    """
    给定一个整型矩阵，返回子矩阵的最大累计和。
    """
    def process(self, matrix):
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for start_row in range(m):
            for end_row in range(start_row, m):
                pre_sum = 0
                if start_row == end_row:
                    for j in range(n):
                        curr_sum = pre_sum + matrix[start_row][j]
                        ans = max(ans, curr_sum)
                        pre_sum = max(0, pre_sum + matrix[start_row][j])
                else:
                    help = [0] * n
                    for i in range(n):
                        help[i] = sum(matrix[j][i] for j in range(start_row, end_row + 1))
                    for j in range(n):
                        curr_sum = pre_sum + help[j]
                        ans = max(ans, curr_sum)
                        pre_sum = max(0, pre_sum + help[j])


        