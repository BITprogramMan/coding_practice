class Solution:
    """
    牛牛有一些排成一行的正方形。每个正方形已经被染成红色或者绿色。牛牛现在可
    以选择任意一个正方形然后用这两种颜色的任意一种进行染色,这个正方形的颜色将
    会被覆盖。牛牛的目标是在完成染色之后,每个红色R都比每个绿色G距离最左侧近。
    牛牛想知道他最少需要涂染几个正方形。
    如样例所示: s = RGRGR
    我们涂染之后变成RRRGG满足要求了,涂染的个数为2,没有比这个更好的涂染方案。 
    """
    def process(self, nums):
        n = len(nums)
        left_g = [0] * n
        right_r = [0] * n
        left_g[0] = 1 if nums[0] == 'G' else 0
        right_r[n - 1] = 1 if nums[-1] == 'R' else 0
        for i in range(1, n):
            left_g[i] = left_g[i - 1] + (1 if nums[i] == 'G' else 0)
        ans = left_g[-1]
        for i in range(n - 2, -1, -1):
            right_r[i] = right_r[i + 1] + (1 if nums[i] == 'R' else 0)
            ans = min(ans, left_g[i] + right_r[i + 1])
        return ans

if __name__ == '__main__':
    solution = Solution()
    res = solution.process('RGRGR')
    print(res)
