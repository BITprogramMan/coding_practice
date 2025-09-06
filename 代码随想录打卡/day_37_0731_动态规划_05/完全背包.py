class Solution:
    """
    有N件物品和一个最多能背重量为W的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。
    每件物品都有无限个（也就是可以放入背包多次），求解将哪些物品装入背包里物品价值总和最大。
    """
    def knapsack(self, n, bag_weight, weight, value):
        dp = [[0] * (bag_weight + 1) for _ in range(n)]
        for w in range(weight[0], bag_weight + 1):
            dp[0][w] = dp[w - weight[0]] + value[0]
        for i in range(1, n):
            for j in range(bag_weight + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= weight[i]:
                    dp[i][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i])
        return dp[-1][-1]
    
    def knapsackv1(self, n, bag_weight, weight, value):
        dp = [0] * (bag_weight + 1)
        for w in range(weight[0], bag_weight + 1):
            dp[w] = dp[w - weight[0]] + value[0]
        for i in range(1, n):
            for j in range(bag_weight + 1):
                if j >= weight[i]:
                    dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
        return dp[-1]
