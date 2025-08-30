class Solution:
    """
    字符串只由'0'和'1'两种字符构成，
    当字符串长度为1时，所有可能的字符串为"0"、"1"；
    当字符串长度为2时，所有可能的字符串为"00"、"01"、"10"、"11"；
    当字符串长度为3时，所有可能的字符串为"000"、"001"、"010"、"011"、"100"、
    "101"、"110"、"111"
    ...
    如果某一个字符串中，只要是出现'0'的位置，左边就靠着'1'，这样的字符串叫作达
    标字符串。
    给定一个正数N，返回所有长度为N的字符串中，达标字符串的数量。
    比如，N=3，返回3，因为只有"101"、"110"、"111"达标。
    """

    def ZeroLeftOneStringNumber(self, n):
        """
        本质还是斐波那契数列
        """
        def mulMatrix(matrix1, matrix2):
            m, n = len(matrix1), len(matrix2[0])
            res = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for k in range(len(matrix1[0])):
                        res[i][j] += matrix1[i][k] * matrix2[k][j]
            return res

        def matrixPower(matrix, p):
            m, n = len(matrix), len(matrix[0])
            res = [[0] * n for _ in range(m)]
            for i in range(m):
                res[i][i] = 1
            while p != 0:
                if p & 1 == 1:
                    res = mulMatrix(res, matrix)
                matrix = mulMatrix(matrix, matrix)
                p = (p >> 1)
            return res
        if n < 1:
            return 0
        elif n < 3:
            return n
        base = [[1, 1], [1, 0]]
        res = matrixPower(base, n - 2)
        return 2 * res[0][0] + res[1][0]