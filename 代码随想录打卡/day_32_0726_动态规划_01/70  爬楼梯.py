class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev_step2, prev_step1 = 1, 2
        for i in range(n - 2):
            prev_step2, prev_step1 = prev_step1, prev_step1 + prev_step2
        return prev_step1