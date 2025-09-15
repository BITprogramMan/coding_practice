class Solution:
    """
    牛牛和羊羊都很喜欢青草。今天他们决定玩青草游戏。
    最初有一个装有n份青草的箱子,牛牛和羊羊依次进行,牛牛先开始。在每个回合中,每个
    玩家必须吃一些箱子中的青草,所吃的青草份数必须是4的x次幂,比如1,4,16,64等等。
    不能在箱子中吃到有效份数青草的玩家落败。假定牛牛和羊羊都是按照最佳方法进行游
    戏,请输出胜利者的名字。
    """
    def process(self, n):
        if n == 0:
            return '后手'
        if n == 1:
            return '先手'
        if n & (n - 1) == 0 and n & (0xaaaaaaaa) == 0:
            return '先手'
        else:
            base = 1
            while base <= n // 4:
                if self.process(n - base) == '后手':
                    return '先手'
                base = base * 4
            return '后手'


    def processv1(self, n):

        def recursive(n, dp):

            if n == 0:
                return '后手'
            if n == 1:
                return '先手'
            if n & (n - 1) == 0 and n & (0xaaaaaaaa) == 0:
                return '先手'
            if n in dp:
                return dp[n]
            else:
                base = 1
                while base <= n // 4:
                    if self.process(n - base) == '后手':
                        dp[n] = '先手'
                        return dp[n]
                    base = base * 4
                dp[n] = '后手'
                return dp[n]
            
        dp = dict()
        return recursive(n, dp)

    def processv2(self, n):
        """
        打表法，根据打标结果找规律，不关系具体逻辑，适用于输入与输出都比较简单，比如整数或者可枚举的值
        """
        if n % 5 == 0 or n % 5 == 2:
            return '先手'
        else:
            return '后手'


