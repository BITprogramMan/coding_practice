class Solution:
    """
    小虎去附近的商店买苹果，奸诈的商贩使用了捆绑交易，只提供6个每袋和8个
    每袋的包装包装不可拆分。可是小虎现在只想购买恰好n个苹果，小虎想购买尽
    量少的袋数方便携带。如果不能购买恰好n个苹果，小虎将不会购买。输入一个
    整数n，表示小虎想购买的个苹果，返回最小使用多少袋子。如果无论如何都不
    能正好装下，返回-1。
    """
    def process(self, n):
        if n & 1 == 1:
            return -1
        if n % 8 == 0:
            return n // 8
        num_bags_8 = n // 8
        rest = n % 8
        while num_bags_8 >= 0 and rest < 24:
            if rest % 6 == 0:
                return num_bags_8 + rest // 6
            else:
                num_bags_8 -= 1
                rest += 8
        return -1




