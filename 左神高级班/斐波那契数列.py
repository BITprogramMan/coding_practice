class Solution:
    def fib(self, n):
        if n < 1:
            return 0
        if n == 1 or n == 2:
            return 1
        base = [[1, 1], [1, 0]]
        res = self.matrixPower(base, n - 2)
        return 2 * res[0][0] + res[1][0]
    def matrixPower(self, matrix, p):
        def multiMatrix(matrix1, matrix2):
            res = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        res[i][j] += matrix1[i][k] * matrix2[k][j]
            return res

        res = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            res[i][i] = 1
        while p != 0:
            if p & 1 == 1:
                res = multiMatrix(res, matrix)
            matrix = multiMatrix(matrix, matrix)
            p = p >> 1
        return res


if __name__ == '__main__':
    solution = Solution()
    n = 5
    print(solution.fib(n))
