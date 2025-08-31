class Solution:
    """
    牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容
    量为w。牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
    牛牛想知道在总体积不超过背包容量的情况下，他一共有多少种零食放法(总体积为0也算一种放法)。
    """
    def ways(self, arr, w):
        if len(arr) < 1 or w < 0:
            return 0
        n = len(arr)
        dp = [[0] * (w + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for j in range(1, w + 1):
            dp[0][j] = 2 if arr[0] <= j else 1
        for i in range(1, n):
            for j in range(1, w + 1):
                dp[i][j] = dp[i - 1][j]
                if j - arr[i] >= 0:
                    dp[i][j] += dp[i - 1][j - arr[i]]
        return dp[-1][w]
    

    def ways1(self, arr, w):
        if len(arr) < 1 or w < 0:
            return 0
        n = len(arr)
        dp_curr = [0] * (w + 1)
        dp_update = [0] * (w + 1)
        for j in range(w + 1):
            dp_curr[0][j] = 2 if arr[0] <= j else 1
        for i in range(1, n):
            for j in range(1, w + 1):
                dp_update[j] = dp_curr[j]
                if j - arr[i] >= 0:
                    dp_update[j] += dp_curr[j - arr[i]]
            dp_curr = dp_update[:]
        return dp_curr[w]
