class Solution:
    def add(self, n1, n2):
        res = 0
        while n2 != 0:
            res = n1 ^ n2
            n2 = (n1 & n2) << 1
            n1 = res
        return res
    
    def negNum(self, n):
        return self.add(~n, 1)

    def minus(self, n1, n2):
        return self.add(n1, self.negNum(n2))


    def multi(self, n1, n2): 
        res = 0
        while n2 != 0:
            if n2 & 1 == 1:
                res += n1
            n2 = n2 >> 1
            n1 = n1 << 1
        return res
    
    def isNeg(self, n):
        return n < 0
    
    def div(self, n1, n2):
        x = self.negNum(n1) if self.isNeg(n1) else n1
        y = self.negNum(n2) if self.isNeg(n2) else n2
        res = 0
        i = 31
        while i >= -1:
            if (x >> i) >= y:
                res = (res | (1 << i))
                x = self.minus(x, y << i)
            i = self.minus(i, 1)
        return self.negNum(res) if self.isNeg(n1) ^ self.isNeg(n2) else res

    


if __name__ == '__main__':
    solution = Solution()
    print(solution.add(5, 6))

