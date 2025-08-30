class Solution:
    """
    给定一个字符串，如果该字符串符合人们日常书写一个整数的形式，返回int类
    型的这个数；如果不符合或者越界返回-1或者报错。
    """
    def convert(self, s):
        def is_valid(s):
            if s[0] != '-' and (s[0] < '0' or s[0] > '9'):
                return False
            if s[0] == '-' and (len(s) == '1' or s[1] == '0'):
                return False
            if s[0] == '0' and len(s) > 1:
                return False
            for i in range(1, len(s)):
                if s[i] < '0' or s[i] > '9':
                    return False
            return True
        if len(s) < 1 or not is_valid(s):
            return 0
        posi = (s[0] != '-')
        # 32位有符号整数的最小值
        min_value = -2**31
        minq = min_value // 10
        minr = min_value % 10
        
        res = 0
        # 从适当的位置开始遍历（有符号则从1开始，无符号从0开始）
        start_index = 0 if posi else 1
        
        for i in range(start_index, len(s)):
            cur = ord('0') - ord(s[i])
            # 检查是否会溢出
            if (res < minq) or (res == minq and cur < minr):
                return 0  # 无法转换
            
            res = res * 10 + cur
        
        # 处理特殊情况：正数但结果等于最小值（这种情况在32位整数中不可能，因为最小值的绝对值比最大值大1）
        if posi and res == min_value:
            return 0  # 无法转换
        
        # 如果是正数，需要取反（因为res在计算过程中是负数）
        return -res if posi else res

