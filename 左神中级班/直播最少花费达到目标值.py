class Solution:
    """
    CC里面有一个土豪很喜欢一位女直播Kiki唱歌，平时就经常给她点赞、送礼、私聊。最近CC直播平台在举行
    中秋之星主播唱歌比赛，假设一开始该女主播的初始人气值为start， 能够晋升下一轮人气需要刚好达到end，
    土豪给主播增加人气的可以采取的方法有：
    a. 点赞 花费x C币，人气 + 2
    b. 送礼 花费y C币，人气 * 2
    c. 私聊 花费z C币，人气 - 2
    其中 end 远大于start且end为偶数， 请写一个程序帮助土豪计算一下，最少花费多少C币就能帮助该主播
    Kiki将人气刚好达到end，从而能够晋级下一轮？
    输入描述：
    第一行输入5个数据，分别为：x y z start end，每项数据以空格分开。
    其中：0＜x, y, z＜＝10000， 0＜start, end＜＝1000000
    输出描述：
    需要花费的最少C币。
    示例1:
    输入
    3 100 1 2 6
    输出
    6
    """
    def process(self, x, y, z, start, end):
        if start & 1 == 0:
            if end & 1 == 1:
                return -1
            else:
                limit =  (end - start) // 2 * x
        elif start & 1 == 1:
            if end & 1 == 1:
                limit =  (end - start) // 2 * x
            else:
                limit = y
                tmp_start = start * 2
                if tmp_start >= end :
                    limit += (tmp_start - end) // 2 * x
                else:
                    limit += (end - tmp_start) // 2 * z
        def recursive(curr, cost, cost_limit, end, x, y, z):
            if curr > cost_limit:
                return float('inf')
            if curr == end:
                return cost
            if curr < 0:
                return float('inf')
            if curr > 2 * end:
                return float('inf')
            res = min(recursive(curr - 2, cost + x, cost_limit, start, x, y, z), recursive(curr + 2, cost + z, cost_limit, start, x, y, z))
            if curr & 1 == 0:
                res = min(res, recursive(curr // 2, cost + y, cost_limit, start, x, y, z))
            return res

    def processv1(self, x, y, z, start, end):
        if start & 1 == 0:
            if end & 1 == 1:
                return -1
            else:
                limit_cost =  (end - start) // 2 * x
        if start & 1 == 1:
            if end & 1 == 1:
                limit_cost =  (end - start) // 2 * x
            else:
                limit_cost = y
                tmp_start = start * 2
                if tmp_start >= end :
                    limit_cost += (tmp_start - end) // 2 * x
                else:
                    limit_cost += (end - tmp_start) // 2 * z
        limit_target = 2 * end
        dp = [[float('inf')] * (limit_cost + 1) for _ in range(limit_target + 1)]
        for i in range(limit_cost + 1):
            dp[i][start] = i
        
         