class Solution:
    """
    在数据加密和数据压缩中常需要对特殊的字符串进行编码。给定的字母表A由26个小写英文字母组成，即
    A={a, b...z}。该字母表产生的长序字符串是指定字符串中字母从左到右出现的次序与字母在字母表中出现
    的次序相同，且每个字符最多出现1次。例如，a，b，ab，bc，xyz等字符串是升序字符串。对字母表A产生
    的所有长度不超过6的升序字符串按照字典排列编码如下：a(1)，b(2)，c(3)……，z(26)，ab(27)，
    ac(28)……对于任意长度不超过16的升序字符串，迅速计算出它在上述字典中的编码。
    输入描述：
    第1行是一个正整数N，表示接下来共有N行，在接下来的N行中，每行给出一个字符串。输出描述：
    输出N行，每行对应于一个字符串编码。
    示例1:
    输入
    3
    a
    b
    ab
    输出
    1
    2
    27
    """
    def f(self, char_idx, length):
        """
        计算以char_idx为开头，长度为length的字符串有多少个
        """
        res = 0
        if length == 1:
            return 1
        for i in range(char_idx + 1, 26):
            res += self.f(i, length - 1)
        return res
    
    def g(self, length):
        """
        计算长度为length的字符串有多少个
        """
        res = 0
        for i in range(1, 27):
            res += self.f(i, length)
        return res
    
    def process(self, s):
        n = len(s)
        res = 0
        for i in range(1, n):
            res += self.g(i)
        first = ord(s[0]) - ord('a') + 1
        for i in range(1, first):
            res += self.f(i, n)
        pre = first
        for i in range(1, n):
            cur = ord(s[i]) - ord('a') + 1
            for j in range(pre + 1, cur):
                res += self.f(j, n - i)
            pre = cur
        return res + 1

