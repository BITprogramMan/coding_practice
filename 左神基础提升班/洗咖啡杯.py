class Solution:
    def process(self, drinks, a, b, index, washLine):
        if index == len(drinks) - 1:
            return min(max(washLine, drinks[index]) + a, drinks[index] + b)
        wash = max(washLine, drinks[index]) + a
        next1 = self.process(drinks, a, b, index + 1, wash)
        p1 = max(wash, next1)
        dry = drinks[index] + b
        next2 = self.process(drinks, a, b, index + 1, washLine)
        p2 = max(next2, dry)
        return min(p1, p2)

    def dp(self, drinks, a, b):
        if a >= b:
            return drinks[-1] + b
        limit = 0
        N = len(drinks)
        for i in range(N):
            limit = max(limit, drinks[i]) + a
        dp = [[0] * (limit + 1) for _ in range(N)]
        for index in range(N - 2, -1, -1):
            for washLine in range(limit + 1):
                p1 = float('inf')
                wash = max(washLine, drinks[index]) + a
                if wash <= limit:
                    p1 = max(wash, dp[index + 1][wash])
                p2 = max(drinks[index] + b, dp[index + 1][washLine])
                dp[index][washLine] = min(p1, p2)
        return dp[0][0]
                

        