class Solution:
    """
    一个 char 类型的数组 chs，其中所有的字符都不同。
    例如，chs=['A', 'B', 'C', ... 'Z']，则字符串与整数的对应关系如下:
    A, B... Z, AA,AB...AZ,BA,BB...ZZ,AAA... ZZZ, AAAA...
    1, 2...26,27, 28... 52,53,54...702,703...18278, 18279...
    例如，chs=['A', 'B', 'C']，则字符串与整数的对应关系如下:
    A,B,C,AA,AB...CC,AAA...CCC,AAAA...
    1, 2,3,4,5...12,13...39,40...
    给定一个数组 chs，实现根据对应关系完成字符串与整数相互转换的两个函数。
    """

    def get_nth_from_char(self, chs, ch):
        try:
            return chs.index(ch) + 1  # 返回 1-based 位置
        except ValueError:
            return -1  # 字符不在 chs 中

    def str2num(self, chs):
        if not chs or not s:
            return 0

        base = len(chs)
        cur = 1
        total = 0

        # 从右往左处理每一位

        for i in range(len(s) - 1, -1, -1):
            char_val = self.get_nth_from_char(chs, s[i])
            if char_val == -1:
                raise ValueError(f"Character '{s[i]}' not in character set")
            total += char_val * cur
            cur *= base

        return total
    
    def num2str(self, chs, n):
        if not chs or n < 1:
            return ""
        
        base = len(chs)
        cur = 1
        length = 0
        temp_n = n

        # 确定结果字符串的长度
        while temp_n >= cur:
            length += 1
            temp_n -= cur
            cur *= base

        # 构建结果字符串
        res = []
        cur = cur // base  # 回退到最高位的权重
        remaining = temp_n

        for _ in range(length):
            index = remaining // cur
            char = self.get_kth_char_at_chs(chs, index + 1)
            res.append(char)
            remaining %= cur
            cur //= base

        return ''.join(res)

    def get_kth_char_at_chs(self, chs, k):
        if k < 1 or k > len(chs):
            return None  # Python 中用 '\0' 或 None 表示无效字符，但这里保持逻辑一致
        return chs[k - 1]




if __name__ == '__main__':
    solution = Solution()
    s = 'ABC'
    res = solution.str2num(s)
    print(res)
