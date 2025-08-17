class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prev_step1, prev_step2= 1, 0
        for i in range(n - 1):
           prev_step2, prev_step1 = prev_step1, prev_step1 + prev_step2
        return prev_step1