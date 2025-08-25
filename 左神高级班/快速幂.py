class Solution:
    def power(self, x, n):
        if n < 0:
            if x == 0:
                raise ValueError("0的负数次幂未定义")
            else:
                return 1 / self.power(x, -n)
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
        res = 1
        base = x
        while n:
            if n & 1 == 1:
                res = res * base
            base = base * base
            n = n >> 1
        return res
    
    def power_recursive(self, x, n):
        if n < 0:
            if x == 0:
                raise ValueError("0的负数次幂未定义")
            else:
                return 1 / self.power(x, -n)
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
        if n == 1:
            return x
        half = self.power_recursive(x, n // 2)
        if n & 1 == 1:
            return x * half * half
        else:
            return half * half


