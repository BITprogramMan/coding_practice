class Solution:

    def order_print(self, matrix, start_x, start_y, end_x, end_y, reverse=False):
        res = []
        if reverse:
            for x in range(end_x, start_x - 1, -1):
                res.append(matrix[x][end_y])
                end_y += 1
        else:
            for x in range(start_x, end_x + 1):
                res.append(matrix[x][start_y])
                start_y -= 1
        return res
    
    def process(self, matrix):
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return None
        m, n = len(matrix), len(matrix[0])
        start_x, start_y, end_x, end_y = 0, 0, 0, 0
        res = []
        reverse = False
        while end_y < n:
            res.extend(self.order_print(matrix, start_x, start_y, end_x, end_y, reverse))
            reverse = not reverse
            if end_x < m - 1 and start_y < n - 1:
                end_x += 1
                start_y += 1
            elif end_x == m - 1:
                end_y += 1
                if start_y < n - 1:
                    start_y += 1
                else:
                    start_x += 1
            elif start_y == n - 1:
                start_x += 1
                if end_x < m - 1:
                    end_x += 1
                else:
                    end_y += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2],[4,5],[7,8]]
    res = solution.process(matrix)
    print(res)
        