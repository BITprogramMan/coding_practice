class Solution:
    def getKthCharAtChs(self, chs, k):
        if k < 1 or k > len(chs):
            return ''
        return chs[k - 1]
    
    def getNthFromChar(self, chs, ch):
        res = -1
        for i in range(len(chs)):
            if chs[i] == ch:
                res = i + 1
                break
        return res


    def NumberAndString(self, chs, n):
        if len(chs) < 1 or n < 1:
            return ''
        base = len(chs)
        total_len = 0
        curr = 1
        while n >= curr:
            total_len += 1
            n -= curr
            curr = curr * base
        res = [''] * total_len
        index = 0
        num_curr = 0
        while index != total_len:
            curr = curr / base
            num_curr = n / curr
            res[index] = self.getKthCharAtChs(chs, num_curr + 1)
            n = n % curr
        return ''.join(res)


        

    def getNum(self, chs, source_str):
        if len(chs) < 1:
            return ''
        base = len(chs)
        res = 0
        curr = 1
        for i in range(len(source_str) - 1, -1):
            res += self.getNthFromChar(chs, source_str[i]) * curr
            curr = curr * base
        return res