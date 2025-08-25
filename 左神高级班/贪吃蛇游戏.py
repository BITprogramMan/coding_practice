class Solution:
    """
    给定一个二维数组matrix，每个单元都是一个整数，有正有负。最开始的时候小Q操纵
    一条长度为0的蛇蛇从矩阵最左侧任选一个单元格进入地图，蛇每次只能够到达当前位
    置的右上相邻，右侧相邻和右下相邻的单元格。蛇蛇到达一个单元格后，自身的长度会
    瞬间加上该单元格的数值，任何情况下长度为负则游戏结束。小Q是个天才，他拥有一
    个超能力，可以在游戏开始的时候把地图中的某一个节点的值变为其相反数（注：最多
    只能改变一个节点）。问在小Q游戏过程中，他的蛇蛇最长长度可以到多少？
    比如：
    1 -4 10
    3 -2 -1
    2 -1 0
    0 5 -2
    最优路径为从最左侧的3开始，3 -> -4(利用能力变成4) -> 10。所以返回17。
    """
    def snake(self, matrix):
        """
        可以改为动态规划，没有枚举行为，所以记忆化搜索就是最优解了，dp表在有枚举行为的情况下才可能会有优化的地方
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return 0
        ans = float('-inf')
        def process(matrix, row, col):
            if col == len(matrix[0]) - 1:
                return matrix[row][col], -matrix[row][col]
            
            restAns = process(matrix, row, col + 1)
            restUnuse, restUse = restAns
            if row - 1 >= 0:
                restAns = process(matrix, row - 1, col + 1)
                restUnuse = max(restUnuse, restAns[0])
                restUse = max(restUse, restAns[1])
            if row + 1 < len(matrix):
                restAns = process(matrix, row + 1, col + 1)
                restUnuse = max(restUnuse, restAns[0])
                restUse = max(restUse, restAns[1])
            no = matrix[row][col] + restUnuse
            yes = max(matrix[row][col] + restUse, restUnuse - matrix[row][col])
            return no, yes            

        for row in range(len(matrix)):
            cur = process(matrix, row, 0)
            ans = max(ans, max(cur[0], cur[1]))
        return ans
    

    def snake2(self, matrix):
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[[None] * 2 for _ in range(n)] for i in range(m)]
        for i in range(m):
            dp[i][n - 1][0] = matrix[i][n - 1]
            dp[i][n - 1][1] = -matrix[i][n - 1]
        for j in range(n - 2, -1, -1):
            for i in range(m):
                restUnuse = dp[i][j + 1][0]
                restUse = dp[i][j + 1][1]
                if i > 0:
                    restUnuse = max(restUnuse, dp[i - 1][j + 1][0])
                    restUse = max(restUse, dp[i - 1][j + 1][1])
                if i < m - 1:
                    restUnuse = max(restUnuse, dp[i + 1][j + 1][0])
                    restUse = max(restUse, dp[i + 1][j + 1][1])
                dp[i][j][0] = restUnuse + matrix[i][j]
                dp[i][j][1] = max(restUse + matrix[i][j], restUnuse - matrix[i][j])
        res = float('-inf')
        for i in range(m):
            res = max(res, max(dp[i][0][0], dp[i][0][1]))
        return res

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, -4, 10], [3, -2, -1], [2, -1, 0], [0, 5, -2]]
    res = solution.snake(matrix)
    res1 = solution.snake2(matrix)
    print(res, res1,sep='\t')


