class MinPathSum:
    """
    给你一个二维数组matrix，其中每个数都是正数，要求从左上角走到右下角。每
    一步只能向右或者向下，沿途经过的数字要累加起来。最后请返回最小的路径和。
    """
    def minPathSum1(self, matrix):
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return -1
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = matrix[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + matrix[i][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + matrix[0][i]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
        return dp[-1][-1]
    

    def minPathSum1v1(self, matrix):
        """
        动态规划的空间压缩
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return -1
        m, n = len(matrix), len(matrix[0])
        less = min(m, n)
        more = max(m, n)
        is_less_row = (m == less)
        dp = [0] * less
        dp[0] = matrix[0][0]
        for i in range(1, less):
            dp[i] = dp[i - 1] + (matrix[i][0] if is_less_row else matrix[0][i])
        for i in range(1, more):
            dp[0] = dp[0] + (matrix[0][i] if is_less_row else matrix[i][0])
            for j in range(1, less):
                dp[j] = min(dp[j - 1], dp[j]) + (matrix[j][i] if is_less_row else matrix[i][j])
        return dp[-1]


