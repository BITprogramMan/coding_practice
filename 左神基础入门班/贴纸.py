class Solution:
    def minStickers(self, stickers, target):
        n = len(stickers)
        map = [[0] * 26 for _ in range(n)]
        for i in range(n):
            for char in stickers[i]:
                map[i][ord(char) - ord('a')] += 1
        dp = {'': 0}
        def process(dp, target, map, n):
            if target in dp:
                return dp[target]
            tmap = [0] * 26
            ans = float('inf')
            for char in target:
                tmap[ord(char) - ord('a')] += 1
            for i in range(n):
                if map[i][ord(target[0]) - ord('a')] == 0:
                    continue
                remain = ''
                for j in range(26):
                    if tmap[j] > 0:
                        num = max(0, tmap[j] - map[i][j])
                        if num > 0:
                            remain += chr(ord('a') + j) * num
                tmp = process(dp, remain, map, n)
                if tmp != -1:
                    ans = min(ans, tmp + 1)
            dp[target] = -1 if ans == float('inf') else ans
            return dp[target]
        return process(dp, map, target, n)