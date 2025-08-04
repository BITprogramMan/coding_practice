from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        nums = 1
        while top <= bottom:
            for i in range(left, right + 1):
                res[top][i] = nums
                nums += 1
            top += 1
            for i in range(top, bottom + 1):
                res[i][right] = nums
                nums += 1
            right -= 1
            for i in range(right, left - 1, -1):
                res[bottom][i] = nums
                nums += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                res[i][left] = nums
                nums += 1
            left += 1
        return res
    
    def generateMatrixv1(self, n: int) -> List[List[int]]:
        offset = n // 2
        startx, starty = 0, 0
        res = [[0] * n for _ in range(n)]
        count = 1
        for i in range(offset):
            endx, endy = n - 1 - i, n - 1 - i
            for y in range(starty, endy):
                res[startx][y] = count
                count += 1
            for x in range(startx, endx):
                res[x][endy] = count 
                count += 1
            for y in range(endy, starty, -1):
                res[endx][y] = count
                count += 1
            for x in range(endx, startx, -1):
                res[x][starty] = count
                count += 1
            startx += 1
            starty += 1
        if n & 1 == 1:
            res[offset][offset] = n ** 2
        return res





if __name__ == '__main__':
    solution = Solution()
    res = solution.generateMatrixv1(1)
    print(res)
